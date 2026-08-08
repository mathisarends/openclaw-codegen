"""Generated models RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    ModelsAuthLogoutParams,
    ModelsAuthStatusParams,
    ModelsListParams,
    ModelsListResult,
    ModelsListView,
    ModelsProbeParams,
    ModelsProbeResult,
)


class ModelsMethod(StrEnum):
    AUTH_LOGOUT = "models.authLogout"
    AUTH_STATUS = "models.authStatus"
    LIST = "models.list"
    PROBE = "models.probe"


class ModelsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def auth_logout(
        self,
        *,
        provider: str,
        profile_ids: list[str] | None = None,
        agent_id: str | None = None,
    ) -> Any:
        payload = ModelsAuthLogoutParams(
            provider=provider,
            profile_ids=profile_ids,
            agent_id=agent_id,
        )
        return await self._client.request(
            ModelsMethod.AUTH_LOGOUT,
            params=payload,
        )

    async def auth_status(
        self,
        *,
        refresh: bool | None = None,
        agent_id: str | None = None,
    ) -> Any:
        payload = ModelsAuthStatusParams(
            refresh=refresh,
            agent_id=agent_id,
        )
        return await self._client.request(
            ModelsMethod.AUTH_STATUS,
            params=payload,
        )

    async def probe(
        self,
        *,
        provider: str,
        profile_id: str | None = None,
        timeout_ms: int | None = None,
        agent_id: str | None = None,
    ) -> ModelsProbeResult:
        payload = ModelsProbeParams(
            provider=provider,
            profile_id=profile_id,
            timeout_ms=timeout_ms,
            agent_id=agent_id,
        )
        return await self._client.request(
            ModelsMethod.PROBE,
            params=payload,
            result_model=ModelsProbeResult,
        )

    async def list(
        self,
        *,
        include_provider_capabilities: bool | None = None,
        view: ModelsListView | None = None,
    ) -> ModelsListResult:
        payload = ModelsListParams(
            include_provider_capabilities=include_provider_capabilities,
            view=view,
        )
        return await self._client.request(
            ModelsMethod.LIST,
            params=payload,
            result_model=ModelsListResult,
        )
