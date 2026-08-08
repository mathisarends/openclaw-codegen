"""Generated diagnostics RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class DiagnosticsMethod(StrEnum):
    STABILITY = "diagnostics.stability"


class DiagnosticsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def stability(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            DiagnosticsMethod.STABILITY,
            params=payload,
        )
