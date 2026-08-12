"""Generated node RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    NodeDescribeParams,
    NodeEventParams,
    NodeEventResult,
    NodeInvokeParams,
    NodeInvokeProgressParams,
    NodeInvokeResultParams,
    NodeListParams,
    NodePairApproveParams,
    NodePairListParams,
    NodePairRejectParams,
    NodePairRemoveParams,
    NodePendingAckParams,
    NodePendingDrainParams,
    NodePendingDrainResult,
    NodePendingEnqueueParams,
    NodePendingEnqueuePriority,
    NodePendingEnqueueResult,
    NodePendingEnqueueType,
    NodePluginToolDescriptor,
    NodePluginToolsUpdateParams,
    NodeRenameParams,
    NodeSkillDescriptor,
    NodeSkillsUpdateParams,
)


class NodeMethod(StrEnum):
    DESCRIBE = "node.describe"
    EVENT = "node.event"
    INVOKE = "node.invoke"
    INVOKE_PROGRESS = "node.invoke.progress"
    INVOKE_RESULT = "node.invoke.result"
    LIST = "node.list"
    PAIR_APPROVE = "node.pair.approve"
    PAIR_LIST = "node.pair.list"
    PAIR_REJECT = "node.pair.reject"
    PAIR_REMOVE = "node.pair.remove"
    PENDING_ACK = "node.pending.ack"
    PENDING_DRAIN = "node.pending.drain"
    PENDING_ENQUEUE = "node.pending.enqueue"
    PENDING_PULL = "node.pending.pull"
    PLUGIN_SURFACE_REFRESH = "node.pluginSurface.refresh"
    PLUGIN_TOOLS_UPDATE = "node.pluginTools.update"
    RENAME = "node.rename"
    SKILLS_UPDATE = "node.skills.update"


class NodeClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def describe(
        self,
        *,
        node_id: str,
    ) -> Any:
        payload = NodeDescribeParams(
            node_id=node_id,
        )
        return await self._client.request(
            NodeMethod.DESCRIBE,
            params=payload,
        )

    async def event(
        self,
        *,
        event: str,
        payload: Any | None = None,
        payload_json: str | None = None,
    ) -> NodeEventResult:
        payload = NodeEventParams(
            event=event,
            payload=payload,
            payload_json=payload_json,
        )
        return await self._client.request(
            NodeMethod.EVENT,
            params=payload,
            result_model=NodeEventResult,
        )

    async def invoke(
        self,
        *,
        node_id: str,
        command: str,
        idempotency_key: str,
        params: Any | None = None,
        timeout_ms: int | None = None,
        session_key: str | None = None,
        turn_source_channel: str | None = None,
        turn_source_to: str | None = None,
        turn_source_account_id: str | None = None,
        turn_source_thread_id: str | float | None = None,
    ) -> Any:
        payload = NodeInvokeParams(
            node_id=node_id,
            command=command,
            idempotency_key=idempotency_key,
            params=params,
            timeout_ms=timeout_ms,
            session_key=session_key,
            turn_source_channel=turn_source_channel,
            turn_source_to=turn_source_to,
            turn_source_account_id=turn_source_account_id,
            turn_source_thread_id=turn_source_thread_id,
        )
        return await self._client.request(
            NodeMethod.INVOKE,
            params=payload,
        )

    async def progress_invoke(
        self,
        *,
        invoke_id: str,
        node_id: str,
        seq: int,
        chunk: str,
    ) -> Any:
        payload = NodeInvokeProgressParams(
            invoke_id=invoke_id,
            node_id=node_id,
            seq=seq,
            chunk=chunk,
        )
        return await self._client.request(
            NodeMethod.INVOKE_PROGRESS,
            params=payload,
        )

    async def result_invoke(
        self,
        *,
        id: str,
        node_id: str,
        ok: bool,
        payload: Any | None = None,
        payload_json: str | None = None,
        error: dict[str, Any] | None = None,
    ) -> Any:
        payload = NodeInvokeResultParams(
            id=id,
            node_id=node_id,
            ok=ok,
            payload=payload,
            payload_json=payload_json,
            error=error,
        )
        return await self._client.request(
            NodeMethod.INVOKE_RESULT,
            params=payload,
        )

    async def approve_pair(
        self,
        *,
        request_id: str,
    ) -> Any:
        payload = NodePairApproveParams(
            request_id=request_id,
        )
        return await self._client.request(
            NodeMethod.PAIR_APPROVE,
            params=payload,
        )

    async def list_pair(
        self,
    ) -> Any:
        payload = NodePairListParams()
        return await self._client.request(
            NodeMethod.PAIR_LIST,
            params=payload,
        )

    async def reject_pair(
        self,
        *,
        request_id: str,
    ) -> Any:
        payload = NodePairRejectParams(
            request_id=request_id,
        )
        return await self._client.request(
            NodeMethod.PAIR_REJECT,
            params=payload,
        )

    async def remove_pair(
        self,
        *,
        node_id: str,
    ) -> Any:
        payload = NodePairRemoveParams(
            node_id=node_id,
        )
        return await self._client.request(
            NodeMethod.PAIR_REMOVE,
            params=payload,
        )

    async def ack_pending(
        self,
        *,
        ids: list[str],
    ) -> Any:
        payload = NodePendingAckParams(
            ids=ids,
        )
        return await self._client.request(
            NodeMethod.PENDING_ACK,
            params=payload,
        )

    async def drain_pending(
        self,
        *,
        max_items: int | None = None,
    ) -> NodePendingDrainResult:
        payload = NodePendingDrainParams(
            max_items=max_items,
        )
        return await self._client.request(
            NodeMethod.PENDING_DRAIN,
            params=payload,
            result_model=NodePendingDrainResult,
        )

    async def enqueue_pending(
        self,
        *,
        node_id: str,
        type: NodePendingEnqueueType,
        priority: NodePendingEnqueuePriority | None = None,
        expires_in_ms: int | None = None,
        wake: bool | None = None,
    ) -> NodePendingEnqueueResult:
        payload = NodePendingEnqueueParams(
            node_id=node_id,
            type=type,
            priority=priority,
            expires_in_ms=expires_in_ms,
            wake=wake,
        )
        return await self._client.request(
            NodeMethod.PENDING_ENQUEUE,
            params=payload,
            result_model=NodePendingEnqueueResult,
        )

    async def pull_pending(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            NodeMethod.PENDING_PULL,
            params=payload,
        )

    async def refresh_plugin_surface(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            NodeMethod.PLUGIN_SURFACE_REFRESH,
            params=payload,
        )

    async def update_plugin_tools(
        self,
        *,
        tools: list[NodePluginToolDescriptor],
    ) -> Any:
        payload = NodePluginToolsUpdateParams(
            tools=tools,
        )
        return await self._client.request(
            NodeMethod.PLUGIN_TOOLS_UPDATE,
            params=payload,
        )

    async def rename(
        self,
        *,
        node_id: str,
        display_name: str,
    ) -> Any:
        payload = NodeRenameParams(
            node_id=node_id,
            display_name=display_name,
        )
        return await self._client.request(
            NodeMethod.RENAME,
            params=payload,
        )

    async def update_skills(
        self,
        *,
        skills: list[NodeSkillDescriptor],
    ) -> Any:
        payload = NodeSkillsUpdateParams(
            skills=skills,
        )
        return await self._client.request(
            NodeMethod.SKILLS_UPDATE,
            params=payload,
        )

    async def list(
        self,
    ) -> Any:
        payload = NodeListParams()
        return await self._client.request(
            NodeMethod.LIST,
            params=payload,
        )
