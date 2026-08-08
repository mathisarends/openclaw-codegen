import pytest
from generator.naming import (
    client_method_name,
    field_name,
    method_member,
    model_stem,
    operation_stem,
    pascal_case,
    python_literal,
    snake_case,
)


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("sessionKey", "session_key"),
        ("HTTPServer", "http_server"),
        ("class", "class_"),
        ("2fa-code", "field_2fa_code"),
    ],
)
def test_snake_case_handles_schema_identifiers(source: str, expected: str) -> None:
    assert snake_case(source) == expected


def test_pydantic_base_model_members_are_not_shadowed() -> None:
    assert field_name("schema") == "schema_"


def test_nested_rpc_names_are_flattened_deterministically() -> None:
    assert client_method_name("sessions.files.list") == "list_files"


def test_single_segment_rpc_names_are_left_unreversed() -> None:
    assert client_method_name("chat.send") == "send"
    assert client_method_name("health") == "health"


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("session_key", "SessionKey"),
        ("http_server", "HttpServer"),
        ("chat", "Chat"),
    ],
)
def test_pascal_case_capitalizes_each_snake_case_part(source: str, expected: str) -> None:
    assert pascal_case(source) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("WidgetGetParams", "WidgetGet"),
        ("WidgetGetResult", "WidgetGet"),
        ("WidgetGetAck", "WidgetGet"),
        ("Widget", "Widget"),
    ],
)
def test_model_stem_strips_operation_suffixes(source: str, expected: str) -> None:
    assert model_stem(source) == expected


def test_operation_stem_normalizes_case_and_punctuation() -> None:
    assert operation_stem("Widget.Get-Thing") == "widgetgetthing"


def test_method_member_uppercases_the_domain_relative_method() -> None:
    assert method_member("chat.message.get") == "MESSAGE_GET"
    assert method_member("widget.thing-one") == "THING_ONE"


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (True, "True"),
        (False, "False"),
        (None, "None"),
        ("hi", "'hi'"),
        (42, "42"),
    ],
)
def test_python_literal_renders_bools_and_none_before_falling_back_to_repr(value: object, expected: str) -> None:
    assert python_literal(value) == expected
