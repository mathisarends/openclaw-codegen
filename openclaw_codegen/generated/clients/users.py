"""Generated users RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class UsersMethod(StrEnum):
    LINK_EMAIL = "users.linkEmail"
    LIST = "users.list"
    SELF = "users.self"
    SET_AVATAR = "users.setAvatar"
    SET_DISPLAY_NAME = "users.setDisplayName"


class UsersClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def link_email(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            UsersMethod.LINK_EMAIL,
            params=payload,
        )

    async def self(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            UsersMethod.SELF,
            params=payload,
        )

    async def set_avatar(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            UsersMethod.SET_AVATAR,
            params=payload,
        )

    async def set_display_name(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            UsersMethod.SET_DISPLAY_NAME,
            params=payload,
        )

    async def list(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            UsersMethod.LIST,
            params=payload,
        )
