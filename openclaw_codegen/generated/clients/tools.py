"""Generated tools RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    ToolsCatalogParams,
    ToolsCatalogResult,
    ToolsEffectiveParams,
    ToolsEffectiveResult,
    ToolsInvokeParams,
    ToolsInvokeResult,
)


class ToolsMethod(StrEnum):
    CATALOG = "tools.catalog"
    EFFECTIVE = "tools.effective"
    INVOKE = "tools.invoke"


class ToolsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def catalog(
        self,
        *,
        agent_id: str | None = None,
        include_plugins: bool | None = None,
    ) -> ToolsCatalogResult:
        payload = ToolsCatalogParams(
            agent_id=agent_id,
            include_plugins=include_plugins,
        )
        return await self._client.request(
            ToolsMethod.CATALOG,
            params=payload,
            result_model=ToolsCatalogResult,
        )

    async def effective(
        self,
        *,
        session_key: str,
        agent_id: str | None = None,
    ) -> ToolsEffectiveResult:
        payload = ToolsEffectiveParams(
            session_key=session_key,
            agent_id=agent_id,
        )
        return await self._client.request(
            ToolsMethod.EFFECTIVE,
            params=payload,
            result_model=ToolsEffectiveResult,
        )

    async def invoke(
        self,
        *,
        name: str,
        args: dict[str, Any] | None = None,
        session_key: str | None = None,
        agent_id: str | None = None,
        confirm: bool | None = None,
        idempotency_key: str | None = None,
        conversation_read_origin: Literal["direct-operator"] | None = None,
    ) -> ToolsInvokeResult:
        payload = ToolsInvokeParams(
            name=name,
            args=args,
            session_key=session_key,
            agent_id=agent_id,
            confirm=confirm,
            idempotency_key=idempotency_key,
            conversation_read_origin=conversation_read_origin,
        )
        return await self._client.request(
            ToolsMethod.INVOKE,
            params=payload,
            result_model=ToolsInvokeResult,
        )
