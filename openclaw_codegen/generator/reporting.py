"""Build the machine-readable generation report."""

from openclaw_codegen.generator.operation_generation import unresolved_operations
from openclaw_codegen.generator.types import (
    GeneratorOverrides,
    InferredOperations,
    JsonObject,
    MatchOrigin,
    ProtocolSchema,
)


def build_generation_report(
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
