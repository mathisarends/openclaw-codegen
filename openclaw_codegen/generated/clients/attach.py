"""Generated attach RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class AttachMethod(StrEnum):
    GRANT = "attach.grant"
    REVOKE = "attach.revoke"


class AttachClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def grant(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            AttachMethod.GRANT,
            params=payload,
        )

    async def revoke(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            AttachMethod.REVOKE,
            params=payload,
        )
