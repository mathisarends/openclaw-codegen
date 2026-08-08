"""Generated wizard RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    WizardCancelParams,
    WizardNextParams,
    WizardNextResult,
    WizardStartFlow,
    WizardStartParams,
    WizardStartResult,
    WizardStatusParams,
    WizardStatusResult,
    WorktreeBranchKind,
)


class WizardMethod(StrEnum):
    CANCEL = "wizard.cancel"
    NEXT = "wizard.next"
    START = "wizard.start"
    STATUS = "wizard.status"


class WizardClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def cancel(
        self,
        *,
        session_id: str,
    ) -> Any:
        payload = WizardCancelParams(
            session_id=session_id,
        )
        return await self._client.request(
            WizardMethod.CANCEL,
            params=payload,
        )

    async def next(
        self,
        *,
        session_id: str,
        answer: dict[str, Any] | None = None,
    ) -> WizardNextResult:
        payload = WizardNextParams(
            session_id=session_id,
            answer=answer,
        )
        return await self._client.request(
            WizardMethod.NEXT,
            params=payload,
            result_model=WizardNextResult,
        )

    async def start(
        self,
        *,
        mode: WorktreeBranchKind | None = None,
        workspace: str | None = None,
        install_daemon: bool | None = None,
        flow: WizardStartFlow | None = None,
        channel: str | None = None,
    ) -> WizardStartResult:
        payload = WizardStartParams(
            mode=mode,
            workspace=workspace,
            install_daemon=install_daemon,
            flow=flow,
            channel=channel,
        )
        return await self._client.request(
            WizardMethod.START,
            params=payload,
            result_model=WizardStartResult,
        )

    async def status(
        self,
        *,
        session_id: str,
    ) -> WizardStatusResult:
        payload = WizardStatusParams(
            session_id=session_id,
        )
        return await self._client.request(
            WizardMethod.STATUS,
            params=payload,
            result_model=WizardStatusResult,
        )
