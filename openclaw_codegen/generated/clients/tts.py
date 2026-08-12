"""Generated tts RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    TtsSpeakParams,
    TtsSpeakResult,
)


class TtsMethod(StrEnum):
    CONVERT = "tts.convert"
    DISABLE = "tts.disable"
    ENABLE = "tts.enable"
    PERSONAS = "tts.personas"
    PROVIDERS = "tts.providers"
    SET_PERSONA = "tts.setPersona"
    SET_PROVIDER = "tts.setProvider"
    SPEAK = "tts.speak"
    STATUS = "tts.status"


class TtsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def convert(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TtsMethod.CONVERT,
            params=payload,
        )

    async def disable(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TtsMethod.DISABLE,
            params=payload,
        )

    async def enable(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TtsMethod.ENABLE,
            params=payload,
        )

    async def personas(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TtsMethod.PERSONAS,
            params=payload,
        )

    async def providers(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TtsMethod.PROVIDERS,
            params=payload,
        )

    async def set_persona(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TtsMethod.SET_PERSONA,
            params=payload,
        )

    async def set_provider(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TtsMethod.SET_PROVIDER,
            params=payload,
        )

    async def speak(
        self,
        *,
        text: str,
    ) -> TtsSpeakResult:
        payload = TtsSpeakParams(
            text=text,
        )
        return await self._client.request(
            TtsMethod.SPEAK,
            params=payload,
            result_model=TtsSpeakResult,
        )

    async def status(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            TtsMethod.STATUS,
            params=payload,
        )
