"""Generated agents RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    AgentsCreateParams,
    AgentsCreateResult,
    AgentsDeleteParams,
    AgentsDeleteResult,
    AgentsFilesGetParams,
    AgentsFilesGetResult,
    AgentsFilesListParams,
    AgentsFilesListResult,
    AgentsFilesSetParams,
    AgentsFilesSetResult,
    AgentsListParams,
    AgentsListResult,
    AgentsUpdateParams,
    AgentsUpdateResult,
    AgentsWorkspaceGetParams,
    AgentsWorkspaceGetResult,
    AgentsWorkspaceListParams,
    AgentsWorkspaceListResult,
)


class AgentsMethod(StrEnum):
    CREATE = "agents.create"
    DELETE = "agents.delete"
    FILES_GET = "agents.files.get"
    FILES_LIST = "agents.files.list"
    FILES_SET = "agents.files.set"
    LIST = "agents.list"
    UPDATE = "agents.update"
    WORKSPACE_GET = "agents.workspace.get"
    WORKSPACE_LIST = "agents.workspace.list"


class AgentsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def create(
        self,
        *,
        name: str,
        workspace: str | None = None,
        model: str | None = None,
        emoji: str | None = None,
        avatar: str | None = None,
    ) -> AgentsCreateResult:
        payload = AgentsCreateParams(
            name=name,
            workspace=workspace,
            model=model,
            emoji=emoji,
            avatar=avatar,
        )
        return await self._client.request(
            AgentsMethod.CREATE,
            params=payload,
            result_model=AgentsCreateResult,
        )

    async def delete(
        self,
        *,
        agent_id: str,
        delete_files: bool | None = None,
    ) -> AgentsDeleteResult:
        payload = AgentsDeleteParams(
            agent_id=agent_id,
            delete_files=delete_files,
        )
        return await self._client.request(
            AgentsMethod.DELETE,
            params=payload,
            result_model=AgentsDeleteResult,
        )

    async def get_files(
        self,
        *,
        agent_id: str,
        name: str,
    ) -> AgentsFilesGetResult:
        payload = AgentsFilesGetParams(
            agent_id=agent_id,
            name=name,
        )
        return await self._client.request(
            AgentsMethod.FILES_GET,
            params=payload,
            result_model=AgentsFilesGetResult,
        )

    async def list_files(
        self,
        *,
        agent_id: str,
    ) -> AgentsFilesListResult:
        payload = AgentsFilesListParams(
            agent_id=agent_id,
        )
        return await self._client.request(
            AgentsMethod.FILES_LIST,
            params=payload,
            result_model=AgentsFilesListResult,
        )

    async def set_files(
        self,
        *,
        agent_id: str,
        name: str,
        content: str,
    ) -> AgentsFilesSetResult:
        payload = AgentsFilesSetParams(
            agent_id=agent_id,
            name=name,
            content=content,
        )
        return await self._client.request(
            AgentsMethod.FILES_SET,
            params=payload,
            result_model=AgentsFilesSetResult,
        )

    async def update(
        self,
        *,
        agent_id: str,
        name: str | None = None,
        workspace: str | None = None,
        model: str | None = None,
        emoji: str | None = None,
        avatar: str | None = None,
    ) -> AgentsUpdateResult:
        payload = AgentsUpdateParams(
            agent_id=agent_id,
            name=name,
            workspace=workspace,
            model=model,
            emoji=emoji,
            avatar=avatar,
        )
        return await self._client.request(
            AgentsMethod.UPDATE,
            params=payload,
            result_model=AgentsUpdateResult,
        )

    async def get_workspace(
        self,
        *,
        agent_id: str,
        path: str,
    ) -> AgentsWorkspaceGetResult:
        payload = AgentsWorkspaceGetParams(
            agent_id=agent_id,
            path=path,
        )
        return await self._client.request(
            AgentsMethod.WORKSPACE_GET,
            params=payload,
            result_model=AgentsWorkspaceGetResult,
        )

    async def list_workspace(
        self,
        *,
        agent_id: str,
        path: str | None = None,
        offset: int | None = None,
        limit: int | None = None,
    ) -> AgentsWorkspaceListResult:
        payload = AgentsWorkspaceListParams(
            agent_id=agent_id,
            path=path,
            offset=offset,
            limit=limit,
        )
        return await self._client.request(
            AgentsMethod.WORKSPACE_LIST,
            params=payload,
            result_model=AgentsWorkspaceListResult,
        )

    async def list(
        self,
    ) -> AgentsListResult:
        payload = AgentsListParams()
        return await self._client.request(
            AgentsMethod.LIST,
            params=payload,
            result_model=AgentsListResult,
        )
