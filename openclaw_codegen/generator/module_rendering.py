from openclaw_codegen.generator.naming import client_class_name


def render_events(event_overrides: dict[str, str]) -> str:
    lines = [
        '"""Generated event payload registry. Do not edit manually."""',
        "from typing import Any",
        "",
        "from pydantic import TypeAdapter",
        "",
        "from openclaw_codegen.generated import protocol",
        "",
        "EVENT_PAYLOAD_TYPES: dict[str, Any] = {",
    ]
    lines.extend(f"    {event!r}: protocol.{model}," for event, model in sorted(event_overrides.items()))
    lines.extend(
        [
            "}",
            "_EVENT_ADAPTERS = {",
            "    event: TypeAdapter(payload_type) for event, payload_type in EVENT_PAYLOAD_TYPES.items()",
            "}",
            "",
            "",
            "def parse_event_payload(event: str, payload: Any) -> Any:",
            "    adapter = _EVENT_ADAPTERS.get(event)",
            "    return payload if adapter is None else adapter.validate_python(payload)",
            "",
            "",
            '__all__ = ["EVENT_PAYLOAD_TYPES", "parse_event_payload"]',
            "",
        ]
    )
    return "\n".join(lines)


def render_root_init(*, has_event_registry: bool) -> str:
    imports = ["from .clients._accessors import OpenClawClients", "from .version import SCHEMA_PACKAGE_VERSION"]
    exports = ["OpenClawClients", "SCHEMA_PACKAGE_VERSION"]
    if has_event_registry:
        imports.append("from .events import EVENT_PAYLOAD_TYPES, parse_event_payload")
        exports.extend(["EVENT_PAYLOAD_TYPES", "parse_event_payload"])
    return "\n".join(
        [
            '"""Generated OpenClaw protocol surface. Do not edit manually."""',
            "",
            *imports,
            "",
            "__all__ = [" + ", ".join(f'"{name}"' for name in exports) + "]",
            "",
        ]
    )


def render_version(version: str) -> str:
    return "\n".join(
        [
            '"""Generated OpenClaw schema package version. Do not edit manually."""',
            "",
            f"SCHEMA_PACKAGE_VERSION = {version!r}",
            "",
            '__all__ = ["SCHEMA_PACKAGE_VERSION"]',
            "",
        ]
    )


def render_clients_init(domains: list[str]) -> str:
    clients = [client_class_name(domain) for domain in domains]
    lines = ['"""Generated OpenClaw RPC clients. Do not edit manually."""', ""]
    lines.extend(f"from .{domain} import {client}" for domain, client in zip(domains, clients, strict=True))
    lines.extend(["", "__all__ = ["])
    lines.extend(f'    "{client}",' for client in clients)
    lines.extend(["]", ""])
    return "\n".join(lines)


def render_requester() -> str:
    return "\n".join(
        [
            '"""Generated requester protocol. Do not edit manually."""',
            "",
            "from collections.abc import Mapping",
            "from typing import Any, Protocol",
            "",
            "from pydantic import BaseModel",
            "",
            "",
            "class Requester(Protocol):",
            "    async def request(",
            "        self,",
            "        method: str,",
            "        params: BaseModel | Mapping[str, Any] | None = None,",
            "        *,",
            "        result_model: type[BaseModel] | None = None,",
            "        timeout: float | None = None,",
            "    ) -> Any: ...",
            "",
        ]
    )


def render_client_accessors(domains: list[str]) -> str:
    lines = [
        '"""Generated direct RPC client accessors. Do not edit manually."""',
        "",
        "from functools import cached_property",
        "from typing import cast",
        "",
    ]
    lines.append("from openclaw_codegen.generated.clients import (")
    lines.extend(f"    {client_class_name(domain)}," for domain in domains)
    lines.append(")")
    lines.extend(
        [
            "from openclaw_codegen.generated.clients._requester import Requester",
            "",
            "",
            "class OpenClawClients:",
            '    """Typed, lazily-created RPC clients for an OpenClaw requester."""',
            "",
            "    @property",
            "    def _requester(self) -> Requester:",
            "        return cast(Requester, self)",
        ]
    )
    for domain in domains:
        client = client_class_name(domain)
        lines.extend(
            [
                "",
                "    @cached_property",
                f"    def {domain}(self) -> {client}:",
                f"        return {client}(self._requester)",
            ]
        )
    lines.extend(["", "", '__all__ = ["OpenClawClients"]', ""])
    return "\n".join(lines)
