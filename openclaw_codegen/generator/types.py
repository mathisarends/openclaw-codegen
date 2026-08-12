from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal, NotRequired, Self, TypedDict

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
    def from_package_root(cls, package_root: Path) -> Self:
        return cls(
            package_root=package_root,
            schema=package_root / "schema" / "protocol.schema.json",
            metadata=package_root / "schema" / "metadata.json",
            overrides=package_root / "schema" / "overrides.json",
            generated=package_root / "openclaw_codegen" / "generated",
            report=package_root / "schema" / "generation-report.json",
        )

    @classmethod
    def from_installed_package(cls, package_dir: Path) -> Self:
        """Locate bundled inputs and outputs inside an installed package."""
        return cls(
            package_root=package_dir.parent,
            schema=package_dir / "schema" / "protocol.schema.json",
            metadata=package_dir / "schema" / "metadata.json",
            overrides=package_dir / "schema" / "overrides.json",
            generated=package_dir / "generated",
            report=package_dir / "schema" / "generation-report.json",
        )

    @classmethod
    def default(cls) -> Self:
        """Use repository paths from source and bundled paths from an installation."""
        package_dir = Path(__file__).resolve().parents[1]
        repository_root = package_dir.parent
        if (repository_root / "schema" / "protocol.schema.json").is_file():
            return cls.from_package_root(repository_root)
        return cls.from_installed_package(package_dir)
