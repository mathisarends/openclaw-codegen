"""Generated migrations RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    MigrationsMemoryApplyParams,
    MigrationsMemoryApplyResult,
    MigrationsMemoryPlanParams,
    MigrationsMemoryPlanResult,
)


class MigrationsMethod(StrEnum):
    MEMORY_APPLY = "migrations.memory.apply"
    MEMORY_PLAN = "migrations.memory.plan"


class MigrationsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def apply_memory(
        self,
        *,
        idempotency_key: str,
        agent_id: str,
        provider_id: str,
        plan_fingerprint: str,
        item_ids: list[str],
        overwrite: bool | None = None,
    ) -> MigrationsMemoryApplyResult:
        payload = MigrationsMemoryApplyParams(
            idempotency_key=idempotency_key,
            agent_id=agent_id,
            provider_id=provider_id,
            plan_fingerprint=plan_fingerprint,
            item_ids=item_ids,
            overwrite=overwrite,
        )
        return await self._client.request(
            MigrationsMethod.MEMORY_APPLY,
            params=payload,
            result_model=MigrationsMemoryApplyResult,
        )

    async def plan_memory(
        self,
        *,
        agent_id: str,
        overwrite: bool | None = None,
    ) -> MigrationsMemoryPlanResult:
        payload = MigrationsMemoryPlanParams(
            agent_id=agent_id,
            overwrite=overwrite,
        )
        return await self._client.request(
            MigrationsMethod.MEMORY_PLAN,
            params=payload,
            result_model=MigrationsMemoryPlanResult,
        )
