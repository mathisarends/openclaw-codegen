"""Generated conversations RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    ConversationListParams,
    ConversationListResult,
    ConversationSendParams,
    ConversationSendResult,
    ConversationTurnCancelParams,
    ConversationTurnCancelResult,
    ConversationTurnParams,
    ConversationTurnResult,
)


class ConversationsMethod(StrEnum):
    LIST = "conversations.list"
    SEND = "conversations.send"
    TURN = "conversations.turn"
    TURN_CANCEL = "conversations.turn.cancel"


class ConversationsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def send(
        self,
        *,
        agent_id: str,
        operation_id: str,
        conversation_ref: str,
        message: str,
        source_session_key: str | None = None,
    ) -> ConversationSendResult:
        payload = ConversationSendParams(
            agent_id=agent_id,
            operation_id=operation_id,
            conversation_ref=conversation_ref,
            message=message,
            source_session_key=source_session_key,
        )
        return await self._client.request(
            ConversationsMethod.SEND,
            params=payload,
            result_model=ConversationSendResult,
        )

    async def turn(
        self,
        *,
        agent_id: str,
        turn_id: str,
        conversation_ref: str,
        message: str,
        timeout_ms: int,
        source_session_key: str | None = None,
    ) -> ConversationTurnResult:
        payload = ConversationTurnParams(
            agent_id=agent_id,
            turn_id=turn_id,
            conversation_ref=conversation_ref,
            message=message,
            timeout_ms=timeout_ms,
            source_session_key=source_session_key,
        )
        return await self._client.request(
            ConversationsMethod.TURN,
            params=payload,
            result_model=ConversationTurnResult,
        )

    async def cancel_turn(
        self,
        *,
        agent_id: str,
        turn_id: str,
    ) -> ConversationTurnCancelResult:
        payload = ConversationTurnCancelParams(
            agent_id=agent_id,
            turn_id=turn_id,
        )
        return await self._client.request(
            ConversationsMethod.TURN_CANCEL,
            params=payload,
            result_model=ConversationTurnCancelResult,
        )

    async def list(
        self,
        *,
        agent_id: str,
        channel: str | None = None,
        query: str | None = None,
        limit: int | None = None,
    ) -> ConversationListResult:
        payload = ConversationListParams(
            agent_id=agent_id,
            channel=channel,
            query=query,
            limit=limit,
        )
        return await self._client.request(
            ConversationsMethod.LIST,
            params=payload,
            result_model=ConversationListResult,
        )
