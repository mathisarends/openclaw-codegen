"""Generated mcp RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester


class McpMethod(StrEnum):
    APP_CALL_TOOL = "mcp.app.callTool"
    APP_LIST_RESOURCE_TEMPLATES = "mcp.app.listResourceTemplates"
    APP_LIST_RESOURCES = "mcp.app.listResources"
    APP_LIST_TOOLS = "mcp.app.listTools"
    APP_READ_RESOURCE = "mcp.app.readResource"
    APP_UPDATE_MODEL_CONTEXT = "mcp.app.updateModelContext"
    APP_VIEW = "mcp.app.view"


class McpClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def call_tool_app(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            McpMethod.APP_CALL_TOOL,
            params=payload,
        )

    async def list_resource_templates_app(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            McpMethod.APP_LIST_RESOURCE_TEMPLATES,
            params=payload,
        )

    async def list_resources_app(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            McpMethod.APP_LIST_RESOURCES,
            params=payload,
        )

    async def list_tools_app(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            McpMethod.APP_LIST_TOOLS,
            params=payload,
        )

    async def read_resource_app(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            McpMethod.APP_READ_RESOURCE,
            params=payload,
        )

    async def update_model_context_app(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            McpMethod.APP_UPDATE_MODEL_CONTEXT,
            params=payload,
        )

    async def view_app(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            McpMethod.APP_VIEW,
            params=payload,
        )
