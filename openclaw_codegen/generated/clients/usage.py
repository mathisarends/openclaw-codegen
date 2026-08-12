"""Generated usage RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class UsageMethod(StrEnum):
    COST = "usage.cost"
    STATUS = "usage.status"


class UsageClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def cost(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            UsageMethod.COST,
            params=payload,
        )

    async def status(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            UsageMethod.STATUS,
            params=payload,
        )
