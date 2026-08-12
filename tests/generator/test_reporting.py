from openclaw_codegen.generator.reporting import build_generation_report


def test_generation_report_lists_unresolved_methods_and_counts() -> None:
    schema = {"definitions": {"AParams": {}, "AResult": {}}, "methods": {"a": {}, "b": {}}}
    inferred = {
        "a": {"params": "AParams", "params_origin": "exact", "result": "AResult", "result_origin": "exact"},
        "b": {"params": None, "params_origin": None, "result": None, "result_origin": None},
    }
    overrides = {"operations": {}, "events": {"chat": "ChatEvent"}, "field_defaults": {}}

    report = build_generation_report(
        schema, {"version": "1.0.0"}, overrides, inferred, {"AParams", "AResult"}, "digest123", {"root": None}
    )

    assert report["unresolved_methods"] == {"naming_mismatch": {}, "schema_gap": ["b"]}
    assert report["normalized_matches"] == {}
    assert report["schema"] == {"version": "1.0.0", "sha256": "digest123"}
    assert report["known_events"] == {"chat": "ChatEvent"}
    assert report["counts"] == {
        "definitions": 2,
        "methods": 2,
        "generated_models": 2,
        "generated_operations": 2,
        "generated_domains": 1,
        "inferred_params": 1,
        "inferred_results": 1,
        "naming_mismatches": 0,
        "schema_gaps": 1,
    }


def test_generation_report_records_models_recovered_by_normalized_match() -> None:
    schema = {"definitions": {"AParams": {}, "AResult": {}}, "methods": {"a": {}}}
    inferred = {
        "a": {"params": "AParams", "params_origin": "normalized", "result": "AResult", "result_origin": "exact"}
    }
    overrides = {"operations": {}, "events": {}, "field_defaults": {}}

    report = build_generation_report(schema, {"version": "x"}, overrides, inferred, set(), "d", {"root": None})

    assert report["normalized_matches"] == {"a": {"params": "AParams"}}
    assert report["unresolved_methods"] == {"naming_mismatch": {}, "schema_gap": []}


def test_generation_report_treats_overridden_results_as_resolved() -> None:
    schema = {"definitions": {}, "methods": {"a": {}}}
    inferred = {"a": {"params": "AParams", "params_origin": "override", "result": "Type", "result_origin": "override"}}
    overrides = {"operations": {"a": {"result": "mod:Type"}}, "events": {}, "field_defaults": {}}

    report = build_generation_report(schema, {"version": "x"}, overrides, inferred, set(), "d", {"root": None})

    assert report["unresolved_methods"] == {"naming_mismatch": {}, "schema_gap": []}
