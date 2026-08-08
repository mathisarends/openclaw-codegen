"""Generated device RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    DevicePairApproveParams,
    DevicePairListParams,
    DevicePairRejectParams,
    DevicePairRemoveParams,
    DevicePairRenameParams,
    DevicePairSetupCodeBootstrapProfile,
    DevicePairSetupCodeParams,
    DevicePairSetupCodeResult,
    DeviceTokenRevokeParams,
    DeviceTokenRotateParams,
)


class DeviceMethod(StrEnum):
    PAIR_APPROVE = "device.pair.approve"
    PAIR_LIST = "device.pair.list"
    PAIR_REJECT = "device.pair.reject"
    PAIR_REMOVE = "device.pair.remove"
    PAIR_RENAME = "device.pair.rename"
    PAIR_SETUP_CODE = "device.pair.setupCode"
    TOKEN_REVOKE = "device.token.revoke"
    TOKEN_ROTATE = "device.token.rotate"


class DeviceClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def approve_pair(
        self,
        *,
        request_id: str,
    ) -> Any:
        payload = DevicePairApproveParams(
            request_id=request_id,
        )
        return await self._client.request(
            DeviceMethod.PAIR_APPROVE,
            params=payload,
        )

    async def list_pair(
        self,
    ) -> Any:
        payload = DevicePairListParams()
        return await self._client.request(
            DeviceMethod.PAIR_LIST,
            params=payload,
        )

    async def reject_pair(
        self,
        *,
        request_id: str,
    ) -> Any:
        payload = DevicePairRejectParams(
            request_id=request_id,
        )
        return await self._client.request(
            DeviceMethod.PAIR_REJECT,
            params=payload,
        )

    async def remove_pair(
        self,
        *,
        device_id: str,
    ) -> Any:
        payload = DevicePairRemoveParams(
            device_id=device_id,
        )
        return await self._client.request(
            DeviceMethod.PAIR_REMOVE,
            params=payload,
        )

    async def rename_pair(
        self,
        *,
        device_id: str,
        label: str,
    ) -> Any:
        payload = DevicePairRenameParams(
            device_id=device_id,
            label=label,
        )
        return await self._client.request(
            DeviceMethod.PAIR_RENAME,
            params=payload,
        )

    async def setup_code_pair(
        self,
        *,
        public_url: str | None = None,
        prefer_remote_url: bool | None = None,
        include_qr: bool | None = None,
        bootstrap_profile: DevicePairSetupCodeBootstrapProfile | None = None,
    ) -> DevicePairSetupCodeResult:
        payload = DevicePairSetupCodeParams(
            public_url=public_url,
            prefer_remote_url=prefer_remote_url,
            include_qr=include_qr,
            bootstrap_profile=bootstrap_profile,
        )
        return await self._client.request(
            DeviceMethod.PAIR_SETUP_CODE,
            params=payload,
            result_model=DevicePairSetupCodeResult,
        )

    async def revoke_token(
        self,
        *,
        device_id: str,
        role: str,
    ) -> Any:
        payload = DeviceTokenRevokeParams(
            device_id=device_id,
            role=role,
        )
        return await self._client.request(
            DeviceMethod.TOKEN_REVOKE,
            params=payload,
        )

    async def rotate_token(
        self,
        *,
        device_id: str,
        role: str,
        scopes: list[str] | None = None,
    ) -> Any:
        payload = DeviceTokenRotateParams(
            device_id=device_id,
            role=role,
            scopes=scopes,
        )
        return await self._client.request(
            DeviceMethod.TOKEN_ROTATE,
            params=payload,
        )
