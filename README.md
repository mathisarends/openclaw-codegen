# openclaw-codegen

Python client for the [OpenClaw](https://github.com/) Gateway API.

The transport, connection lifecycle, and local connection defaults are handwritten. All protocol
models, all 350 RPC operations across 55 clients, and known event payload mappings are generated
from the pinned OpenClaw Gateway schema. Domain clients are exposed directly and created lazily, so
the transport client does not need a handwritten registry.

```python
async with OpenClawClient(token="...") as client:
    history = await client.chat.history(session_key="agent:main:main")
    run = await client.chat.send(session_key="agent:main:main", message="Hello")
    sessions = await client.sessions.list()
    agents = await client.agents.list()
```

## Installation

Not yet published to PyPI. Install from a local checkout:

```bash
uv add /path/to/openclaw-codegen
# or, editable:
uv pip install -e /path/to/openclaw-codegen
```

## Development

```bash
uv sync --dev
uv run pytest
uv run ruff check .
```

## Regenerating the client

Regenerate offline from `schema/protocol.schema.json`:

```console
python scripts/generate.py
```

Download an explicit published schema version, pin its package version and SHA-256, and regenerate:

```bash
python scripts/generate.py --download-schema 2026.7.2-beta.7
```

Floating distribution tags such as `beta` and `latest` are rejected so schema updates remain
reproducible.

The generated `SCHEMA_PACKAGE_VERSION` constant identifies the exact protocol package used by the
client. During the handshake, gateways with a different version in the same release major emit an
`OpenClawCompatibilityWarning`; different protocol or release majors are rejected. Pass
`strict_version=True` to `OpenClawClient` to require an exact gateway/schema version match.

Use `--check` in CI to fail when generated files are stale. `schema/metadata.json` records the
immutable package version, source URL, and SHA-256. `schema/overrides.json` contains the visible
exceptions that the schema cannot express. `schema/generation-report.json` lists unresolved methods
and explains intentionally lossy mappings.

To update the protocol, replace the schema with a concrete published version, update its metadata
hash, regenerate, and review the schema and generated diffs together.

## Limitations

This client is a **best-effort projection** of the OpenClaw Gateway protocol onto Python types, not
a hand-verified binding. The generator works from a single published JSON Schema document that has
no explicit per-method payload contracts and no event-name registry, so several things are inferred
rather than known:

- **Untyped payloads.** Anonymous nested object schemas that the source schema doesn't name are
  represented as plain `dict[str, Any]` instead of a model — currently ~190 fields across the
  generated protocol module (see `props`, `client`, `parameters`, `error`, etc. in
  `src/openclaw_codegen/generated/protocol.py`). Reading or writing through those fields gets no
  structural validation or autocomplete; treat them as opaque JSON.
- **Params/result models matched by name, not by contract.** Since the schema doesn't declare which
  model belongs to which RPC method, the generator infers `<Method>Params`/`<Method>Result` pairs by
  naming convention. `schema/generation-report.json` records the result of that inference:
  - `naming_mismatches`: methods with a plausibly-named model the generator declined to bind
    automatically (fix via `schema/overrides.json`, see below).
  - `schema_gaps`: methods the schema describes no model for at all — these operations are typed
    with untyped `dict[str, Any]` params/results, or are missing entirely from the generated client.
  Run `python scripts/generate.py` and inspect the report after any schema update; the counts and
  lists change whenever the upstream schema does.
- **`schema/overrides.json` is a manual patch layer.** It hand-supplies the domain configs, event
  registry entries, field defaults, extra model definitions, and per-operation model bindings that
  the schema itself cannot express. It is maintained by hand against one pinned schema version — it
  is not re-derived automatically, so it can silently go stale (miss a new naming mismatch, bind a
  method to the wrong model) when the schema is updated without also reviewing the override diff.
- **Version drift between client and gateway.** The generated `SCHEMA_PACKAGE_VERSION` constant
  (`src/openclaw_codegen/generated/version.py`) freezes the exact `@openclaw/gateway-protocol`
  version this client was generated from (see `schema/metadata.json`). At connect time
  (`client.py:_validate_gateway_compatibility`):
  - a **different release major** than the gateway's reported version raises immediately — the
    client refuses to talk to a gateway it can't plausibly understand;
  - any other version mismatch (older, newer, or unparsable) only emits an
    `OpenClawCompatibilityWarning` and proceeds — the RPC/event shapes may not actually match what
    the connected gateway sends or expects;
  - pass `strict_version=True` to `OpenClawClient` to turn *any* version mismatch into a hard error
    instead of a warning.
  In short: outside of a major-version guard, this client trusts that the gateway hasn't changed
  shape since the pinned schema was generated. There is no runtime schema negotiation.

Because of these three points, treat this client as a convenience layer generated to cover most of
the protocol (350 of the gateway's RPC methods across 55 domains), not a guarantee of full or
permanently up-to-date coverage. Pin gateway and client versions together, review
`schema/generation-report.json` after regenerating, and fall back to the untyped `dict[str, Any]`
payloads (or a manual override) for anything the generator couldn't resolve.

## Origin

This package was ported from the `openclaw_client` package originally developed inside the `cara`
project, and rebranded as a standalone `openclaw-codegen` distribution.
