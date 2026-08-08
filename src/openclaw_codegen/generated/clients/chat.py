"""Generated chat RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal
from uuid import uuid4

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    ChatAbortParams,
    ChatHistoryParams,
    ChatInjectParams,
    ChatMessageGetParams,
    ChatMessageGetResult,
    ChatMetadataParams,
    ChatSendAck,
    ChatSendParams,
    ChatSendQueueMode,
    ChatToolTitlesParams,
    ChatToolTitlesResult,
)


class ChatMethod(StrEnum):
    ABORT = "chat.abort"
    HISTORY = "chat.history"
    INJECT = "chat.inject"
    MESSAGE_GET = "chat.message.get"
    METADATA = "chat.metadata"
    SEND = "chat.send"
    STARTUP = "chat.startup"
    TOOL_TITLES = "chat.toolTitles"


class ChatClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def abort(
        self,
        *,
        session_key: str,
        agent_id: str | None = None,
        run_id: str | None = None,
        preserve_side_runs: bool | None = None,
    ) -> Any:
        payload = ChatAbortParams(
            session_key=session_key,
            agent_id=agent_id,
            run_id=run_id,
            preserve_side_runs=preserve_side_runs,
        )
        return await self._client.request(
            ChatMethod.ABORT,
            params=payload,
        )

    async def history(
        self,
        *,
        session_key: str,
        agent_id: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        message_id: str | None = None,
        session_id: str | None = None,
        max_chars: int | None = None,
    ) -> Any:
        payload = ChatHistoryParams(
            session_key=session_key,
            agent_id=agent_id,
            limit=limit,
            offset=offset,
            message_id=message_id,
            session_id=session_id,
            max_chars=max_chars,
        )
        return await self._client.request(
            ChatMethod.HISTORY,
            params=payload,
        )

    async def inject(
        self,
        *,
        session_key: str,
        message: str,
        agent_id: str | None = None,
        label: str | None = None,
    ) -> Any:
        payload = ChatInjectParams(
            session_key=session_key,
            message=message,
            agent_id=agent_id,
            label=label,
        )
        return await self._client.request(
            ChatMethod.INJECT,
            params=payload,
        )

    async def get_message(
        self,
        *,
        session_key: str,
        message_id: str,
        agent_id: str | None = None,
        max_chars: int | None = None,
    ) -> ChatMessageGetResult:
        payload = ChatMessageGetParams(
            session_key=session_key,
            message_id=message_id,
            agent_id=agent_id,
            max_chars=max_chars,
        )
        return await self._client.request(
            ChatMethod.MESSAGE_GET,
            params=payload,
            result_model=ChatMessageGetResult,
        )

    async def metadata(
        self,
        *,
        agent_id: str | None = None,
    ) -> Any:
        payload = ChatMetadataParams(
            agent_id=agent_id,
        )
        return await self._client.request(
            ChatMethod.METADATA,
            params=payload,
        )

    async def send(
        self,
        *,
        session_key: str,
        message: str,
        idempotency_key: str | None = None,
        agent_id: str | None = None,
        session_id: str | None = None,
        thinking: str | None = None,
        fast_mode: bool | Literal["auto"] | None = None,
        fast_auto_on_seconds: int | None = None,
        queue_mode: ChatSendQueueMode | None = None,
        deliver: bool | None = None,
        originating_channel: str | None = None,
        originating_to: str | None = None,
        originating_account_id: str | None = None,
        originating_thread_id: str | None = None,
        reply_to_id: str | None = None,
        attachments: list[dict[str, Any]] | None = None,
        tool_bindings: dict[str, Any] | None = None,
        timeout_ms: int | None = None,
        system_input_provenance: dict[str, Any] | None = None,
        system_provenance_receipt: str | None = None,
        suppress_command_interpretation: bool | None = None,
        expected_leaf_entry_id: str | None = None,
        expected_session_routing_contract: str | None = None,
    ) -> ChatSendAck:
        payload = ChatSendParams(
            session_key=session_key,
            message=message,
            idempotency_key=idempotency_key or str(uuid4()),
            agent_id=agent_id,
            session_id=session_id,
            thinking=thinking,
            fast_mode=fast_mode,
            fast_auto_on_seconds=fast_auto_on_seconds,
            queue_mode=queue_mode,
            deliver=deliver,
            originating_channel=originating_channel,
            originating_to=originating_to,
            originating_account_id=originating_account_id,
            originating_thread_id=originating_thread_id,
            reply_to_id=reply_to_id,
            attachments=attachments,
            tool_bindings=tool_bindings,
            timeout_ms=timeout_ms,
            system_input_provenance=system_input_provenance,
            system_provenance_receipt=system_provenance_receipt,
            suppress_command_interpretation=suppress_command_interpretation,
            expected_leaf_entry_id=expected_leaf_entry_id,
            expected_session_routing_contract=expected_session_routing_contract,
        )
        return await self._client.request(
            ChatMethod.SEND,
            params=payload,
            result_model=ChatSendAck,
        )

    async def startup(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            ChatMethod.STARTUP,
            params=payload,
        )

    async def tool_titles(
        self,
        *,
        session_key: str,
        items: list[dict[str, Any]],
        agent_id: str | None = None,
    ) -> ChatToolTitlesResult:
        payload = ChatToolTitlesParams(
            session_key=session_key,
            items=items,
            agent_id=agent_id,
        )
        return await self._client.request(
            ChatMethod.TOOL_TITLES,
            params=payload,
            result_model=ChatToolTitlesResult,
        )
