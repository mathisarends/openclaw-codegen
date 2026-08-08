"""Generated terminal RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    SessionsCatalogContinueParams,
    TerminalAttachParams,
    TerminalAttachResult,
    TerminalCloseParams,
    TerminalInputParams,
    TerminalListResult,
    TerminalOpenParams,
    TerminalOpenResult,
    TerminalResizeParams,
    TerminalTextParams,
    TerminalTextResult,
    TerminalUploadParams,
    TerminalUploadResult,
)


class TerminalMethod(StrEnum):
    ATTACH = "terminal.attach"
    CLOSE = "terminal.close"
    INPUT = "terminal.input"
    LIST = "terminal.list"
    OPEN = "terminal.open"
    RESIZE = "terminal.resize"
    TEXT = "terminal.text"
    UPLOAD = "terminal.upload"


class TerminalClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def attach(
        self,
        *,
        session_id: str,
    ) -> TerminalAttachResult:
        payload = TerminalAttachParams(
            session_id=session_id,
        )
        return await self._client.request(
            TerminalMethod.ATTACH,
            params=payload,
            result_model=TerminalAttachResult,
        )

    async def close(
        self,
        *,
        session_id: str,
    ) -> Any:
        payload = TerminalCloseParams(
            session_id=session_id,
        )
        return await self._client.request(
            TerminalMethod.CLOSE,
            params=payload,
        )

    async def input(
        self,
        *,
        session_id: str,
        data: str,
    ) -> Any:
        payload = TerminalInputParams(
            session_id=session_id,
            data=data,
        )
        return await self._client.request(
            TerminalMethod.INPUT,
            params=payload,
        )

    async def open(
        self,
        *,
        cols: int,
        rows: int,
        agent_id: str | None = None,
        catalog: SessionsCatalogContinueParams | None = None,
    ) -> TerminalOpenResult:
        payload = TerminalOpenParams(
            cols=cols,
            rows=rows,
            agent_id=agent_id,
            catalog=catalog,
        )
        return await self._client.request(
            TerminalMethod.OPEN,
            params=payload,
            result_model=TerminalOpenResult,
        )

    async def resize(
        self,
        *,
        session_id: str,
        cols: int,
        rows: int,
    ) -> Any:
        payload = TerminalResizeParams(
            session_id=session_id,
            cols=cols,
            rows=rows,
        )
        return await self._client.request(
            TerminalMethod.RESIZE,
            params=payload,
        )

    async def text(
        self,
        *,
        session_id: str,
    ) -> TerminalTextResult:
        payload = TerminalTextParams(
            session_id=session_id,
        )
        return await self._client.request(
            TerminalMethod.TEXT,
            params=payload,
            result_model=TerminalTextResult,
        )

    async def upload(
        self,
        *,
        session_id: str,
        name: str,
        content_base64: str,
    ) -> TerminalUploadResult:
        payload = TerminalUploadParams(
            session_id=session_id,
            name=name,
            content_base64=content_base64,
        )
        return await self._client.request(
            TerminalMethod.UPLOAD,
            params=payload,
            result_model=TerminalUploadResult,
        )

    async def list(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> TerminalListResult:
        payload = params
        return await self._client.request(
            TerminalMethod.LIST,
            params=payload,
            result_model=TerminalListResult,
        )
