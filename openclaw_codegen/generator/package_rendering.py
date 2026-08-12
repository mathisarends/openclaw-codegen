"""Render the complete generated client package in memory."""

import json
from dataclasses import dataclass
from pathlib import Path

from openclaw_codegen.generator.model_generation import ModelGenerator
from openclaw_codegen.generator.module_rendering import (
    render_client_accessors,
    render_clients_init,
    render_events,
    render_requester,
    render_root_init,
    render_version,
)
from openclaw_codegen.generator.naming import snake_case
from openclaw_codegen.generator.operation_generation import render_client
from openclaw_codegen.generator.reporting import build_generation_report
from openclaw_codegen.generator.schema import GenerationInput
from openclaw_codegen.generator.types import GenerationPaths, InferredOperations, MethodMetadata


@dataclass(frozen=True)
class RenderedPackage:
    outputs: dict[Path, str]
    domains: dict[str, str | None]


def render_package(
    source: GenerationInput,
    inferred: InferredOperations,
    paths: GenerationPaths,
) -> RenderedPackage:
    domains = _discover_domains(source.schema["methods"])
    model_generator = ModelGenerator(source.definitions, source.overrides["field_defaults"])
    outputs = _render_clients(source, inferred, paths, domains, model_generator)
    outputs[paths.generated / "protocol.py"] = model_generator.render(list(source.definitions))
    outputs[paths.generated / "version.py"] = render_version(source.schema_version)

    clients_dir = paths.generated / "clients"
    outputs[clients_dir / "_requester.py"] = render_requester()
    outputs[clients_dir / "_accessors.py"] = render_client_accessors(domains)
    outputs[clients_dir / "__init__.py"] = render_clients_init(domains)

    events = source.overrides["events"]
    if events:
        outputs[paths.generated / "events.py"] = render_events(events)
    outputs[paths.generated / "__init__.py"] = render_root_init(has_event_registry=bool(events))

    report = build_generation_report(
        source.schema,
        source.metadata,
        source.overrides,
        inferred,
        set(source.definitions),
        source.schema_digest,
        domains,
    )
    outputs[paths.report] = json.dumps(report, indent=2, sort_keys=True) + "\n"
    return RenderedPackage(outputs, domains)


def _render_clients(
    source: GenerationInput,
    inferred: InferredOperations,
    paths: GenerationPaths,
    domains: dict[str, str | None],
    model_generator: ModelGenerator,
) -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    model_generator.render(list(source.definitions))
    for domain, wire_domain in domains.items():
        methods = _domain_methods(source.schema["methods"], wire_domain)
        outputs[paths.generated / "clients" / f"{domain}.py"] = render_client(
            domain,
            methods,
            inferred,
            source.overrides["operations"],
            source.definitions,
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
