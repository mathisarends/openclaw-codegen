"""Generated environments RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    EnvironmentsCreateParams,
    EnvironmentsCreateResult,
    EnvironmentsDestroyParams,
    EnvironmentsDestroyResult,
    EnvironmentsListParams,
    EnvironmentsListResult,
    EnvironmentsStatusParams,
    EnvironmentsStatusResult,
)


class EnvironmentsMethod(StrEnum):
    CREATE = "environments.create"
    DESTROY = "environments.destroy"
    LIST = "environments.list"
    STATUS = "environments.status"


class EnvironmentsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def create(
        self,
        *,
        profile_id: str,
        idempotency_key: str,
    ) -> EnvironmentsCreateResult:
        payload = EnvironmentsCreateParams(
            profile_id=profile_id,
            idempotency_key=idempotency_key,
        )
        return await self._client.request(
            EnvironmentsMethod.CREATE,
            params=payload,
            result_model=EnvironmentsCreateResult,
        )

    async def destroy(
        self,
        *,
        environment_id: str,
        force: bool | None = None,
    ) -> EnvironmentsDestroyResult:
        payload = EnvironmentsDestroyParams(
            environment_id=environment_id,
            force=force,
        )
        return await self._client.request(
            EnvironmentsMethod.DESTROY,
            params=payload,
            result_model=EnvironmentsDestroyResult,
        )

    async def status(
        self,
        *,
        environment_id: str,
    ) -> EnvironmentsStatusResult:
        payload = EnvironmentsStatusParams(
            environment_id=environment_id,
        )
        return await self._client.request(
            EnvironmentsMethod.STATUS,
            params=payload,
            result_model=EnvironmentsStatusResult,
        )

    async def list(
        self,
    ) -> EnvironmentsListResult:
        payload = EnvironmentsListParams()
        return await self._client.request(
            EnvironmentsMethod.LIST,
            params=payload,
            result_model=EnvironmentsListResult,
        )
