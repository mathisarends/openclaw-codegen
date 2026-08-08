"""Generated question RPC client. Do not edit manually."""

from enum import StrEnum

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    Question,
    QuestionGetParams,
    QuestionGetResult,
    QuestionListParams,
    QuestionListResult,
    QuestionRequestParams,
    QuestionRequestResult,
    QuestionResolveParams,
    QuestionResolveResult,
    QuestionWaitAnswerParams,
    QuestionWaitAnswerResult,
)


class QuestionMethod(StrEnum):
    GET = "question.get"
    LIST = "question.list"
    REQUEST = "question.request"
    RESOLVE = "question.resolve"
    WAIT_ANSWER = "question.waitAnswer"


class QuestionClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def get(
        self,
        *,
        id: str,
    ) -> QuestionGetResult:
        payload = QuestionGetParams(
            id=id,
        )
        return await self._client.request(
            QuestionMethod.GET,
            params=payload,
            result_model=QuestionGetResult,
        )

    async def request(
        self,
        *,
        questions: list[Question],
        id: str | None = None,
        agent_id: str | None = None,
        session_key: str | None = None,
        run_id: str | None = None,
        timeout_ms: int | None = None,
    ) -> QuestionRequestResult:
        payload = QuestionRequestParams(
            questions=questions,
            id=id,
            agent_id=agent_id,
            session_key=session_key,
            run_id=run_id,
            timeout_ms=timeout_ms,
        )
        return await self._client.request(
            QuestionMethod.REQUEST,
            params=payload,
            result_model=QuestionRequestResult,
        )

    async def resolve(
        self,
    ) -> QuestionResolveResult:
        payload = QuestionResolveParams()
        return await self._client.request(
            QuestionMethod.RESOLVE,
            params=payload,
            result_model=QuestionResolveResult,
        )

    async def wait_answer(
        self,
        *,
        id: str,
        timeout_ms: int | None = None,
    ) -> QuestionWaitAnswerResult:
        payload = QuestionWaitAnswerParams(
            id=id,
            timeout_ms=timeout_ms,
        )
        return await self._client.request(
            QuestionMethod.WAIT_ANSWER,
            params=payload,
            result_model=QuestionWaitAnswerResult,
        )

    async def list(
        self,
    ) -> QuestionListResult:
        payload = QuestionListParams()
        return await self._client.request(
            QuestionMethod.LIST,
            params=payload,
            result_model=QuestionListResult,
        )
