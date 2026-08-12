"""Generated native_hook RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class NativeHookMethod(StrEnum):
    INVOKE = "nativeHook.invoke"


class NativeHookClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def invoke(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            NativeHookMethod.INVOKE,
            params=payload,
        )
