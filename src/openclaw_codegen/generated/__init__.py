"""Generated OpenClaw protocol surface. Do not edit manually."""

from .clients._accessors import OpenClawClients
from .events import EVENT_PAYLOAD_TYPES, parse_event_payload
from .version import SCHEMA_PACKAGE_VERSION

__all__ = ["OpenClawClients", "SCHEMA_PACKAGE_VERSION", "EVENT_PAYLOAD_TYPES", "parse_event_payload"]
