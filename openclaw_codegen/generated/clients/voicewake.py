"""Generated voicewake RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class VoicewakeMethod(StrEnum):
    GET = "voicewake.get"
    ROUTING_GET = "voicewake.routing.get"
    ROUTING_SET = "voicewake.routing.set"
    SET = "voicewake.set"


class VoicewakeClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def get(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            VoicewakeMethod.GET,
            params=payload,
        )

    async def get_routing(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            VoicewakeMethod.ROUTING_GET,
            params=payload,
        )

    async def set_routing(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            VoicewakeMethod.ROUTING_SET,
            params=payload,
        )

    async def set(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            VoicewakeMethod.SET,
            params=payload,
        )
