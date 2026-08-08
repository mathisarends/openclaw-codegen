import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen

from generator.types import GenerationPaths

_PACKAGE_NAME = "@openclaw/gateway-protocol"
_UNPKG_ROOT = "https://unpkg.com"
_PACKAGE_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_PATHS = GenerationPaths.from_package_root(_PACKAGE_ROOT)
_EXACT_VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?(?:\+[0-9A-Za-z.-]+)?$")


def download_schema(*, version: str, paths: GenerationPaths = _DEFAULT_PATHS) -> bool:
    """Download a published schema version and update its pin metadata."""
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
    _validate_downloaded_schema(schema, schema_url)
    metadata = {
        "package": _PACKAGE_NAME,
        "version": resolved_version,
        "source": schema_url,
        "sha256": hashlib.sha256(schema).hexdigest(),
    }
    metadata_content = (json.dumps(metadata, indent=2) + "\n").encode()
    return _write_if_changed(paths.schema, schema) | _write_if_changed(paths.metadata, metadata_content)


def _fetch_bytes(url: str) -> bytes:
    with urlopen(url) as response:  # noqa: S310 - the fixed HTTPS host is intentional
        return response.read()


def _validate_downloaded_schema(schema: bytes, source: str) -> None:
    try:
        document = json.loads(schema)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"invalid JSON schema downloaded from {source}") from error
    if not isinstance(document, dict) or not isinstance(document.get("definitions"), dict):
        raise RuntimeError(f"downloaded schema from {source} has no definitions object")
    if not isinstance(document.get("methods"), dict):
        raise RuntimeError(f"downloaded schema from {source} has no methods object")


def _write_if_changed(path: Path, content: bytes) -> bool:
    if path.exists() and path.read_bytes() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return True
