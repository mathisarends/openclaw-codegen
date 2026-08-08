"""Generated session RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    SessionDiscussionInfoParams,
    SessionDiscussionInfoResult,
    SessionDiscussionOpenParams,
    SessionDiscussionOpenResult,
    SessionMemberAddParams,
    SessionMemberRemoveParams,
    SessionMembersListParams,
    SessionMembersListResult,
    SessionSuggestionResolution,
    SessionSuggestionsAddParams,
    SessionSuggestionsAddResult,
    SessionSuggestionsListParams,
    SessionSuggestionsListResult,
    SessionSuggestionsResolveParams,
    SessionSuggestionsResolveResult,
    SessionTypingParams,
    SessionTypingResult,
    SessionVisibility,
    SessionVisibilitySetParams,
    SessionVisibilitySetResult,
)


class SessionMethod(StrEnum):
    DISCUSSION_INFO = "session.discussion.info"
    DISCUSSION_OPEN = "session.discussion.open"
    MEMBERS_ADD = "session.members.add"
    MEMBERS_LIST = "session.members.list"
    MEMBERS_REMOVE = "session.members.remove"
    SUGGESTIONS_ADD = "session.suggestions.add"
    SUGGESTIONS_LIST = "session.suggestions.list"
    SUGGESTIONS_RESOLVE = "session.suggestions.resolve"
    TYPING = "session.typing"
    VISIBILITY_SET = "session.visibility.set"


class SessionClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def info_discussion(
        self,
        *,
        session_key: str,
    ) -> SessionDiscussionInfoResult:
        payload = SessionDiscussionInfoParams(
            session_key=session_key,
        )
        return await self._client.request(
            SessionMethod.DISCUSSION_INFO,
            params=payload,
            result_model=SessionDiscussionInfoResult,
        )

    async def open_discussion(
        self,
        *,
        session_key: str,
    ) -> SessionDiscussionOpenResult:
        payload = SessionDiscussionOpenParams(
            session_key=session_key,
        )
        return await self._client.request(
            SessionMethod.DISCUSSION_OPEN,
            params=payload,
            result_model=SessionDiscussionOpenResult,
        )

    async def add_members(
        self,
        *,
        session_key: str,
        identity_id: str,
        agent_id: str | None = None,
    ) -> Any:
        payload = SessionMemberAddParams(
            session_key=session_key,
            identity_id=identity_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionMethod.MEMBERS_ADD,
            params=payload,
        )

    async def list_members(
        self,
        *,
        session_key: str,
        agent_id: str | None = None,
    ) -> SessionMembersListResult:
        payload = SessionMembersListParams(
            session_key=session_key,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionMethod.MEMBERS_LIST,
            params=payload,
            result_model=SessionMembersListResult,
        )

    async def remove_members(
        self,
        *,
        session_key: str,
        identity_id: str,
        agent_id: str | None = None,
    ) -> Any:
        payload = SessionMemberRemoveParams(
            session_key=session_key,
            identity_id=identity_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionMethod.MEMBERS_REMOVE,
            params=payload,
        )

    async def add_suggestions(
        self,
        *,
        session_key: str,
        text: str,
        agent_id: str | None = None,
    ) -> SessionSuggestionsAddResult:
        payload = SessionSuggestionsAddParams(
            session_key=session_key,
            text=text,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionMethod.SUGGESTIONS_ADD,
            params=payload,
            result_model=SessionSuggestionsAddResult,
        )

    async def list_suggestions(
        self,
        *,
        session_key: str,
        agent_id: str | None = None,
    ) -> SessionSuggestionsListResult:
        payload = SessionSuggestionsListParams(
            session_key=session_key,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionMethod.SUGGESTIONS_LIST,
            params=payload,
            result_model=SessionSuggestionsListResult,
        )

    async def resolve_suggestions(
        self,
        *,
        session_key: str,
        id: str,
        resolution: SessionSuggestionResolution,
        agent_id: str | None = None,
    ) -> SessionSuggestionsResolveResult:
        payload = SessionSuggestionsResolveParams(
            session_key=session_key,
            id=id,
            resolution=resolution,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionMethod.SUGGESTIONS_RESOLVE,
            params=payload,
            result_model=SessionSuggestionsResolveResult,
        )

    async def typing(
        self,
        *,
        session_key: str,
        session_id: str,
        typing: bool,
        agent_id: str | None = None,
    ) -> SessionTypingResult:
        payload = SessionTypingParams(
            session_key=session_key,
            session_id=session_id,
            typing=typing,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionMethod.TYPING,
            params=payload,
            result_model=SessionTypingResult,
        )

    async def set_visibility(
        self,
        *,
        session_key: str,
        visibility: SessionVisibility,
        agent_id: str | None = None,
    ) -> SessionVisibilitySetResult:
        payload = SessionVisibilitySetParams(
            session_key=session_key,
            visibility=visibility,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionMethod.VISIBILITY_SET,
            params=payload,
            result_model=SessionVisibilitySetResult,
        )
