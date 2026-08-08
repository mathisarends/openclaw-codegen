"""Generated system RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    SystemInfoParams,
    SystemInfoResult,
)


class SystemMethod(StrEnum):
    INFO = "system.info"


class SystemClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def info(
        self,
    ) -> SystemInfoResult:
        payload = SystemInfoParams()
        return await self._client.request(
            SystemMethod.INFO,
            params=payload,
            result_model=SystemInfoResult,
        )
