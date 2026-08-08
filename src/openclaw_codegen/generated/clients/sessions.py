"""Generated sessions RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    SessionsAbortParams,
    SessionsBranchesListParams,
    SessionsBranchesListResult,
    SessionsBranchesSwitchParams,
    SessionsBranchesSwitchResult,
    SessionsCatalogArchiveParams,
    SessionsCatalogArchiveResult,
    SessionsCatalogContinueParams,
    SessionsCatalogContinueResult,
    SessionsCatalogListParams,
    SessionsCatalogListResult,
    SessionsCatalogReadParams,
    SessionsCatalogReadResult,
    SessionsCleanupParams,
    SessionsCompactionBranchParams,
    SessionsCompactionBranchResult,
    SessionsCompactionGetParams,
    SessionsCompactionGetResult,
    SessionsCompactionListParams,
    SessionsCompactionListResult,
    SessionsCompactionRestoreParams,
    SessionsCompactionRestoreResult,
    SessionsCompactParams,
    SessionsCompanionAskParams,
    SessionsCompanionAskResult,
    SessionsCompanionResetParams,
    SessionsCompanionResetResult,
    SessionsCompanionStateParams,
    SessionsCompanionStateResult,
    SessionsCreateParams,
    SessionsCreateResult,
    SessionsDeleteParams,
    SessionsDescribeParams,
    SessionsDiffParams,
    SessionsDiffResult,
    SessionsDispatchParams,
    SessionsDispatchResult,
    SessionsFilesGetParams,
    SessionsFilesGetResult,
    SessionsFilesListParams,
    SessionsFilesListResult,
    SessionsFilesRevealParams,
    SessionsFilesRevealResult,
    SessionsFilesSetParams,
    SessionsFilesSetResult,
    SessionsForkParams,
    SessionsForkResult,
    SessionsGroupsDeleteParams,
    SessionsGroupsListParams,
    SessionsGroupsListResult,
    SessionsGroupsPutParams,
    SessionsGroupsRenameParams,
    SessionsListBoardFace,
    SessionsListParams,
    SessionsListSortBy,
    SessionsMessagesSubscribeParams,
    SessionsMessagesUnsubscribeParams,
    SessionsObserverVisibilityParams,
    SessionsObserverVisibilityResult,
    SessionsPatchParams,
    SessionsPluginPatchParams,
    SessionsPluginPatchResult,
    SessionsPreviewParams,
    SessionsReclaimParams,
    SessionsReclaimResult,
    SessionsResetParams,
    SessionsResetReason,
    SessionsResolveParams,
    SessionsRewindParams,
    SessionsRewindResult,
    SessionsSearchParams,
    SessionsSearchResult,
    SessionsSendParams,
    SessionsUsageGroupBy,
    SessionsUsageMode,
    SessionsUsageParams,
    SessionsUsageRange,
    SessionVisibility,
)


class SessionsMethod(StrEnum):
    ABORT = "sessions.abort"
    BRANCHES_LIST = "sessions.branches.list"
    BRANCHES_SWITCH = "sessions.branches.switch"
    CATALOG_ARCHIVE = "sessions.catalog.archive"
    CATALOG_CONTINUE = "sessions.catalog.continue"
    CATALOG_LIST = "sessions.catalog.list"
    CATALOG_READ = "sessions.catalog.read"
    CLEANUP = "sessions.cleanup"
    COMPACT = "sessions.compact"
    COMPACTION_BRANCH = "sessions.compaction.branch"
    COMPACTION_GET = "sessions.compaction.get"
    COMPACTION_LIST = "sessions.compaction.list"
    COMPACTION_RESTORE = "sessions.compaction.restore"
    COMPANION_ASK = "sessions.companion.ask"
    COMPANION_RESET = "sessions.companion.reset"
    COMPANION_STATE = "sessions.companion.state"
    CREATE = "sessions.create"
    DELETE = "sessions.delete"
    DESCRIBE = "sessions.describe"
    DIFF = "sessions.diff"
    DISPATCH = "sessions.dispatch"
    FILES_GET = "sessions.files.get"
    FILES_LIST = "sessions.files.list"
    FILES_REVEAL = "sessions.files.reveal"
    FILES_SET = "sessions.files.set"
    FORK = "sessions.fork"
    GET = "sessions.get"
    GROUPS_DELETE = "sessions.groups.delete"
    GROUPS_LIST = "sessions.groups.list"
    GROUPS_PUT = "sessions.groups.put"
    GROUPS_RENAME = "sessions.groups.rename"
    LIST = "sessions.list"
    MESSAGES_SUBSCRIBE = "sessions.messages.subscribe"
    MESSAGES_UNSUBSCRIBE = "sessions.messages.unsubscribe"
    OBSERVER_VISIBILITY = "sessions.observer.visibility"
    PATCH = "sessions.patch"
    PLUGIN_PATCH = "sessions.pluginPatch"
    PREVIEW = "sessions.preview"
    RECLAIM = "sessions.reclaim"
    RESET = "sessions.reset"
    RESOLVE = "sessions.resolve"
    REWIND = "sessions.rewind"
    SEARCH = "sessions.search"
    SEND = "sessions.send"
    STEER = "sessions.steer"
    SUBSCRIBE = "sessions.subscribe"
    UNSUBSCRIBE = "sessions.unsubscribe"
    USAGE = "sessions.usage"
    USAGE_LOGS = "sessions.usage.logs"
    USAGE_TIMESERIES = "sessions.usage.timeseries"
    VIEWERS_SET = "sessions.viewers.set"


class SessionsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def abort(
        self,
        *,
        key: str | None = None,
        run_id: str | None = None,
        agent_id: str | None = None,
        clear_queued: bool | None = None,
    ) -> Any:
        payload = SessionsAbortParams(
            key=key,
            run_id=run_id,
            agent_id=agent_id,
            clear_queued=clear_queued,
        )
        return await self._client.request(
            SessionsMethod.ABORT,
            params=payload,
        )

    async def list_branches(
        self,
        *,
        session_key: str,
        agent_id: str | None = None,
    ) -> SessionsBranchesListResult:
        payload = SessionsBranchesListParams(
            session_key=session_key,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.BRANCHES_LIST,
            params=payload,
            result_model=SessionsBranchesListResult,
        )

    async def switch_branches(
        self,
        *,
        session_key: str,
        leaf_entry_id: str,
        agent_id: str | None = None,
    ) -> SessionsBranchesSwitchResult:
        payload = SessionsBranchesSwitchParams(
            session_key=session_key,
            leaf_entry_id=leaf_entry_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.BRANCHES_SWITCH,
            params=payload,
            result_model=SessionsBranchesSwitchResult,
        )

    async def archive_catalog(
        self,
        *,
        catalog_id: str,
        host_id: str,
        thread_id: str,
        confirm_no_other_runner: Literal[True],
    ) -> SessionsCatalogArchiveResult:
        payload = SessionsCatalogArchiveParams(
            catalog_id=catalog_id,
            host_id=host_id,
            thread_id=thread_id,
            confirm_no_other_runner=confirm_no_other_runner,
        )
        return await self._client.request(
            SessionsMethod.CATALOG_ARCHIVE,
            params=payload,
            result_model=SessionsCatalogArchiveResult,
        )

    async def continue__catalog(
        self,
        *,
        catalog_id: str,
        host_id: str,
        thread_id: str,
    ) -> SessionsCatalogContinueResult:
        payload = SessionsCatalogContinueParams(
            catalog_id=catalog_id,
            host_id=host_id,
            thread_id=thread_id,
        )
        return await self._client.request(
            SessionsMethod.CATALOG_CONTINUE,
            params=payload,
            result_model=SessionsCatalogContinueResult,
        )

    async def list_catalog(
        self,
        *,
        catalog_id: str | None = None,
        cursors: dict[str, Any] | None = None,
        agent_id: str | None = None,
        progress_id: str | None = None,
        search: str | None = None,
        limit_per_host: int | None = None,
        host_ids: list[str] | None = None,
    ) -> SessionsCatalogListResult:
        payload = SessionsCatalogListParams(
            catalog_id=catalog_id,
            cursors=cursors,
            agent_id=agent_id,
            progress_id=progress_id,
            search=search,
            limit_per_host=limit_per_host,
            host_ids=host_ids,
        )
        return await self._client.request(
            SessionsMethod.CATALOG_LIST,
            params=payload,
            result_model=SessionsCatalogListResult,
        )

    async def read_catalog(
        self,
        *,
        catalog_id: str,
        host_id: str,
        thread_id: str,
        limit: int | None = None,
        cursor: str | None = None,
    ) -> SessionsCatalogReadResult:
        payload = SessionsCatalogReadParams(
            catalog_id=catalog_id,
            host_id=host_id,
            thread_id=thread_id,
            limit=limit,
            cursor=cursor,
        )
        return await self._client.request(
            SessionsMethod.CATALOG_READ,
            params=payload,
            result_model=SessionsCatalogReadResult,
        )

    async def cleanup(
        self,
        *,
        agent: str | None = None,
        all_agents: bool | None = None,
        enforce: bool | None = None,
        active_key: str | None = None,
        fix_missing: bool | None = None,
        fix_dm_scope: bool | None = None,
    ) -> Any:
        payload = SessionsCleanupParams(
            agent=agent,
            all_agents=all_agents,
            enforce=enforce,
            active_key=active_key,
            fix_missing=fix_missing,
            fix_dm_scope=fix_dm_scope,
        )
        return await self._client.request(
            SessionsMethod.CLEANUP,
            params=payload,
        )

    async def compact(
        self,
        *,
        key: str,
        agent_id: str | None = None,
        max_lines: int | None = None,
    ) -> Any:
        payload = SessionsCompactParams(
            key=key,
            agent_id=agent_id,
            max_lines=max_lines,
        )
        return await self._client.request(
            SessionsMethod.COMPACT,
            params=payload,
        )

    async def branch_compaction(
        self,
        *,
        key: str,
        checkpoint_id: str,
        agent_id: str | None = None,
    ) -> SessionsCompactionBranchResult:
        payload = SessionsCompactionBranchParams(
            key=key,
            checkpoint_id=checkpoint_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.COMPACTION_BRANCH,
            params=payload,
            result_model=SessionsCompactionBranchResult,
        )

    async def get_compaction(
        self,
        *,
        key: str,
        checkpoint_id: str,
        agent_id: str | None = None,
    ) -> SessionsCompactionGetResult:
        payload = SessionsCompactionGetParams(
            key=key,
            checkpoint_id=checkpoint_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.COMPACTION_GET,
            params=payload,
            result_model=SessionsCompactionGetResult,
        )

    async def list_compaction(
        self,
        *,
        key: str,
        agent_id: str | None = None,
    ) -> SessionsCompactionListResult:
        payload = SessionsCompactionListParams(
            key=key,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.COMPACTION_LIST,
            params=payload,
            result_model=SessionsCompactionListResult,
        )

    async def restore_compaction(
        self,
        *,
        key: str,
        checkpoint_id: str,
        agent_id: str | None = None,
    ) -> SessionsCompactionRestoreResult:
        payload = SessionsCompactionRestoreParams(
            key=key,
            checkpoint_id=checkpoint_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.COMPACTION_RESTORE,
            params=payload,
            result_model=SessionsCompactionRestoreResult,
        )

    async def ask_companion(
        self,
        *,
        session_key: str,
        question: str,
    ) -> SessionsCompanionAskResult:
        payload = SessionsCompanionAskParams(
            session_key=session_key,
            question=question,
        )
        return await self._client.request(
            SessionsMethod.COMPANION_ASK,
            params=payload,
            result_model=SessionsCompanionAskResult,
        )

    async def reset_companion(
        self,
        *,
        session_key: str,
    ) -> SessionsCompanionResetResult:
        payload = SessionsCompanionResetParams(
            session_key=session_key,
        )
        return await self._client.request(
            SessionsMethod.COMPANION_RESET,
            params=payload,
            result_model=SessionsCompanionResetResult,
        )

    async def state_companion(
        self,
        *,
        session_key: str,
    ) -> SessionsCompanionStateResult:
        payload = SessionsCompanionStateParams(
            session_key=session_key,
        )
        return await self._client.request(
            SessionsMethod.COMPANION_STATE,
            params=payload,
            result_model=SessionsCompanionStateResult,
        )

    async def create(
        self,
        *,
        key: str | None = None,
        agent_id: str | None = None,
        label: str | None = None,
        model: str | None = None,
        thinking_level: str | None = None,
        incognito: bool | None = None,
        visibility: SessionVisibility | None = None,
        catalog_id: str | None = None,
        parent_session_key: str | None = None,
        spawn_depth: int | None = None,
        fork: bool | None = None,
        emit_command_hooks: bool | None = None,
        succeeds_parent: bool | None = None,
        task: str | None = None,
        message: str | None = None,
        attachments: list[dict[str, Any]] | None = None,
        worktree: bool | None = None,
        worktree_base_ref: str | None = None,
        worktree_name: str | None = None,
        exec_node: str | None = None,
        cwd: str | None = None,
    ) -> SessionsCreateResult:
        payload = SessionsCreateParams(
            key=key,
            agent_id=agent_id,
            label=label,
            model=model,
            thinking_level=thinking_level,
            incognito=incognito,
            visibility=visibility,
            catalog_id=catalog_id,
            parent_session_key=parent_session_key,
            spawn_depth=spawn_depth,
            fork=fork,
            emit_command_hooks=emit_command_hooks,
            succeeds_parent=succeeds_parent,
            task=task,
            message=message,
            attachments=attachments,
            worktree=worktree,
            worktree_base_ref=worktree_base_ref,
            worktree_name=worktree_name,
            exec_node=exec_node,
            cwd=cwd,
        )
        return await self._client.request(
            SessionsMethod.CREATE,
            params=payload,
            result_model=SessionsCreateResult,
        )

    async def delete(
        self,
        *,
        key: str,
        agent_id: str | None = None,
        delete_transcript: bool | None = None,
        expected_session_id: str | None = None,
        expected_lifecycle_revision: str | None = None,
        expected_session_updated_at: float | None = None,
        emit_lifecycle_hooks: bool | None = None,
        archived_only: bool | None = None,
    ) -> Any:
        payload = SessionsDeleteParams(
            key=key,
            agent_id=agent_id,
            delete_transcript=delete_transcript,
            expected_session_id=expected_session_id,
            expected_lifecycle_revision=expected_lifecycle_revision,
            expected_session_updated_at=expected_session_updated_at,
            emit_lifecycle_hooks=emit_lifecycle_hooks,
            archived_only=archived_only,
        )
        return await self._client.request(
            SessionsMethod.DELETE,
            params=payload,
        )

    async def describe(
        self,
        *,
        key: str,
        include_derived_titles: bool | None = None,
        include_last_message: bool | None = None,
    ) -> Any:
        payload = SessionsDescribeParams(
            key=key,
            include_derived_titles=include_derived_titles,
            include_last_message=include_last_message,
        )
        return await self._client.request(
            SessionsMethod.DESCRIBE,
            params=payload,
        )

    async def diff(
        self,
        *,
        session_key: str,
        agent_id: str | None = None,
    ) -> SessionsDiffResult:
        payload = SessionsDiffParams(
            session_key=session_key,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.DIFF,
            params=payload,
            result_model=SessionsDiffResult,
        )

    async def dispatch(
        self,
        *,
        key: str,
        profile_id: str,
        agent_id: str | None = None,
    ) -> SessionsDispatchResult:
        payload = SessionsDispatchParams(
            key=key,
            profile_id=profile_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.DISPATCH,
            params=payload,
            result_model=SessionsDispatchResult,
        )

    async def get_files(
        self,
        *,
        session_key: str,
        path: str,
        agent_id: str | None = None,
    ) -> SessionsFilesGetResult:
        payload = SessionsFilesGetParams(
            session_key=session_key,
            path=path,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.FILES_GET,
            params=payload,
            result_model=SessionsFilesGetResult,
        )

    async def list_files(
        self,
        *,
        session_key: str,
        agent_id: str | None = None,
        path: str | None = None,
        search: str | None = None,
    ) -> SessionsFilesListResult:
        payload = SessionsFilesListParams(
            session_key=session_key,
            agent_id=agent_id,
            path=path,
            search=search,
        )
        return await self._client.request(
            SessionsMethod.FILES_LIST,
            params=payload,
            result_model=SessionsFilesListResult,
        )

    async def reveal_files(
        self,
        *,
        key: str,
        agent_id: str | None = None,
    ) -> SessionsFilesRevealResult:
        payload = SessionsFilesRevealParams(
            key=key,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.FILES_REVEAL,
            params=payload,
            result_model=SessionsFilesRevealResult,
        )

    async def set_files(
        self,
        *,
        session_key: str,
        path: str,
        content: str,
        expected_hash: str,
        agent_id: str | None = None,
    ) -> SessionsFilesSetResult:
        payload = SessionsFilesSetParams(
            session_key=session_key,
            path=path,
            content=content,
            expected_hash=expected_hash,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.FILES_SET,
            params=payload,
            result_model=SessionsFilesSetResult,
        )

    async def fork(
        self,
        *,
        session_key: str,
        entry_id: str,
        agent_id: str | None = None,
    ) -> SessionsForkResult:
        payload = SessionsForkParams(
            session_key=session_key,
            entry_id=entry_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.FORK,
            params=payload,
            result_model=SessionsForkResult,
        )

    async def get(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SessionsMethod.GET,
            params=payload,
        )

    async def delete_groups(
        self,
        *,
        name: str,
    ) -> Any:
        payload = SessionsGroupsDeleteParams(
            name=name,
        )
        return await self._client.request(
            SessionsMethod.GROUPS_DELETE,
            params=payload,
        )

    async def list_groups(
        self,
    ) -> SessionsGroupsListResult:
        payload = SessionsGroupsListParams()
        return await self._client.request(
            SessionsMethod.GROUPS_LIST,
            params=payload,
            result_model=SessionsGroupsListResult,
        )

    async def put_groups(
        self,
        *,
        names: list[str],
        section_order: list[str] | None = None,
    ) -> Any:
        payload = SessionsGroupsPutParams(
            names=names,
            section_order=section_order,
        )
        return await self._client.request(
            SessionsMethod.GROUPS_PUT,
            params=payload,
        )

    async def rename_groups(
        self,
        *,
        name: str,
        to: str,
    ) -> Any:
        payload = SessionsGroupsRenameParams(
            name=name,
            to=to,
        )
        return await self._client.request(
            SessionsMethod.GROUPS_RENAME,
            params=payload,
        )

    async def subscribe_messages(
        self,
        *,
        key: str,
        agent_id: str | None = None,
        include_approvals: Literal[True] | None = None,
    ) -> Any:
        payload = SessionsMessagesSubscribeParams(
            key=key,
            agent_id=agent_id,
            include_approvals=include_approvals,
        )
        return await self._client.request(
            SessionsMethod.MESSAGES_SUBSCRIBE,
            params=payload,
        )

    async def unsubscribe_messages(
        self,
        *,
        key: str,
        agent_id: str | None = None,
    ) -> Any:
        payload = SessionsMessagesUnsubscribeParams(
            key=key,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.MESSAGES_UNSUBSCRIBE,
            params=payload,
        )

    async def visibility_observer(
        self,
        *,
        visible: bool,
    ) -> SessionsObserverVisibilityResult:
        payload = SessionsObserverVisibilityParams(
            visible=visible,
        )
        return await self._client.request(
            SessionsMethod.OBSERVER_VISIBILITY,
            params=payload,
            result_model=SessionsObserverVisibilityResult,
        )

    async def patch(
        self,
        *,
        key: str,
        agent_id: str | None = None,
        expected_session_id: str | None = None,
        expected_lifecycle_revision: str | None = None,
        label: str | None = None,
        category: str | None = None,
        board_face: SessionsListBoardFace | None = None,
        icon: str | None = None,
        status_note: str | None = None,
        attention: Literal["hand", "key", "alert", "flag", "lock", "hourglass"] | None = None,
        ttl_minutes: int | None = None,
        archived: bool | None = None,
        pinned: bool | None = None,
        unread: bool | None = None,
        thinking_level: str | None = None,
        fast_mode: bool | None | Literal["auto"] = None,
        tool_overrides: dict[str, Any] | None = None,
        verbose_level: str | None = None,
        trace_level: str | None = None,
        reasoning_level: str | None = None,
        response_usage: None | Literal["off", "tokens", "full", "on"] = None,
        elevated_level: str | None = None,
        exec_host: str | None = None,
        exec_security: str | None = None,
        exec_ask: str | None = None,
        exec_node: str | None = None,
        model: str | None = None,
        completion_owner_session_key: str | None = None,
        inherited_tool_policy_version: None | Literal[1] = None,
        inherited_tool_allow: list[str] | None = None,
        inherited_tool_deny: list[str] | None = None,
        send_policy: None | Literal["allow", "deny"] = None,
        group_activation: None | Literal["mention", "always"] = None,
    ) -> Any:
        payload = SessionsPatchParams(
            key=key,
            agent_id=agent_id,
            expected_session_id=expected_session_id,
            expected_lifecycle_revision=expected_lifecycle_revision,
            label=label,
            category=category,
            board_face=board_face,
            icon=icon,
            status_note=status_note,
            attention=attention,
            ttl_minutes=ttl_minutes,
            archived=archived,
            pinned=pinned,
            unread=unread,
            thinking_level=thinking_level,
            fast_mode=fast_mode,
            tool_overrides=tool_overrides,
            verbose_level=verbose_level,
            trace_level=trace_level,
            reasoning_level=reasoning_level,
            response_usage=response_usage,
            elevated_level=elevated_level,
            exec_host=exec_host,
            exec_security=exec_security,
            exec_ask=exec_ask,
            exec_node=exec_node,
            model=model,
            completion_owner_session_key=completion_owner_session_key,
            inherited_tool_policy_version=inherited_tool_policy_version,
            inherited_tool_allow=inherited_tool_allow,
            inherited_tool_deny=inherited_tool_deny,
            send_policy=send_policy,
            group_activation=group_activation,
        )
        return await self._client.request(
            SessionsMethod.PATCH,
            params=payload,
        )

    async def plugin_patch(
        self,
        *,
        key: str,
        plugin_id: str,
        namespace: str,
        value: Any | None = None,
        unset: bool | None = None,
    ) -> SessionsPluginPatchResult:
        payload = SessionsPluginPatchParams(
            key=key,
            plugin_id=plugin_id,
            namespace=namespace,
            value=value,
            unset=unset,
        )
        return await self._client.request(
            SessionsMethod.PLUGIN_PATCH,
            params=payload,
            result_model=SessionsPluginPatchResult,
        )

    async def preview(
        self,
        *,
        keys: list[str],
        limit: int | None = None,
        max_chars: int | None = None,
    ) -> Any:
        payload = SessionsPreviewParams(
            keys=keys,
            limit=limit,
            max_chars=max_chars,
        )
        return await self._client.request(
            SessionsMethod.PREVIEW,
            params=payload,
        )

    async def reclaim(
        self,
        *,
        key: str,
        agent_id: str | None = None,
    ) -> SessionsReclaimResult:
        payload = SessionsReclaimParams(
            key=key,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.RECLAIM,
            params=payload,
            result_model=SessionsReclaimResult,
        )

    async def reset(
        self,
        *,
        key: str,
        agent_id: str | None = None,
        reason: SessionsResetReason | None = None,
    ) -> Any:
        payload = SessionsResetParams(
            key=key,
            agent_id=agent_id,
            reason=reason,
        )
        return await self._client.request(
            SessionsMethod.RESET,
            params=payload,
        )

    async def resolve(
        self,
        *,
        key: str | None = None,
        session_id: str | None = None,
        label: str | None = None,
        agent_id: str | None = None,
        spawned_by: str | None = None,
        include_global: bool | None = None,
        include_unknown: bool | None = None,
        allow_missing: bool | None = None,
    ) -> Any:
        payload = SessionsResolveParams(
            key=key,
            session_id=session_id,
            label=label,
            agent_id=agent_id,
            spawned_by=spawned_by,
            include_global=include_global,
            include_unknown=include_unknown,
            allow_missing=allow_missing,
        )
        return await self._client.request(
            SessionsMethod.RESOLVE,
            params=payload,
        )

    async def rewind(
        self,
        *,
        session_key: str,
        entry_id: str,
        agent_id: str | None = None,
    ) -> SessionsRewindResult:
        payload = SessionsRewindParams(
            session_key=session_key,
            entry_id=entry_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SessionsMethod.REWIND,
            params=payload,
            result_model=SessionsRewindResult,
        )

    async def search(
        self,
        *,
        query: str,
        agent_id: str | None = None,
        session_keys: list[str] | None = None,
        limit: int | None = None,
    ) -> SessionsSearchResult:
        payload = SessionsSearchParams(
            query=query,
            agent_id=agent_id,
            session_keys=session_keys,
            limit=limit,
        )
        return await self._client.request(
            SessionsMethod.SEARCH,
            params=payload,
            result_model=SessionsSearchResult,
        )

    async def send(
        self,
        *,
        key: str,
        message: str,
        agent_id: str | None = None,
        thinking: str | None = None,
        attachments: list[dict[str, Any]] | None = None,
        timeout_ms: int | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        payload = SessionsSendParams(
            key=key,
            message=message,
            agent_id=agent_id,
            thinking=thinking,
            attachments=attachments,
            timeout_ms=timeout_ms,
            idempotency_key=idempotency_key,
        )
        return await self._client.request(
            SessionsMethod.SEND,
            params=payload,
        )

    async def steer(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SessionsMethod.STEER,
            params=payload,
        )

    async def subscribe(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SessionsMethod.SUBSCRIBE,
            params=payload,
        )

    async def unsubscribe(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SessionsMethod.UNSUBSCRIBE,
            params=payload,
        )

    async def usage(
        self,
        *,
        key: str | None = None,
        agent_id: str | None = None,
        agent_scope: Literal["all"] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        mode: SessionsUsageMode | None = None,
        range: SessionsUsageRange | None = None,
        group_by: SessionsUsageGroupBy | None = None,
        include_historical: bool | None = None,
        utc_offset: str | None = None,
        time_zone: str | None = None,
        limit: int | None = None,
        include_context_weight: bool | None = None,
    ) -> Any:
        payload = SessionsUsageParams(
            key=key,
            agent_id=agent_id,
            agent_scope=agent_scope,
            start_date=start_date,
            end_date=end_date,
            mode=mode,
            range=range,
            group_by=group_by,
            include_historical=include_historical,
            utc_offset=utc_offset,
            time_zone=time_zone,
            limit=limit,
            include_context_weight=include_context_weight,
        )
        return await self._client.request(
            SessionsMethod.USAGE,
            params=payload,
        )

    async def logs_usage(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SessionsMethod.USAGE_LOGS,
            params=payload,
        )

    async def timeseries_usage(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SessionsMethod.USAGE_TIMESERIES,
            params=payload,
        )

    async def set_viewers(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SessionsMethod.VIEWERS_SET,
            params=payload,
        )

    async def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        active_minutes: int | None = None,
        require_last_interaction: bool | None = None,
        sort_by: SessionsListSortBy | None = None,
        include_global: bool | None = None,
        include_unknown: bool | None = None,
        configured_agents_only: bool | None = None,
        include_derived_titles: bool | None = None,
        include_last_message: bool | None = None,
        label: str | None = None,
        board_face: SessionsListBoardFace | None = None,
        creator_id: str | None = None,
        spawned_by: str | None = None,
        agent_id: str | None = None,
        search: str | None = None,
        archived: bool | Literal["all"] | None = None,
    ) -> Any:
        payload = SessionsListParams(
            limit=limit,
            offset=offset,
            active_minutes=active_minutes,
            require_last_interaction=require_last_interaction,
            sort_by=sort_by,
            include_global=include_global,
            include_unknown=include_unknown,
            configured_agents_only=configured_agents_only,
            include_derived_titles=include_derived_titles,
            include_last_message=include_last_message,
            label=label,
            board_face=board_face,
            creator_id=creator_id,
            spawned_by=spawned_by,
            agent_id=agent_id,
            search=search,
            archived=archived,
        )
        return await self._client.request(
            SessionsMethod.LIST,
            params=payload,
        )
