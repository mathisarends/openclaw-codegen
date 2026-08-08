import hashlib
import json
from pathlib import Path

import pytest
from generator import download_schema, schema_download
from generator.types import GenerationPaths


def test_schema_download_updates_an_explicit_version_pin(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    schema = json.dumps({"definitions": {}, "methods": {}}).encode()
    requested_urls: list[str] = []

    def fetch(url: str) -> bytes:
        requested_urls.append(url)
        if url.endswith("package.json"):
            return json.dumps({"name": "@openclaw/gateway-protocol", "version": "2026.8.0-beta.1"}).encode()
        return schema

    monkeypatch.setattr(schema_download, "_fetch_bytes", fetch)
    paths = GenerationPaths.from_package_root(tmp_path)

    assert download_schema(version="2026.8.0-beta.1", paths=paths)
    assert not download_schema(version="2026.8.0-beta.1", paths=paths)
    assert requested_urls[:2] == [
        "https://unpkg.com/@openclaw/gateway-protocol@2026.8.0-beta.1/package.json",
        "https://unpkg.com/@openclaw/gateway-protocol@2026.8.0-beta.1/protocol.schema.json",
    ]
    assert paths.schema.read_bytes() == schema
    metadata = json.loads(paths.metadata.read_text(encoding="utf-8"))
    assert metadata["version"] == "2026.8.0-beta.1"
    assert metadata["sha256"] == hashlib.sha256(schema).hexdigest()


def test_invalid_schema_download_does_not_replace_pin(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    paths = GenerationPaths.from_package_root(tmp_path)
    paths.schema.parent.mkdir(parents=True)
    paths.schema.write_bytes(b"old schema")
    paths.metadata.write_bytes(b"old metadata")

    responses = iter(
        [
            json.dumps({"name": "@openclaw/gateway-protocol", "version": "2026.8.0"}).encode(),
            b"not JSON",
        ]
    )
    monkeypatch.setattr(schema_download, "_fetch_bytes", lambda _url: next(responses))

    with pytest.raises(RuntimeError, match="invalid JSON schema"):
        download_schema(version="2026.8.0", paths=paths)
    assert paths.schema.read_bytes() == b"old schema"
    assert paths.metadata.read_bytes() == b"old metadata"


def test_download_schema_rejects_unexpected_package_metadata(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(
        schema_download,
        "_fetch_bytes",
        lambda _url: json.dumps({"name": "@some/other-package", "version": "1.0.0"}).encode(),
    )
    paths = GenerationPaths.from_package_root(tmp_path)

    with pytest.raises(RuntimeError, match="unexpected package metadata"):
        download_schema(version="2026.8.0", paths=paths)


@pytest.mark.parametrize("version", ["beta", "latest", "next", ""])
def test_schema_download_rejects_floating_or_empty_versions(version: str, tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="explicit published version"):
        download_schema(version=version, paths=GenerationPaths.from_package_root(tmp_path))


@pytest.mark.parametrize(
    ("document", "expected_message"),
    [
        ({"methods": {}}, "has no definitions object"),
        ({"definitions": {}}, "has no methods object"),
        ([], "has no definitions object"),
    ],
)
def test_validate_downloaded_schema_requires_definitions_and_methods(document: object, expected_message: str) -> None:
    with pytest.raises(RuntimeError, match=expected_message):
        schema_download._validate_downloaded_schema(json.dumps(document).encode(), "https://example.test/schema")
