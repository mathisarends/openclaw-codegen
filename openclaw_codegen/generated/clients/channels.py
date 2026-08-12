"""Generated channels RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    ChannelsLogoutParams,
    ChannelsPairingApproveParams,
    ChannelsPairingApproveResult,
    ChannelsPairingDismissParams,
    ChannelsPairingDismissResult,
    ChannelsPairingListParams,
    ChannelsPairingListResult,
    ChannelsStartParams,
    ChannelsStatusParams,
    ChannelsStatusResult,
    ChannelsStopParams,
)


class ChannelsMethod(StrEnum):
    LOGOUT = "channels.logout"
    PAIRING_APPROVE = "channels.pairing.approve"
    PAIRING_DISMISS = "channels.pairing.dismiss"
    PAIRING_LIST = "channels.pairing.list"
    START = "channels.start"
    STATUS = "channels.status"
    STOP = "channels.stop"


class ChannelsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def logout(
        self,
        *,
        channel: str,
        account_id: str | None = None,
    ) -> Any:
        payload = ChannelsLogoutParams(
            channel=channel,
            account_id=account_id,
        )
        return await self._client.request(
            ChannelsMethod.LOGOUT,
            params=payload,
        )

    async def approve_pairing(
        self,
        *,
        channel: str,
        account_id: str,
        request_id: str,
        notify: bool | None = None,
        bootstrap_command_owner: bool | None = None,
    ) -> ChannelsPairingApproveResult:
        payload = ChannelsPairingApproveParams(
            channel=channel,
            account_id=account_id,
            request_id=request_id,
            notify=notify,
            bootstrap_command_owner=bootstrap_command_owner,
        )
        return await self._client.request(
            ChannelsMethod.PAIRING_APPROVE,
            params=payload,
            result_model=ChannelsPairingApproveResult,
        )

    async def dismiss_pairing(
        self,
        *,
        channel: str,
        account_id: str,
        request_id: str,
    ) -> ChannelsPairingDismissResult:
        payload = ChannelsPairingDismissParams(
            channel=channel,
            account_id=account_id,
            request_id=request_id,
        )
        return await self._client.request(
            ChannelsMethod.PAIRING_DISMISS,
            params=payload,
            result_model=ChannelsPairingDismissResult,
        )

    async def list_pairing(
        self,
        *,
        channel: str | None = None,
        account_id: str | None = None,
    ) -> ChannelsPairingListResult:
        payload = ChannelsPairingListParams(
            channel=channel,
            account_id=account_id,
        )
        return await self._client.request(
            ChannelsMethod.PAIRING_LIST,
            params=payload,
            result_model=ChannelsPairingListResult,
        )

    async def start(
        self,
        *,
        channel: str,
        account_id: str | None = None,
    ) -> Any:
        payload = ChannelsStartParams(
            channel=channel,
            account_id=account_id,
        )
        return await self._client.request(
            ChannelsMethod.START,
            params=payload,
        )

    async def status(
        self,
        *,
        probe: bool | None = None,
        timeout_ms: int | None = None,
        channel: str | None = None,
    ) -> ChannelsStatusResult:
        payload = ChannelsStatusParams(
            probe=probe,
            timeout_ms=timeout_ms,
            channel=channel,
        )
        return await self._client.request(
            ChannelsMethod.STATUS,
            params=payload,
            result_model=ChannelsStatusResult,
        )

    async def stop(
        self,
        *,
        channel: str,
        account_id: str | None = None,
    ) -> Any:
        payload = ChannelsStopParams(
            channel=channel,
            account_id=account_id,
        )
        return await self._client.request(
            ChannelsMethod.STOP,
            params=payload,
        )
