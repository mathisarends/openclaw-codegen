"""Generated exec RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    ExecApprovalGetParams,
    ExecApprovalRequestParams,
    ExecApprovalResolveParams,
    ExecApprovalsGetParams,
    ExecApprovalsNodeGetParams,
    ExecApprovalsNodeSetParams,
    ExecApprovalsSetParams,
)


class ExecMethod(StrEnum):
    APPROVAL_GET = "exec.approval.get"
    APPROVAL_LIST = "exec.approval.list"
    APPROVAL_REQUEST = "exec.approval.request"
    APPROVAL_RESOLVE = "exec.approval.resolve"
    APPROVAL_WAIT_DECISION = "exec.approval.waitDecision"
    APPROVALS_GET = "exec.approvals.get"
    APPROVALS_NODE_GET = "exec.approvals.node.get"
    APPROVALS_NODE_SET = "exec.approvals.node.set"
    APPROVALS_SET = "exec.approvals.set"


class ExecClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def get_approval(
        self,
        *,
        id: str,
    ) -> Any:
        payload = ExecApprovalGetParams(
            id=id,
        )
        return await self._client.request(
            ExecMethod.APPROVAL_GET,
            params=payload,
        )

    async def list_approval(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            ExecMethod.APPROVAL_LIST,
            params=payload,
        )

    async def request_approval(
        self,
        *,
        id: str | None = None,
        command: str | None = None,
        command_argv: list[str] | None = None,
        system_run_plan: dict[str, Any] | None = None,
        env: dict[str, Any] | None = None,
        cwd: str | None = None,
        node_id: str | None = None,
        host: str | None = None,
        security: str | None = None,
        ask: str | None = None,
        warning_text: str | None = None,
        unavailable_decisions: list[Literal["allow-always"]] | None = None,
        command_spans: list[dict[str, Any]] | None = None,
        agent_id: str | None = None,
        resolved_path: str | None = None,
        session_key: str | None = None,
        session_id: str | None = None,
        run_id: str | None = None,
        tool_call_id: str | None = None,
        turn_source_channel: str | None = None,
        turn_source_to: str | None = None,
        turn_source_account_id: str | None = None,
        turn_source_thread_id: str | float | None = None,
        approval_reviewer_device_ids: list[str] | None = None,
        require_delivery_route: bool | None = None,
        suppress_delivery: bool | None = None,
        timeout_ms: int | None = None,
        two_phase: bool | None = None,
    ) -> Any:
        payload = ExecApprovalRequestParams(
            id=id,
            command=command,
            command_argv=command_argv,
            system_run_plan=system_run_plan,
            env=env,
            cwd=cwd,
            node_id=node_id,
            host=host,
            security=security,
            ask=ask,
            warning_text=warning_text,
            unavailable_decisions=unavailable_decisions,
            command_spans=command_spans,
            agent_id=agent_id,
            resolved_path=resolved_path,
            session_key=session_key,
            session_id=session_id,
            run_id=run_id,
            tool_call_id=tool_call_id,
            turn_source_channel=turn_source_channel,
            turn_source_to=turn_source_to,
            turn_source_account_id=turn_source_account_id,
            turn_source_thread_id=turn_source_thread_id,
            approval_reviewer_device_ids=approval_reviewer_device_ids,
            require_delivery_route=require_delivery_route,
            suppress_delivery=suppress_delivery,
            timeout_ms=timeout_ms,
            two_phase=two_phase,
        )
        return await self._client.request(
            ExecMethod.APPROVAL_REQUEST,
            params=payload,
        )

    async def resolve_approval(
        self,
        *,
        id: str,
        decision: str,
    ) -> Any:
        payload = ExecApprovalResolveParams(
            id=id,
            decision=decision,
        )
        return await self._client.request(
            ExecMethod.APPROVAL_RESOLVE,
            params=payload,
        )

    async def wait_decision_approval(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            ExecMethod.APPROVAL_WAIT_DECISION,
            params=payload,
        )

    async def get_approvals(
        self,
    ) -> Any:
        payload = ExecApprovalsGetParams()
        return await self._client.request(
            ExecMethod.APPROVALS_GET,
            params=payload,
        )

    async def get_node_approvals(
        self,
        *,
        node_id: str,
    ) -> Any:
        payload = ExecApprovalsNodeGetParams(
            node_id=node_id,
        )
        return await self._client.request(
            ExecMethod.APPROVALS_NODE_GET,
            params=payload,
        )

    async def set_node_approvals(
        self,
        *,
        node_id: str,
        file: dict[str, Any] | None = None,
        native: dict[str, Any] | None = None,
        base_hash: str | None = None,
    ) -> Any:
        payload = ExecApprovalsNodeSetParams(
            node_id=node_id,
            file=file,
            native=native,
            base_hash=base_hash,
        )
        return await self._client.request(
            ExecMethod.APPROVALS_NODE_SET,
            params=payload,
        )

    async def set_approvals(
        self,
        *,
        file: dict[str, Any],
        base_hash: str | None = None,
    ) -> Any:
        payload = ExecApprovalsSetParams(
            file=file,
            base_hash=base_hash,
        )
        return await self._client.request(
            ExecMethod.APPROVALS_SET,
            params=payload,
        )
