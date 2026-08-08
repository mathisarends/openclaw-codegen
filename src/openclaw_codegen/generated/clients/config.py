"""Generated config RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    ConfigApplyParams,
    ConfigGetParams,
    ConfigPatchParams,
    ConfigSchemaLookupParams,
    ConfigSchemaLookupResult,
    ConfigSchemaParams,
    ConfigSetParams,
)


class ConfigMethod(StrEnum):
    APPLY = "config.apply"
    GET = "config.get"
    OPEN_FILE = "config.openFile"
    PATCH = "config.patch"
    SCHEMA = "config.schema"
    SCHEMA_LOOKUP = "config.schema.lookup"
    SET = "config.set"


class ConfigClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def apply(
        self,
        *,
        raw: str,
        base_hash: str | None = None,
        session_key: str | None = None,
        delivery_context: dict[str, Any] | None = None,
        note: str | None = None,
        restart_delay_ms: int | None = None,
    ) -> Any:
        payload = ConfigApplyParams(
            raw=raw,
            base_hash=base_hash,
            session_key=session_key,
            delivery_context=delivery_context,
            note=note,
            restart_delay_ms=restart_delay_ms,
        )
        return await self._client.request(
            ConfigMethod.APPLY,
            params=payload,
        )

    async def get(
        self,
    ) -> Any:
        payload = ConfigGetParams()
        return await self._client.request(
            ConfigMethod.GET,
            params=payload,
        )

    async def open_file(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            ConfigMethod.OPEN_FILE,
            params=payload,
        )

    async def patch(
        self,
        *,
        raw: str,
        base_hash: str | None = None,
        session_key: str | None = None,
        delivery_context: dict[str, Any] | None = None,
        note: str | None = None,
        restart_delay_ms: int | None = None,
        replace_paths: list[str] | None = None,
    ) -> Any:
        payload = ConfigPatchParams(
            raw=raw,
            base_hash=base_hash,
            session_key=session_key,
            delivery_context=delivery_context,
            note=note,
            restart_delay_ms=restart_delay_ms,
            replace_paths=replace_paths,
        )
        return await self._client.request(
            ConfigMethod.PATCH,
            params=payload,
        )

    async def schema(
        self,
    ) -> Any:
        payload = ConfigSchemaParams()
        return await self._client.request(
            ConfigMethod.SCHEMA,
            params=payload,
        )

    async def lookup_schema(
        self,
        *,
        path: str,
    ) -> ConfigSchemaLookupResult:
        payload = ConfigSchemaLookupParams(
            path=path,
        )
        return await self._client.request(
            ConfigMethod.SCHEMA_LOOKUP,
            params=payload,
            result_model=ConfigSchemaLookupResult,
        )

    async def set(
        self,
        *,
        raw: str,
        base_hash: str | None = None,
    ) -> Any:
        payload = ConfigSetParams(
            raw=raw,
            base_hash=base_hash,
        )
        return await self._client.request(
            ConfigMethod.SET,
            params=payload,
        )
