import pytest
from generator.model_generation import ModelGenerator, include_model_dependencies


def test_model_dependencies_are_rendered_before_their_consumers() -> None:
    definitions = {
        "Child": {"type": "object", "properties": {"value": {"type": "string"}}},
        "Parent": {
            "type": "object",
            "properties": {"child": {"$ref": "#/definitions/Child"}},
        },
    }
    rendered = ModelGenerator(definitions, {}).render(["Parent", "Child"])
    assert rendered.index("class Child") < rendered.index("class Parent")


def test_model_dependency_cycles_are_reported_clearly() -> None:
    definitions = {
        "Left": {"type": "object", "properties": {"right": {"$ref": "#/definitions/Right"}}},
        "Right": {"type": "object", "properties": {"left": {"$ref": "#/definitions/Left"}}},
    }
    with pytest.raises(RuntimeError, match="dependency cycle: Left, Right"):
        ModelGenerator(definitions, {}).render(["Left", "Right"])


@pytest.mark.parametrize(
    ("schema", "expected"),
    [
        ({"type": "string"}, "str"),
        ({"type": "integer"}, "int"),
        ({"type": "number"}, "float"),
        ({"type": "boolean"}, "bool"),
        ({"type": "null"}, "None"),
        ({"type": "array", "items": {"type": "string"}}, "list[str]"),
        ({}, "Any"),
    ],
)
def test_type_for_maps_primitive_and_array_schemas(schema: dict, expected: str) -> None:
    assert ModelGenerator({}, {}).type_for(schema) == expected


def test_type_for_resolves_refs_consts_and_enums() -> None:
    model_generator = ModelGenerator({}, {})
    assert model_generator.type_for({"$ref": "#/definitions/Widget"}) == "Widget"
    assert model_generator.type_for({"const": "auto"}) == "Literal['auto']"
    assert model_generator.type_for({"enum": [1, 2, 3]}) == "Literal[1, 2, 3]"


def test_type_for_anyof_union_combines_types_and_groups_literals() -> None:
    schema = {"anyOf": [{"const": "auto"}, {"const": "manual"}, {"type": "string"}]}
    assert ModelGenerator({}, {}).type_for(schema) == "str | Literal['auto', 'manual']"


def test_type_for_list_schema_combines_and_dedupes_literal_and_type_variants() -> None:
    schema = [{"const": "a"}, {"type": "string"}, {"type": "string"}]
    assert ModelGenerator({}, {}).type_for(schema) == "str | Literal['a']"
    assert ModelGenerator({}, {}).type_for([]) == "Any"


def test_type_for_resolves_named_object_shape_but_falls_back_for_self_reference() -> None:
    foo_schema = {"type": "object", "properties": {"a": {"type": "string"}}}
    model_generator = ModelGenerator({"Foo": foo_schema}, {})

    assert model_generator.type_for(foo_schema, current="Bar") == "Foo"
    assert model_generator.type_for(foo_schema, current="Foo") == "dict[str, Any]"


def test_type_for_object_with_additional_properties_uses_dict_generic() -> None:
    schema = {"type": "object", "additionalProperties": {"type": "integer"}}
    assert ModelGenerator({}, {}).type_for(schema) == "dict[str, int]"


def test_type_for_lossy_anonymous_object_falls_back_to_dict_any() -> None:
    schema = {"type": "object", "properties": {"a": {"type": "string"}}}
    assert ModelGenerator({}, {}).type_for(schema) == "dict[str, Any]"


def test_type_for_allof_falls_back_to_any() -> None:
    assert ModelGenerator({}, {}).type_for({"allOf": [{"type": "string"}]}) == "Any"


def test_render_extracts_nested_field_enum_from_anyof_consts() -> None:
    definitions = {
        "Widget": {
            "type": "object",
            "properties": {
                "state": {"anyOf": [{"const": "idle", "type": "string"}, {"const": "busy", "type": "string"}]},
            },
        },
    }
    rendered = ModelGenerator(definitions, {}).render(["Widget"])
    assert "class WidgetState(StrEnum):" in rendered
    assert "IDLE = 'idle'" in rendered
    assert "BUSY = 'busy'" in rendered
    assert "state: WidgetState | None = Field(default=None)" in rendered


def test_render_field_requires_alias_when_python_name_diverges_from_json_name() -> None:
    definitions = {
        "Widget": {"type": "object", "required": ["schema"], "properties": {"schema": {"type": "string"}}},
    }
    rendered = ModelGenerator(definitions, {}).render(["Widget"])
    assert "schema_: str = Field(alias='schema')" in rendered


def test_render_field_applies_string_length_and_pattern_constraints() -> None:
    definitions = {
        "Widget": {
            "type": "object",
            "required": ["code"],
            "properties": {"code": {"type": "string", "minLength": 1, "maxLength": 10, "pattern": "^[A-Z]+$"}},
        },
    }
    rendered = ModelGenerator(definitions, {}).render(["Widget"])
    assert "code: str = Field(min_length=1, max_length=10, pattern='^[A-Z]+$')" in rendered


def test_render_field_uuid4_default_uses_default_factory() -> None:
    definitions = {
        "Widget": {"type": "object", "required": ["id"], "properties": {"id": {"type": "string"}}},
    }
    rendered = ModelGenerator(definitions, {"Widget.id": "uuid4"}).render(["Widget"])
    assert "id: str = Field(default_factory=lambda: str(uuid4()))" in rendered


def test_has_default_and_default_for_lookup_by_qualified_field_name() -> None:
    model_generator = ModelGenerator({}, {"Widget.id": "uuid4"})
    assert model_generator.has_default("Widget", "id") is True
    assert model_generator.default_for("Widget", "id") == "uuid4"
    assert model_generator.has_default("Widget", "name") is False
    assert model_generator.default_for("Widget", "name") is None


def test_include_model_dependencies_expands_inline_equivalent_definitions() -> None:
    definitions = {
        "Address": {"type": "object", "properties": {"city": {"type": "string"}}},
        "Person": {
            "type": "object",
            "properties": {"home": {"type": "object", "properties": {"city": {"type": "string"}}}},
        },
    }
    selected = {"Person"}
    include_model_dependencies(definitions, selected)
    assert selected == {"Person", "Address"}
