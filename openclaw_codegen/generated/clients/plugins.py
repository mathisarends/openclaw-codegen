"""Generated plugins RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    PluginsInstallParams,
    PluginsInstallResult,
    PluginsListParams,
    PluginsListResult,
    PluginsRefreshParams,
    PluginsRefreshResult,
    PluginsSearchParams,
    PluginsSearchResult,
    PluginsSessionActionParams,
    PluginsSessionActionResult,
    PluginsSetEnabledParams,
    PluginsSetEnabledResult,
    PluginsUiDescriptorsParams,
    PluginsUiDescriptorsResult,
    PluginsUninstallParams,
    PluginsUninstallResult,
)


class PluginsMethod(StrEnum):
    INSTALL = "plugins.install"
    LIST = "plugins.list"
    REFRESH = "plugins.refresh"
    SEARCH = "plugins.search"
    SESSION_ACTION = "plugins.sessionAction"
    SET_ENABLED = "plugins.setEnabled"
    UI_DESCRIPTORS = "plugins.uiDescriptors"
    UNINSTALL = "plugins.uninstall"


class PluginsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def install(
        self,
    ) -> PluginsInstallResult:
        payload = PluginsInstallParams()
        return await self._client.request(
            PluginsMethod.INSTALL,
            params=payload,
            result_model=PluginsInstallResult,
        )

    async def refresh(
        self,
    ) -> PluginsRefreshResult:
        payload = PluginsRefreshParams()
        return await self._client.request(
            PluginsMethod.REFRESH,
            params=payload,
            result_model=PluginsRefreshResult,
        )

    async def search(
        self,
        *,
        query: str,
        limit: int | None = None,
    ) -> PluginsSearchResult:
        payload = PluginsSearchParams(
            query=query,
            limit=limit,
        )
        return await self._client.request(
            PluginsMethod.SEARCH,
            params=payload,
            result_model=PluginsSearchResult,
        )

    async def session_action(
        self,
        *,
        plugin_id: str,
        action_id: str,
        session_key: str | None = None,
        payload: Any | None = None,
    ) -> PluginsSessionActionResult:
        payload = PluginsSessionActionParams(
            plugin_id=plugin_id,
            action_id=action_id,
            session_key=session_key,
            payload=payload,
        )
        return await self._client.request(
            PluginsMethod.SESSION_ACTION,
            params=payload,
            result_model=PluginsSessionActionResult,
        )

    async def set_enabled(
        self,
        *,
        plugin_id: str,
        enabled: bool,
    ) -> PluginsSetEnabledResult:
        payload = PluginsSetEnabledParams(
            plugin_id=plugin_id,
            enabled=enabled,
        )
        return await self._client.request(
            PluginsMethod.SET_ENABLED,
            params=payload,
            result_model=PluginsSetEnabledResult,
        )

    async def ui_descriptors(
        self,
    ) -> PluginsUiDescriptorsResult:
        payload = PluginsUiDescriptorsParams()
        return await self._client.request(
            PluginsMethod.UI_DESCRIPTORS,
            params=payload,
            result_model=PluginsUiDescriptorsResult,
        )

    async def uninstall(
        self,
        *,
        plugin_id: str,
    ) -> PluginsUninstallResult:
        payload = PluginsUninstallParams(
            plugin_id=plugin_id,
        )
        return await self._client.request(
            PluginsMethod.UNINSTALL,
            params=payload,
            result_model=PluginsUninstallResult,
        )

    async def list(
        self,
    ) -> PluginsListResult:
        payload = PluginsListParams()
        return await self._client.request(
            PluginsMethod.LIST,
            params=payload,
            result_model=PluginsListResult,
        )
