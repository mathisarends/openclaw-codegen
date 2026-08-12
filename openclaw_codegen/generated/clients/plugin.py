"""Generated plugin RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    PluginApprovalRequestParams,
    PluginApprovalRequestSeverity,
    PluginApprovalResolveParams,
)


class PluginMethod(StrEnum):
    APPROVAL_LIST = "plugin.approval.list"
    APPROVAL_REQUEST = "plugin.approval.request"
    APPROVAL_RESOLVE = "plugin.approval.resolve"
    APPROVAL_WAIT_DECISION = "plugin.approval.waitDecision"
    SURFACE_REFRESH = "plugin.surface.refresh"


class PluginClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def list_approval(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            PluginMethod.APPROVAL_LIST,
            params=payload,
        )

    async def request_approval(
        self,
        *,
        title: str,
        description: str,
        plugin_id: str | None = None,
        detail: str | None = None,
        severity: PluginApprovalRequestSeverity | None = None,
        tool_name: str | None = None,
        tool_call_id: str | None = None,
        allowed_decisions: list[Literal["allow-once", "allow-always", "deny"]] | None = None,
        agent_id: str | None = None,
        session_key: str | None = None,
        approval_reviewer_device_ids: list[str] | None = None,
        turn_source_channel: str | None = None,
        turn_source_to: str | None = None,
        turn_source_account_id: str | None = None,
        turn_source_thread_id: str | float | None = None,
        timeout_ms: int | None = None,
        two_phase: bool | None = None,
    ) -> Any:
        payload = PluginApprovalRequestParams(
            title=title,
            description=description,
            plugin_id=plugin_id,
            detail=detail,
            severity=severity,
            tool_name=tool_name,
            tool_call_id=tool_call_id,
            allowed_decisions=allowed_decisions,
            agent_id=agent_id,
            session_key=session_key,
            approval_reviewer_device_ids=approval_reviewer_device_ids,
            turn_source_channel=turn_source_channel,
            turn_source_to=turn_source_to,
            turn_source_account_id=turn_source_account_id,
            turn_source_thread_id=turn_source_thread_id,
            timeout_ms=timeout_ms,
            two_phase=two_phase,
        )
        return await self._client.request(
            PluginMethod.APPROVAL_REQUEST,
            params=payload,
        )

    async def resolve_approval(
        self,
        *,
        id: str,
        decision: str,
    ) -> Any:
        payload = PluginApprovalResolveParams(
            id=id,
            decision=decision,
        )
        return await self._client.request(
            PluginMethod.APPROVAL_RESOLVE,
            params=payload,
        )

    async def wait_decision_approval(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            PluginMethod.APPROVAL_WAIT_DECISION,
            params=payload,
        )

    async def refresh_surface(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            PluginMethod.SURFACE_REFRESH,
            params=payload,
        )
