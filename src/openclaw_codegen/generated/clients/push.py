"""Generated push RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    PushTestEnvironment,
    PushTestParams,
    PushTestResult,
)


class PushMethod(StrEnum):
    TEST = "push.test"
    WEB_SUBSCRIBE = "push.web.subscribe"
    WEB_TEST = "push.web.test"
    WEB_UNSUBSCRIBE = "push.web.unsubscribe"
    WEB_VAPID_PUBLIC_KEY = "push.web.vapidPublicKey"


class PushClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def test(
        self,
        *,
        node_id: str,
        title: str | None = None,
        body: str | None = None,
        environment: PushTestEnvironment | None = None,
    ) -> PushTestResult:
        payload = PushTestParams(
            node_id=node_id,
            title=title,
            body=body,
            environment=environment,
        )
        return await self._client.request(
            PushMethod.TEST,
            params=payload,
            result_model=PushTestResult,
        )

    async def subscribe_web(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            PushMethod.WEB_SUBSCRIBE,
            params=payload,
        )

    async def test_web(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            PushMethod.WEB_TEST,
            params=payload,
        )

    async def unsubscribe_web(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            PushMethod.WEB_UNSUBSCRIBE,
            params=payload,
        )

    async def vapid_public_key_web(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            PushMethod.WEB_VAPID_PUBLIC_KEY,
            params=payload,
        )
