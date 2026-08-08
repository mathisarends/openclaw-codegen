import hashlib
import json
from pathlib import Path

import pytest
from generator import pipeline
from generator.pipeline import generate
from generator.types import GenerationPaths

_PACKAGE_ROOT = Path(__file__).resolve().parents[2]


def test_domain_selection_is_declared_in_overrides() -> None:
    overrides = json.loads((_PACKAGE_ROOT / "schema" / "overrides.json").read_text(encoding="utf-8"))
    assert overrides["domains"] == {"chat": {"event_registry": True}}


def test_validate_schema_returns_the_digest_when_it_matches_the_pin() -> None:
    raw = b'{"a": 1}'
    digest = hashlib.sha256(raw).hexdigest()
    assert pipeline._validate_schema(raw, {"sha256": digest}) == digest


def test_validate_schema_rejects_a_digest_mismatch() -> None:
    with pytest.raises(RuntimeError, match="schema SHA-256 mismatch"):
        pipeline._validate_schema(b"data", {"sha256": "deadbeef"})


def test_event_domain_returns_none_when_no_domain_owns_the_registry() -> None:
    assert pipeline._event_domain({"chat": {}, "sessions": {"event_registry": False}}) is None


def test_event_domain_returns_the_owning_domain() -> None:
    assert pipeline._event_domain({"chat": {"event_registry": True}, "sessions": {}}) == "chat"


def test_event_domain_rejects_multiple_owners() -> None:
    domains = {"chat": {"event_registry": True}, "sessions": {"event_registry": True}}
    with pytest.raises(RuntimeError, match="only one generated domain"):
        pipeline._event_domain(domains)


def test_discover_domains_maps_dotless_methods_to_root() -> None:
    assert pipeline._discover_domains({"health": {}, "chat.send": {}}) == {"root": None, "chat": "chat"}


def test_discover_domains_rejects_colliding_wire_domains() -> None:
    methods = {"chatRoom.a": {}, "chat_room.b": {}}
    with pytest.raises(RuntimeError, match="RPC domains"):
        pipeline._discover_domains(methods)


def test_domain_methods_filters_by_prefix_or_selects_dotless_methods() -> None:
    methods = {"health": {}, "chat.send": {}, "chat.history": {}, "sessions.list": {}}
    assert pipeline._domain_methods(methods, None) == ["health"]
    assert pipeline._domain_methods(methods, "chat") == ["chat.send", "chat.history"]


def test_generation_report_lists_unresolved_methods_and_counts() -> None:
    schema = {"definitions": {"AParams": {}, "AResult": {}}, "methods": {"a": {}, "b": {}}}
    inferred = {
        "a": {"params": "AParams", "params_origin": "exact", "result": "AResult", "result_origin": "exact"},
        "b": {"params": None, "params_origin": None, "result": None, "result_origin": None},
    }
    overrides = {"operations": {}, "events": {"chat": "ChatEvent"}, "domains": {}, "field_defaults": {}}

    report = pipeline._generation_report(
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


def test_generation_report_records_models_recovered_by_the_normalized_match() -> None:
    schema = {"definitions": {"AParams": {}, "AResult": {}}, "methods": {"a": {}}}
    inferred = {
        "a": {"params": "AParams", "params_origin": "normalized", "result": "AResult", "result_origin": "exact"}
    }
    overrides = {"operations": {}, "events": {}, "domains": {}, "field_defaults": {}}

    report = pipeline._generation_report(schema, {"version": "x"}, overrides, inferred, set(), "d", {"root": None})

    assert report["normalized_matches"] == {"a": {"params": "AParams"}}
    assert report["unresolved_methods"] == {"naming_mismatch": {}, "schema_gap": []}


def test_generation_report_treats_overridden_results_as_resolved() -> None:
    schema = {"definitions": {}, "methods": {"a": {}}}
    inferred = {"a": {"params": "AParams", "params_origin": "override", "result": "Type", "result_origin": "override"}}
    overrides = {"operations": {"a": {"result": "mod:Type"}}, "events": {}, "domains": {}, "field_defaults": {}}

    report = pipeline._generation_report(schema, {"version": "x"}, overrides, inferred, set(), "d", {"root": None})

    assert report["unresolved_methods"] == {"naming_mismatch": {}, "schema_gap": []}


def test_operation_overrides_must_name_a_known_model() -> None:
    with pytest.raises(RuntimeError, match=r"operation override a.params names unknown model 'Missing'"):
        pipeline._validate_operation_overrides({"a": {"params": "Missing"}}, {"AParams": {}})


def test_operation_overrides_accept_external_and_defined_models() -> None:
    overrides = {"a": {"params": "AParams", "result": "some_module:External"}}
    pipeline._validate_operation_overrides(overrides, {"AParams": {}})


def test_obsolete_outputs_lists_legacy_paths_per_domain(tmp_path: Path) -> None:
    paths = GenerationPaths.from_package_root(tmp_path)
    obsolete = pipeline._obsolete_outputs(paths, ["chat"])
    assert paths.generated / "namespaces" / "chat.py" in obsolete
    assert paths.generated / "chat" / "client.py" in obsolete
    assert paths.generated / "chat" / "events.py" in obsolete
    assert paths.generated / "models.py" in obsolete


def test_apply_outputs_check_mode_reports_changes_without_writing(tmp_path: Path) -> None:
    target = tmp_path / "out.py"
    assert pipeline._apply_outputs({target: "content"}, [], check=True) is True
    assert not target.exists()


def test_apply_outputs_writes_new_files_and_is_idempotent(tmp_path: Path) -> None:
    target = tmp_path / "sub" / "out.py"
    assert pipeline._apply_outputs({target: "content"}, [], check=False) is True
    assert target.read_text(encoding="utf-8") == "content"
    assert pipeline._apply_outputs({target: "content"}, [], check=False) is False


def test_apply_outputs_removes_obsolete_files_only_when_not_checking(tmp_path: Path) -> None:
    obsolete = tmp_path / "old.py"
    obsolete.write_text("legacy", encoding="utf-8")

    assert pipeline._apply_outputs({}, [obsolete], check=True) is True
    assert obsolete.exists()

    assert pipeline._apply_outputs({}, [obsolete], check=False) is True
    assert not obsolete.exists()


def test_generate_end_to_end_writes_expected_outputs_and_detects_drift(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(pipeline, "_format_python", lambda path, content, *, package_root: content)
    paths = GenerationPaths.from_package_root(tmp_path)
    paths.schema.parent.mkdir(parents=True)
    raw_schema = json.dumps(
        {
            "definitions": {"HealthResult": {"type": "object", "properties": {"ok": {"type": "boolean"}}}},
            "methods": {"health": {}},
        }
    ).encode()
    paths.schema.write_bytes(raw_schema)
    paths.metadata.write_text(
        json.dumps({"version": "1.0.0", "sha256": hashlib.sha256(raw_schema).hexdigest()}), encoding="utf-8"
    )
    paths.overrides.write_text(
        json.dumps({"domains": {}, "events": {}, "field_defaults": {}, "operations": {}}), encoding="utf-8"
    )

    assert generate(paths=paths) is True
    assert "class HealthResult" in (paths.generated / "protocol.py").read_text(encoding="utf-8")
    assert "SCHEMA_PACKAGE_VERSION = '1.0.0'" in (paths.generated / "version.py").read_text(encoding="utf-8")
    assert (paths.generated / "clients" / "root.py").exists()
    assert not (paths.generated / "events.py").exists()

    assert generate(paths=paths) is False
    assert generate(check=True, paths=paths) is False

    (paths.generated / "protocol.py").write_text("stale", encoding="utf-8")
    with pytest.raises(SystemExit, match="generated files are stale"):
        generate(check=True, paths=paths)
