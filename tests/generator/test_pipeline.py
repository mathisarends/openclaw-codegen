import hashlib
import json
from pathlib import Path

import pytest

from openclaw_codegen.generator import output, package_rendering
from openclaw_codegen.generator.pipeline import generate
from openclaw_codegen.generator.types import GenerationPaths


def test_discover_domains_maps_dotless_methods_to_root() -> None:
    assert package_rendering._discover_domains({"health": {}, "chat.send": {}}) == {"root": None, "chat": "chat"}


def test_discover_domains_rejects_colliding_wire_domains() -> None:
    methods = {"chatRoom.a": {}, "chat_room.b": {}}
    with pytest.raises(RuntimeError, match="RPC domains"):
        package_rendering._discover_domains(methods)


def test_domain_methods_filters_by_prefix_or_selects_dotless_methods() -> None:
    methods = {"health": {}, "chat.send": {}, "chat.history": {}, "sessions.list": {}}
    assert package_rendering._domain_methods(methods, None) == ["health"]
    assert package_rendering._domain_methods(methods, "chat") == ["chat.send", "chat.history"]


def test_generate_end_to_end_writes_expected_outputs_and_detects_drift(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(output, "_format_python", lambda path, content, *, package_root: content)
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
        json.dumps({"events": {}, "field_defaults": {}, "operations": {}}), encoding="utf-8"
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
