"""Generated talk RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    SessionsSearchHitRole,
    TalkCatalogParams,
    TalkCatalogResult,
    TalkClientCloseParams,
    TalkClientCreateParams,
    TalkClientCreateResult,
    TalkClientSteerMode,
    TalkClientSteerParams,
    TalkClientToolCallParams,
    TalkClientToolCallResult,
    TalkClientTranscriptParams,
    TalkConfigParams,
    TalkConfigResult,
    TalkEventBrain,
    TalkEventMode,
    TalkEventTransport,
    TalkModeParams,
    TalkSessionAcknowledgeMarkParams,
    TalkSessionAppendAudioParams,
    TalkSessionCancelOutputParams,
    TalkSessionCancelTurnParams,
    TalkSessionCloseParams,
    TalkSessionCreateParams,
    TalkSessionCreateResult,
    TalkSessionJoinParams,
    TalkSessionJoinResult,
    TalkSessionSteerParams,
    TalkSessionSubmitToolResultParams,
    TalkSpeakParams,
    TalkSpeakResult,
)


class TalkMethod(StrEnum):
    CATALOG = "talk.catalog"
    CLIENT_CLOSE = "talk.client.close"
    CLIENT_CREATE = "talk.client.create"
    CLIENT_STEER = "talk.client.steer"
    CLIENT_TOOL_CALL = "talk.client.toolCall"
    CLIENT_TRANSCRIPT = "talk.client.transcript"
    CONFIG = "talk.config"
    MODE = "talk.mode"
    SESSION_ACKNOWLEDGE_MARK = "talk.session.acknowledgeMark"
    SESSION_APPEND_AUDIO = "talk.session.appendAudio"
    SESSION_CANCEL_OUTPUT = "talk.session.cancelOutput"
    SESSION_CANCEL_TURN = "talk.session.cancelTurn"
    SESSION_CLOSE = "talk.session.close"
    SESSION_CREATE = "talk.session.create"
    SESSION_END_TURN = "talk.session.endTurn"
    SESSION_JOIN = "talk.session.join"
    SESSION_START_TURN = "talk.session.startTurn"
    SESSION_STEER = "talk.session.steer"
    SESSION_SUBMIT_TOOL_RESULT = "talk.session.submitToolResult"
    SPEAK = "talk.speak"


class TalkClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def catalog(
        self,
    ) -> TalkCatalogResult:
        payload = TalkCatalogParams()
        return await self._client.request(
            TalkMethod.CATALOG,
            params=payload,
            result_model=TalkCatalogResult,
        )

    async def close_client(
        self,
        *,
        session_key: str,
        voice_session_id: str,
    ) -> Any:
        payload = TalkClientCloseParams(
            session_key=session_key,
            voice_session_id=voice_session_id,
        )
        return await self._client.request(
            TalkMethod.CLIENT_CLOSE,
            params=payload,
        )

    async def create_client(
        self,
        *,
        session_key: str | None = None,
        voice_session_id: str | None = None,
        provider: str | None = None,
        model: str | None = None,
        voice: str | None = None,
        vad_threshold: float | None = None,
        silence_duration_ms: int | None = None,
        prefix_padding_ms: int | None = None,
        reasoning_effort: str | None = None,
        mode: TalkEventMode | None = None,
        transport: TalkEventTransport | None = None,
        brain: TalkEventBrain | None = None,
        capabilities: list[Literal["camera-frame", "voice-transcript"]] | None = None,
    ) -> TalkClientCreateResult:
        payload = TalkClientCreateParams(
            session_key=session_key,
            voice_session_id=voice_session_id,
            provider=provider,
            model=model,
            voice=voice,
            vad_threshold=vad_threshold,
            silence_duration_ms=silence_duration_ms,
            prefix_padding_ms=prefix_padding_ms,
            reasoning_effort=reasoning_effort,
            mode=mode,
            transport=transport,
            brain=brain,
            capabilities=capabilities,
        )
        return await self._client.request(
            TalkMethod.CLIENT_CREATE,
            params=payload,
            result_model=TalkClientCreateResult,
        )

    async def steer_client(
        self,
        *,
        session_key: str,
        text: str,
        mode: TalkClientSteerMode | None = None,
    ) -> Any:
        payload = TalkClientSteerParams(
            session_key=session_key,
            text=text,
            mode=mode,
        )
        return await self._client.request(
            TalkMethod.CLIENT_STEER,
            params=payload,
        )

    async def tool_call_client(
        self,
        *,
        session_key: str,
        call_id: str,
        name: str,
        voice_session_id: str | None = None,
        args: Any | None = None,
        relay_session_id: str | None = None,
    ) -> TalkClientToolCallResult:
        payload = TalkClientToolCallParams(
            session_key=session_key,
            call_id=call_id,
            name=name,
            voice_session_id=voice_session_id,
            args=args,
            relay_session_id=relay_session_id,
        )
        return await self._client.request(
            TalkMethod.CLIENT_TOOL_CALL,
            params=payload,
            result_model=TalkClientToolCallResult,
        )

    async def transcript_client(
        self,
        *,
        session_key: str,
        voice_session_id: str,
        entry_id: str,
        role: SessionsSearchHitRole,
        text: str,
        timestamp: float | None = None,
    ) -> Any:
        payload = TalkClientTranscriptParams(
            session_key=session_key,
            voice_session_id=voice_session_id,
            entry_id=entry_id,
            role=role,
            text=text,
            timestamp=timestamp,
        )
        return await self._client.request(
            TalkMethod.CLIENT_TRANSCRIPT,
            params=payload,
        )

    async def config(
        self,
        *,
        include_secrets: bool | None = None,
    ) -> TalkConfigResult:
        payload = TalkConfigParams(
            include_secrets=include_secrets,
        )
        return await self._client.request(
            TalkMethod.CONFIG,
            params=payload,
            result_model=TalkConfigResult,
        )

    async def mode(
        self,
        *,
        enabled: bool,
        phase: str | None = None,
    ) -> Any:
        payload = TalkModeParams(
            enabled=enabled,
            phase=phase,
        )
        return await self._client.request(
            TalkMethod.MODE,
            params=payload,
        )

    async def acknowledge_mark_session(
        self,
        *,
        session_id: str,
        mark_name: str,
    ) -> Any:
        payload = TalkSessionAcknowledgeMarkParams(
            session_id=session_id,
            mark_name=mark_name,
        )
        return await self._client.request(
            TalkMethod.SESSION_ACKNOWLEDGE_MARK,
            params=payload,
        )

    async def append_audio_session(
        self,
        *,
        session_id: str,
        audio_base64: str,
        timestamp: float | None = None,
    ) -> Any:
        payload = TalkSessionAppendAudioParams(
            session_id=session_id,
            audio_base64=audio_base64,
            timestamp=timestamp,
        )
        return await self._client.request(
            TalkMethod.SESSION_APPEND_AUDIO,
            params=payload,
        )

    async def cancel_output_session(
        self,
        *,
        session_id: str,
        turn_id: str | None = None,
        reason: str | None = None,
    ) -> Any:
        payload = TalkSessionCancelOutputParams(
            session_id=session_id,
            turn_id=turn_id,
            reason=reason,
        )
        return await self._client.request(
            TalkMethod.SESSION_CANCEL_OUTPUT,
            params=payload,
        )

    async def cancel_turn_session(
        self,
        *,
        session_id: str,
        turn_id: str | None = None,
        reason: str | None = None,
    ) -> Any:
        payload = TalkSessionCancelTurnParams(
            session_id=session_id,
            turn_id=turn_id,
            reason=reason,
        )
        return await self._client.request(
            TalkMethod.SESSION_CANCEL_TURN,
            params=payload,
        )

    async def close_session(
        self,
        *,
        session_id: str,
    ) -> Any:
        payload = TalkSessionCloseParams(
            session_id=session_id,
        )
        return await self._client.request(
            TalkMethod.SESSION_CLOSE,
            params=payload,
        )

    async def create_session(
        self,
        *,
        session_key: str | None = None,
        spawned_by: str | None = None,
        provider: str | None = None,
        model: str | None = None,
        voice: str | None = None,
        language: str | None = None,
        vad_threshold: float | None = None,
        silence_duration_ms: int | None = None,
        prefix_padding_ms: int | None = None,
        reasoning_effort: str | None = None,
        mode: TalkEventMode | None = None,
        transport: TalkEventTransport | None = None,
        brain: TalkEventBrain | None = None,
        ttl_ms: int | None = None,
    ) -> TalkSessionCreateResult:
        payload = TalkSessionCreateParams(
            session_key=session_key,
            spawned_by=spawned_by,
            provider=provider,
            model=model,
            voice=voice,
            language=language,
            vad_threshold=vad_threshold,
            silence_duration_ms=silence_duration_ms,
            prefix_padding_ms=prefix_padding_ms,
            reasoning_effort=reasoning_effort,
            mode=mode,
            transport=transport,
            brain=brain,
            ttl_ms=ttl_ms,
        )
        return await self._client.request(
            TalkMethod.SESSION_CREATE,
            params=payload,
            result_model=TalkSessionCreateResult,
        )

    async def end_turn_session(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TalkMethod.SESSION_END_TURN,
            params=payload,
        )

    async def join_session(
        self,
        *,
        session_id: str,
        token: str,
    ) -> TalkSessionJoinResult:
        payload = TalkSessionJoinParams(
            session_id=session_id,
            token=token,
        )
        return await self._client.request(
            TalkMethod.SESSION_JOIN,
            params=payload,
            result_model=TalkSessionJoinResult,
        )

    async def start_turn_session(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TalkMethod.SESSION_START_TURN,
            params=payload,
        )

    async def steer_session(
        self,
        *,
        session_id: str,
        text: str,
        session_key: str | None = None,
        mode: TalkClientSteerMode | None = None,
    ) -> Any:
        payload = TalkSessionSteerParams(
            session_id=session_id,
            text=text,
            session_key=session_key,
            mode=mode,
        )
        return await self._client.request(
            TalkMethod.SESSION_STEER,
            params=payload,
        )

    async def submit_tool_result_session(
        self,
        *,
        session_id: str,
        call_id: str,
        result: Any,
        options: dict[str, Any] | None = None,
    ) -> Any:
        payload = TalkSessionSubmitToolResultParams(
            session_id=session_id,
            call_id=call_id,
            result=result,
            options=options,
        )
        return await self._client.request(
            TalkMethod.SESSION_SUBMIT_TOOL_RESULT,
            params=payload,
        )

    async def speak(
        self,
        *,
        text: str,
        voice_id: str | None = None,
        model_id: str | None = None,
        output_format: str | None = None,
        speed: float | None = None,
        rate_wpm: int | None = None,
        stability: float | None = None,
        similarity: float | None = None,
        style: float | None = None,
        speaker_boost: bool | None = None,
        seed: int | None = None,
        normalize: str | None = None,
        language: str | None = None,
        latency_tier: int | None = None,
    ) -> TalkSpeakResult:
        payload = TalkSpeakParams(
            text=text,
            voice_id=voice_id,
            model_id=model_id,
            output_format=output_format,
            speed=speed,
            rate_wpm=rate_wpm,
            stability=stability,
            similarity=similarity,
            style=style,
            speaker_boost=speaker_boost,
            seed=seed,
            normalize=normalize,
            language=language,
            latency_tier=latency_tier,
        )
        return await self._client.request(
            TalkMethod.SPEAK,
            params=payload,
            result_model=TalkSpeakResult,
        )
