"""Generated audit RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    AuditActivityListDirection,
    AuditActivityListKind,
    AuditActivityListParams,
    AuditActivityListResult,
    AuditActivityToolActionV1Status,
    AuditEventKind,
    AuditListParams,
    AuditListResult,
)


class AuditMethod(StrEnum):
    ACTIVITY_LIST = "audit.activity.list"
    LIST = "audit.list"


class AuditClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def list_activity(
        self,
        *,
        agent_id: str | None = None,
        session_key: str | None = None,
        run_id: str | None = None,
        kind: AuditActivityListKind | None = None,
        status: AuditActivityToolActionV1Status | None = None,
        direction: AuditActivityListDirection | None = None,
        channel: str | None = None,
        after: int | None = None,
        before: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
    ) -> AuditActivityListResult:
        payload = AuditActivityListParams(
            agent_id=agent_id,
            session_key=session_key,
            run_id=run_id,
            kind=kind,
            status=status,
            direction=direction,
            channel=channel,
            after=after,
            before=before,
            limit=limit,
            cursor=cursor,
        )
        return await self._client.request(
            AuditMethod.ACTIVITY_LIST,
            params=payload,
            result_model=AuditActivityListResult,
        )

    async def list(
        self,
        *,
        agent_id: str | None = None,
        session_key: str | None = None,
        run_id: str | None = None,
        kind: AuditEventKind | None = None,
        status: AuditActivityToolActionV1Status | None = None,
        after: int | None = None,
        before: int | None = None,
        limit: int | None = None,
        cursor: str | None = None,
    ) -> AuditListResult:
        payload = AuditListParams(
            agent_id=agent_id,
            session_key=session_key,
            run_id=run_id,
            kind=kind,
            status=status,
            after=after,
            before=before,
            limit=limit,
            cursor=cursor,
        )
        return await self._client.request(
            AuditMethod.LIST,
            params=payload,
            result_model=AuditListResult,
        )
