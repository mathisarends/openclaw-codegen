"""Generated web RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    WebLoginStartParams,
    WebLoginWaitParams,
)


class WebMethod(StrEnum):
    LOGIN_START = "web.login.start"
    LOGIN_WAIT = "web.login.wait"


class WebClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def start_login(
        self,
        *,
        force: bool | None = None,
        timeout_ms: int | None = None,
        verbose: bool | None = None,
        account_id: str | None = None,
    ) -> Any:
        payload = WebLoginStartParams(
            force=force,
            timeout_ms=timeout_ms,
            verbose=verbose,
            account_id=account_id,
        )
        return await self._client.request(
            WebMethod.LOGIN_START,
            params=payload,
        )

    async def wait_login(
        self,
        *,
        timeout_ms: int | None = None,
        account_id: str | None = None,
        current_qr_data_url: str | None = None,
    ) -> Any:
        payload = WebLoginWaitParams(
            timeout_ms=timeout_ms,
            account_id=account_id,
            current_qr_data_url=current_qr_data_url,
        )
        return await self._client.request(
            WebMethod.LOGIN_WAIT,
            params=payload,
        )
