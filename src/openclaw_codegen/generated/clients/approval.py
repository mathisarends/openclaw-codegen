"""Generated approval RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    ApprovalDecision,
    ApprovalGetParams,
    ApprovalGetResult,
    ApprovalHistoryParams,
    ApprovalHistoryResult,
    ApprovalKind,
    ApprovalResolveParams,
    ApprovalResolveResult,
)


class ApprovalMethod(StrEnum):
    GET = "approval.get"
    HISTORY = "approval.history"
    RESOLVE = "approval.resolve"


class ApprovalClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def get(
        self,
        *,
        id: str,
    ) -> ApprovalGetResult:
        payload = ApprovalGetParams(
            id=id,
        )
        return await self._client.request(
            ApprovalMethod.GET,
            params=payload,
            result_model=ApprovalGetResult,
        )

    async def history(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        kind: ApprovalKind | None = None,
    ) -> ApprovalHistoryResult:
        payload = ApprovalHistoryParams(
            cursor=cursor,
            limit=limit,
            kind=kind,
        )
        return await self._client.request(
            ApprovalMethod.HISTORY,
            params=payload,
            result_model=ApprovalHistoryResult,
        )

    async def resolve(
        self,
        *,
        id: str,
        kind: ApprovalKind,
        decision: ApprovalDecision,
    ) -> ApprovalResolveResult:
        payload = ApprovalResolveParams(
            id=id,
            kind=kind,
            decision=decision,
        )
        return await self._client.request(
            ApprovalMethod.RESOLVE,
            params=payload,
            result_model=ApprovalResolveResult,
        )
