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

```bash
uv add openclaw-codegen
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

## Origin

This package was ported from the `openclaw_client` package originally developed inside the `cara`
project, and rebranded as a standalone `openclaw-codegen` distribution.
