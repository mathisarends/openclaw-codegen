"""Generated assistant RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class AssistantMethod(StrEnum):
    MEDIA_GET = "assistant.media.get"


class AssistantClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def get_media(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            AssistantMethod.MEDIA_GET,
            params=payload,
        )
