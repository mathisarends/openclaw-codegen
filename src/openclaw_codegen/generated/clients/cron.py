"""Generated cron RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    CronAddParams,
    CronAddResult,
    CronGetParams,
    CronJobLastDeliveryStatus,
    CronJobLastRunStatus,
    CronJobWakeMode,
    CronListEnabled,
    CronListLastRunStatus,
    CronListParams,
    CronListScheduleKind,
    CronListSortBy,
    CronListSortDir,
    CronRemoveParams,
    CronRunParams,
    CronRunsParams,
    CronRunsScope,
    CronRunsStatus,
    CronScratchGetParams,
    CronScratchGetResult,
    CronScratchSetParams,
    CronScratchSetResult,
    CronStatusParams,
    CronUpdateParams,
)


class CronMethod(StrEnum):
    ADD = "cron.add"
    GET = "cron.get"
    LIST = "cron.list"
    REMOVE = "cron.remove"
    RUN = "cron.run"
    RUNS = "cron.runs"
    SCRATCH_GET = "cron.scratch.get"
    SCRATCH_SET = "cron.scratch.set"
    STATUS = "cron.status"
    UPDATE = "cron.update"


class CronClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def add(
        self,
        *,
        name: str,
        schedule: dict[str, Any],
        session_target: str | Literal["main", "isolated", "current"],
        wake_mode: CronJobWakeMode,
        payload: dict[str, Any],
        declaration_key: str | None = None,
        display_name: str | None = None,
        owner: dict[str, Any] | None = None,
        agent_id: str | None = None,
        session_key: str | None = None,
        description: str | None = None,
        enabled: bool | None = None,
        delete_after_run: bool | None = None,
        pacing: dict[str, Any] | None = None,
        trigger: dict[str, Any] | None = None,
        delivery: dict[str, Any] | None = None,
        failure_alert: dict[str, Any] | Literal[False] | None = None,
    ) -> CronAddResult:
        payload = CronAddParams(
            name=name,
            schedule=schedule,
            session_target=session_target,
            wake_mode=wake_mode,
            payload=payload,
            declaration_key=declaration_key,
            display_name=display_name,
            owner=owner,
            agent_id=agent_id,
            session_key=session_key,
            description=description,
            enabled=enabled,
            delete_after_run=delete_after_run,
            pacing=pacing,
            trigger=trigger,
            delivery=delivery,
            failure_alert=failure_alert,
        )
        return await self._client.request(
            CronMethod.ADD,
            params=payload,
            result_model=CronAddResult,
        )

    async def get(
        self,
    ) -> Any:
        payload = CronGetParams()
        return await self._client.request(
            CronMethod.GET,
            params=payload,
        )

    async def remove(
        self,
    ) -> Any:
        payload = CronRemoveParams()
        return await self._client.request(
            CronMethod.REMOVE,
            params=payload,
        )

    async def run(
        self,
    ) -> Any:
        payload = CronRunParams()
        return await self._client.request(
            CronMethod.RUN,
            params=payload,
        )

    async def runs(
        self,
        *,
        agent_id: str | None = None,
        scope: CronRunsScope | None = None,
        id: str | None = None,
        job_id: str | None = None,
        run_id: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        statuses: list[CronJobLastRunStatus] | None = None,
        status: CronRunsStatus | None = None,
        delivery_statuses: list[CronJobLastDeliveryStatus] | None = None,
        delivery_status: CronJobLastDeliveryStatus | None = None,
        query: str | None = None,
        sort_dir: CronListSortDir | None = None,
    ) -> Any:
        payload = CronRunsParams(
            agent_id=agent_id,
            scope=scope,
            id=id,
            job_id=job_id,
            run_id=run_id,
            limit=limit,
            offset=offset,
            statuses=statuses,
            status=status,
            delivery_statuses=delivery_statuses,
            delivery_status=delivery_status,
            query=query,
            sort_dir=sort_dir,
        )
        return await self._client.request(
            CronMethod.RUNS,
            params=payload,
        )

    async def get_scratch(
        self,
    ) -> CronScratchGetResult:
        payload = CronScratchGetParams()
        return await self._client.request(
            CronMethod.SCRATCH_GET,
            params=payload,
            result_model=CronScratchGetResult,
        )

    async def set_scratch(
        self,
    ) -> CronScratchSetResult:
        payload = CronScratchSetParams()
        return await self._client.request(
            CronMethod.SCRATCH_SET,
            params=payload,
            result_model=CronScratchSetResult,
        )

    async def status(
        self,
    ) -> Any:
        payload = CronStatusParams()
        return await self._client.request(
            CronMethod.STATUS,
            params=payload,
        )

    async def update(
        self,
    ) -> Any:
        payload = CronUpdateParams()
        return await self._client.request(
            CronMethod.UPDATE,
            params=payload,
        )

    async def list(
        self,
        *,
        include_disabled: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        query: str | None = None,
        enabled: CronListEnabled | None = None,
        schedule_kind: CronListScheduleKind | None = None,
        last_run_status: CronListLastRunStatus | None = None,
        sort_by: CronListSortBy | None = None,
        sort_dir: CronListSortDir | None = None,
        agent_id: str | None = None,
        compact: bool | None = None,
        include_delivery_previews: bool | None = None,
    ) -> Any:
        payload = CronListParams(
            include_disabled=include_disabled,
            limit=limit,
            offset=offset,
            query=query,
            enabled=enabled,
            schedule_kind=schedule_kind,
            last_run_status=last_run_status,
            sort_by=sort_by,
            sort_dir=sort_dir,
            agent_id=agent_id,
            compact=compact,
            include_delivery_previews=include_delivery_previews,
        )
        return await self._client.request(
            CronMethod.LIST,
            params=payload,
        )
