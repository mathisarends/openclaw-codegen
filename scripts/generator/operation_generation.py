import difflib
import re
from collections import Counter
from collections.abc import Callable, Iterable

from generator.model_generation import ModelGenerator
from generator.naming import (
    client_class_name,
    client_method_name,
    field_name,
    method_member,
    normalized_stem,
    operation_stem,
    pascal_case,
)
from generator.types import (
    Definitions,
    InferredOperations,
    JsonObject,
    MatchOrigin,
    ProtocolSchema,
    UnresolvedOperations,
)

type _Parameter = tuple[str, str, str | None]
type _MethodData = tuple[str | None, str | None, list[_Parameter]]

_SUGGESTION_CUTOFF = 0.75
_SLOT_SUFFIXES = (("params", "Params"), ("result", "Result"))


def infer_operations(schema: ProtocolSchema, operation_overrides: dict[str, JsonObject]) -> InferredOperations:
    """Map every RPC method onto its params and result model.

    The published schema carries no per-method payload contract, so models are
    recovered by name: an exact stem match first, then a plural-insensitive one,
    with explicit overrides winning over both.
    """
    methods = list(schema["methods"])
    params = _ModelIndex(schema["definitions"], "Params", methods)
    results = _ModelIndex(schema["definitions"], "Result", methods)
    inferred: InferredOperations = {}
    for method in methods:
        override = operation_overrides.get(method, {})
        params_name, params_origin = _resolve_model(method, params, override.get("params"))
        result_name, result_origin = _resolve_model(method, results, override.get("result"))
        inferred[method] = {
            "params": params_name,
            "params_origin": params_origin,
            "result": result_name,
            "result_origin": result_origin,
        }
    return inferred


def unresolved_operations(schema: ProtocolSchema, inferred: InferredOperations) -> UnresolvedOperations:
    """Split methods that kept an untyped slot into naming mismatches and genuine schema gaps.

    A naming mismatch has an unclaimed definition close enough to be the missing
    model, so it can be repaired with an override. A schema gap has no candidate
    at all and can only be typed against a live gateway.
    """
    claimed = {name for models in inferred.values() for name in (models["params"], models["result"])}
    candidates = {slot: _unclaimed_models(schema["definitions"], suffix, claimed) for slot, suffix in _SLOT_SUFFIXES}
    naming_mismatch: dict[str, dict[str, str]] = {}
    schema_gap: list[str] = []
    for method, models in inferred.items():
        missing = {
            slot: candidates[slot]
            for slot, resolved in (("params", models["params"]), ("result", models["result"]))
            if resolved is None
        }
        if not missing:
            continue
        suggestions = {slot: match for slot, pool in missing.items() if (match := _closest_model(method, pool))}
        if suggestions:
            naming_mismatch[method] = suggestions
        else:
            schema_gap.append(method)
    return {"naming_mismatch": naming_mismatch, "schema_gap": schema_gap}


def render_client(
    domain: str,
    methods: list[str],
    inferred: InferredOperations,
    operation_overrides: dict[str, JsonObject],
    definitions: Definitions,
    model_generator: ModelGenerator,
) -> str:
    return _ClientRenderer(domain, methods, inferred, operation_overrides, definitions, model_generator).render()


class _ModelIndex:
    """Looks up `<stem><suffix>` definitions for an RPC method name."""

    def __init__(self, definitions: Definitions, suffix: str, methods: Iterable[str]) -> None:
        stems = [name.removesuffix(suffix) for name in definitions if name.endswith(suffix)]
        self._suffix = suffix
        self._exact = _unique_index(stems, operation_stem)
        self._normalized = _unique_index(stems, normalized_stem)
        self._claimed = {self._model_name(self._exact.get(operation_stem(method))) for method in methods}

    def resolve(self, method: str) -> tuple[str | None, MatchOrigin | None]:
        exact = self._exact.get(operation_stem(method))
        if exact is not None:
            return self._model_name(exact), "exact"
        normalized = self._normalized.get(normalized_stem(method))
        if normalized is not None and self._model_name(normalized) not in self._claimed:
            return self._model_name(normalized), "normalized"
        return None, None

    def _model_name(self, stem: str | None) -> str | None:
        return None if stem is None else f"{stem}{self._suffix}"


def _unique_index(stems: list[str], key: Callable[[str], str]) -> dict[str, str | None]:
    """Index stems by `key`, mapping keys that more than one stem claims to None."""
    index: dict[str, str | None] = {}
    for stem in stems:
        computed = key(stem)
        index[computed] = None if computed in index else stem
    return index


def _resolve_model(method: str, index: _ModelIndex, override: str | None) -> tuple[str | None, MatchOrigin | None]:
    if override is not None:
        return override.split(":")[-1], "override"
    return index.resolve(method)


def _unclaimed_models(definitions: Definitions, suffix: str, claimed: set[str | None]) -> dict[str, str]:
    return {
        normalized_stem(name.removesuffix(suffix)): name
        for name in definitions
        if name.endswith(suffix) and name not in claimed
    }


def _closest_model(method: str, candidates: dict[str, str]) -> str | None:
    matches = difflib.get_close_matches(normalized_stem(method), candidates, n=1, cutoff=_SUGGESTION_CUTOFF)
    return candidates[matches[0]] if matches else None


class _ClientRenderer:
    def __init__(
        self,
        domain: str,
        methods: list[str],
        inferred: InferredOperations,
        operation_overrides: dict[str, JsonObject],
        definitions: Definitions,
        model_generator: ModelGenerator,
    ) -> None:
        self._domain = domain
        self._methods = methods
        self._inferred = inferred
        self._operation_overrides = operation_overrides
        self._definitions = definitions
        self._model_generator = model_generator

    def render(self) -> str:
        selected_methods = self._methods
        self._validate_unique_method_names(selected_methods)
        external_imports = self._external_imports()
        model_imports, method_data = self._resolve_methods(selected_methods)
        lines = self._module_header(external_imports, model_imports)
        self._render_method_enum(lines, selected_methods)
        self._render_client(lines, selected_methods, method_data)
        lines.append("")
        return "\n".join(lines)

    def _validate_unique_method_names(self, selected_methods: list[str]) -> None:
        names = [client_method_name(method) for method in selected_methods]
        duplicates = [name for name, count in Counter(names).items() if count > 1]
        if duplicates:
            raise RuntimeError(f"duplicate generated {self._domain} methods: {', '.join(sorted(duplicates))}")

    def _external_imports(self) -> set[tuple[str, str]]:
        imports: set[tuple[str, str]] = set()
        for override in self._operation_overrides.values():
            result = override.get("result")
            if isinstance(result, str) and ":" in result:
                module, name = result.split(":", 1)
                imports.add((module, name))
        return imports

    def _resolve_methods(self, selected_methods: list[str]) -> tuple[set[str], dict[str, _MethodData]]:
        model_imports: set[str] = set()
        method_data: dict[str, _MethodData] = {}
        for method in selected_methods:
            operation = self._inferred[method]
            params_name = operation["params"]
            result_name = operation["result"]
            parameters = self._parameters_for(params_name, model_imports)
            if result_name and not self._is_external(method):
                model_imports.add(result_name)
            method_data[method] = (params_name, result_name, parameters)
        return model_imports, method_data

    def _is_external(self, method: str) -> bool:
        result = self._operation_overrides.get(method, {}).get("result")
        return isinstance(result, str) and ":" in result

    def _parameters_for(self, params_name: str | None, model_imports: set[str]) -> list[_Parameter]:
        if params_name is None:
            return []
        model_imports.add(params_name)
        schema = self._definitions[params_name]
        required = set(schema.get("required", []))
        properties = schema.get("properties", {})
        ordered_fields = sorted(properties, key=lambda name: name not in required)
        parameters: list[_Parameter] = []
        for json_name in ordered_fields:
            annotation = self._model_generator.type_for(properties[json_name], current=params_name)
            default: str | None = None
            if json_name not in required or self._model_generator.has_default(params_name, json_name):
                if "None" not in annotation.split(" | "):
                    annotation = f"{annotation} | None"
                default = "None"
            parameters.append((field_name(json_name), annotation, default))
            referenced_types = set(re.findall(r"\b[A-Z][A-Za-z0-9_]*\b", annotation))
            model_imports.update(referenced_types & self._model_generator.known_type_names)
        return parameters

    def _module_header(self, external_imports: set[tuple[str, str]], model_imports: set[str]) -> list[str]:
        lines = [
            f'"""Generated {self._domain} RPC client. Do not edit manually."""',
            "",
            "from enum import StrEnum",
            "from typing import Any, Literal",
            "from uuid import uuid4",
            "",
            "from openclaw_codegen.generated.clients._requester import Requester",
        ]
        if external_imports:
            lines.extend(["", *(f"from {module} import {name}" for module, name in sorted(external_imports))])
        if model_imports:
            lines.extend(["", "from openclaw_codegen.generated.protocol import ("])
            lines.extend(f"    {name}," for name in sorted(model_imports))
            lines.append(")")
        return lines

    def _render_method_enum(self, lines: list[str], selected_methods: list[str]) -> None:
        lines.extend(["", "", f"class {pascal_case(self._domain)}Method(StrEnum):"])
        lines.extend(f"    {method_member(method)} = {method!r}" for method in sorted(selected_methods))

    def _render_client(
        self, lines: list[str], selected_methods: list[str], method_data: dict[str, _MethodData]
    ) -> None:
        client = client_class_name(self._domain)
        lines.extend(
            [
                "",
                f"class {client}:",
                "    def __init__(self, client: Requester) -> None:",
                "        self._client = client",
            ]
        )
        client_methods = sorted(
            selected_methods,
            key=lambda method: (client_method_name(method) == "list", method),
        )
        for method in client_methods:
            self._render_method(lines, method, method_data[method])
        lines.append("")

    def _render_method(self, lines: list[str], method: str, data: _MethodData) -> None:
        params_name, result_name, parameters = data
        method_name = client_method_name(method)
        return_type = result_name or "Any"
        lines.extend(["", f"    async def {method_name}(", "        self,"])
        if params_name is None:
            lines.extend(["        *,", "        params: dict[str, Any] | None = None,"])
        elif parameters:
            lines.append("        *,")
            for name, annotation, default in parameters:
                suffix = "" if default is None else f" = {default}"
                lines.append(f"        {name}: {annotation}{suffix},")
        lines.append(f"    ) -> {return_type}:")
        self._render_payload(lines, params_name, parameters)
        method_enum = f"{pascal_case(self._domain)}Method.{method_member(method)}"
        lines.extend(
            [
                "        return await self._client.request(",
                f"            {method_enum},",
                "            params=payload,",
            ]
        )
        if result_name:
            lines.append(f"            result_model={result_name},")
        lines.append("        )")

    def _render_payload(self, lines: list[str], params_name: str | None, parameters: list[_Parameter]) -> None:
        if params_name is None:
            lines.append("        payload = params")
            return
        lines.append(f"        payload = {params_name}(")
        json_names = {field_name(name): name for name in self._definitions[params_name].get("properties", {})}
        for name, _, _ in parameters:
            json_name = json_names[name]
            if self._model_generator.default_for(params_name, json_name) == "uuid4":
                lines.append(f"            {name}={name} or str(uuid4()),")
            else:
                lines.append(f"            {name}={name},")
        lines.append("        )")
