"""Generated requester protocol. Do not edit manually."""

from collections.abc import Mapping
from typing import Any, Protocol

from pydantic import BaseModel


class Requester(Protocol):
    async def request(
        self,
        method: str,
        params: BaseModel | Mapping[str, Any] | None = None,
        *,
        result_model: type[BaseModel] | None = None,
        timeout: float | None = None,
    ) -> Any: ...
