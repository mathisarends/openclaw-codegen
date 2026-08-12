"""Generated update RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    UpdateRunParams,
    UpdateStatusParams,
)


class UpdateMethod(StrEnum):
    RUN = "update.run"
    STATUS = "update.status"


class UpdateClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def run(
        self,
        *,
        session_key: str | None = None,
        delivery_context: dict[str, Any] | None = None,
        note: str | None = None,
        continuation_message: str | None = None,
        restart_delay_ms: int | None = None,
        timeout_ms: int | None = None,
    ) -> Any:
        payload = UpdateRunParams(
            session_key=session_key,
            delivery_context=delivery_context,
            note=note,
            continuation_message=continuation_message,
            restart_delay_ms=restart_delay_ms,
            timeout_ms=timeout_ms,
        )
        return await self._client.request(
            UpdateMethod.RUN,
            params=payload,
        )

    async def status(
        self,
    ) -> Any:
        payload = UpdateStatusParams()
        return await self._client.request(
            UpdateMethod.STATUS,
            params=payload,
        )
