from .client import OpenClawClient
from .connection import PROTOCOL_VERSION, GatewayAuth, GatewayClientInfo, OperatorScope
from .exceptions import (
    OpenClawClientError,
    OpenClawCompatibilityWarning,
    OpenClawGatewayError,
    OpenClawNotConnectedError,
    OpenClawProtocolError,
)
from .generated.events import parse_event_payload
from .generated.protocol import (
    ChatAbortedEvent,
    ChatDeltaEvent,
    ChatErrorEvent,
    ChatEvent,
    ChatFinalEvent,
    ChatSendAck,
    ChatSendParams,
    ChatStatusEvent,
    ConnectParams,
    EventFrame,
    HelloOk,
)
from .generated.version import SCHEMA_PACKAGE_VERSION

__all__ = [
    "PROTOCOL_VERSION",
    "SCHEMA_PACKAGE_VERSION",
    "ChatAbortedEvent",
    "ChatDeltaEvent",
    "ChatErrorEvent",
    "ChatEvent",
    "ChatFinalEvent",
    "ChatSendAck",
    "ChatSendParams",
    "ChatStatusEvent",
    "ConnectParams",
    "GatewayAuth",
    "GatewayClientInfo",
    "EventFrame",
    "HelloOk",
    "OpenClawClient",
    "OpenClawClientError",
    "OpenClawCompatibilityWarning",
    "OpenClawGatewayError",
    "OpenClawNotConnectedError",
    "OpenClawProtocolError",
    "OperatorScope",
    "parse_event_payload",
]
