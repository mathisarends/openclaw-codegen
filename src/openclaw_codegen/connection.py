import platform
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

PROTOCOL_VERSION = 4


class OperatorScope(StrEnum):
    READ = "operator.read"
    WRITE = "operator.write"


class _ConnectionModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, extra="forbid", populate_by_name=True)


class GatewayClientInfo(_ConnectionModel):
    """Client identity supplied inside the schema-generated connect request."""

    id: Literal["gateway-client"] = "gateway-client"
    display_name: str | None = None
    version: str = "0.1.0"
    platform: str = Field(default_factory=platform.system)
    mode: Literal["backend"] = "backend"
    instance_id: str | None = None


class GatewayAuth(_ConnectionModel):
    """Supported trusted-backend authentication fields."""

    token: str | None = None
    password: str | None = None
    device_token: str | None = None


class ConnectChallenge(_ConnectionModel):
    nonce: str = Field(min_length=1)
    ts: int = Field(ge=0)


__all__ = [
    "PROTOCOL_VERSION",
    "ConnectChallenge",
    "GatewayAuth",
    "GatewayClientInfo",
    "OperatorScope",
]
