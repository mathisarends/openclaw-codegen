"""Fetch an exact OpenClaw protocol schema release from the package registry."""

import json
import re
from dataclasses import dataclass
from urllib.parse import quote
from urllib.request import urlopen

_PACKAGE_NAME = "@openclaw/gateway-protocol"
_UNPKG_ROOT = "https://unpkg.com"
_EXACT_VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?(?:\+[0-9A-Za-z.-]+)?$")


@dataclass(frozen=True)
class SchemaRelease:
    package: str
    version: str
    source: str
    schema: bytes


def fetch_schema_release(version: str) -> SchemaRelease:
    if not _EXACT_VERSION_PATTERN.fullmatch(version):
        raise ValueError("schema version must be an explicit published version, for example 2026.7.2-beta.7")

    requested_version = quote(version, safe="")
    package_url = f"{_UNPKG_ROOT}/{_PACKAGE_NAME}@{requested_version}/package.json"
    package_document = json.loads(_fetch_bytes(package_url))
    if package_document.get("name") != _PACKAGE_NAME or not isinstance(package_document.get("version"), str):
        raise RuntimeError(f"unexpected package metadata downloaded from {package_url}")

    resolved_version = package_document["version"]
    if resolved_version != version:
        raise RuntimeError(f"requested schema version {version!r}, but the registry resolved {resolved_version!r}")
    schema_url = f"{_UNPKG_ROOT}/{_PACKAGE_NAME}@{resolved_version}/protocol.schema.json"
    schema = _fetch_bytes(schema_url)
    _validate_schema_document(schema, schema_url)
    return SchemaRelease(_PACKAGE_NAME, resolved_version, schema_url, schema)


def _fetch_bytes(url: str) -> bytes:
    with urlopen(url) as response:  # noqa: S310 - the fixed HTTPS host is intentional
        return response.read()


def _validate_schema_document(schema: bytes, source: str) -> None:
    try:
        document = json.loads(schema)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"invalid JSON schema downloaded from {source}") from error
    if not isinstance(document, dict) or not isinstance(document.get("definitions"), dict):
        raise RuntimeError(f"downloaded schema from {source} has no definitions object")
    if not isinstance(document.get("methods"), dict):
        raise RuntimeError(f"downloaded schema from {source} has no methods object")
