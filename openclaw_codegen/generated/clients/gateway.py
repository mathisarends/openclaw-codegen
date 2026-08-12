"""Generated gateway RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    GatewaySuspendPrepareParams,
    GatewaySuspendPrepareResult,
    GatewaySuspendResumeParams,
    GatewaySuspendResumeResult,
    GatewaySuspendStatusParams,
    GatewaySuspendStatusResult,
)


class GatewayMethod(StrEnum):
    IDENTITY_GET = "gateway.identity.get"
    RESTART_PREFLIGHT = "gateway.restart.preflight"
    RESTART_REQUEST = "gateway.restart.request"
    SUSPEND_PREPARE = "gateway.suspend.prepare"
    SUSPEND_RESUME = "gateway.suspend.resume"
    SUSPEND_STATUS = "gateway.suspend.status"


class GatewayClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def get_identity(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            GatewayMethod.IDENTITY_GET,
            params=payload,
        )

    async def preflight_restart(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            GatewayMethod.RESTART_PREFLIGHT,
            params=payload,
        )

    async def request_restart(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            GatewayMethod.RESTART_REQUEST,
            params=payload,
        )

    async def prepare_suspend(
        self,
        *,
        request_id: str,
    ) -> GatewaySuspendPrepareResult:
        payload = GatewaySuspendPrepareParams(
            request_id=request_id,
        )
        return await self._client.request(
            GatewayMethod.SUSPEND_PREPARE,
            params=payload,
            result_model=GatewaySuspendPrepareResult,
        )

    async def resume_suspend(
        self,
        *,
        suspension_id: str,
    ) -> GatewaySuspendResumeResult:
        payload = GatewaySuspendResumeParams(
            suspension_id=suspension_id,
        )
        return await self._client.request(
            GatewayMethod.SUSPEND_RESUME,
            params=payload,
            result_model=GatewaySuspendResumeResult,
        )

    async def status_suspend(
        self,
        *,
        suspension_id: str,
    ) -> GatewaySuspendStatusResult:
        payload = GatewaySuspendStatusParams(
            suspension_id=suspension_id,
        )
        return await self._client.request(
            GatewayMethod.SUSPEND_STATUS,
            params=payload,
            result_model=GatewaySuspendStatusResult,
        )
