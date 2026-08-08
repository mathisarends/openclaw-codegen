"""Generated openclaw RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class OpenclawMethod(StrEnum):
    APPROVAL_LIST = "openclaw.approval.list"
    CHANGES_LIST = "openclaw.changes.list"
    CHAT = "openclaw.chat"
    CHAT_HISTORY = "openclaw.chat.history"
    SETUP_ACTIVATE = "openclaw.setup.activate"
    SETUP_AUTH_START = "openclaw.setup.auth.start"
    SETUP_DETECT = "openclaw.setup.detect"
    SETUP_PREPARE_START = "openclaw.setup.prepare.start"
    SETUP_VERIFY = "openclaw.setup.verify"


class OpenclawClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def list_approval(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            OpenclawMethod.APPROVAL_LIST,
            params=payload,
        )

    async def list_changes(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            OpenclawMethod.CHANGES_LIST,
            params=payload,
        )

    async def chat(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            OpenclawMethod.CHAT,
            params=payload,
        )

    async def history_chat(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            OpenclawMethod.CHAT_HISTORY,
            params=payload,
        )

    async def activate_setup(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            OpenclawMethod.SETUP_ACTIVATE,
            params=payload,
        )

    async def start_auth_setup(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            OpenclawMethod.SETUP_AUTH_START,
            params=payload,
        )

    async def detect_setup(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            OpenclawMethod.SETUP_DETECT,
            params=payload,
        )

    async def start_prepare_setup(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            OpenclawMethod.SETUP_PREPARE_START,
            params=payload,
        )

    async def verify_setup(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            OpenclawMethod.SETUP_VERIFY,
            params=payload,
        )
