"""Generated agent RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    AgentWaitParams,
)


class AgentMethod(StrEnum):
    IDENTITY_GET = "agent.identity.get"
    WAIT = "agent.wait"


class AgentClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def get_identity(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            AgentMethod.IDENTITY_GET,
            params=payload,
        )

    async def wait(
        self,
        *,
        run_id: str,
        timeout_ms: int | None = None,
    ) -> Any:
        payload = AgentWaitParams(
            run_id=run_id,
            timeout_ms=timeout_ms,
        )
        return await self._client.request(
            AgentMethod.WAIT,
            params=payload,
        )
