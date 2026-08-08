"""Generated ui RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    UiClosePaneCommand,
    UiCommandParams,
    UiCommandResult,
    UiFocusCommand,
    UiNavigateCommand,
    UiPanelCommand,
    UiSidebarCommand,
    UiSplitCommand,
)


class UiMethod(StrEnum):
    COMMAND = "ui.command"


class UiClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def command(
        self,
        *,
        command: UiSplitCommand
        | UiClosePaneCommand
        | UiFocusCommand
        | UiSidebarCommand
        | UiPanelCommand
        | UiNavigateCommand,
        session_key: str | None = None,
    ) -> UiCommandResult:
        payload = UiCommandParams(
            command=command,
            session_key=session_key,
        )
        return await self._client.request(
            UiMethod.COMMAND,
            params=payload,
            result_model=UiCommandResult,
        )
