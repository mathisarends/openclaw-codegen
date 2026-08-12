"""Load and validate the inputs used by the client generator."""

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import cast

from openclaw_codegen.generator.types import (
    Definitions,
    GenerationPaths,
    GeneratorOverrides,
    JsonObject,
    ProtocolSchema,
)


@dataclass(frozen=True)
class GenerationInput:
    schema: ProtocolSchema
    metadata: JsonObject
    overrides: GeneratorOverrides
    definitions: Definitions
    schema_digest: str
    schema_version: str


def load_generation_input(paths: GenerationPaths) -> GenerationInput:
    raw_schema = paths.schema.read_bytes()
    metadata = _read_json(paths.metadata)
    schema_digest = _validate_schema_digest(raw_schema, metadata)
    schema_version = metadata.get("version")
    if not isinstance(schema_version, str):
        raise RuntimeError("schema metadata has no package version")

    schema = cast(ProtocolSchema, json.loads(raw_schema))
    overrides = cast(GeneratorOverrides, _read_json(paths.overrides))
    definitions = {**schema["definitions"], **overrides.get("model_definitions", {})}
    _validate_operation_overrides(overrides["operations"], definitions)
    return GenerationInput(schema, metadata, overrides, definitions, schema_digest, schema_version)


def _read_json(path: Path) -> JsonObject:
    return json.loads(path.read_text(encoding="utf-8"))


def _validate_schema_digest(raw_schema: bytes, metadata: JsonObject) -> str:
    digest = hashlib.sha256(raw_schema).hexdigest()
    if digest != metadata["sha256"]:
        raise RuntimeError(f"schema SHA-256 mismatch: expected {metadata['sha256']}, got {digest}")
    return digest


def _validate_operation_overrides(operation_overrides: dict[str, JsonObject], definitions: Definitions) -> None:
    """Reject overrides naming a model that neither the schema nor `model_definitions` defines."""
    for method, override in operation_overrides.items():
        for slot in ("params", "result"):
            model = override.get(slot)
            if model is None:
                continue
            if not isinstance(model, str):
                raise RuntimeError(f"operation override {method}.{slot} must be a model name, got {model!r}")
            if ":" not in model and model not in definitions:
                raise RuntimeError(f"operation override {method}.{slot} names unknown model {model!r}")
