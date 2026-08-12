"""Orchestrate generation of the typed OpenClaw client."""

from openclaw_codegen.generator.operation_generation import infer_operations
from openclaw_codegen.generator.output import apply_outputs, format_outputs, obsolete_outputs
from openclaw_codegen.generator.package_rendering import render_package
from openclaw_codegen.generator.schema import load_generation_input
from openclaw_codegen.generator.types import GenerationPaths

_DEFAULT_PATHS = GenerationPaths.default()


def generate(*, check: bool = False, paths: GenerationPaths = _DEFAULT_PATHS) -> bool:
    """Generate the client package, or verify that its files are current."""
    source = load_generation_input(paths)
    inferred = infer_operations(source.schema, source.overrides["operations"])
    package = render_package(source, inferred, paths)
    outputs = format_outputs(package.outputs, package_root=paths.package_root)
    changed = apply_outputs(outputs, obsolete_outputs(paths, list(package.domains)), check=check)
    if check and changed:
        raise SystemExit("generated files are stale; run: openclaw-codegen")
    return changed
