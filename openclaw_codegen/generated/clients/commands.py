"""Generated commands RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    CommandEntryScope,
    CommandsListParams,
    CommandsListResult,
)


class CommandsMethod(StrEnum):
    LIST = "commands.list"


class CommandsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def list(
        self,
        *,
        agent_id: str | None = None,
        provider: str | None = None,
        scope: CommandEntryScope | None = None,
        include_args: bool | None = None,
    ) -> CommandsListResult:
        payload = CommandsListParams(
            agent_id=agent_id,
            provider=provider,
            scope=scope,
            include_args=include_args,
        )
        return await self._client.request(
            CommandsMethod.LIST,
            params=payload,
            result_model=CommandsListResult,
        )
