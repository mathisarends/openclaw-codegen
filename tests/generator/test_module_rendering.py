from generator.module_rendering import (
    render_client_accessors,
    render_clients_init,
    render_events,
    render_requester,
    render_root_init,
    render_version,
)


def test_root_module_exposes_generated_client_accessors_and_events() -> None:
    rendered = render_root_init(has_event_registry=True)
    assert "from .clients._accessors import OpenClawClients" in rendered
    assert "from .version import SCHEMA_PACKAGE_VERSION" in rendered
    assert "from .events import EVENT_PAYLOAD_TYPES, parse_event_payload" in rendered


def test_root_module_omits_event_registry_when_no_domain_owns_it() -> None:
    rendered = render_root_init(has_event_registry=False)
    assert "from .events import" not in rendered
    assert '__all__ = ["OpenClawClients", "SCHEMA_PACKAGE_VERSION"]' in rendered


def test_render_version_pins_the_resolved_schema_package() -> None:
    rendered = render_version("2026.7.2-beta.7")
    assert "SCHEMA_PACKAGE_VERSION = '2026.7.2-beta.7'" in rendered


def test_render_events_builds_sorted_payload_registry_and_parser() -> None:
    rendered = render_events("chat", {"chat.final": "ChatFinalEvent", "chat.delta": "ChatDeltaEvent"})
    assert rendered.index("'chat.delta': protocol.ChatDeltaEvent,") < rendered.index(
        "'chat.final': protocol.ChatFinalEvent,"
    )
    assert "from openclaw_codegen.generated import protocol" in rendered
    assert "def parse_event_payload(event: str, payload: Any) -> Any:" in rendered
    assert '__all__ = ["EVENT_PAYLOAD_TYPES", "parse_event_payload"]' in rendered


def test_client_accessors_use_client_names_and_flat_modules() -> None:
    rendered = render_client_accessors(["chat", "sessions", "agents"])
    assert "from openclaw_codegen.generated.clients import (" in rendered
    assert "    AgentsClient," in rendered
    assert "class OpenClawClients:" in rendered
    assert "from openclaw_codegen.generated.clients._requester import Requester" in rendered
    assert "def _requester(self) -> Requester:" in rendered
    assert "def chat(self) -> ChatClient:" in rendered
    assert "return ChatClient(self._requester)" in rendered
    assert rendered.count("cast(") == 1


def test_requester_protocol_is_rendered_once_as_shared_infrastructure() -> None:
    rendered = render_requester()
    assert "class Requester(Protocol):" in rendered
    assert "async def request(" in rendered


def test_clients_package_reexports_all_concrete_clients() -> None:
    rendered = render_clients_init(["chat", "sessions", "agents"])
    assert "from .chat import ChatClient" in rendered
    assert "from .sessions import SessionsClient" in rendered
    assert '    "AgentsClient",' in rendered
