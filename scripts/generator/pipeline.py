import hashlib
import json
import subprocess
from pathlib import Path
from typing import cast

from generator.model_generation import ModelGenerator
from generator.module_rendering import (
    render_client_accessors,
    render_clients_init,
    render_events,
    render_requester,
    render_root_init,
    render_version,
)
from generator.naming import snake_case
from generator.operation_generation import infer_operations, render_client, unresolved_operations
from generator.types import (
    Definitions,
    DomainConfig,
    GenerationPaths,
    GeneratorOverrides,
    InferredOperations,
    JsonObject,
    MatchOrigin,
    MethodMetadata,
    ProtocolSchema,
)

_PACKAGE_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_PATHS = GenerationPaths.from_package_root(_PACKAGE_ROOT)


def generate(*, check: bool = False, paths: GenerationPaths = _DEFAULT_PATHS) -> bool:
    """Generate all configured domains, or verify that their outputs are current."""
    raw_schema = paths.schema.read_bytes()
    metadata = _read_json(paths.metadata)
    digest = _validate_schema(raw_schema, metadata)
    schema_package_version = metadata.get("version")
    if not isinstance(schema_package_version, str):
        raise RuntimeError("schema metadata has no package version")
    schema = cast(ProtocolSchema, json.loads(raw_schema))
    overrides = cast(GeneratorOverrides, _read_json(paths.overrides))
    definitions = {**schema["definitions"], **overrides.get("model_definitions", {})}
    _validate_operation_overrides(overrides["operations"], definitions)
    inferred = infer_operations(schema, overrides["operations"])
    domains = _discover_domains(schema["methods"])
    outputs = _render_clients(schema, overrides, definitions, inferred, paths, domains)
    model_generator = ModelGenerator(definitions, overrides["field_defaults"])
    outputs[paths.generated / "protocol.py"] = model_generator.render(list(definitions))
    outputs[paths.generated / "version.py"] = render_version(schema_package_version)
    clients_dir = paths.generated / "clients"
    outputs[clients_dir / "_requester.py"] = render_requester()
    outputs[clients_dir / "_accessors.py"] = render_client_accessors(domains)
    outputs[clients_dir / "__init__.py"] = render_clients_init(domains)
    event_domain = _event_domain(overrides["domains"])
    if event_domain is not None:
        outputs[paths.generated / "events.py"] = render_events(event_domain, overrides["events"])
    outputs[paths.generated / "__init__.py"] = render_root_init(has_event_registry=event_domain is not None)
    report = _generation_report(schema, metadata, overrides, inferred, set(definitions), digest, domains)
    outputs[paths.report] = json.dumps(report, indent=2, sort_keys=True) + "\n"
    formatted_outputs = {
        path: _format_python(path, content, package_root=paths.package_root) if path.suffix == ".py" else content
        for path, content in outputs.items()
    }
    changed = _apply_outputs(formatted_outputs, _obsolete_outputs(paths, domains), check=check)
    if check and changed:
        raise SystemExit("generated files are stale; run: python scripts/generate.py")
    return changed


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


def _read_json(path: Path) -> JsonObject:
    return json.loads(path.read_text(encoding="utf-8"))


def _format_python(path: Path, content: str, *, package_root: Path) -> str:
    candidates = [
        package_root / ".venv" / "Scripts" / "ruff.exe",
        package_root / ".venv" / "bin" / "ruff",
    ]
    ruff = next((candidate for candidate in candidates if candidate.exists()), None)
    if ruff is None:
        raise RuntimeError("Ruff is required to generate the OpenClaw client")
    checked = subprocess.run(
        [str(ruff), "check", "--fix", "--fix-only", "--stdin-filename", str(path), "-"],
        cwd=package_root,
        input=content,
        capture_output=True,
        check=True,
        text=True,
    ).stdout
    return subprocess.run(
        [str(ruff), "format", "--stdin-filename", str(path), "-"],
        cwd=package_root,
        input=checked,
        capture_output=True,
        check=True,
        text=True,
    ).stdout


def _validate_schema(raw_schema: bytes, metadata: JsonObject) -> str:
    digest = hashlib.sha256(raw_schema).hexdigest()
    if digest != metadata["sha256"]:
        raise RuntimeError(f"schema SHA-256 mismatch: expected {metadata['sha256']}, got {digest}")
    return digest


def _event_domain(domain_configs: dict[str, DomainConfig]) -> str | None:
    event_domains = [domain for domain, config in domain_configs.items() if config.get("event_registry", False)]
    if len(event_domains) > 1:
        raise RuntimeError("only one generated domain can expose the root event registry")
    return event_domains[0] if event_domains else None


def _render_clients(
    schema: ProtocolSchema,
    overrides: GeneratorOverrides,
    definitions: Definitions,
    inferred: InferredOperations,
    paths: GenerationPaths,
    domains: dict[str, str | None],
) -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    model_generator = ModelGenerator(definitions, overrides["field_defaults"])
    model_generator.render(list(definitions))
    for domain, wire_domain in domains.items():
        selected_methods = _domain_methods(schema["methods"], wire_domain)
        outputs[paths.generated / "clients" / f"{domain}.py"] = render_client(
            domain,
            selected_methods,
            inferred,
            overrides["operations"],
            definitions,
            model_generator,
        )
    return outputs


def _discover_domains(methods: dict[str, MethodMetadata]) -> dict[str, str | None]:
    domains: dict[str, str | None] = {}
    for method in methods:
        wire_domain = method.split(".", 1)[0] if "." in method else None
        domain = snake_case(wire_domain) if wire_domain is not None else "root"
        existing = domains.setdefault(domain, wire_domain)
        if existing != wire_domain:
            raise RuntimeError(f"RPC domains {existing!r} and {wire_domain!r} both map to {domain!r}")
    return domains


def _domain_methods(methods: dict[str, MethodMetadata], wire_domain: str | None) -> list[str]:
    if wire_domain is None:
        return [method for method in methods if "." not in method]
    return [method for method in methods if method.startswith(f"{wire_domain}.")]


def _generation_report(
    schema: ProtocolSchema,
    metadata: JsonObject,
    overrides: GeneratorOverrides,
    inferred: InferredOperations,
    generated_models: set[str],
    digest: str,
    domains: dict[str, str | None],
) -> JsonObject:
    unresolved = unresolved_operations(schema, inferred)
    return {
        "schema": {"version": metadata["version"], "sha256": digest},
        "counts": {
            "definitions": len(schema["definitions"]),
            "methods": len(schema["methods"]),
            "generated_models": len(generated_models),
            "generated_operations": len(schema["methods"]),
            "generated_domains": len(domains),
            "inferred_params": sum(value["params"] is not None for value in inferred.values()),
            "inferred_results": sum(value["result"] is not None for value in inferred.values()),
            "naming_mismatches": len(unresolved["naming_mismatch"]),
            "schema_gaps": len(unresolved["schema_gap"]),
        },
        "normalized_matches": _matches_by_origin(inferred, "normalized"),
        "unresolved_methods": unresolved,
        "known_events": overrides["events"],
        "notes": [
            "The published schema has no event-name registry; event mappings require explicit overrides.",
            "The published schema has no per-method payload contract; params and result models are matched by name.",
            "unresolved_methods.naming_mismatch lists unclaimed models close enough to be fixed by an override.",
            "unresolved_methods.schema_gap lists methods the schema describes no model for at all.",
            "Anonymous nested object schemas are represented as dict[str, Any].",
            "JSON Schema conditional constraints are left to the gateway for runtime validation.",
        ],
    }


def _matches_by_origin(inferred: InferredOperations, origin: MatchOrigin) -> dict[str, dict[str, str]]:
    matches: dict[str, dict[str, str]] = {}
    for method, models in inferred.items():
        slots = {
            slot: name
            for slot, name, slot_origin in (
                ("params", models["params"], models["params_origin"]),
                ("result", models["result"], models["result_origin"]),
            )
            if slot_origin == origin and name is not None
        }
        if slots:
            matches[method] = slots
    return matches


def _obsolete_outputs(paths: GenerationPaths, domains: list[str]) -> list[Path]:
    outputs = [
        paths.generated / "models.py",
        paths.generated / "operations.py",
        paths.generated / "namespaces.py",
        paths.generated / "namespaces" / "__init__.py",
    ]
    outputs.extend(paths.generated / "namespaces" / f"{domain}.py" for domain in domains)
    outputs.extend(paths.generated / domain / "models.py" for domain in domains)
    for domain in domains:
        outputs.extend(
            [
                paths.generated / domain / "__init__.py",
                paths.generated / domain / "client.py",
                paths.generated / domain / "events.py",
            ]
        )
    return outputs


def _apply_outputs(outputs: dict[Path, str], obsolete: list[Path], *, check: bool) -> bool:
    changed = False
    for path in obsolete:
        if path.exists():
            changed = True
            if not check:
                path.unlink()
    for path, content in outputs.items():
        existing = path.read_text(encoding="utf-8") if path.exists() else None
        if existing != content:
            changed = True
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
    return changed
