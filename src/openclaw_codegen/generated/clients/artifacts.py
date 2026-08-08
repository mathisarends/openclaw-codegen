"""Generated artifacts RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    ArtifactsDownloadParams,
    ArtifactsDownloadResult,
    ArtifactsGetParams,
    ArtifactsGetResult,
    ArtifactsListParams,
    ArtifactsListResult,
)


class ArtifactsMethod(StrEnum):
    DOWNLOAD = "artifacts.download"
    GET = "artifacts.get"
    LIST = "artifacts.list"


class ArtifactsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def download(
        self,
        *,
        artifact_id: str,
        session_key: str | None = None,
        run_id: str | None = None,
        task_id: str | None = None,
        agent_id: str | None = None,
    ) -> ArtifactsDownloadResult:
        payload = ArtifactsDownloadParams(
            artifact_id=artifact_id,
            session_key=session_key,
            run_id=run_id,
            task_id=task_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            ArtifactsMethod.DOWNLOAD,
            params=payload,
            result_model=ArtifactsDownloadResult,
        )

    async def get(
        self,
        *,
        artifact_id: str,
        session_key: str | None = None,
        run_id: str | None = None,
        task_id: str | None = None,
        agent_id: str | None = None,
    ) -> ArtifactsGetResult:
        payload = ArtifactsGetParams(
            artifact_id=artifact_id,
            session_key=session_key,
            run_id=run_id,
            task_id=task_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            ArtifactsMethod.GET,
            params=payload,
            result_model=ArtifactsGetResult,
        )

    async def list(
        self,
        *,
        session_key: str | None = None,
        run_id: str | None = None,
        task_id: str | None = None,
        agent_id: str | None = None,
    ) -> ArtifactsListResult:
        payload = ArtifactsListParams(
            session_key=session_key,
            run_id=run_id,
            task_id=task_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            ArtifactsMethod.LIST,
            params=payload,
            result_model=ArtifactsListResult,
        )
