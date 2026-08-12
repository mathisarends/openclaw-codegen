import pytest

from openclaw_codegen.generator.model_generation import ModelGenerator
from openclaw_codegen.generator.operation_generation import infer_operations, render_client, unresolved_operations


def test_operation_inference_matches_unique_parameter_and_result_models() -> None:
    schema = {
        "definitions": {
            "WidgetGetParams": {"type": "object"},
            "WidgetGetResult": {"type": "object"},
        },
        "methods": {"widget.get": {}},
    }
    assert infer_operations(schema, {}) == {
        "widget.get": {
            "params": "WidgetGetParams",
            "params_origin": "exact",
            "result": "WidgetGetResult",
            "result_origin": "exact",
        }
    }


def test_duplicate_generated_method_names_fail_before_rendering() -> None:
    methods = {"widget.thing-one": {}, "widget.thing_one": {}}
    schema = {"definitions": {}, "methods": methods}
    with pytest.raises(RuntimeError, match="duplicate generated widget methods: THING_ONE|thing_one"):
        render_client("widget", list(methods), infer_operations(schema, {}), {}, {}, ModelGenerator({}, {}))


def test_operation_inference_returns_none_for_missing_or_ambiguous_matches() -> None:
    schema = {
        "definitions": {
            "WidgetGetParams": {"type": "object"},
            "Widget-Get-Params": {"type": "object"},
            "WidgetGetResult": {"type": "object"},
        },
        "methods": {"widget.get": {}, "widget.missing": {}},
    }
    inferred = infer_operations(schema, {})
    assert (inferred["widget.get"]["params"], inferred["widget.get"]["result"]) == (None, "WidgetGetResult")
    assert (inferred["widget.missing"]["params"], inferred["widget.missing"]["result"]) == (None, None)


def test_operation_inference_falls_back_to_a_plural_insensitive_match() -> None:
    schema = {
        "definitions": {"WidgetProposalListParams": {"type": "object"}},
        "methods": {"widgets.proposals.list": {}},
    }
    inferred = infer_operations(schema, {})
    assert inferred["widgets.proposals.list"]["params"] == "WidgetProposalListParams"
    assert inferred["widgets.proposals.list"]["params_origin"] == "normalized"


def test_normalized_match_never_steals_a_model_an_exact_match_already_claims() -> None:
    schema = {
        "definitions": {"WidgetItemGetParams": {"type": "object"}},
        "methods": {"widget.item.get": {}, "widgets.items.get": {}},
    }
    inferred = infer_operations(schema, {})
    assert inferred["widget.item.get"]["params"] == "WidgetItemGetParams"
    assert inferred["widgets.items.get"]["params"] is None


def test_normalized_match_is_refused_when_two_models_normalize_alike() -> None:
    schema = {
        "definitions": {"WidgetRunParams": {"type": "object"}, "WidgetRunsParams": {"type": "object"}},
        "methods": {"widget.execute": {}},
    }
    assert infer_operations(schema, {})["widget.execute"]["params"] is None


def test_overrides_win_over_inference_and_are_reported_as_such() -> None:
    schema = {
        "definitions": {"WidgetGetParams": {"type": "object"}, "WidgetGetResult": {"type": "object"}},
        "methods": {"widget.get": {}},
    }
    overrides = {"widget.get": {"params": "HandWrittenParams", "result": "mod:ExternalResult"}}
    inferred = infer_operations(schema, overrides)
    assert inferred["widget.get"] == {
        "params": "HandWrittenParams",
        "params_origin": "override",
        "result": "ExternalResult",
        "result_origin": "override",
    }


def test_unresolved_operations_separate_naming_mismatches_from_schema_gaps() -> None:
    schema = {
        "definitions": {"WidgetSpinActionParams": {"type": "object"}},
        "methods": {"widget.spin": {}, "widget.nothing": {}},
    }
    inferred = infer_operations(schema, {})

    unresolved = unresolved_operations(schema, inferred)

    assert unresolved["naming_mismatch"] == {"widget.spin": {"params": "WidgetSpinActionParams"}}
    assert unresolved["schema_gap"] == ["widget.nothing"]


def test_unresolved_operations_ignore_models_another_method_already_uses() -> None:
    schema = {
        "definitions": {"WidgetSpinParams": {"type": "object"}},
        "methods": {"widget.spin": {}, "widget.spins": {}},
    }
    inferred = infer_operations(schema, {})

    unresolved = unresolved_operations(schema, inferred)

    assert unresolved["naming_mismatch"] == {}
    assert unresolved["schema_gap"] == ["widget.spin", "widget.spins"]


def test_render_client_orders_required_parameters_and_injects_uuid4_defaults() -> None:
    definitions = {
        "WidgetCreateParams": {
            "type": "object",
            "required": ["name", "requestId"],
            "properties": {
                "name": {"type": "string"},
                "requestId": {"type": "string"},
                "note": {"type": "string"},
            },
        },
        "WidgetCreateResult": {"type": "object", "properties": {"id": {"type": "string"}}},
    }
    schema = {"definitions": definitions, "methods": {"widget.create": {}}}
    inferred = infer_operations(schema, {})
    model_generator = ModelGenerator(definitions, {"WidgetCreateParams.requestId": "uuid4"})

    rendered = render_client("widget", ["widget.create"], inferred, {}, definitions, model_generator)

    assert "params: dict[str, Any] | None = None," not in rendered

    assert rendered.index("name: str,") < rendered.index("request_id: str | None = None,")
    assert rendered.index("request_id: str | None = None,") < rendered.index("note: str | None = None,")
    assert "name=name," in rendered
    assert "request_id=request_id or str(uuid4())," in rendered
    assert "note=note," in rendered
    assert "async def create(" in rendered
    assert "result_model=WidgetCreateResult," in rendered
    assert "CREATE = 'widget.create'" in rendered
    assert "__all__" not in rendered
    assert "from openclaw_codegen.generated.clients._requester import Requester" in rendered
    assert "class Requester(Protocol):" not in rendered


def test_render_client_forces_list_method_last_and_supports_external_result_imports() -> None:
    definitions = {"WidgetZapResult": {"type": "object", "properties": {}}}
    methods = {"widget.zap": {}, "widget.list": {}}
    schema = {"definitions": definitions, "methods": methods}
    operation_overrides = {"widget.list": {"result": "some_module:ExternalResult"}}
    inferred = infer_operations(schema, operation_overrides)
    model_generator = ModelGenerator(definitions, {})

    rendered = render_client("widget", list(methods), inferred, operation_overrides, definitions, model_generator)

    assert "from some_module import ExternalResult" in rendered
    assert rendered.index("LIST = 'widget.list'") < rendered.index("ZAP = 'widget.zap'")
    assert rendered.index("async def zap(") < rendered.index("async def list(")
    assert "result_model=ExternalResult," in rendered
    assert "-> ExternalResult:" in rendered
    assert "-> WidgetZapResult:" in rendered


def test_render_client_passes_params_through_when_the_schema_defines_no_model() -> None:
    schema = {"definitions": {}, "methods": {"widget.mystery": {}}}
    inferred = infer_operations(schema, {})

    rendered = render_client("widget", ["widget.mystery"], inferred, {}, {}, ModelGenerator({}, {}))

    assert "params: dict[str, Any] | None = None," in rendered
    assert "payload = params" in rendered
    assert "-> Any:" in rendered


def test_render_client_keeps_flat_arguments_when_only_the_result_model_is_missing() -> None:
    definitions = {
        "WidgetPokeParams": {"type": "object", "required": ["name"], "properties": {"name": {"type": "string"}}}
    }
    schema = {"definitions": definitions, "methods": {"widget.poke": {}}}
    inferred = infer_operations(schema, {})

    rendered = render_client("widget", ["widget.poke"], inferred, {}, definitions, ModelGenerator(definitions, {}))

    assert "params: dict[str, Any] | None = None," not in rendered
    assert "name: str," in rendered
    assert "payload = WidgetPokeParams(" in rendered
    assert "-> Any:" in rendered
    assert "result_model=" not in rendered
