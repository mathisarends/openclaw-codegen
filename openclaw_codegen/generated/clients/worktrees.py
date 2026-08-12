"""Generated worktrees RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    WorktreesBranchesParams,
    WorktreesBranchesResult,
    WorktreesCreateParams,
    WorktreesGcParams,
    WorktreesGcResult,
    WorktreesListParams,
    WorktreesListResult,
    WorktreesRemoveParams,
    WorktreesRemoveResult,
    WorktreesRestoreParams,
)


class WorktreesMethod(StrEnum):
    BRANCHES = "worktrees.branches"
    CREATE = "worktrees.create"
    GC = "worktrees.gc"
    LIST = "worktrees.list"
    REMOVE = "worktrees.remove"
    RESTORE = "worktrees.restore"


class WorktreesClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def branches(
        self,
        *,
        repo_root: str,
        include_repository_status: bool | None = None,
    ) -> WorktreesBranchesResult:
        payload = WorktreesBranchesParams(
            repo_root=repo_root,
            include_repository_status=include_repository_status,
        )
        return await self._client.request(
            WorktreesMethod.BRANCHES,
            params=payload,
            result_model=WorktreesBranchesResult,
        )

    async def create(
        self,
        *,
        repo_root: str,
        name: str | None = None,
        base_ref: str | None = None,
    ) -> Any:
        payload = WorktreesCreateParams(
            repo_root=repo_root,
            name=name,
            base_ref=base_ref,
        )
        return await self._client.request(
            WorktreesMethod.CREATE,
            params=payload,
        )

    async def gc(
        self,
    ) -> WorktreesGcResult:
        payload = WorktreesGcParams()
        return await self._client.request(
            WorktreesMethod.GC,
            params=payload,
            result_model=WorktreesGcResult,
        )

    async def remove(
        self,
        *,
        id: str,
        force: bool | None = None,
    ) -> WorktreesRemoveResult:
        payload = WorktreesRemoveParams(
            id=id,
            force=force,
        )
        return await self._client.request(
            WorktreesMethod.REMOVE,
            params=payload,
            result_model=WorktreesRemoveResult,
        )

    async def restore(
        self,
        *,
        id: str,
    ) -> Any:
        payload = WorktreesRestoreParams(
            id=id,
        )
        return await self._client.request(
            WorktreesMethod.RESTORE,
            params=payload,
        )

    async def list(
        self,
    ) -> WorktreesListResult:
        payload = WorktreesListParams()
        return await self._client.request(
            WorktreesMethod.LIST,
            params=payload,
            result_model=WorktreesListResult,
        )
