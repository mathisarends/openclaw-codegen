"""Generated memory RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class MemoryMethod(StrEnum):
    SEARCH = "memory.search"


class MemoryClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def search(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            MemoryMethod.SEARCH,
            params=payload,
        )
