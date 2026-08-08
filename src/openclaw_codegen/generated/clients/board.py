"""Generated board RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    BoardActionParams,
    BoardCanvasDocumentSource,
    BoardDataReadParams,
    BoardEventParams,
    BoardGetParams,
    BoardPromptAuthorizeParams,
    BoardTabCreateOp,
    BoardTabDeleteOp,
    BoardTabsReorderOp,
    BoardTabUpdateOp,
    BoardUpdateParams,
    BoardWidgetAppViewParams,
    BoardWidgetAppViewResult,
    BoardWidgetDeclared,
    BoardWidgetGrantDecision,
    BoardWidgetGrantParams,
    BoardWidgetHeightMode,
    BoardWidgetHtmlContent,
    BoardWidgetMcpAppPutContent,
    BoardWidgetMoveOp,
    BoardWidgetPluginContent,
    BoardWidgetPresentation,
    BoardWidgetPutParams,
    BoardWidgetRemoveOp,
    BoardWidgetResizeOp,
)


class BoardMethod(StrEnum):
    ACTION = "board.action"
    DATA_READ = "board.data.read"
    EVENT = "board.event"
    GET = "board.get"
    PROMPT_AUTHORIZE = "board.prompt.authorize"
    UPDATE = "board.update"
    WIDGET_APP_VIEW = "board.widget.appView"
    WIDGET_GRANT = "board.widget.grant"
    WIDGET_PUT = "board.widget.put"


class BoardClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def action(
        self,
    ) -> Any:
        payload = BoardActionParams()
        return await self._client.request(
            BoardMethod.ACTION,
            params=payload,
        )

    async def read_data(
        self,
        *,
        ticket: str,
        binding_id: str,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = BoardDataReadParams(
            ticket=ticket,
            binding_id=binding_id,
            params=params,
        )
        return await self._client.request(
            BoardMethod.DATA_READ,
            params=payload,
        )

    async def event(
        self,
    ) -> Any:
        payload = BoardEventParams()
        return await self._client.request(
            BoardMethod.EVENT,
            params=payload,
        )

    async def get(
        self,
        *,
        session_key: str,
    ) -> Any:
        payload = BoardGetParams(
            session_key=session_key,
        )
        return await self._client.request(
            BoardMethod.GET,
            params=payload,
        )

    async def authorize_prompt(
        self,
        *,
        ticket: str,
    ) -> Any:
        payload = BoardPromptAuthorizeParams(
            ticket=ticket,
        )
        return await self._client.request(
            BoardMethod.PROMPT_AUTHORIZE,
            params=payload,
        )

    async def update(
        self,
        *,
        session_key: str,
        ops: list[
            BoardTabCreateOp
            | BoardTabUpdateOp
            | BoardTabDeleteOp
            | BoardTabsReorderOp
            | BoardWidgetMoveOp
            | BoardWidgetResizeOp
            | BoardWidgetRemoveOp
        ],
    ) -> Any:
        payload = BoardUpdateParams(
            session_key=session_key,
            ops=ops,
        )
        return await self._client.request(
            BoardMethod.UPDATE,
            params=payload,
        )

    async def app_view_widget(
        self,
        *,
        session_key: str,
        name: str,
        revision: int,
        instance_id: str,
    ) -> BoardWidgetAppViewResult:
        payload = BoardWidgetAppViewParams(
            session_key=session_key,
            name=name,
            revision=revision,
            instance_id=instance_id,
        )
        return await self._client.request(
            BoardMethod.WIDGET_APP_VIEW,
            params=payload,
            result_model=BoardWidgetAppViewResult,
        )

    async def grant_widget(
        self,
        *,
        session_key: str,
        name: str,
        decision: BoardWidgetGrantDecision,
        revision: int,
        instance_id: str,
    ) -> Any:
        payload = BoardWidgetGrantParams(
            session_key=session_key,
            name=name,
            decision=decision,
            revision=revision,
            instance_id=instance_id,
        )
        return await self._client.request(
            BoardMethod.WIDGET_GRANT,
            params=payload,
        )

    async def put_widget(
        self,
        *,
        session_key: str,
        name: str,
        content: BoardWidgetHtmlContent
        | BoardWidgetMcpAppPutContent
        | BoardWidgetPluginContent
        | BoardCanvasDocumentSource,
        title: str | None = None,
        presentation: BoardWidgetPresentation | None = None,
        height_mode: BoardWidgetHeightMode | None = None,
        placement: dict[str, Any] | None = None,
        declared: BoardWidgetDeclared | None = None,
    ) -> Any:
        payload = BoardWidgetPutParams(
            session_key=session_key,
            name=name,
            content=content,
            title=title,
            presentation=presentation,
            height_mode=height_mode,
            placement=placement,
            declared=declared,
        )
        return await self._client.request(
            BoardMethod.WIDGET_PUT,
            params=payload,
        )
