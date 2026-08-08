"""Minimal connectivity smoke test against a local OpenClaw gateway.

Run with the gateway already running (see `openclaw gateway status`):

    python examples/quickstart.py

If your gateway uses token auth (the local default), the token is read
automatically from ~/.openclaw/openclaw.json. Pass one explicitly to override:

    python examples/quickstart.py --token <TOKEN>
"""

import argparse
import asyncio
import json
from pathlib import Path

from openclaw_codegen import (
    ChatAbortedEvent,
    ChatDeltaEvent,
    ChatErrorEvent,
    ChatFinalEvent,
    OpenClawClient,
    OpenClawGatewayError,
    parse_event_payload,
)

_DEFAULT_CONFIG_PATH = Path.home() / ".openclaw" / "openclaw.json"


def _discover_token() -> str | None:
    if not _DEFAULT_CONFIG_PATH.exists():
        return None
    config = json.loads(_DEFAULT_CONFIG_PATH.read_text(encoding="utf-8"))
    return config.get("gateway", {}).get("auth", {}).get("token")


async def _wait_for_chat_reply(client: OpenClawClient, run_id: str) -> str:
    text = ""
    async for event in client.events():
        if event.event != "chat":
            continue
        payload = parse_event_payload(event.event, event.payload)
        if payload.run_id != run_id:
            continue
        match payload:
            case ChatDeltaEvent(delta_text=delta_text, replace=True):
                text = delta_text
            case ChatDeltaEvent(delta_text=delta_text):
                text += delta_text
            case ChatFinalEvent():
                return text
            case ChatAbortedEvent():
                raise RuntimeError(payload.error_message or "chat run was aborted")
            case ChatErrorEvent():
                raise RuntimeError(payload.error_message or "chat run failed")


async def main(url: str, token: str | None) -> None:
    async with OpenClawClient(url, token=token) as client:
        hello = client.hello
        print(f"connected: gateway v{hello.server.version}, conn_id={hello.server.conn_id}")
        print(f"protocol: {hello.protocol}")
        print(f"methods: {hello.features.methods}")
        print(f"events: {hello.features.events}")

        try:
            run = await client.chat.send(
                session_key="quickstart-session",
                message="ping",
            )
        except OpenClawGatewayError as error:
            print(f"chat.send failed ({error.error.code}): {error.error.message}")
        else:
            reply = await _wait_for_chat_reply(client, run.run_id)
            print(f"chat reply: {reply!r}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="ws://127.0.0.1:18789")
    parser.add_argument("--token", default=None)
    args = parser.parse_args()
    asyncio.run(main(args.url, args.token or _discover_token()))
