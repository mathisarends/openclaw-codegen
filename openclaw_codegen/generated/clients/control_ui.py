"""Generated control_ui RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class ControlUiMethod(StrEnum):
    GITHUB_PREVIEW = "controlUi.githubPreview"
    SESSION_PULL_REQUESTS_SUBSCRIBE = "controlUi.sessionPullRequests.subscribe"


class ControlUiClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def github_preview(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            ControlUiMethod.GITHUB_PREVIEW,
            params=payload,
        )

    async def subscribe_session_pull_requests(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            ControlUiMethod.SESSION_PULL_REQUESTS_SUBSCRIBE,
            params=payload,
        )
