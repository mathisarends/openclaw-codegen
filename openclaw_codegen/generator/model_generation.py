import json
from collections import Counter
from typing import Any

from openclaw_codegen.generator.naming import field_name, model_stem, pascal_case, python_literal, snake_case
from openclaw_codegen.generator.types import Definitions, JsonObject


def _canonical(schema: JsonObject) -> str:
    return json.dumps(schema, sort_keys=True, separators=(",", ":"))


def _string_values(schema: JsonObject) -> list[str] | None:
    values = schema.get("enum")
    if schema.get("type") == "string" and values and all(isinstance(value, str) for value in values):
        return values
    variants = schema.get("anyOf") or schema.get("oneOf")
    if not variants:
        return None
    values = [variant.get("const") for variant in variants]
    if all(
        variant.get("type") == "string" and isinstance(value, str)
        for variant, value in zip(variants, values, strict=True)
    ):
        return values
    return None


class ModelGenerator:
    """Resolve schema types and render one domain's model module."""

    def __init__(self, definitions: Definitions, defaults: dict[str, str]) -> None:
        self._definitions = definitions
        self._defaults = defaults
        self._canonical_names: dict[str, str] = {}
        for name, schema in definitions.items():
            self._canonical_names.setdefault(_canonical(schema), name)
        self._enums: dict[str, tuple[str, list[str]]] = {}
        self._lossy_anonymous_objects = 0
        self._unsupported_keywords: Counter[str] = Counter()

    @property
    def enum_names(self) -> list[str]:
        return list(dict.fromkeys(name for name, _ in self._enums.values()))

    @property
    def known_type_names(self) -> set[str]:
        return set(self._definitions) | set(self.enum_names)

    def has_default(self, model_name: str, json_name: str) -> bool:
        return f"{model_name}.{json_name}" in self._defaults

    def default_for(self, model_name: str, json_name: str) -> str | None:
        return self._defaults.get(f"{model_name}.{json_name}")

    def type_for(self, schema: JsonObject | list[Any], *, current: str | None = None) -> str:
        if isinstance(schema, list):
            literal_values = [item["const"] for item in schema if "const" in item]
            item_types = [self.type_for(item, current=current) for item in schema if "const" not in item]
            if literal_values:
                values = ", ".join(python_literal(value) for value in literal_values)
                item_types.append(f"Literal[{values}]")
            item_types = list(dict.fromkeys(item_types))
            return " | ".join(item_types) if item_types else "Any"
        if not schema:
            return "Any"
        enum = self._enums.get(_canonical(schema))
        if enum is not None:
            return enum[0]
        if "$ref" in schema:
            return schema["$ref"].rsplit("/", 1)[-1]
        if "const" in schema:
            return f"Literal[{python_literal(schema['const'])}]"
        if "enum" in schema:
            values = ", ".join(python_literal(value) for value in schema["enum"])
            return f"Literal[{values}]"
        variants = schema.get("anyOf") or schema.get("oneOf")
        if variants is not None:
            literal_values = [item["const"] for item in variants if "const" in item]
            non_literals = [item for item in variants if "const" not in item]
            types = [self.type_for(item, current=current) for item in non_literals]
            if literal_values:
                values = ", ".join(python_literal(value) for value in literal_values)
                types.append(f"Literal[{values}]")
            types = list(dict.fromkeys(types))
            return " | ".join(types) if types else "Any"
        schema_type = schema.get("type")
        if isinstance(schema_type, list):
            types = list(dict.fromkeys(self.type_for({"type": item}, current=current) for item in schema_type))
            return " | ".join(types)
        primitive_types = {
            "string": "str",
            "integer": "int",
            "number": "float",
            "boolean": "bool",
            "null": "None",
        }
        if schema_type in primitive_types:
            return primitive_types[schema_type]
        if schema_type == "array":
            return f"list[{self.type_for(schema.get('items', {}), current=current)}]"
        if schema_type == "object" or "properties" in schema or "patternProperties" in schema:
            canonical_name = self._canonical_names.get(_canonical(schema))
            if canonical_name is not None and canonical_name != current:
                return canonical_name
            additional = schema.get("additionalProperties")
            if isinstance(additional, dict):
                return f"dict[str, {self.type_for(additional, current=current)}]"
            self._lossy_anonymous_objects += int(bool(schema.get("properties")))
            return "dict[str, Any]"
        if "allOf" in schema:
            self._unsupported_keywords["allOf"] += 1
        return "Any"

    def render(self, selected: list[str]) -> str:
        self._collect_enums(selected)
        selected = self._order_by_dependencies(selected)
        lines = [
            '"""Generated from the pinned OpenClaw schema. Do not edit manually."""',
            "",
            "from enum import StrEnum",
            "from typing import Any, Literal",
            "from uuid import uuid4",
            "",
            "from pydantic import BaseModel, ConfigDict, Field, TypeAdapter",
            "from pydantic.alias_generators import to_camel",
            "",
            "",
            "class _SchemaModel(BaseModel):",
            "    model_config = ConfigDict(",
            "        alias_generator=to_camel,",
            '        extra="forbid",',
            "        populate_by_name=True,",
            '        regex_engine="python-re",',
            "    )",
            "",
        ]
        self._render_enums(lines)
        aliases = self._render_models(lines, selected)
        for name, schema in aliases:
            lines.extend(["", f"type {name} = {self.type_for(schema, current=name)}", ""])
        lines.extend(
            [
                "",
                "_EVENT_ADAPTERS: dict[str, TypeAdapter[Any]] = {}",
                "",
                "",
                "def parse_generated_event(event: str, payload: Any) -> Any:",
                "    adapter = _EVENT_ADAPTERS.get(event)",
                "    return payload if adapter is None else adapter.validate_python(payload)",
                "",
                "",
                "__all__ = [",
            ]
        )
        lines.extend(f'    "{name}",' for name in selected)
        lines.extend(f'    "{name}",' for name, _ in self._enums.values() if name not in selected)
        lines.extend(['    "parse_generated_event",', "]", ""])
        return "\n".join(lines)

    def _render_enums(self, lines: list[str]) -> None:
        for enum_name, values in self._enums.values():
            lines.extend(["", f"class {enum_name}(StrEnum):"])
            used_members: set[str] = set()
            for value in values:
                member = snake_case(value).removesuffix("_").upper()
                candidate = member
                suffix = 2
                while candidate in used_members:
                    candidate = f"{member}_{suffix}"
                    suffix += 1
                used_members.add(candidate)
                lines.append(f"    {candidate} = {value!r}")
            lines.append("")

    def _render_models(self, lines: list[str], selected: list[str]) -> list[tuple[str, JsonObject]]:
        aliases: list[tuple[str, JsonObject]] = []
        for name in selected:
            schema = self._definitions[name]
            if schema.get("type") == "object" or "properties" in schema:
                lines.extend(["", f"class {name}(_SchemaModel):"])
                properties = schema.get("properties", {})
                required = set(schema.get("required", []))
                if properties:
                    lines.extend(
                        self._field(name, field, value, field in required) for field, value in properties.items()
                    )
                else:
                    lines.append("    pass")
                lines.append("")
            elif self._enums.get(_canonical(schema), (None, []))[0] != name:
                aliases.append((name, schema))
        return aliases

    def _field(self, model_name: str, json_name: str, schema: JsonObject, required: bool) -> str:
        python_name = field_name(json_name)
        annotation = self.type_for(schema, current=model_name)
        args: list[str] = []
        if self.default_for(model_name, json_name) == "uuid4":
            args.append("default_factory=lambda: str(uuid4())")
        elif not required:
            annotation = f"{annotation} | None" if "None" not in annotation.split(" | ") else annotation
            args.append("default=None")
        constraints = (
            ("minimum", "ge"),
            ("exclusiveMinimum", "gt"),
            ("maximum", "le"),
            ("exclusiveMaximum", "lt"),
            ("minLength", "min_length"),
            ("maxLength", "max_length"),
            ("minItems", "min_length"),
            ("maxItems", "max_length"),
            ("pattern", "pattern"),
        )
        args.extend(f"{target}={schema[source]!r}" for source, target in constraints if source in schema)
        if python_name != snake_case(json_name):
            args.append(f"alias={json_name!r}")
        if args:
            return f"    {python_name}: {annotation} = Field({', '.join(args)})"
        return f"    {python_name}: {annotation}"

    def _collect_enums(self, selected: list[str]) -> None:
        for model_name in selected:
            schema = self._definitions[model_name]
            values = _string_values(schema)
            if values:
                self._enums.setdefault(_canonical(schema), (model_name, values))
        for model_name in selected:
            schema = self._definitions[model_name]
            for json_name, field_schema in schema.get("properties", {}).items():
                values = _string_values(field_schema)
                if values:
                    self._enums.setdefault(
                        _canonical(field_schema),
                        (f"{model_stem(model_name)}{pascal_case(json_name)}", values),
                    )

    def _order_by_dependencies(self, selected: list[str]) -> list[str]:
        selected_set = set(selected)
        dependencies: dict[str, set[str]] = {name: set() for name in selected}

        def walk(value: Any, owner: str, *, root: bool = False) -> None:
            if isinstance(value, dict):
                dependency = self._canonical_names.get(_canonical(value))
                if not root and dependency in selected_set and dependency != owner:
                    dependencies[owner].add(dependency)
                if "$ref" in value:
                    referenced = value["$ref"].rsplit("/", 1)[-1]
                    if referenced in selected_set and referenced != owner:
                        dependencies[owner].add(referenced)
                for nested in value.values():
                    walk(nested, owner)
            elif isinstance(value, list):
                for nested in value:
                    walk(nested, owner)

        for name in selected:
            walk(self._definitions[name], name, root=True)
        ordered: list[str] = []
        pending = set(selected)
        while pending:
            ready = [name for name in selected if name in pending and not dependencies[name] & pending]
            if not ready:
                cycle = ", ".join(sorted(pending))
                raise RuntimeError(f"generated models contain a dependency cycle: {cycle}")
            ordered.extend(ready)
            pending.difference_update(ready)
        return ordered


def include_model_dependencies(definitions: Definitions, selected: set[str]) -> None:
    """Expand a model selection with inline-equivalent definition dependencies."""
    canonical_names: dict[str, str] = {}
    for name, model_schema in definitions.items():
        canonical_names.setdefault(_canonical(model_schema), name)
    pending = list(selected)
    while pending:
        current = pending.pop()

        def walk(value: Any, *, root: bool = False) -> None:
            if isinstance(value, dict):
                dependency = canonical_names.get(_canonical(value))
                if not root and dependency is not None and dependency not in selected:
                    selected.add(dependency)
                    pending.append(dependency)
                for nested in value.values():
                    walk(nested)
            elif isinstance(value, list):
                for nested in value:
                    walk(nested)

        walk(definitions[current], root=True)
