"""Generated secrets RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    SecretsReloadParams,
    SecretsResolveParams,
    SecretsResolveResult,
)


class SecretsMethod(StrEnum):
    RELOAD = "secrets.reload"
    RESOLVE = "secrets.resolve"


class SecretsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def reload(
        self,
    ) -> Any:
        payload = SecretsReloadParams()
        return await self._client.request(
            SecretsMethod.RELOAD,
            params=payload,
        )

    async def resolve(
        self,
        *,
        command_name: str,
        target_ids: list[str],
        allowed_paths: list[str] | None = None,
        forced_active_paths: list[str] | None = None,
        optional_active_paths: list[str] | None = None,
        provider_overrides: dict[str, Any] | None = None,
    ) -> SecretsResolveResult:
        payload = SecretsResolveParams(
            command_name=command_name,
            target_ids=target_ids,
            allowed_paths=allowed_paths,
            forced_active_paths=forced_active_paths,
            optional_active_paths=optional_active_paths,
            provider_overrides=provider_overrides,
        )
        return await self._client.request(
            SecretsMethod.RESOLVE,
            params=payload,
            result_model=SecretsResolveResult,
        )
