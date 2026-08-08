"""Generated tasks RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    TasksCancelParams,
    TasksCancelResult,
    TasksGetParams,
    TasksGetResult,
    TasksListParams,
    TasksListResult,
    TaskSummaryStatus,
)


class TasksMethod(StrEnum):
    CANCEL = "tasks.cancel"
    GET = "tasks.get"
    LIST = "tasks.list"


class TasksClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def cancel(
        self,
        *,
        task_id: str,
        reason: str | None = None,
    ) -> TasksCancelResult:
        payload = TasksCancelParams(
            task_id=task_id,
            reason=reason,
        )
        return await self._client.request(
            TasksMethod.CANCEL,
            params=payload,
            result_model=TasksCancelResult,
        )

    async def get(
        self,
        *,
        task_id: str,
    ) -> TasksGetResult:
        payload = TasksGetParams(
            task_id=task_id,
        )
        return await self._client.request(
            TasksMethod.GET,
            params=payload,
            result_model=TasksGetResult,
        )

    async def list(
        self,
        *,
        status: TaskSummaryStatus | list[TaskSummaryStatus] | None = None,
        agent_id: str | None = None,
        session_key: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
    ) -> TasksListResult:
        payload = TasksListParams(
            status=status,
            agent_id=agent_id,
            session_key=session_key,
            limit=limit,
            cursor=cursor,
        )
        return await self._client.request(
            TasksMethod.LIST,
            params=payload,
            result_model=TasksListResult,
        )
