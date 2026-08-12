import asyncio
import contextlib
import json
import re
import warnings
from collections.abc import AsyncIterator, Mapping
from types import TracebackType
from typing import Any, Self, overload
from urllib.parse import urlparse

from pydantic import BaseModel, TypeAdapter, ValidationError
from websockets.asyncio.client import ClientConnection, connect
from websockets.exceptions import ConnectionClosed

from openclaw_codegen.connection import (
    PROTOCOL_VERSION,
    ConnectChallenge,
    GatewayAuth,
    GatewayClientInfo,
    OperatorScope,
)
from openclaw_codegen.exceptions import (
    OpenClawClientError,
    OpenClawCompatibilityWarning,
    OpenClawGatewayError,
    OpenClawNotConnectedError,
    OpenClawProtocolError,
)
from openclaw_codegen.generated import OpenClawClients
from openclaw_codegen.generated.protocol import (
    ConnectParams,
    ErrorShape,
    EventFrame,
    GatewayFrame,
    HelloOk,
    RequestFrame,
    ResponseFrame,
)
from openclaw_codegen.generated.version import SCHEMA_PACKAGE_VERSION

type JsonObject = dict[str, Any]

_DEFAULT_GATEWAY_URL = "ws://127.0.0.1:18789"
_DEFAULT_REQUEST_TIMEOUT = 30.0
_DEFAULT_HANDSHAKE_TIMEOUT = 15.0
_DEFAULT_MAX_PAYLOAD = 25 * 1024 * 1024
_VERSION_PATTERN = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:[-+].*)?$")


class OpenClawClient(OpenClawClients):
    """Async WebSocket client for the OpenClaw Gateway protocol v4.

    This first slice targets trusted local backend use with shared-token,
    password, or pre-issued device-token authentication. Device enrollment and
    challenge signing are intentionally not part of the initial scope.
    """

    def __init__(
        self,
        url: str = _DEFAULT_GATEWAY_URL,
        *,
        token: str | None = None,
        password: str | None = None,
        device_token: str | None = None,
        request_timeout: float = _DEFAULT_REQUEST_TIMEOUT,
        handshake_timeout: float = _DEFAULT_HANDSHAKE_TIMEOUT,
        strict_version: bool = False,
        client_info: GatewayClientInfo | None = None,
    ) -> None:
        _validate_gateway_url(url)
        if sum(value is not None for value in (token, password, device_token)) > 1:
            raise ValueError("provide only one of token, password, or device_token")
        if request_timeout <= 0 or handshake_timeout <= 0:
            raise ValueError("request and handshake timeouts must be greater than zero")
        self._url = url
        self._auth = (
            GatewayAuth(token=token, password=password, device_token=device_token)
            if token is not None or password is not None or device_token is not None
            else None
        )
        self._request_timeout = request_timeout
        self._handshake_timeout = handshake_timeout
        self._strict_version = strict_version
        self._client_info = client_info or GatewayClientInfo()
        self._socket: ClientConnection | None = None
        self._reader_task: asyncio.Task[None] | None = None
        self._pending: dict[str, asyncio.Future[ResponseFrame]] = {}
        self._event_queue: asyncio.Queue[EventFrame | BaseException] = asyncio.Queue()
        self._send_lock = asyncio.Lock()
        self._hello: HelloOk | None = None

    @property
    def is_connected(self) -> bool:
        return (
            self._socket is not None
            and self._hello is not None
            and self._reader_task is not None
            and not self._reader_task.done()
        )

    @property
    def hello(self) -> HelloOk:
        if self._hello is None:
            raise OpenClawNotConnectedError("the client has not completed the gateway handshake")
        return self._hello

    async def __aenter__(self) -> Self:
        await self.connect()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()

    async def connect(self) -> HelloOk:
        if self.is_connected:
            return self.hello
        if self._socket is not None:
            raise OpenClawClientError("a gateway connection attempt is already in progress")

        self._event_queue = asyncio.Queue()
        try:
            self._socket = await connect(
                self._url,
                max_size=_DEFAULT_MAX_PAYLOAD,
                open_timeout=self._handshake_timeout,
            )
            self._hello = await self._perform_handshake(self._socket)
            self._reader_task = asyncio.create_task(self._read_frames(), name="openclaw-gateway-reader")
            return self._hello
        except BaseException:
            await self.close()
            raise

    async def _perform_handshake(self, socket: ClientConnection) -> HelloOk:
        raw_challenge = await asyncio.wait_for(socket.recv(), timeout=self._handshake_timeout)
        challenge = _parse_event_frame(raw_challenge)
        _validate_connect_challenge(challenge)

        request = RequestFrame(
            type="req",
            method="connect",
            params=_connect_params(self._client_info, self._auth),
        )
        await socket.send(request.model_dump_json(by_alias=True, exclude_none=True))

        raw_response = await asyncio.wait_for(socket.recv(), timeout=self._handshake_timeout)
        response = _parse_response_frame(raw_response)
        if response.id != request.id:
            raise OpenClawProtocolError("connect response id does not match the request id")
        hello = _parse_hello(response)
        _validate_gateway_compatibility(hello, strict=self._strict_version)
        return hello

    async def close(self) -> None:
        reader_task = self._reader_task
        self._reader_task = None
        if reader_task is not None and reader_task is not asyncio.current_task():
            reader_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await reader_task
        socket = self._socket
        self._socket = None
        self._hello = None
        if socket is not None:
            await socket.close()
        self._fail_consumers(OpenClawNotConnectedError("gateway connection closed"))

    @overload
    async def request[ResultT: BaseModel](
        self,
        method: str,
        params: BaseModel | Mapping[str, Any] | None = None,
        *,
        result_model: type[ResultT],
        timeout: float | None = None,
    ) -> ResultT: ...

    @overload
    async def request(
        self,
        method: str,
        params: BaseModel | Mapping[str, Any] | None = None,
        *,
        result_model: None = None,
        timeout: float | None = None,
    ) -> Any: ...

    async def request[ResultT: BaseModel](
        self,
        method: str,
        params: BaseModel | Mapping[str, Any] | None = None,
        *,
        result_model: type[ResultT] | None = None,
        timeout: float | None = None,
    ) -> ResultT | Any:
        socket = self._socket
        if socket is None or self._hello is None or self._reader_task is None:
            raise OpenClawNotConnectedError("connect() must complete before sending requests")
        request = RequestFrame(type="req", method=method, params=_serialize_params(params))
        future: asyncio.Future[ResponseFrame] = asyncio.get_running_loop().create_future()
        self._pending[request.id] = future
        try:
            async with self._send_lock:
                await socket.send(request.model_dump_json(by_alias=True, exclude_none=True))
            response = await asyncio.wait_for(future, timeout=self._request_timeout if timeout is None else timeout)
        except TimeoutError as error:
            raise TimeoutError(f"gateway request {method!r} timed out") from error
        finally:
            self._pending.pop(request.id, None)
        payload = _unwrap_response(response)
        return payload if result_model is None else result_model.model_validate(payload)

    async def events(self) -> AsyncIterator[EventFrame]:
        """Yield all server-push events until the connection closes."""
        while True:
            item = await self._event_queue.get()
            if isinstance(item, BaseException):
                raise item
            yield item

    async def _read_frames(self) -> None:
        socket = self._socket
        assert socket is not None
        try:
            async for raw_frame in socket:
                frame = _GATEWAY_FRAME_ADAPTER.validate_python(_load_frame(raw_frame))
                match frame:
                    case ResponseFrame():
                        future = self._pending.get(frame.id)
                        if future is not None and not future.done():
                            future.set_result(frame)
                    case EventFrame():
                        await self._event_queue.put(frame)
        except asyncio.CancelledError:
            raise
        except ConnectionClosed as error:
            failure: BaseException = OpenClawClientError(f"gateway connection closed: {error}")
        except (ValidationError, json.JSONDecodeError, UnicodeDecodeError) as error:
            failure = OpenClawProtocolError("gateway sent an invalid frame")
            failure.__cause__ = error
        except BaseException as error:
            failure = error
        else:
            failure = OpenClawClientError("gateway connection closed")
        if self._socket is socket:
            self._socket = None
            self._hello = None
        self._fail_consumers(failure)

    def _fail_consumers(self, error: BaseException) -> None:
        for future in tuple(self._pending.values()):
            if not future.done():
                future.set_exception(error)
        self._event_queue.put_nowait(error)


def _validate_gateway_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"ws", "wss"} or not parsed.hostname:
        raise ValueError("gateway URL must be an absolute ws:// or wss:// URL")
    if parsed.scheme == "ws" and parsed.hostname not in {"127.0.0.1", "::1", "localhost"}:
        raise ValueError("plaintext ws:// is only allowed for loopback gateway URLs; use wss:// remotely")


def _serialize_params(params: BaseModel | Mapping[str, Any] | None) -> JsonObject | None:
    if params is None:
        return None
    if isinstance(params, BaseModel):
        return params.model_dump(by_alias=True, exclude_none=True)
    return dict(params)


def _load_frame(raw_frame: str | bytes) -> JsonObject:
    if isinstance(raw_frame, bytes):
        raw_frame = raw_frame.decode("utf-8")
    data = json.loads(raw_frame)
    if not isinstance(data, dict):
        raise OpenClawProtocolError("gateway frame must be a JSON object")
    return data


def _parse_event_frame(raw_frame: str | bytes) -> EventFrame:
    try:
        return EventFrame.model_validate(_load_frame(raw_frame))
    except (ValidationError, json.JSONDecodeError, UnicodeDecodeError) as error:
        raise OpenClawProtocolError("gateway sent an invalid event frame") from error


def _parse_response_frame(raw_frame: str | bytes) -> ResponseFrame:
    try:
        return ResponseFrame.model_validate(_load_frame(raw_frame))
    except (ValidationError, json.JSONDecodeError, UnicodeDecodeError) as error:
        raise OpenClawProtocolError("gateway sent an invalid response frame") from error


def _validate_connect_challenge(challenge: EventFrame) -> None:
    if challenge.event != "connect.challenge":
        raise OpenClawProtocolError(f"expected connect.challenge, received {challenge.event!r}")
    try:
        ConnectChallenge.model_validate(challenge.payload)
    except ValidationError as error:
        raise OpenClawProtocolError("gateway sent an invalid connect challenge") from error


def _parse_hello(response: ResponseFrame) -> HelloOk:
    payload = _unwrap_response(response)
    try:
        return HelloOk.model_validate(payload)
    except ValidationError as error:
        raise OpenClawProtocolError("gateway sent an invalid connect response") from error


def _validate_gateway_compatibility(hello: HelloOk, *, strict: bool) -> None:
    if hello.protocol != PROTOCOL_VERSION:
        raise OpenClawProtocolError(
            f"gateway negotiated protocol {hello.protocol}, but this client requires protocol {PROTOCOL_VERSION}"
        )

    gateway_version = hello.server.version
    if gateway_version == SCHEMA_PACKAGE_VERSION:
        return
    if strict:
        raise OpenClawProtocolError(
            f"gateway version {gateway_version!r} does not match client schema version {SCHEMA_PACKAGE_VERSION!r}"
        )

    gateway_release = _parse_release(gateway_version)
    schema_release = _parse_release(SCHEMA_PACKAGE_VERSION)
    if gateway_release is not None and schema_release is not None and gateway_release[0] != schema_release[0]:
        raise OpenClawProtocolError(
            f"gateway version {gateway_version!r} is incompatible with client schema version {SCHEMA_PACKAGE_VERSION!r}"
        )

    if gateway_release is None:
        relationship = "an unrecognized"
    elif schema_release is not None and gateway_release > schema_release:
        relationship = "a newer"
    elif schema_release is not None and gateway_release < schema_release:
        relationship = "an older"
    else:
        relationship = "a different"
    warnings.warn(
        f"gateway reported {relationship} version {gateway_version!r}; this client was generated from "
        f"schema version {SCHEMA_PACKAGE_VERSION!r}",
        OpenClawCompatibilityWarning,
        stacklevel=3,
    )


def _parse_release(version: str) -> tuple[int, int, int] | None:
    match = _VERSION_PATTERN.fullmatch(version)
    if match is None:
        return None
    major, minor, patch = match.groups()
    return int(major), int(minor), int(patch)


def _unwrap_response(response: ResponseFrame) -> Any:
    if response.ok:
        return response.payload
    error = response.error or ErrorShape(code="UNKNOWN", message="gateway request failed without a structured error")
    raise OpenClawGatewayError(error)


def _connect_params(client_info: GatewayClientInfo, auth: GatewayAuth | None) -> JsonObject:
    params = ConnectParams(
        min_protocol=PROTOCOL_VERSION,
        max_protocol=PROTOCOL_VERSION,
        client=client_info.model_dump(by_alias=True, exclude_none=True),
        role="operator",
        scopes=[OperatorScope.READ, OperatorScope.WRITE],
        caps=[],
        commands=[],
        permissions={},
        auth=None if auth is None else auth.model_dump(by_alias=True, exclude_none=True),
        user_agent="openclaw-client-python/0.1.0",
    )
    return params.model_dump(by_alias=True, exclude_none=True)


_GATEWAY_FRAME_ADAPTER = TypeAdapter(GatewayFrame)
