"""Generated logs RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    LogsTailParams,
    LogsTailResult,
)


class LogsMethod(StrEnum):
    TAIL = "logs.tail"


class LogsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def tail(
        self,
        *,
        cursor: int | None = None,
        limit: int | None = None,
        max_bytes: int | None = None,
    ) -> LogsTailResult:
        payload = LogsTailParams(
            cursor=cursor,
            limit=limit,
            max_bytes=max_bytes,
        )
        return await self._client.request(
            LogsMethod.TAIL,
            params=payload,
            result_model=LogsTailResult,
        )
