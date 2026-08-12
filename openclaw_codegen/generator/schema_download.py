"""Update the locally pinned protocol schema from the package registry."""

import hashlib
import json
from pathlib import Path

from openclaw_codegen.generator.schema_registry import fetch_schema_release
from openclaw_codegen.generator.types import GenerationPaths

_DEFAULT_PATHS = GenerationPaths.default()


def download_schema(*, version: str, paths: GenerationPaths = _DEFAULT_PATHS) -> bool:
    """Download a published schema version and update its pin metadata."""
    release = fetch_schema_release(version)
    metadata = {
        "package": release.package,
        "version": release.version,
        "source": release.source,
        "sha256": hashlib.sha256(release.schema).hexdigest(),
    }
    metadata_content = (json.dumps(metadata, indent=2) + "\n").encode()
    return _write_if_changed(paths.schema, release.schema) | _write_if_changed(paths.metadata, metadata_content)


def _write_if_changed(path: Path, content: bytes) -> bool:
    if path.exists() and path.read_bytes() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return True
