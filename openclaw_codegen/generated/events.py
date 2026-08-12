"""Generated event payload registry. Do not edit manually."""

from typing import Any

from pydantic import TypeAdapter

from openclaw_codegen.generated import protocol

EVENT_PAYLOAD_TYPES: dict[str, Any] = {
    "chat": protocol.ChatEvent,
}
_EVENT_ADAPTERS = {event: TypeAdapter(payload_type) for event, payload_type in EVENT_PAYLOAD_TYPES.items()}


def parse_event_payload(event: str, payload: Any) -> Any:
    adapter = _EVENT_ADAPTERS.get(event)
    return payload if adapter is None else adapter.validate_python(payload)


__all__ = ["EVENT_PAYLOAD_TYPES", "parse_event_payload"]
