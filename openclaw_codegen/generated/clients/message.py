"""Generated message RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    MessageActionInboundTurnKind,
    MessageActionParams,
)


class MessageMethod(StrEnum):
    ACTION = "message.action"


class MessageClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def action(
        self,
        *,
        channel: str,
        action: str,
        params: dict[str, Any],
        idempotency_key: str,
        account_id: str | None = None,
        requester_account_id: str | None = None,
        requester_sender_id: str | None = None,
        sender_is_owner: bool | None = None,
        session_key: str | None = None,
        session_id: str | None = None,
        inbound_turn_kind: MessageActionInboundTurnKind | None = None,
        agent_id: str | None = None,
        tool_context: dict[str, Any] | None = None,
        conversation_read_origin: Literal["direct-operator"] | None = None,
    ) -> Any:
        payload = MessageActionParams(
            channel=channel,
            action=action,
            params=params,
            idempotency_key=idempotency_key,
            account_id=account_id,
            requester_account_id=requester_account_id,
            requester_sender_id=requester_sender_id,
            sender_is_owner=sender_is_owner,
            session_key=session_key,
            session_id=session_id,
            inbound_turn_kind=inbound_turn_kind,
            agent_id=agent_id,
            tool_context=tool_context,
            conversation_read_origin=conversation_read_origin,
        )
        return await self._client.request(
            MessageMethod.ACTION,
            params=payload,
        )
