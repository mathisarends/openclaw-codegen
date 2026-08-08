import json
from collections.abc import AsyncIterator, Callable, Coroutine
from contextlib import asynccontextmanager
from typing import Any

import pytest
from websockets.asyncio.server import ServerConnection, serve

from openclaw_codegen import (
    SCHEMA_PACKAGE_VERSION,
    ChatFinalEvent,
    ChatSendParams,
    OpenClawClient,
    OpenClawCompatibilityWarning,
    OpenClawGatewayError,
    OpenClawNotConnectedError,
    OpenClawProtocolError,
    parse_event_payload,
)
from openclaw_codegen.generated.clients.agents import AgentsClient
from openclaw_codegen.generated.clients.chat import ChatClient
from openclaw_codegen.generated.clients.root import RootClient

GatewayHandler = Callable[[ServerConnection], Coroutine[Any, Any, None]]


@asynccontextmanager
async def _run_gateway(handler: GatewayHandler) -> AsyncIterator[str]:
    async with serve(handler, "127.0.0.1", 0) as server:
        port = server.sockets[0].getsockname()[1]
        yield f"ws://127.0.0.1:{port}"


def _hello(
    request_id: str,
    *,
    server_version: str = SCHEMA_PACKAGE_VERSION,
    protocol: int = 4,
) -> dict[str, object]:
    return {
        "type": "res",
        "id": request_id,
        "ok": True,
        "payload": {
            "type": "hello-ok",
            "protocol": protocol,
            "server": {"version": server_version, "connId": "connection-1"},
            "features": {"methods": ["chat.send", "health"], "events": ["chat"]},
            "snapshot": {
                "presence": [],
                "health": {},
                "stateVersion": {"presence": 0, "health": 0},
                "uptimeMs": 0,
            },
            "auth": {"role": "operator", "scopes": ["operator.read", "operator.write"]},
            "policy": {
                "maxPayload": 26214400,
                "maxBufferedBytes": 52428800,
                "tickIntervalMs": 15000,
            },
        },
    }


async def _handshake(
    connection: ServerConnection,
    *,
    server_version: str = SCHEMA_PACKAGE_VERSION,
    protocol: int = 4,
) -> None:
    await connection.send(
        json.dumps(
            {
                "type": "event",
                "event": "connect.challenge",
                "payload": {"nonce": "nonce", "ts": 1737264000000},
            }
        )
    )
    request = json.loads(await connection.recv())
    assert request["method"] == "connect"
    assert request["params"]["minProtocol"] == 4
    assert request["params"]["client"]["id"] == "gateway-client"
    await connection.send(json.dumps(_hello(request["id"], server_version=server_version, protocol=protocol)))


def test_client_exposes_generated_clients_directly_and_lazily() -> None:
    client = OpenClawClient()
    assert isinstance(client.chat, ChatClient)
    assert isinstance(client.agents, AgentsClient)
    assert isinstance(client.root, RootClient)
    assert client.chat is client.chat
    assert not hasattr(client, "send_chat")
    assert not hasattr(client, "stream_chat")
    assert not hasattr(client, "run_chat")


@pytest.mark.asyncio
async def test_request_raises_structured_gateway_error() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection)
        request = json.loads(await connection.recv())
        await connection.send(
            json.dumps(
                {
                    "type": "res",
                    "id": request["id"],
                    "ok": False,
                    "error": {
                        "code": "FORBIDDEN",
                        "message": "missing scope",
                        "details": {
                            "code": "MISSING_SCOPE",
                            "missingScope": "operator.admin",
                            "requiredScopes": ["operator.admin"],
                        },
                    },
                }
            )
        )
        await connection.wait_closed()

    async with _run_gateway(handler) as url, OpenClawClient(url) as client:
        assert client.hello.server.version == SCHEMA_PACKAGE_VERSION
        assert client.hello.server.conn_id == "connection-1"
        assert client.hello.features.methods == ["chat.send", "health"]
        with pytest.raises(OpenClawGatewayError) as raised:
            await client.request("config.get")
        assert raised.value.code == "FORBIDDEN"
        assert raised.value.error.details["missingScope"] == "operator.admin"


@pytest.mark.asyncio
async def test_generated_clients_send_exact_rpc_methods() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection)

        history_request = json.loads(await connection.recv())
        assert history_request["method"] == "chat.history"
        assert history_request["params"] == {"sessionKey": "session-1"}
        await connection.send(
            json.dumps(
                {
                    "type": "res",
                    "id": history_request["id"],
                    "ok": True,
                    "payload": {"messages": []},
                }
            )
        )

        send_request = json.loads(await connection.recv())
        assert send_request["method"] == "chat.send"
        assert send_request["params"]["sessionKey"] == "session-1"
        assert send_request["params"]["message"] == "Hello"
        assert send_request["params"]["idempotencyKey"]
        await connection.send(
            json.dumps(
                {
                    "type": "res",
                    "id": send_request["id"],
                    "ok": True,
                    "payload": {"runId": "run-1", "status": "started"},
                }
            )
        )

        sessions_request = json.loads(await connection.recv())
        assert sessions_request["method"] == "sessions.list"
        assert sessions_request["params"] == {"limit": 10}
        await connection.send(
            json.dumps(
                {
                    "type": "res",
                    "id": sessions_request["id"],
                    "ok": True,
                    "payload": {"sessions": []},
                }
            )
        )
        await connection.wait_closed()

    async with _run_gateway(handler) as url, OpenClawClient(url) as client:
        history = await client.chat.history(session_key="session-1")
        assert history == {"messages": []}
        run = await client.chat.send(session_key="session-1", message="Hello")
        assert run.run_id == "run-1"
        sessions = await client.sessions.list(limit=10)
        assert sessions == {"sessions": []}


def test_rejects_plaintext_remote_gateway() -> None:
    with pytest.raises(ValueError, match="plaintext"):
        OpenClawClient("ws://example.com:18789")


@pytest.mark.parametrize("url", ["http://127.0.0.1:18789", "ws://", "not-a-url"])
def test_rejects_urls_without_a_supported_websocket_scheme_and_host(url: str) -> None:
    with pytest.raises(ValueError, match="ws:// or wss://"):
        OpenClawClient(url)


@pytest.mark.parametrize("url", ["wss://example.com", "ws://localhost:18789", "ws://127.0.0.1:18789"])
def test_accepts_secure_remote_and_plaintext_loopback_urls(url: str) -> None:
    OpenClawClient(url)


def test_constructor_rejects_more_than_one_auth_method() -> None:
    with pytest.raises(ValueError, match="only one of token, password, or device_token"):
        OpenClawClient(token="a", password="b")


@pytest.mark.parametrize("kwargs", [{"request_timeout": 0}, {"handshake_timeout": -1}])
def test_constructor_rejects_non_positive_timeouts(kwargs: dict[str, float]) -> None:
    with pytest.raises(ValueError, match="must be greater than zero"):
        OpenClawClient(**kwargs)


def test_hello_raises_before_the_handshake_completes() -> None:
    client = OpenClawClient()
    assert client.is_connected is False
    with pytest.raises(OpenClawNotConnectedError):
        _ = client.hello


@pytest.mark.asyncio
async def test_request_before_connect_raises_not_connected() -> None:
    client = OpenClawClient()
    with pytest.raises(OpenClawNotConnectedError):
        await client.request("health")


@pytest.mark.asyncio
async def test_close_without_connecting_is_a_safe_no_op() -> None:
    await OpenClawClient().close()


@pytest.mark.asyncio
async def test_is_connected_reflects_the_connection_lifecycle() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection)
        await connection.wait_closed()

    async with _run_gateway(handler) as url:
        async with OpenClawClient(url) as client:
            assert client.is_connected is True
        assert client.is_connected is False


@pytest.mark.asyncio
async def test_connect_warns_for_a_newer_gateway_version() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection, server_version="2026.8.0")
        await connection.wait_closed()

    async with _run_gateway(handler) as url:
        with pytest.warns(OpenClawCompatibilityWarning, match="newer version"):
            async with OpenClawClient(url):
                pass


@pytest.mark.asyncio
async def test_strict_version_requires_an_exact_gateway_version() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection, server_version="2026.8.0")
        await connection.wait_closed()

    async with _run_gateway(handler) as url:
        with pytest.raises(OpenClawProtocolError, match="does not match client schema version"):
            async with OpenClawClient(url, strict_version=True):
                pass


@pytest.mark.asyncio
async def test_connect_rejects_an_incompatible_gateway_major_version() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection, server_version="2027.1.0")
        await connection.wait_closed()

    async with _run_gateway(handler) as url:
        with pytest.raises(OpenClawProtocolError, match="is incompatible with client schema version"):
            async with OpenClawClient(url):
                pass


@pytest.mark.asyncio
async def test_connect_rejects_a_different_negotiated_protocol() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection, protocol=5)
        await connection.wait_closed()

    async with _run_gateway(handler) as url:
        with pytest.raises(OpenClawProtocolError, match="requires protocol 4"):
            async with OpenClawClient(url):
                pass


@pytest.mark.asyncio
async def test_connect_rejects_an_unexpected_challenge_event() -> None:
    async def handler(connection: ServerConnection) -> None:
        await connection.send(json.dumps({"type": "event", "event": "not.challenge", "payload": {}}))
        await connection.wait_closed()

    async with _run_gateway(handler) as url:
        with pytest.raises(OpenClawProtocolError, match="expected connect.challenge"):
            async with OpenClawClient(url):
                pass


@pytest.mark.asyncio
async def test_connect_rejects_an_invalid_challenge_payload() -> None:
    async def handler(connection: ServerConnection) -> None:
        await connection.send(json.dumps({"type": "event", "event": "connect.challenge", "payload": {}}))
        await connection.wait_closed()

    async with _run_gateway(handler) as url:
        with pytest.raises(OpenClawProtocolError, match="invalid connect challenge"):
            async with OpenClawClient(url):
                pass


@pytest.mark.asyncio
async def test_connect_rejects_a_mismatched_response_id() -> None:
    async def handler(connection: ServerConnection) -> None:
        await connection.send(
            json.dumps({"type": "event", "event": "connect.challenge", "payload": {"nonce": "n", "ts": 0}})
        )
        await connection.recv()
        await connection.send(json.dumps(_hello("wrong-id")))
        await connection.wait_closed()

    async with _run_gateway(handler) as url:
        with pytest.raises(OpenClawProtocolError, match="does not match the request id"):
            async with OpenClawClient(url):
                pass


@pytest.mark.asyncio
async def test_connect_rejects_an_invalid_hello_response() -> None:
    async def handler(connection: ServerConnection) -> None:
        await connection.send(
            json.dumps({"type": "event", "event": "connect.challenge", "payload": {"nonce": "n", "ts": 0}})
        )
        request = json.loads(await connection.recv())
        await connection.send(
            json.dumps({"type": "res", "id": request["id"], "ok": True, "payload": {"type": "hello-ok"}})
        )
        await connection.wait_closed()

    async with _run_gateway(handler) as url:
        with pytest.raises(OpenClawProtocolError, match="invalid connect response"):
            async with OpenClawClient(url):
                pass


@pytest.mark.asyncio
async def test_request_times_out_when_the_gateway_never_responds() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection)
        await connection.recv()
        await connection.wait_closed()

    async with _run_gateway(handler) as url, OpenClawClient(url, request_timeout=0.05) as client:
        with pytest.raises(TimeoutError, match="timed out"):
            await client.request("health")


@pytest.mark.asyncio
async def test_request_falls_back_to_an_unknown_error_without_structured_details() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection)
        request = json.loads(await connection.recv())
        await connection.send(json.dumps({"type": "res", "id": request["id"], "ok": False}))
        await connection.wait_closed()

    async with _run_gateway(handler) as url, OpenClawClient(url) as client:
        with pytest.raises(OpenClawGatewayError) as raised:
            await client.request("health")
        assert raised.value.code == "UNKNOWN"


@pytest.mark.asyncio
async def test_request_serializes_plain_mapping_params_as_is() -> None:
    async def handler(connection: ServerConnection) -> None:
        await _handshake(connection)
        request = json.loads(await connection.recv())
        assert request["params"] == {"foo": "bar"}
        await connection.send(json.dumps({"type": "res", "id": request["id"], "ok": True, "payload": None}))
        await connection.wait_closed()

    async with _run_gateway(handler) as url, OpenClawClient(url) as client:
        await client.request("health", {"foo": "bar"})


def test_chat_params_use_gateway_aliases() -> None:
    params = ChatSendParams(session_key="session-1", message="Hi", fast_mode="auto")
    dumped = params.model_dump(by_alias=True)
    assert dumped["sessionKey"] == "session-1"
    assert dumped["fastMode"] == "auto"


def test_chat_event_discriminator_selects_concrete_model() -> None:
    event = parse_event_payload(
        "chat",
        {
            "runId": "run-1",
            "sessionKey": "session-1",
            "seq": 1,
            "state": "final",
        },
    )
    assert isinstance(event, ChatFinalEvent)
