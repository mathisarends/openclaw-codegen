from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, NotRequired, TypedDict

type JsonObject = dict[str, Any]
type Definitions = dict[str, JsonObject]

type MatchOrigin = Literal["exact", "normalized", "override"]


class OperationModels(TypedDict):
    params: str | None
    params_origin: MatchOrigin | None
    result: str | None
    result_origin: MatchOrigin | None


type InferredOperations = dict[str, OperationModels]


class UnresolvedOperations(TypedDict):
    """Methods without a params or result model, split by why the model is missing."""

    naming_mismatch: dict[str, dict[str, str]]
    schema_gap: list[str]


class MethodMetadata(TypedDict):
    since: NotRequired[str]
    scope: NotRequired[str]


class DomainConfig(TypedDict):
    event_registry: NotRequired[bool]


class ProtocolSchema(TypedDict):
    definitions: Definitions
    methods: dict[str, MethodMetadata]


class GeneratorOverrides(TypedDict):
    domains: dict[str, DomainConfig]
    events: dict[str, str]
    field_defaults: dict[str, str]
    model_definitions: NotRequired[Definitions]
    operations: dict[str, JsonObject]


@dataclass(frozen=True)
class GenerationPaths:
    """All filesystem locations touched by one generation run."""

    package_root: Path
    schema: Path
    metadata: Path
    overrides: Path
    generated: Path
    report: Path

    @classmethod
    def from_package_root(cls, package_root: Path) -> "GenerationPaths":
        return cls(
            package_root=package_root,
            schema=package_root / "schema" / "protocol.schema.json",
            metadata=package_root / "schema" / "metadata.json",
            overrides=package_root / "schema" / "overrides.json",
            generated=package_root / "src" / "openclaw_codegen" / "generated",
            report=package_root / "schema" / "generation-report.json",
        )
