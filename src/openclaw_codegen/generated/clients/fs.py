"""Generated fs RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    FsListDirParams,
    FsListDirResult,
)


class FsMethod(StrEnum):
    LIST_DIR = "fs.listDir"


class FsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def list_dir(
        self,
        *,
        path: str | None = None,
        node_id: str | None = None,
    ) -> FsListDirResult:
        payload = FsListDirParams(
            path=path,
            node_id=node_id,
        )
        return await self._client.request(
            FsMethod.LIST_DIR,
            params=payload,
            result_model=FsListDirResult,
        )
