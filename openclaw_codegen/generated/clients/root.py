"""Generated root RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    AgentBootstrapContextMode,
    AgentBootstrapContextRunKind,
    AgentParams,
    AgentPromptMode,
    AgentSessionEffects,
    AgentSourceReplyDeliveryMode,
    ConnectParams,
    PollParams,
    SendParams,
    WakeMode,
    WakeParams,
)


class RootMethod(StrEnum):
    AGENT = "agent"
    CONNECT = "connect"
    HEALTH = "health"
    LAST_HEARTBEAT = "last-heartbeat"
    POLL = "poll"
    SEND = "send"
    SET_HEARTBEATS = "set-heartbeats"
    STATUS = "status"
    SYSTEM_EVENT = "system-event"
    SYSTEM_PRESENCE = "system-presence"
    WAKE = "wake"


class RootClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def agent(
        self,
        *,
        message: str,
        idempotency_key: str,
        agent_id: str | None = None,
        provider: str | None = None,
        model: str | None = None,
        to: str | None = None,
        reply_to: str | None = None,
        session_id: str | None = None,
        session_key: str | None = None,
        expected_existing_session_id: str | None = None,
        thinking: str | None = None,
        deliver: bool | None = None,
        attachments: list[Any] | None = None,
        channel: str | None = None,
        reply_channel: str | None = None,
        account_id: str | None = None,
        reply_account_id: str | None = None,
        thread_id: str | None = None,
        group_id: str | None = None,
        group_channel: str | None = None,
        group_space: str | None = None,
        timeout: int | None = None,
        best_effort_deliver: bool | None = None,
        lane: str | None = None,
        cwd: str | None = None,
        cleanup_bundle_mcp_on_run_end: bool | None = None,
        model_run: bool | None = None,
        prompt_mode: AgentPromptMode | None = None,
        extra_system_prompt: str | None = None,
        bootstrap_context_mode: AgentBootstrapContextMode | None = None,
        bootstrap_context_run_kind: AgentBootstrapContextRunKind | None = None,
        acp_turn_source: Literal["manual_spawn"] | None = None,
        internal_runtime_handoff_id: str | None = None,
        exec_approval_followup_expected_session_id: str | None = None,
        internal_events: list[dict[str, Any]] | None = None,
        input_provenance: dict[str, Any] | None = None,
        suppress_prompt_persistence: bool | None = None,
        session_effects: AgentSessionEffects | None = None,
        source_reply_delivery_mode: AgentSourceReplyDeliveryMode | None = None,
        disable_message_tool: bool | None = None,
        swarm_collector: bool | None = None,
        swarm_output_schema: dict[str, Any] | None = None,
        force_restart_safe_tools: bool | None = None,
        force_code_mode_tools: bool | None = None,
        voice_wake_trigger: str | None = None,
        label: str | None = None,
    ) -> Any:
        payload = AgentParams(
            message=message,
            idempotency_key=idempotency_key,
            agent_id=agent_id,
            provider=provider,
            model=model,
            to=to,
            reply_to=reply_to,
            session_id=session_id,
            session_key=session_key,
            expected_existing_session_id=expected_existing_session_id,
            thinking=thinking,
            deliver=deliver,
            attachments=attachments,
            channel=channel,
            reply_channel=reply_channel,
            account_id=account_id,
            reply_account_id=reply_account_id,
            thread_id=thread_id,
            group_id=group_id,
            group_channel=group_channel,
            group_space=group_space,
            timeout=timeout,
            best_effort_deliver=best_effort_deliver,
            lane=lane,
            cwd=cwd,
            cleanup_bundle_mcp_on_run_end=cleanup_bundle_mcp_on_run_end,
            model_run=model_run,
            prompt_mode=prompt_mode,
            extra_system_prompt=extra_system_prompt,
            bootstrap_context_mode=bootstrap_context_mode,
            bootstrap_context_run_kind=bootstrap_context_run_kind,
            acp_turn_source=acp_turn_source,
            internal_runtime_handoff_id=internal_runtime_handoff_id,
            exec_approval_followup_expected_session_id=exec_approval_followup_expected_session_id,
            internal_events=internal_events,
            input_provenance=input_provenance,
            suppress_prompt_persistence=suppress_prompt_persistence,
            session_effects=session_effects,
            source_reply_delivery_mode=source_reply_delivery_mode,
            disable_message_tool=disable_message_tool,
            swarm_collector=swarm_collector,
            swarm_output_schema=swarm_output_schema,
            force_restart_safe_tools=force_restart_safe_tools,
            force_code_mode_tools=force_code_mode_tools,
            voice_wake_trigger=voice_wake_trigger,
            label=label,
        )
        return await self._client.request(
            RootMethod.AGENT,
            params=payload,
        )

    async def connect(
        self,
        *,
        min_protocol: int,
        max_protocol: int,
        client: dict[str, Any],
        caps: list[str] | None = None,
        commands: list[str] | None = None,
        permissions: dict[str, Any] | None = None,
        path_env: str | None = None,
        role: str | None = None,
        scopes: list[str] | None = None,
        device: dict[str, Any] | None = None,
        auth: dict[str, Any] | None = None,
        locale: str | None = None,
        user_agent: str | None = None,
    ) -> Any:
        payload = ConnectParams(
            min_protocol=min_protocol,
            max_protocol=max_protocol,
            client=client,
            caps=caps,
            commands=commands,
            permissions=permissions,
            path_env=path_env,
            role=role,
            scopes=scopes,
            device=device,
            auth=auth,
            locale=locale,
            user_agent=user_agent,
        )
        return await self._client.request(
            RootMethod.CONNECT,
            params=payload,
        )

    async def health(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            RootMethod.HEALTH,
            params=payload,
        )

    async def last_heartbeat(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            RootMethod.LAST_HEARTBEAT,
            params=payload,
        )

    async def poll(
        self,
        *,
        to: str,
        question: str,
        options: list[str],
        idempotency_key: str,
        max_selections: int | None = None,
        duration_seconds: int | None = None,
        duration_hours: int | None = None,
        silent: bool | None = None,
        is_anonymous: bool | None = None,
        thread_id: str | None = None,
        channel: str | None = None,
        account_id: str | None = None,
    ) -> Any:
        payload = PollParams(
            to=to,
            question=question,
            options=options,
            idempotency_key=idempotency_key,
            max_selections=max_selections,
            duration_seconds=duration_seconds,
            duration_hours=duration_hours,
            silent=silent,
            is_anonymous=is_anonymous,
            thread_id=thread_id,
            channel=channel,
            account_id=account_id,
        )
        return await self._client.request(
            RootMethod.POLL,
            params=payload,
        )

    async def send(
        self,
        *,
        to: str,
        idempotency_key: str,
        message: str | None = None,
        media_url: str | None = None,
        media_urls: list[str] | None = None,
        buffer: str | None = None,
        filename: str | None = None,
        content_type: str | None = None,
        as_voice: bool | None = None,
        gif_playback: bool | None = None,
        channel: str | None = None,
        account_id: str | None = None,
        agent_id: str | None = None,
        reply_to_id: str | None = None,
        thread_id: str | None = None,
        force_document: bool | None = None,
        silent: bool | None = None,
        parse_mode: Literal["HTML"] | None = None,
        session_key: str | None = None,
    ) -> Any:
        payload = SendParams(
            to=to,
            idempotency_key=idempotency_key,
            message=message,
            media_url=media_url,
            media_urls=media_urls,
            buffer=buffer,
            filename=filename,
            content_type=content_type,
            as_voice=as_voice,
            gif_playback=gif_playback,
            channel=channel,
            account_id=account_id,
            agent_id=agent_id,
            reply_to_id=reply_to_id,
            thread_id=thread_id,
            force_document=force_document,
            silent=silent,
            parse_mode=parse_mode,
            session_key=session_key,
        )
        return await self._client.request(
            RootMethod.SEND,
            params=payload,
        )

    async def set_heartbeats(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            RootMethod.SET_HEARTBEATS,
            params=payload,
        )

    async def status(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            RootMethod.STATUS,
            params=payload,
        )

    async def system_event(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            RootMethod.SYSTEM_EVENT,
            params=payload,
        )

    async def system_presence(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            RootMethod.SYSTEM_PRESENCE,
            params=payload,
        )

    async def wake(
        self,
        *,
        mode: WakeMode,
        text: str,
        session_key: str | None = None,
        agent_id: str | None = None,
    ) -> Any:
        payload = WakeParams(
            mode=mode,
            text=text,
            session_key=session_key,
            agent_id=agent_id,
        )
        return await self._client.request(
            RootMethod.WAKE,
            params=payload,
        )
