"""Generated doctor RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class DoctorMethod(StrEnum):
    MEMORY_BACKFILL_DREAM_DIARY = "doctor.memory.backfillDreamDiary"
    MEMORY_DEDUPE_DREAM_DIARY = "doctor.memory.dedupeDreamDiary"
    MEMORY_DREAM_DIARY = "doctor.memory.dreamDiary"
    MEMORY_REM_HARNESS = "doctor.memory.remHarness"
    MEMORY_REPAIR_DREAMING_ARTIFACTS = "doctor.memory.repairDreamingArtifacts"
    MEMORY_RESET_DREAM_DIARY = "doctor.memory.resetDreamDiary"
    MEMORY_RESET_GROUNDED_SHORT_TERM = "doctor.memory.resetGroundedShortTerm"
    MEMORY_STATUS = "doctor.memory.status"


class DoctorClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def backfill_dream_diary_memory(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            DoctorMethod.MEMORY_BACKFILL_DREAM_DIARY,
            params=payload,
        )

    async def dedupe_dream_diary_memory(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            DoctorMethod.MEMORY_DEDUPE_DREAM_DIARY,
            params=payload,
        )

    async def dream_diary_memory(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            DoctorMethod.MEMORY_DREAM_DIARY,
            params=payload,
        )

    async def rem_harness_memory(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            DoctorMethod.MEMORY_REM_HARNESS,
            params=payload,
        )

    async def repair_dreaming_artifacts_memory(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            DoctorMethod.MEMORY_REPAIR_DREAMING_ARTIFACTS,
            params=payload,
        )

    async def reset_dream_diary_memory(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            DoctorMethod.MEMORY_RESET_DREAM_DIARY,
            params=payload,
        )

    async def reset_grounded_short_term_memory(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            DoctorMethod.MEMORY_RESET_GROUNDED_SHORT_TERM,
            params=payload,
        )

    async def status_memory(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            DoctorMethod.MEMORY_STATUS,
            params=payload,
        )
