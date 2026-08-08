"""Generated task_suggestions RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    TaskSuggestionsAcceptParams,
    TaskSuggestionsAcceptResult,
    TaskSuggestionsCreateParams,
    TaskSuggestionsCreateResult,
    TaskSuggestionsDismissParams,
    TaskSuggestionsDismissResult,
    TaskSuggestionsListParams,
    TaskSuggestionsListResult,
)


class TaskSuggestionsMethod(StrEnum):
    ACCEPT = "taskSuggestions.accept"
    CREATE = "taskSuggestions.create"
    DISMISS = "taskSuggestions.dismiss"
    LIST = "taskSuggestions.list"


class TaskSuggestionsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def accept(
        self,
        *,
        task_id: str,
    ) -> TaskSuggestionsAcceptResult:
        payload = TaskSuggestionsAcceptParams(
            task_id=task_id,
        )
        return await self._client.request(
            TaskSuggestionsMethod.ACCEPT,
            params=payload,
            result_model=TaskSuggestionsAcceptResult,
        )

    async def create(
        self,
        *,
        title: str,
        prompt: str,
        tldr: str,
        cwd: str,
        session_key: str,
        agent_id: str | None = None,
    ) -> TaskSuggestionsCreateResult:
        payload = TaskSuggestionsCreateParams(
            title=title,
            prompt=prompt,
            tldr=tldr,
            cwd=cwd,
            session_key=session_key,
            agent_id=agent_id,
        )
        return await self._client.request(
            TaskSuggestionsMethod.CREATE,
            params=payload,
            result_model=TaskSuggestionsCreateResult,
        )

    async def dismiss(
        self,
        *,
        task_id: str,
        reason: str | None = None,
    ) -> TaskSuggestionsDismissResult:
        payload = TaskSuggestionsDismissParams(
            task_id=task_id,
            reason=reason,
        )
        return await self._client.request(
            TaskSuggestionsMethod.DISMISS,
            params=payload,
            result_model=TaskSuggestionsDismissResult,
        )

    async def list(
        self,
        *,
        session_key: str | None = None,
        agent_id: str | None = None,
    ) -> TaskSuggestionsListResult:
        payload = TaskSuggestionsListParams(
            session_key=session_key,
            agent_id=agent_id,
        )
        return await self._client.request(
            TaskSuggestionsMethod.LIST,
            params=payload,
            result_model=TaskSuggestionsListResult,
        )
