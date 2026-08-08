"""Generated skills RPC client. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal

from openclaw_codegen.generated.clients._requester import Requester
from openclaw_codegen.generated.protocol import (
    SkillsBinsParams,
    SkillsBinsResult,
    SkillsCuratorStatusParams,
    SkillsCuratorStatusResult,
    SkillsDetailParams,
    SkillsDetailResult,
    SkillsInstallParams,
    SkillsProposalApplyResult,
    SkillsProposalCreateParams,
    SkillsProposalEvaluateParams,
    SkillsProposalEvaluateResult,
    SkillsProposalEventsListParams,
    SkillsProposalEventsListResult,
    SkillsProposalHistoryScanDirection,
    SkillsProposalHistoryScanParams,
    SkillsProposalHistoryScanResult,
    SkillsProposalHistoryStatusParams,
    SkillsProposalInspectParams,
    SkillsProposalInspectResult,
    SkillsProposalRequestRevisionParams,
    SkillsProposalRequestRevisionResult,
    SkillsProposalReviseParams,
    SkillsProposalsListParams,
    SkillsProposalsListResult,
    SkillsProposalUpdateParams,
    SkillsSearchParams,
    SkillsSearchResult,
    SkillsSecurityVerdictsParams,
    SkillsSecurityVerdictsResult,
    SkillsSkillCardParams,
    SkillsSkillCardResult,
    SkillsStatusParams,
    SkillsUpdateParams,
    SkillsUploadBeginParams,
    SkillsUploadChunkParams,
    SkillsUploadCommitParams,
)


class SkillsMethod(StrEnum):
    BINS = "skills.bins"
    CURATOR_PIN = "skills.curator.pin"
    CURATOR_RESTORE = "skills.curator.restore"
    CURATOR_STATUS = "skills.curator.status"
    CURATOR_UNPIN = "skills.curator.unpin"
    DETAIL = "skills.detail"
    INSTALL = "skills.install"
    PROPOSALS_APPLY = "skills.proposals.apply"
    PROPOSALS_CREATE = "skills.proposals.create"
    PROPOSALS_EVALUATE = "skills.proposals.evaluate"
    PROPOSALS_EVENTS_LIST = "skills.proposals.events.list"
    PROPOSALS_HISTORY_SCAN = "skills.proposals.historyScan"
    PROPOSALS_HISTORY_STATUS = "skills.proposals.historyStatus"
    PROPOSALS_INSPECT = "skills.proposals.inspect"
    PROPOSALS_LIST = "skills.proposals.list"
    PROPOSALS_QUARANTINE = "skills.proposals.quarantine"
    PROPOSALS_REJECT = "skills.proposals.reject"
    PROPOSALS_REQUEST_REVISION = "skills.proposals.requestRevision"
    PROPOSALS_REVISE = "skills.proposals.revise"
    PROPOSALS_UPDATE = "skills.proposals.update"
    SEARCH = "skills.search"
    SECURITY_VERDICTS = "skills.securityVerdicts"
    SKILL_CARD = "skills.skillCard"
    STATUS = "skills.status"
    UPDATE = "skills.update"
    UPLOAD_BEGIN = "skills.upload.begin"
    UPLOAD_CHUNK = "skills.upload.chunk"
    UPLOAD_COMMIT = "skills.upload.commit"


class SkillsClient:
    def __init__(self, client: Requester) -> None:
        self._client = client

    async def bins(
        self,
    ) -> SkillsBinsResult:
        payload = SkillsBinsParams()
        return await self._client.request(
            SkillsMethod.BINS,
            params=payload,
            result_model=SkillsBinsResult,
        )

    async def pin_curator(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SkillsMethod.CURATOR_PIN,
            params=payload,
        )

    async def restore_curator(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SkillsMethod.CURATOR_RESTORE,
            params=payload,
        )

    async def status_curator(
        self,
    ) -> SkillsCuratorStatusResult:
        payload = SkillsCuratorStatusParams()
        return await self._client.request(
            SkillsMethod.CURATOR_STATUS,
            params=payload,
            result_model=SkillsCuratorStatusResult,
        )

    async def unpin_curator(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SkillsMethod.CURATOR_UNPIN,
            params=payload,
        )

    async def detail(
        self,
        *,
        slug: str,
    ) -> SkillsDetailResult:
        payload = SkillsDetailParams(
            slug=slug,
        )
        return await self._client.request(
            SkillsMethod.DETAIL,
            params=payload,
            result_model=SkillsDetailResult,
        )

    async def install(
        self,
    ) -> Any:
        payload = SkillsInstallParams()
        return await self._client.request(
            SkillsMethod.INSTALL,
            params=payload,
        )

    async def apply_proposals(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> SkillsProposalApplyResult:
        payload = params
        return await self._client.request(
            SkillsMethod.PROPOSALS_APPLY,
            params=payload,
            result_model=SkillsProposalApplyResult,
        )

    async def create_proposals(
        self,
        *,
        name: str,
        description: str,
        content: str,
        agent_id: str | None = None,
        support_files: list[dict[str, Any]] | None = None,
        goal: str | None = None,
        evidence: str | None = None,
    ) -> Any:
        payload = SkillsProposalCreateParams(
            name=name,
            description=description,
            content=content,
            agent_id=agent_id,
            support_files=support_files,
            goal=goal,
            evidence=evidence,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_CREATE,
            params=payload,
        )

    async def evaluate_proposals(
        self,
        *,
        proposal_id: str,
        agent_id: str | None = None,
        expected_revision_hash: str | None = None,
        correlation_id: str | None = None,
    ) -> SkillsProposalEvaluateResult:
        payload = SkillsProposalEvaluateParams(
            proposal_id=proposal_id,
            agent_id=agent_id,
            expected_revision_hash=expected_revision_hash,
            correlation_id=correlation_id,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_EVALUATE,
            params=payload,
            result_model=SkillsProposalEvaluateResult,
        )

    async def list_events_proposals(
        self,
        *,
        agent_id: str | None = None,
        proposal_id: str | None = None,
        after_sequence: int | None = None,
        limit: int | None = None,
    ) -> SkillsProposalEventsListResult:
        payload = SkillsProposalEventsListParams(
            agent_id=agent_id,
            proposal_id=proposal_id,
            after_sequence=after_sequence,
            limit=limit,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_EVENTS_LIST,
            params=payload,
            result_model=SkillsProposalEventsListResult,
        )

    async def history_scan_proposals(
        self,
        *,
        agent_id: str | None = None,
        direction: SkillsProposalHistoryScanDirection | None = None,
    ) -> SkillsProposalHistoryScanResult:
        payload = SkillsProposalHistoryScanParams(
            agent_id=agent_id,
            direction=direction,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_HISTORY_SCAN,
            params=payload,
            result_model=SkillsProposalHistoryScanResult,
        )

    async def history_status_proposals(
        self,
        *,
        agent_id: str | None = None,
    ) -> Any:
        payload = SkillsProposalHistoryStatusParams(
            agent_id=agent_id,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_HISTORY_STATUS,
            params=payload,
        )

    async def inspect_proposals(
        self,
        *,
        proposal_id: str,
        agent_id: str | None = None,
    ) -> SkillsProposalInspectResult:
        payload = SkillsProposalInspectParams(
            proposal_id=proposal_id,
            agent_id=agent_id,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_INSPECT,
            params=payload,
            result_model=SkillsProposalInspectResult,
        )

    async def list_proposals(
        self,
        *,
        agent_id: str | None = None,
    ) -> SkillsProposalsListResult:
        payload = SkillsProposalsListParams(
            agent_id=agent_id,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_LIST,
            params=payload,
            result_model=SkillsProposalsListResult,
        )

    async def quarantine_proposals(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SkillsMethod.PROPOSALS_QUARANTINE,
            params=payload,
        )

    async def reject_proposals(
        self,
        *,
        params: dict[str, Any] | None = None,
    ) -> Any:
        payload = params
        return await self._client.request(
            SkillsMethod.PROPOSALS_REJECT,
            params=payload,
        )

    async def request_revision_proposals(
        self,
        *,
        proposal_id: str,
        instructions: str,
        session_key: str,
        idempotency_key: str,
        agent_id: str | None = None,
        target_agent_id: str | None = None,
        expected_revision_hash: str | None = None,
        session_id: str | None = None,
    ) -> SkillsProposalRequestRevisionResult:
        payload = SkillsProposalRequestRevisionParams(
            proposal_id=proposal_id,
            instructions=instructions,
            session_key=session_key,
            idempotency_key=idempotency_key,
            agent_id=agent_id,
            target_agent_id=target_agent_id,
            expected_revision_hash=expected_revision_hash,
            session_id=session_id,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_REQUEST_REVISION,
            params=payload,
            result_model=SkillsProposalRequestRevisionResult,
        )

    async def revise_proposals(
        self,
        *,
        proposal_id: str,
        agent_id: str | None = None,
        expected_revision_hash: str | None = None,
        correlation_id: str | None = None,
        content: str | None = None,
        support_files: list[dict[str, Any]] | None = None,
        description: str | None = None,
        goal: str | None = None,
        evidence: str | None = None,
    ) -> Any:
        payload = SkillsProposalReviseParams(
            proposal_id=proposal_id,
            agent_id=agent_id,
            expected_revision_hash=expected_revision_hash,
            correlation_id=correlation_id,
            content=content,
            support_files=support_files,
            description=description,
            goal=goal,
            evidence=evidence,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_REVISE,
            params=payload,
        )

    async def update_proposals(
        self,
        *,
        skill_name: str,
        content: str,
        agent_id: str | None = None,
        description: str | None = None,
        support_files: list[dict[str, Any]] | None = None,
        goal: str | None = None,
        evidence: str | None = None,
    ) -> Any:
        payload = SkillsProposalUpdateParams(
            skill_name=skill_name,
            content=content,
            agent_id=agent_id,
            description=description,
            support_files=support_files,
            goal=goal,
            evidence=evidence,
        )
        return await self._client.request(
            SkillsMethod.PROPOSALS_UPDATE,
            params=payload,
        )

    async def search(
        self,
        *,
        query: str | None = None,
        limit: int | None = None,
    ) -> SkillsSearchResult:
        payload = SkillsSearchParams(
            query=query,
            limit=limit,
        )
        return await self._client.request(
            SkillsMethod.SEARCH,
            params=payload,
            result_model=SkillsSearchResult,
        )

    async def security_verdicts(
        self,
        *,
        agent_id: str | None = None,
    ) -> SkillsSecurityVerdictsResult:
        payload = SkillsSecurityVerdictsParams(
            agent_id=agent_id,
        )
        return await self._client.request(
            SkillsMethod.SECURITY_VERDICTS,
            params=payload,
            result_model=SkillsSecurityVerdictsResult,
        )

    async def skill_card(
        self,
        *,
        skill_key: str,
        agent_id: str | None = None,
    ) -> SkillsSkillCardResult:
        payload = SkillsSkillCardParams(
            skill_key=skill_key,
            agent_id=agent_id,
        )
        return await self._client.request(
            SkillsMethod.SKILL_CARD,
            params=payload,
            result_model=SkillsSkillCardResult,
        )

    async def status(
        self,
        *,
        agent_id: str | None = None,
    ) -> Any:
        payload = SkillsStatusParams(
            agent_id=agent_id,
        )
        return await self._client.request(
            SkillsMethod.STATUS,
            params=payload,
        )

    async def update(
        self,
    ) -> Any:
        payload = SkillsUpdateParams()
        return await self._client.request(
            SkillsMethod.UPDATE,
            params=payload,
        )

    async def begin_upload(
        self,
        *,
        kind: Literal["skill-archive"],
        slug: str,
        size_bytes: int,
        sha256: str | None = None,
        force: bool | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        payload = SkillsUploadBeginParams(
            kind=kind,
            slug=slug,
            size_bytes=size_bytes,
            sha256=sha256,
            force=force,
            idempotency_key=idempotency_key,
        )
        return await self._client.request(
            SkillsMethod.UPLOAD_BEGIN,
            params=payload,
        )

    async def chunk_upload(
        self,
        *,
        upload_id: str,
        offset: int,
        data_base64: str,
    ) -> Any:
        payload = SkillsUploadChunkParams(
            upload_id=upload_id,
            offset=offset,
            data_base64=data_base64,
        )
        return await self._client.request(
            SkillsMethod.UPLOAD_CHUNK,
            params=payload,
        )

    async def commit_upload(
        self,
        *,
        upload_id: str,
        sha256: str | None = None,
    ) -> Any:
        payload = SkillsUploadCommitParams(
            upload_id=upload_id,
            sha256=sha256,
        )
        return await self._client.request(
            SkillsMethod.UPLOAD_COMMIT,
            params=payload,
        )
