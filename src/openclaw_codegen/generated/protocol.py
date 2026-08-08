"""Generated from the pinned OpenClaw schema. Do not edit manually."""

from enum import StrEnum
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter
from pydantic.alias_generators import to_camel


class _SchemaModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        extra="forbid",
        populate_by_name=True,
        regex_engine="python-re",
    )


class AuthProbeStatus(StrEnum):
    OK = "ok"
    AUTH = "auth"
    RATE_LIMIT = "rate_limit"
    BILLING = "billing"
    TIMEOUT = "timeout"
    FORMAT = "format"
    UNKNOWN = "unknown"
    NO_MODEL = "no_model"


class EnvironmentStatus(StrEnum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    STARTING = "starting"
    STOPPING = "stopping"
    ERROR = "error"


class WorkerEnvironmentState(StrEnum):
    REQUESTED = "requested"
    PROVISIONING = "provisioning"
    BOOTSTRAPPING = "bootstrapping"
    READY = "ready"
    ATTACHED = "attached"
    IDLE = "idle"
    DRAINING = "draining"
    DESTROYING = "destroying"
    DESTROYED = "destroyed"
    FAILED = "failed"
    ORPHANED = "orphaned"


class WorkerTunnelStatus(StrEnum):
    STOPPED = "stopped"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RECONNECTING = "reconnecting"


class WorktreeRepositoryStatus(StrEnum):
    GIT = "git"
    NOT_GIT = "not_git"
    UNAVAILABLE = "unavailable"


class NodePresenceAliveReason(StrEnum):
    BACKGROUND = "background"
    SILENT_PUSH = "silent_push"
    BG_APP_REFRESH = "bg_app_refresh"
    SIGNIFICANT_LOCATION = "significant_location"
    MANUAL = "manual"
    CONNECT = "connect"


class SessionObserverHealth(StrEnum):
    ON_TRACK = "on-track"
    GRINDING = "grinding"
    STUCK = "stuck"
    WAITING_ON_USER = "waiting-on-user"
    WRAPPING_UP = "wrapping-up"
    DONE = "done"
    FAILED = "failed"


class SessionVisibility(StrEnum):
    SHARED = "shared"
    READ_ONLY = "read-only"
    SUGGEST = "suggest"
    DRAFT = "draft"


class SessionSharingRole(StrEnum):
    ADMIN = "admin"
    OWNER = "owner"
    MEMBER = "member"
    VIEWER = "viewer"


class SessionSharingAction(StrEnum):
    VISIBILITY = "visibility"
    MEMBER_ADDED = "member-added"
    MEMBER_REMOVED = "member-removed"


class SessionSuggestionState(StrEnum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DISMISSED = "dismissed"


class SessionSuggestionAction(StrEnum):
    ADDED = "added"
    RESOLVED = "resolved"


class SessionSuggestionResolution(StrEnum):
    SEND = "send"
    QUEUE = "queue"
    EDIT = "edit"
    DISMISS = "dismiss"


class SessionPlacementState(StrEnum):
    LOCAL = "local"
    REQUESTED = "requested"
    PROVISIONING = "provisioning"
    SYNCING = "syncing"
    STARTING = "starting"
    ACTIVE = "active"
    DRAINING = "draining"
    RECONCILING = "reconciling"
    RECLAIMED = "reclaimed"
    FAILED = "failed"


class SessionDiscussionState(StrEnum):
    NONE = "none"
    AVAILABLE = "available"
    OPEN = "open"


class SessionFileKind(StrEnum):
    MODIFIED = "modified"
    READ = "read"


class SessionFilePreviewKind(StrEnum):
    TEXT = "text"
    IMAGE = "image"
    UNSUPPORTED = "unsupported"


class SessionFileRelevance(StrEnum):
    MODIFIED = "modified"
    READ = "read"
    MIXED = "mixed"


class SessionDiffFileStatus(StrEnum):
    ADDED = "added"
    MODIFIED = "modified"
    DELETED = "deleted"
    RENAMED = "renamed"


class TaskSuggestionResolution(StrEnum):
    DISMISSED = "dismissed"
    ACCEPTED = "accepted"
    EXPIRED = "expired"


class SystemChangeKind(StrEnum):
    OPERATION = "operation"
    CONFIG_WRITE = "config-write"
    EXTERNAL_EDIT = "external-edit"


class SystemChangeSource(StrEnum):
    SYSTEM_AGENT = "system-agent"
    DOCTOR = "doctor"
    CONFIG_RPC = "config-rpc"
    CLI = "cli"
    PLUGIN_INSTALL = "plugin-install"
    EXTERNAL = "external"
    UNKNOWN = "unknown"


class AgentKind(StrEnum):
    AGENT = "agent"
    SYSTEM = "system"


class MemoryMigrationItemStatus(StrEnum):
    PLANNED = "planned"
    MIGRATED = "migrated"
    SKIPPED = "skipped"
    WARNING = "warning"
    CONFLICT = "conflict"
    ERROR = "error"


class ApprovalKind(StrEnum):
    EXEC = "exec"
    PLUGIN = "plugin"
    SYSTEM_AGENT = "system-agent"


class ApprovalDecision(StrEnum):
    ALLOW_ONCE = "allow-once"
    ALLOW_ALWAYS = "allow-always"
    DENY = "deny"


class ApprovalAllowDecision(StrEnum):
    ALLOW_ONCE = "allow-once"
    ALLOW_ALWAYS = "allow-always"


class ApprovalAllowedReason(StrEnum):
    USER = "user"


class ApprovalDeniedReason(StrEnum):
    USER = "user"
    MALFORMED_VERDICT = "malformed-verdict"
    NO_ROUTE = "no-route"
    STORAGE_CORRUPT = "storage-corrupt"


class ApprovalExpiredReason(StrEnum):
    TIMEOUT = "timeout"


class ApprovalCancelledReason(StrEnum):
    RUN_ABORTED = "run-aborted"
    GATEWAY_RESTART = "gateway-restart"


class PluginApprovalSeverity(StrEnum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class ApprovalTerminalReason(StrEnum):
    USER = "user"
    TIMEOUT = "timeout"
    MALFORMED_VERDICT = "malformed-verdict"
    NO_ROUTE = "no-route"
    RUN_ABORTED = "run-aborted"
    GATEWAY_RESTART = "gateway-restart"
    STORAGE_CORRUPT = "storage-corrupt"


class QuestionStatus(StrEnum):
    PENDING = "pending"
    ANSWERED = "answered"
    CANCELLED = "cancelled"
    EXPIRED = "expired"


class ChatRunStartupPhase(StrEnum):
    PREPARING_WORKSPACE = "preparing_workspace"
    PROVISIONING_ENVIRONMENT = "provisioning_environment"
    PREPARING_CONTEXT = "preparing_context"
    STARTING_MODEL = "starting_model"


class BoardTabChatDock(StrEnum):
    LEFT = "left"
    RIGHT = "right"
    BOTTOM = "bottom"
    HIDDEN = "hidden"


class BoardWidgetContentKind(StrEnum):
    HTML = "html"
    MCP_APP = "mcp-app"
    PLUGIN = "plugin"


class BoardWidgetPresentation(StrEnum):
    CARD = "card"
    FULL_BLEED = "full-bleed"
    FRAMELESS = "frameless"


class BoardWidgetHeightMode(StrEnum):
    AUTO = "auto"
    FIXED = "fixed"


class BoardWidgetGrantState(StrEnum):
    NONE = "none"
    PENDING = "pending"
    GRANTED = "granted"
    REJECTED = "rejected"


class BoardWidgetGrantDecision(StrEnum):
    GRANTED = "granted"
    REJECTED = "rejected"


class SnapshotAuthMode(StrEnum):
    NONE = "none"
    TOKEN = "token"
    PASSWORD = "password"
    TRUSTED_PROXY = "trusted-proxy"


class GatewaySuspendTaskBlockerRuntime(StrEnum):
    SUBAGENT = "subagent"
    ACP = "acp"
    CLI = "cli"
    CRON = "cron"


class GatewaySuspendBlockerKind(StrEnum):
    QUEUE = "queue"
    REPLY = "reply"
    EMBEDDED_RUN = "embedded-run"
    BACKGROUND_EXEC = "background-exec"
    CRON_RUN = "cron-run"
    TASK = "task"
    ROOT_REQUEST = "root-request"
    SESSION_ADMISSION = "session-admission"
    SESSION_MUTATION = "session-mutation"
    CHAT_RUN = "chat-run"
    QUEUED_TURN = "queued-turn"
    TERMINAL_PERSISTENCE = "terminal-persistence"
    TERMINAL_SESSION = "terminal-session"


class GatewaySuspendPrepareBusyReason(StrEnum):
    ACTIVE_WORK = "active-work"
    GATEWAY_DRAINING = "gateway-draining"


class ConversationSendStatus(StrEnum):
    SENT = "sent"
    QUEUED = "queued"
    SUPPRESSED = "suppressed"
    UNKNOWN = "unknown"


class ConversationListItemKind(StrEnum):
    DIRECT = "direct"
    GROUP = "group"
    CHANNEL = "channel"


class MessageActionInboundTurnKind(StrEnum):
    USER_REQUEST = "user_request"
    ROOM_EVENT = "room_event"


class AgentPromptMode(StrEnum):
    FULL = "full"
    MINIMAL = "minimal"
    NONE = "none"


class AgentBootstrapContextMode(StrEnum):
    FULL = "full"
    LIGHTWEIGHT = "lightweight"


class AgentBootstrapContextRunKind(StrEnum):
    DEFAULT = "default"
    HEARTBEAT = "heartbeat"
    CRON = "cron"


class AgentSessionEffects(StrEnum):
    VISIBLE = "visible"
    INTERNAL = "internal"


class AgentSourceReplyDeliveryMode(StrEnum):
    AUTOMATIC = "automatic"
    MESSAGE_TOOL_ONLY = "message_tool_only"


class AgentIdentityAvatarStatus(StrEnum):
    NONE = "none"
    LOCAL = "local"
    REMOTE = "remote"
    DATA = "data"


class WakeMode(StrEnum):
    NOW = "now"
    NEXT_HEARTBEAT = "next-heartbeat"


class WorktreeRecordOwnerKind(StrEnum):
    MANUAL = "manual"
    WORKBOARD = "workboard"
    SESSION = "session"


class WorktreeBranchKind(StrEnum):
    LOCAL = "local"
    REMOTE = "remote"


class NodePendingEnqueueType(StrEnum):
    STATUS_REQUEST = "status.request"
    LOCATION_REQUEST = "location.request"


class NodePendingEnqueuePriority(StrEnum):
    NORMAL = "normal"
    HIGH = "high"


class PushTestEnvironment(StrEnum):
    SANDBOX = "sandbox"
    PRODUCTION = "production"


class PushTestTransport(StrEnum):
    DIRECT = "direct"
    RELAY = "relay"


class UiSplitCommandDirection(StrEnum):
    RIGHT = "right"
    DOWN = "down"


class UiPanelCommandPanel(StrEnum):
    TERMINAL = "terminal"
    BROWSER = "browser"


class UiPanelCommandDock(StrEnum):
    BOTTOM = "bottom"
    RIGHT = "right"


class SessionsListSortBy(StrEnum):
    UPDATED_AT = "updatedAt"
    LAST_INTERACTION_AT = "lastInteractionAt"


class SessionsListBoardFace(StrEnum):
    CHAT = "chat"
    DASHBOARD = "dashboard"


class SessionCatalogPullRequestSummaryState(StrEnum):
    OPEN = "open"
    DRAFT = "draft"
    MERGED = "merged"
    CLOSED = "closed"


class SessionCatalogHostKind(StrEnum):
    GATEWAY = "gateway"
    NODE = "node"


class SessionCatalogTranscriptItemType(StrEnum):
    USER_MESSAGE = "userMessage"
    AGENT_MESSAGE = "agentMessage"
    REASONING = "reasoning"
    TOOL_CALL = "toolCall"
    TOOL_RESULT = "toolResult"
    OTHER = "other"


class SessionsSearchHitRole(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"


class SessionCompactionCheckpointReason(StrEnum):
    MANUAL = "manual"
    AUTO_THRESHOLD = "auto-threshold"
    OVERFLOW_RETRY = "overflow-retry"
    TIMEOUT_RETRY = "timeout-retry"


class SessionOperationEventPhase(StrEnum):
    START = "start"
    END = "end"


class SessionCreatedActorType(StrEnum):
    HUMAN = "human"
    AGENT = "agent"
    SYSTEM = "system"


class SessionRowKind(StrEnum):
    DIRECT = "direct"
    GROUP = "group"
    GLOBAL = "global"
    UNKNOWN = "unknown"


class SessionRowStatus(StrEnum):
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"
    KILLED = "killed"
    TIMEOUT = "timeout"


class SessionRowSubagentRole(StrEnum):
    ORCHESTRATOR = "orchestrator"
    LEAF = "leaf"


class SessionRowSubagentControlScope(StrEnum):
    CHILDREN = "children"
    NONE = "none"


class SessionRowCreatedVia(StrEnum):
    OPERATOR = "operator"
    SPAWN = "spawn"
    CHANNEL = "channel"
    CRON = "cron"
    TALK = "talk"
    RUN = "run"
    PLUGIN = "plugin"
    INTERNAL = "internal"


class SessionFileBrowserEntryKind(StrEnum):
    FILE = "file"
    DIRECTORY = "directory"


class SessionFileEntryContentEncoding(StrEnum):
    UTF8 = "utf8"
    BASE64 = "base64"


class SessionsDiffUnavailableReason(StrEnum):
    UNKNOWN_SESSION = "unknown_session"
    NOT_GIT = "not_git"


class SessionsResetReason(StrEnum):
    NEW = "new"
    RESET = "reset"


class SessionsUsageMode(StrEnum):
    UTC = "utc"
    GATEWAY = "gateway"
    SPECIFIC = "specific"


class SessionsUsageRange(StrEnum):
    FIELD_7D = "7d"
    FIELD_30D = "30d"
    FIELD_90D = "90d"
    FIELD_1Y = "1y"
    ALL = "all"


class SessionsUsageGroupBy(StrEnum):
    INSTANCE = "instance"
    FAMILY = "family"


class AuditActivityAgentRunV1Action(StrEnum):
    AGENT_RUN_STARTED = "agent.run.started"
    AGENT_RUN_FINISHED = "agent.run.finished"


class AuditActivityAgentRunV1Status(StrEnum):
    STARTED = "started"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    TIMED_OUT = "timed_out"
    BLOCKED = "blocked"


class AuditActivityAgentRunV1ErrorCode(StrEnum):
    RUN_FAILED = "run_failed"
    RUN_CANCELLED = "run_cancelled"
    RUN_TIMED_OUT = "run_timed_out"
    RUN_BLOCKED = "run_blocked"


class AuditActivityToolActionV1Action(StrEnum):
    TOOL_ACTION_STARTED = "tool.action.started"
    TOOL_ACTION_FINISHED = "tool.action.finished"


class AuditActivityToolActionV1Status(StrEnum):
    STARTED = "started"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    TIMED_OUT = "timed_out"
    BLOCKED = "blocked"
    UNKNOWN = "unknown"


class AuditActivityToolActionV1ErrorCode(StrEnum):
    TOOL_FAILED = "tool_failed"
    TOOL_CANCELLED = "tool_cancelled"
    TOOL_TIMED_OUT = "tool_timed_out"
    TOOL_BLOCKED = "tool_blocked"
    TOOL_OUTCOME_UNKNOWN = "tool_outcome_unknown"


class AuditActivityInboundMessageV1ConversationKind(StrEnum):
    DIRECT = "direct"
    GROUP = "group"
    CHANNEL = "channel"
    UNKNOWN = "unknown"


class AuditActivityInboundMessageV1Status(StrEnum):
    SUCCEEDED = "succeeded"
    BLOCKED = "blocked"
    FAILED = "failed"


class AuditActivityInboundMessageV1Outcome(StrEnum):
    COMPLETED = "completed"
    SKIPPED = "skipped"
    FAILED = "failed"


class AuditActivityInboundMessageV1ReasonCode(StrEnum):
    FAST_ABORT = "fast_abort"
    PLUGIN_BOUND_HANDLED = "plugin_bound_handled"
    PLUGIN_BOUND_UNAVAILABLE = "plugin_bound_unavailable"
    PLUGIN_BOUND_DECLINED = "plugin_bound_declined"
    BEFORE_DISPATCH_HANDLED = "before_dispatch_handled"
    ACP_DISPATCH_COMPLETED = "acp_dispatch_completed"
    ACP_DISPATCH_EMPTY = "acp_dispatch_empty"
    DUPLICATE = "duplicate"
    REPLY_OPERATION_ACTIVE = "reply_operation_active"
    REPLY_OPERATION_ABORTED = "reply_operation_aborted"
    ACP_DISPATCH_ABORTED = "acp_dispatch_aborted"
    ACP_DISPATCH_FAILED = "acp_dispatch_failed"
    PLUGIN_BOUND_ERROR = "plugin_bound_error"


class AuditActivityOutboundMessageV1DeliveryKind(StrEnum):
    TEXT = "text"
    MEDIA = "media"
    OTHER = "other"


class AuditActivityOutboundMessageV1Status(StrEnum):
    SUCCEEDED = "succeeded"
    BLOCKED = "blocked"
    FAILED = "failed"
    UNKNOWN = "unknown"


class AuditActivityOutboundMessageV1Outcome(StrEnum):
    SENT = "sent"
    SUPPRESSED = "suppressed"
    FAILED = "failed"
    UNKNOWN = "unknown"


class AuditActivityOutboundMessageV1ErrorCode(StrEnum):
    MESSAGE_DELIVERY_FAILED = "message_delivery_failed"
    MESSAGE_DELIVERY_PARTIAL_FAILURE = "message_delivery_partial_failure"


class AuditActivityOutboundMessageV1ReasonCode(StrEnum):
    CANCELLED_BY_MESSAGE_SENDING_HOOK = "cancelled_by_message_sending_hook"
    CANCELLED_BY_REPLY_PAYLOAD_SENDING_HOOK = "cancelled_by_reply_payload_sending_hook"
    EMPTY_AFTER_MESSAGE_SENDING_HOOK = "empty_after_message_sending_hook"
    EMPTY_AFTER_REPLY_PAYLOAD_SENDING_HOOK = "empty_after_reply_payload_sending_hook"
    NO_VISIBLE_PAYLOAD = "no_visible_payload"


class AuditActivityOutboundMessageV1FailureStage(StrEnum):
    PLATFORM_SEND = "platform_send"
    QUEUE = "queue"
    UNKNOWN = "unknown"


class AuditActivityListKind(StrEnum):
    AGENT_RUN = "agent_run"
    TOOL_ACTION = "tool_action"
    MESSAGE = "message"


class AuditActivityListDirection(StrEnum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"


class AuditEventKind(StrEnum):
    AGENT_RUN = "agent_run"
    TOOL_ACTION = "tool_action"


class AuditEventAction(StrEnum):
    AGENT_RUN_STARTED = "agent.run.started"
    AGENT_RUN_FINISHED = "agent.run.finished"
    TOOL_ACTION_STARTED = "tool.action.started"
    TOOL_ACTION_FINISHED = "tool.action.finished"


class AuditEventErrorCode(StrEnum):
    RUN_FAILED = "run_failed"
    RUN_CANCELLED = "run_cancelled"
    RUN_TIMED_OUT = "run_timed_out"
    RUN_BLOCKED = "run_blocked"
    TOOL_FAILED = "tool_failed"
    TOOL_CANCELLED = "tool_cancelled"
    TOOL_TIMED_OUT = "tool_timed_out"
    TOOL_BLOCKED = "tool_blocked"
    TOOL_OUTCOME_UNKNOWN = "tool_outcome_unknown"


class TaskSummaryStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    TIMED_OUT = "timed_out"


class ConfigSchemaLookupReloadKind(StrEnum):
    RESTART = "restart"
    HOT = "hot"
    NONE = "none"


class SystemAgentChatWelcomeVariant(StrEnum):
    ONBOARDING = "onboarding"
    NEW_AGENT = "new-agent"


class SystemAgentChatAction(StrEnum):
    NONE = "none"
    OPEN_AGENT = "open-agent"
    EXIT = "exit"


class SystemAgentSetupActivateStatus(StrEnum):
    OK = "ok"
    AUTH = "auth"
    RATE_LIMIT = "rate_limit"
    BILLING = "billing"
    TIMEOUT = "timeout"
    FORMAT = "format"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"


class SystemAgentSetupAuthStartStatus(StrEnum):
    RUNNING = "running"
    DONE = "done"
    CANCELLED = "cancelled"
    ERROR = "error"


class WizardStartFlow(StrEnum):
    SETUP = "setup"
    CHANNELS = "channels"


class WizardStepType(StrEnum):
    NOTE = "note"
    SELECT = "select"
    TEXT = "text"
    CONFIRM = "confirm"
    MULTISELECT = "multiselect"
    PROGRESS = "progress"
    ACTION = "action"


class WizardStepFormat(StrEnum):
    PLAIN = "plain"


class WizardStepExecutor(StrEnum):
    GATEWAY = "gateway"
    CLIENT = "client"


class TalkEventType(StrEnum):
    SESSION_STARTED = "session.started"
    SESSION_READY = "session.ready"
    SESSION_CLOSED = "session.closed"
    SESSION_ERROR = "session.error"
    SESSION_REPLACED = "session.replaced"
    TURN_STARTED = "turn.started"
    TURN_ENDED = "turn.ended"
    TURN_CANCELLED = "turn.cancelled"
    CAPTURE_STARTED = "capture.started"
    CAPTURE_STOPPED = "capture.stopped"
    CAPTURE_CANCELLED = "capture.cancelled"
    CAPTURE_ONCE = "capture.once"
    INPUT_AUDIO_DELTA = "input.audio.delta"
    INPUT_AUDIO_COMMITTED = "input.audio.committed"
    TRANSCRIPT_DELTA = "transcript.delta"
    TRANSCRIPT_DONE = "transcript.done"
    OUTPUT_TEXT_DELTA = "output.text.delta"
    OUTPUT_TEXT_DONE = "output.text.done"
    OUTPUT_AUDIO_STARTED = "output.audio.started"
    OUTPUT_AUDIO_DELTA = "output.audio.delta"
    OUTPUT_AUDIO_DONE = "output.audio.done"
    TOOL_CALL = "tool.call"
    TOOL_PROGRESS = "tool.progress"
    TOOL_RESULT = "tool.result"
    TOOL_ERROR = "tool.error"
    USAGE_METRICS = "usage.metrics"
    LATENCY_METRICS = "latency.metrics"
    HEALTH_CHANGED = "health.changed"


class TalkEventMode(StrEnum):
    REALTIME = "realtime"
    STT_TTS = "stt-tts"
    TRANSCRIPTION = "transcription"


class TalkEventTransport(StrEnum):
    WEBRTC = "webrtc"
    PROVIDER_WEBSOCKET = "provider-websocket"
    GATEWAY_RELAY = "gateway-relay"
    MANAGED_ROOM = "managed-room"


class TalkEventBrain(StrEnum):
    AGENT_CONSULT = "agent-consult"
    DIRECT_TOOLS = "direct-tools"
    NONE = "none"


class TalkClientSteerMode(StrEnum):
    STATUS = "status"
    STEER = "steer"
    CANCEL = "cancel"
    FOLLOWUP = "followup"


class TalkAgentControlTarget(StrEnum):
    EMBEDDED_RUN = "embedded_run"
    REPLY_RUN = "reply_run"


class ChannelsPairingApproveNotification(StrEnum):
    NOT_REQUESTED = "not-requested"
    SENT = "sent"
    UNSUPPORTED = "unsupported"
    FAILED = "failed"


class ChannelsPairingApproveCommandOwnerBootstrap(StrEnum):
    NOT_REQUESTED = "not-requested"
    CONFIGURED = "configured"
    ALREADY_CONFIGURED = "already-configured"
    UNAVAILABLE = "unavailable"


class AgentsListScope(StrEnum):
    PER_SENDER = "per-sender"
    GLOBAL = "global"


class ModelsListView(StrEnum):
    DEFAULT = "default"
    CONFIGURED = "configured"
    PROVIDER_CONFIG = "provider-config"
    ALL = "all"


class CommandEntryCategory(StrEnum):
    SESSION = "session"
    OPTIONS = "options"
    STATUS = "status"
    MANAGEMENT = "management"
    MEDIA = "media"
    TOOLS = "tools"
    DOCKS = "docks"


class CommandEntrySource(StrEnum):
    NATIVE = "native"
    SKILL = "skill"
    PLUGIN = "plugin"


class CommandEntryScope(StrEnum):
    TEXT = "text"
    NATIVE = "native"
    BOTH = "both"


class ToolCatalogProfileId(StrEnum):
    MINIMAL = "minimal"
    CODING = "coding"
    MESSAGING = "messaging"
    FULL = "full"


class ToolCatalogEntrySource(StrEnum):
    CORE = "core"
    PLUGIN = "plugin"


class ToolCatalogEntryRisk(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ToolsEffectiveEntrySource(StrEnum):
    CORE = "core"
    PLUGIN = "plugin"
    CHANNEL = "channel"
    MCP = "mcp"


class ToolsEffectiveNoticeSeverity(StrEnum):
    INFO = "info"
    WARNING = "warning"


class SkillsCuratorActionState(StrEnum):
    ACTIVE = "active"
    STALE = "stale"
    ARCHIVED = "archived"


class SkillsProposalHistoryScanDirection(StrEnum):
    OLDER = "older"
    NEWER = "newer"


class SkillsProposalRequestRevisionStatus(StrEnum):
    STARTED = "started"
    IN_FLIGHT = "in_flight"
    OK = "ok"
    TIMEOUT = "timeout"
    ERROR = "error"


class SkillsProposalRecordKind(StrEnum):
    CREATE = "create"
    UPDATE = "update"


class SkillsProposalRecordStatus(StrEnum):
    PENDING = "pending"
    APPLIED = "applied"
    REJECTED = "rejected"
    QUARANTINED = "quarantined"
    STALE = "stale"


class SkillsProposalRecordCreatedBy(StrEnum):
    SKILL_WORKSHOP = "skill-workshop"
    CLI = "cli"
    GATEWAY = "gateway"


class CronJobWakeMode(StrEnum):
    NEXT_HEARTBEAT = "next-heartbeat"
    NOW = "now"


class CronJobLastRunStatus(StrEnum):
    OK = "ok"
    ERROR = "error"
    SKIPPED = "skipped"


class CronJobLastDeliveryStatus(StrEnum):
    DELIVERED = "delivered"
    NOT_DELIVERED = "not-delivered"
    UNKNOWN = "unknown"
    NOT_REQUESTED = "not-requested"


class CronListEnabled(StrEnum):
    ALL = "all"
    ENABLED = "enabled"
    DISABLED = "disabled"


class CronListScheduleKind(StrEnum):
    ALL = "all"
    AT = "at"
    EVERY = "every"
    CRON = "cron"
    ON_EXIT = "on-exit"
    STREAM = "stream"


class CronListLastRunStatus(StrEnum):
    ALL = "all"
    OK = "ok"
    ERROR = "error"
    SKIPPED = "skipped"
    UNKNOWN = "unknown"


class CronListSortBy(StrEnum):
    NEXT_RUN_AT_MS = "nextRunAtMs"
    UPDATED_AT_MS = "updatedAtMs"
    NAME = "name"


class CronListSortDir(StrEnum):
    ASC = "asc"
    DESC = "desc"


class CronRunsScope(StrEnum):
    JOB = "job"
    ALL = "all"


class CronRunsStatus(StrEnum):
    ALL = "all"
    OK = "ok"
    ERROR = "error"
    SKIPPED = "skipped"


class CronRunLogEntryErrorReason(StrEnum):
    AUTH = "auth"
    AUTH_PERMANENT = "auth_permanent"
    FORMAT = "format"
    RATE_LIMIT = "rate_limit"
    OVERLOADED = "overloaded"
    BILLING = "billing"
    SERVER_ERROR = "server_error"
    TIMEOUT = "timeout"
    CONTEXT_OVERFLOW = "context_overflow"
    MODEL_NOT_FOUND = "model_not_found"
    SESSION_EXPIRED = "session_expired"
    EMPTY_RESPONSE = "empty_response"
    NO_ERROR_DETAILS = "no_error_details"
    UNCLASSIFIED = "unclassified"
    UNKNOWN = "unknown"


class TerminalExitEventReason(StrEnum):
    PROCESS_EXIT = "process_exit"
    CLOSED = "closed"
    DISCONNECTED = "disconnected"
    DETACHED = "detached"
    ERROR = "error"


class ExecApprovalsNodeSnapshotDefaultAction(StrEnum):
    ALLOW = "allow"
    DENY = "deny"
    PROMPT = "prompt"


class PluginApprovalRequestSeverity(StrEnum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class PluginCatalogEntryState(StrEnum):
    ENABLED = "enabled"
    DISABLED = "disabled"
    NOT_INSTALLED = "not-installed"
    ERROR = "error"


class PluginControlUiDescriptorSurface(StrEnum):
    SESSION = "session"
    TOOL = "tool"
    RUN = "run"
    SETTINGS = "settings"
    TAB = "tab"
    WIDGET = "widget"


class PluginSearchPackageFamily(StrEnum):
    CODE_PLUGIN = "code-plugin"
    BUNDLE_PLUGIN = "bundle-plugin"


class PluginSearchPackageChannel(StrEnum):
    OFFICIAL = "official"
    COMMUNITY = "community"
    PRIVATE = "private"


class DevicePairSetupCodeBootstrapProfile(StrEnum):
    LIMITED = "limited"
    NODE = "node"


class DevicePairSetupCodeAuth(StrEnum):
    TOKEN = "token"
    PASSWORD = "password"


class DevicePairSetupCodeAccess(StrEnum):
    FULL = "full"
    LIMITED = "limited"
    NODE = "node"


class ChatMessageGetUnavailableReason(StrEnum):
    NOT_FOUND = "not_found"
    OVERSIZED = "oversized"
    NOT_VISIBLE = "not_visible"


class ChatSendQueueMode(StrEnum):
    STEER = "steer"
    FOLLOWUP = "followup"
    COLLECT = "collect"
    INTERRUPT = "interrupt"


class ChatErrorEventErrorKind(StrEnum):
    REFUSAL = "refusal"
    TIMEOUT = "timeout"
    RATE_LIMIT = "rate_limit"
    CONTEXT_LENGTH = "context_length"
    UNKNOWN = "unknown"


class ChatSendStatus(StrEnum):
    STARTED = "started"
    OK = "ok"
    ERROR = "error"


class BoardTab(_SchemaModel):
    tab_id: str = Field(pattern="^[a-z0-9-]{1,40}$")
    title: str = Field(min_length=1, max_length=80)
    position: int = Field(ge=0)
    chat_dock: BoardTabChatDock


class BoardWidgetDeclared(_SchemaModel):
    net_origins: list[str] | None = Field(default=None, max_length=32)
    tools: list[str] | None = Field(default=None, max_length=64)


class BoardTabCreateOp(_SchemaModel):
    kind: Literal["tab_create"]
    tab_id: str = Field(pattern="^[a-z0-9-]{1,40}$")
    title: str = Field(min_length=1, max_length=80)
    chat_dock: BoardTabChatDock | None = Field(default=None)


class BoardTabUpdateOp(_SchemaModel):
    kind: Literal["tab_update"]
    tab_id: str = Field(pattern="^[a-z0-9-]{1,40}$")
    title: str | None = Field(default=None, min_length=1, max_length=80)
    chat_dock: BoardTabChatDock | None = Field(default=None)
    position: int | None = Field(default=None, ge=0)


class BoardTabDeleteOp(_SchemaModel):
    kind: Literal["tab_delete"]
    tab_id: str = Field(pattern="^[a-z0-9-]{1,40}$")


class BoardTabsReorderOp(_SchemaModel):
    kind: Literal["tabs_reorder"]
    tab_ids: list[str]


class BoardWidgetMoveOp(_SchemaModel):
    kind: Literal["widget_move"]
    name: str = Field(pattern="^[a-z0-9][a-z0-9._-]{0,63}$")
    tab_id: str | None = Field(default=None, pattern="^[a-z0-9-]{1,40}$")
    position: int | None = Field(default=None, ge=0)
    after: str | None = Field(default=None, pattern="^[a-z0-9][a-z0-9._-]{0,63}$")


class BoardWidgetResizeOp(_SchemaModel):
    kind: Literal["widget_resize"]
    name: str = Field(pattern="^[a-z0-9][a-z0-9._-]{0,63}$")
    size_w: int
    size_h: int
    height_mode: BoardWidgetHeightMode | None = Field(default=None)


class BoardWidgetRemoveOp(_SchemaModel):
    kind: Literal["widget_remove"]
    name: str = Field(pattern="^[a-z0-9][a-z0-9._-]{0,63}$")


class BoardMcpAppDescriptor(_SchemaModel):
    server_name: str = Field(min_length=1)
    tool_name: str = Field(min_length=1)
    ui_resource_uri: str = Field(min_length=1)
    tool_call_id: str = Field(min_length=1)


class BoardWidgetHtmlContent(_SchemaModel):
    kind: Literal["html"]
    html: str = Field(max_length=262144)


class BoardWidgetMcpAppPutContent(_SchemaModel):
    kind: Literal["mcp-app"]
    view_id: str = Field(min_length=1)


class BoardWidgetPluginContent(_SchemaModel):
    kind: Literal["plugin"]
    plugin_kind: str = Field(pattern="^[a-z0-9][a-z0-9-]{0,63}:[a-z0-9][a-z0-9._-]{0,63}$")
    props: dict[str, Any] | None = Field(default=None)


class BoardCanvasDocumentSource(_SchemaModel):
    kind: Literal["canvas-doc"]
    doc_id: str = Field(min_length=1)


class BoardGetParams(_SchemaModel):
    session_key: str = Field(min_length=1)


class BoardWidgetGrantParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    name: str = Field(pattern="^[a-z0-9][a-z0-9._-]{0,63}$")
    decision: BoardWidgetGrantDecision
    revision: int = Field(ge=1)
    instance_id: str = Field(min_length=1)


class BoardWidgetAppViewParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    name: str = Field(pattern="^[a-z0-9][a-z0-9._-]{0,63}$")
    revision: int = Field(ge=1)
    instance_id: str = Field(min_length=1)


class BoardWidgetAppViewResult(_SchemaModel):
    view_id: str = Field(min_length=1)
    expires_at_ms: int = Field(ge=0)


class BoardPromptAuthorizeParams(_SchemaModel):
    ticket: str = Field(min_length=1, max_length=2048)


class BoardDataReadParams(_SchemaModel):
    ticket: str = Field(min_length=1, max_length=2048)
    binding_id: str = Field(min_length=1, max_length=64)
    params: dict[str, Any] | None = Field(default=None)


class BoardChangedEvent(_SchemaModel):
    session_key: str = Field(min_length=1)
    revision: int = Field(ge=0)
    widget: str | None = Field(default=None, pattern="^[a-z0-9][a-z0-9._-]{0,63}$")


class BoardFocusTabCommand(_SchemaModel):
    kind: Literal["focus_tab"]
    tab_id: str = Field(pattern="^[a-z0-9-]{1,40}$")


class BoardSetChatDockCommand(_SchemaModel):
    kind: Literal["set_chat_dock"]
    dock: BoardTabChatDock


class ConnectParams(_SchemaModel):
    min_protocol: int = Field(ge=1)
    max_protocol: int = Field(ge=1)
    client: dict[str, Any]
    caps: list[str] | None = Field(default=None)
    commands: list[str] | None = Field(default=None)
    permissions: dict[str, Any] | None = Field(default=None)
    path_env: str | None = Field(default=None)
    role: str | None = Field(default=None, min_length=1)
    scopes: list[str] | None = Field(default=None)
    device: dict[str, Any] | None = Field(default=None)
    auth: dict[str, Any] | None = Field(default=None)
    locale: str | None = Field(default=None)
    user_agent: str | None = Field(default=None)


class WorkerAdmissionHandshake(_SchemaModel):
    bundle_hash: str = Field(min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    openclaw_version: str = Field(min_length=1, max_length=128)
    protocol_features: list[str] = Field(max_length=64)


class RequestFrame(_SchemaModel):
    type: Literal["req"]
    id: str = Field(default_factory=lambda: str(uuid4()), min_length=1)
    method: str = Field(min_length=1)
    params: Any | None = Field(default=None)
    traceparent: str | None = Field(default=None, max_length=128)


class PresenceEntry(_SchemaModel):
    host: str | None = Field(default=None, min_length=1)
    ip: str | None = Field(default=None, min_length=1)
    version: str | None = Field(default=None, min_length=1)
    platform: str | None = Field(default=None, min_length=1)
    device_family: str | None = Field(default=None, min_length=1)
    model_identifier: str | None = Field(default=None, min_length=1)
    mode: str | None = Field(default=None, min_length=1)
    last_input_seconds: int | None = Field(default=None, ge=0)
    reason: str | None = Field(default=None, min_length=1)
    tags: list[str] | None = Field(default=None)
    text: str | None = Field(default=None)
    ts: int = Field(ge=0)
    device_id: str | None = Field(default=None, min_length=1)
    roles: list[str] | None = Field(default=None)
    scopes: list[str] | None = Field(default=None)
    instance_id: str | None = Field(default=None, min_length=1)
    user: dict[str, Any] | None = Field(default=None)
    watched_sessions: list[str] | None = Field(default=None)


class StateVersion(_SchemaModel):
    presence: int = Field(ge=0)
    health: int = Field(ge=0)


class ErrorShape(_SchemaModel):
    code: str = Field(min_length=1)
    message: str = Field(min_length=1)
    details: Any | None = Field(default=None)
    retryable: bool | None = Field(default=None)
    retry_after_ms: int | None = Field(default=None, ge=0)


class MissingScopeErrorDetails(_SchemaModel):
    code: Literal["MISSING_SCOPE"]
    missing_scope: str = Field(min_length=1)
    required_scopes: list[str] = Field(min_length=1)


class McpAppViewExpiredErrorDetails(_SchemaModel):
    code: Literal["MCP_APP_VIEW_EXPIRED"]


class UnknownAgentIdErrorDetails(_SchemaModel):
    code: Literal["UNKNOWN_AGENT_ID"]
    agent_id: str = Field(min_length=1)


class WizardNotFoundErrorDetails(_SchemaModel):
    code: Literal["WIZARD_NOT_FOUND"]


class GatewaySuspendTaskBlocker(_SchemaModel):
    task_id: str
    status: Literal["running"]
    runtime: GatewaySuspendTaskBlockerRuntime
    run_id: str | None = Field(default=None)
    label: str | None = Field(default=None)
    title: str | None = Field(default=None)


class GatewaySuspendPrepareParams(_SchemaModel):
    request_id: str = Field(min_length=1, max_length=128, pattern="\\S")


class GatewaySuspendStatusParams(_SchemaModel):
    suspension_id: str = Field(min_length=1, max_length=128, pattern="\\S")


class GatewaySuspendStatusRunningResult(_SchemaModel):
    status: Literal["running"]


class GatewaySuspendStatusReadyResult(_SchemaModel):
    status: Literal["ready"]
    expires_at_ms: int = Field(ge=0)


class GatewaySuspendResumeParams(_SchemaModel):
    suspension_id: str = Field(min_length=1, max_length=128, pattern="\\S")


class GatewaySuspendResumeResult(_SchemaModel):
    ok: Literal[True]
    status: Literal["running"]
    resumed: bool


class EnvironmentsCreateParams(_SchemaModel):
    profile_id: str = Field(min_length=1)
    idempotency_key: str = Field(min_length=1)


class EnvironmentsDestroyParams(_SchemaModel):
    environment_id: str = Field(min_length=1)
    force: bool | None = Field(default=None)


class EnvironmentsListParams(_SchemaModel):
    pass


class EnvironmentsStatusParams(_SchemaModel):
    environment_id: str = Field(min_length=1)


class SystemInfoParams(_SchemaModel):
    pass


class SystemInfoResult(_SchemaModel):
    machine_name: str
    hostname: str
    platform: str
    release: str
    arch: str
    os_label: str
    lan_address: str | None = Field(default=None)
    port: int | None = Field(default=None)
    node_version: str
    pid: int
    process_instance_id: str | None = Field(default=None, min_length=1)
    uptime_ms: int
    cpu_count: int
    cpu_model: str | None = Field(default=None)
    load_average: list[float] | None = Field(default=None, min_length=3)
    memory_total_bytes: int
    memory_free_bytes: int
    disk_total_bytes: int | None = Field(default=None)
    disk_available_bytes: int | None = Field(default=None)
    disk_path: str | None = Field(default=None)
    default_agent_utility_model: dict[str, Any] | None = Field(default=None)


class AgentEvent(_SchemaModel):
    run_id: str = Field(min_length=1)
    seq: int = Field(ge=0)
    stream: str = Field(min_length=1)
    ts: int = Field(ge=0)
    spawned_by: str | None = Field(default=None, min_length=1)
    is_heartbeat: bool | None = Field(default=None)
    data: dict[str, Any]


class ConversationSendParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    source_session_key: str | None = Field(default=None, min_length=1)
    operation_id: str = Field(min_length=1)
    conversation_ref: str = Field(pattern="^conv_[a-f0-9]{32}$")
    message: str = Field(min_length=1)


class ConversationSendResult(_SchemaModel):
    status: ConversationSendStatus
    conversation_ref: str = Field(pattern="^conv_[a-f0-9]{32}$")
    channel: str = Field(min_length=1)
    message_id: str | None = Field(default=None, min_length=1)
    queue_id: str | None = Field(default=None, min_length=1)


class ConversationListItem(_SchemaModel):
    conversation_ref: str = Field(pattern="^conv_[a-f0-9]{32}$")
    channel: str = Field(min_length=1)
    account_id: str = Field(min_length=1)
    kind: ConversationListItemKind
    target: str = Field(min_length=1)
    thread_id: str | None = Field(default=None, min_length=1)
    label: str | None = Field(default=None, min_length=1)
    first_seen_at: int = Field(ge=0)
    last_seen_at: int = Field(ge=0)


class ConversationListParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    channel: str | None = Field(default=None, min_length=1)
    query: str | None = Field(default=None, min_length=1)
    limit: int | None = Field(default=None, ge=1, le=100)


class ConversationTurnCancelParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    turn_id: str = Field(min_length=1)


class ConversationTurnCancelResult(_SchemaModel):
    cancelled: bool


class ConversationTurnParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    source_session_key: str | None = Field(default=None, min_length=1)
    turn_id: str = Field(min_length=1)
    conversation_ref: str = Field(pattern="^conv_[a-f0-9]{32}$")
    message: str = Field(min_length=1)
    timeout_ms: int = Field(ge=1, le=300000)


class ConversationTurnReply(_SchemaModel):
    conversation_ref: str = Field(pattern="^conv_[a-f0-9]{32}$")
    message_id: str = Field(min_length=1)
    reply_to_id: str | None = Field(default=None, min_length=1)
    thread_id: str | None = Field(default=None, min_length=1)
    text: str
    timestamp: int = Field(ge=0)
    transcript_artifact_id: str | None = Field(default=None, min_length=1)
    transcript_message_id: str | None = Field(default=None, min_length=1)


class MessageActionParams(_SchemaModel):
    channel: str = Field(min_length=1)
    action: str = Field(min_length=1)
    params: dict[str, Any]
    account_id: str | None = Field(default=None)
    requester_account_id: str | None = Field(default=None)
    requester_sender_id: str | None = Field(default=None)
    sender_is_owner: bool | None = Field(default=None)
    session_key: str | None = Field(default=None)
    session_id: str | None = Field(default=None)
    inbound_turn_kind: MessageActionInboundTurnKind | None = Field(default=None)
    agent_id: str | None = Field(default=None)
    tool_context: dict[str, Any] | None = Field(default=None)
    conversation_read_origin: Literal["direct-operator"] | None = Field(default=None)
    idempotency_key: str = Field(min_length=1)


class SendParams(_SchemaModel):
    to: str = Field(min_length=1)
    message: str | None = Field(default=None)
    media_url: str | None = Field(default=None)
    media_urls: list[str] | None = Field(default=None)
    buffer: str | None = Field(default=None)
    filename: str | None = Field(default=None)
    content_type: str | None = Field(default=None)
    as_voice: bool | None = Field(default=None)
    gif_playback: bool | None = Field(default=None)
    channel: str | None = Field(default=None)
    account_id: str | None = Field(default=None)
    agent_id: str | None = Field(default=None)
    reply_to_id: str | None = Field(default=None)
    thread_id: str | None = Field(default=None)
    force_document: bool | None = Field(default=None)
    silent: bool | None = Field(default=None)
    parse_mode: Literal["HTML"] | None = Field(default=None)
    session_key: str | None = Field(default=None)
    idempotency_key: str = Field(min_length=1)


class PollParams(_SchemaModel):
    to: str = Field(min_length=1)
    question: str = Field(min_length=1)
    options: list[str] = Field(min_length=2, max_length=12)
    max_selections: int | None = Field(default=None, ge=1, le=12)
    duration_seconds: int | None = Field(default=None, ge=1, le=604800)
    duration_hours: int | None = Field(default=None, ge=1)
    silent: bool | None = Field(default=None)
    is_anonymous: bool | None = Field(default=None)
    thread_id: str | None = Field(default=None)
    channel: str | None = Field(default=None)
    account_id: str | None = Field(default=None)
    idempotency_key: str = Field(min_length=1)


class AgentParams(_SchemaModel):
    message: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    provider: str | None = Field(default=None)
    model: str | None = Field(default=None)
    to: str | None = Field(default=None)
    reply_to: str | None = Field(default=None)
    session_id: str | None = Field(default=None)
    session_key: str | None = Field(default=None)
    expected_existing_session_id: str | None = Field(default=None, min_length=1)
    thinking: str | None = Field(default=None)
    deliver: bool | None = Field(default=None)
    attachments: list[Any] | None = Field(default=None)
    channel: str | None = Field(default=None)
    reply_channel: str | None = Field(default=None)
    account_id: str | None = Field(default=None)
    reply_account_id: str | None = Field(default=None)
    thread_id: str | None = Field(default=None)
    group_id: str | None = Field(default=None)
    group_channel: str | None = Field(default=None)
    group_space: str | None = Field(default=None)
    timeout: int | None = Field(default=None, ge=0)
    best_effort_deliver: bool | None = Field(default=None)
    lane: str | None = Field(default=None)
    cwd: str | None = Field(default=None, min_length=1)
    cleanup_bundle_mcp_on_run_end: bool | None = Field(default=None)
    model_run: bool | None = Field(default=None)
    prompt_mode: AgentPromptMode | None = Field(default=None)
    extra_system_prompt: str | None = Field(default=None)
    bootstrap_context_mode: AgentBootstrapContextMode | None = Field(default=None)
    bootstrap_context_run_kind: AgentBootstrapContextRunKind | None = Field(default=None)
    acp_turn_source: Literal["manual_spawn"] | None = Field(default=None)
    internal_runtime_handoff_id: str | None = Field(default=None, min_length=1)
    exec_approval_followup_expected_session_id: str | None = Field(default=None, min_length=1)
    internal_events: list[dict[str, Any]] | None = Field(default=None)
    input_provenance: dict[str, Any] | None = Field(default=None)
    suppress_prompt_persistence: bool | None = Field(default=None)
    session_effects: AgentSessionEffects | None = Field(default=None)
    source_reply_delivery_mode: AgentSourceReplyDeliveryMode | None = Field(default=None)
    disable_message_tool: bool | None = Field(default=None)
    swarm_collector: bool | None = Field(default=None)
    swarm_output_schema: dict[str, Any] | None = Field(default=None)
    force_restart_safe_tools: bool | None = Field(default=None)
    force_code_mode_tools: bool | None = Field(default=None)
    voice_wake_trigger: str | None = Field(default=None)
    idempotency_key: str = Field(min_length=1)
    label: str | None = Field(default=None, min_length=1, max_length=512)


class AgentIdentityParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None)


class AgentIdentityResult(_SchemaModel):
    agent_id: str = Field(min_length=1)
    name: str | None = Field(default=None, min_length=1)
    avatar: str | None = Field(default=None, min_length=1)
    avatar_source: str | None = Field(default=None, min_length=1)
    avatar_status: AgentIdentityAvatarStatus | None = Field(default=None)
    avatar_reason: str | None = Field(default=None, min_length=1)
    emoji: str | None = Field(default=None, min_length=1)


class AgentWaitParams(_SchemaModel):
    run_id: str = Field(min_length=1)
    timeout_ms: int | None = Field(default=None, ge=0)


class WakeParams(_SchemaModel):
    mode: WakeMode
    text: str = Field(min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class WorktreeRecord(_SchemaModel):
    id: str = Field(min_length=1)
    name: str = Field(pattern="^[a-z0-9][a-z0-9-]{0,63}$")
    repo_fingerprint: str = Field(pattern="^[a-f0-9]{16}$")
    repo_root: str = Field(min_length=1)
    path: str = Field(min_length=1)
    branch: str = Field(min_length=1)
    base_ref: str = Field(min_length=1)
    owner_kind: WorktreeRecordOwnerKind
    owner_id: str | None = Field(default=None, min_length=1)
    snapshot_ref: str | None = Field(default=None, min_length=1)
    created_at: int = Field(ge=0)
    last_active_at: int = Field(ge=0)
    removed_at: int | None = Field(default=None, ge=0)


class WorktreesListParams(_SchemaModel):
    pass


class WorktreesCreateParams(_SchemaModel):
    repo_root: str = Field(min_length=1)
    name: str | None = Field(default=None, pattern="^[a-z0-9][a-z0-9-]{0,63}$")
    base_ref: str | None = Field(default=None, min_length=1)


class WorktreesRemoveParams(_SchemaModel):
    id: str = Field(min_length=1)
    force: bool | None = Field(default=None)


class WorktreesRemoveResult(_SchemaModel):
    removed: bool
    snapshot_ref: str | None = Field(default=None, min_length=1)
    snapshot_error: str | None = Field(default=None, min_length=1)


class WorktreesRestoreParams(_SchemaModel):
    id: str = Field(min_length=1)


class WorktreesGcParams(_SchemaModel):
    pass


class WorktreesGcResult(_SchemaModel):
    removed: list[str]
    orphans_deleted: int = Field(ge=0)
    snapshots_pruned: int = Field(ge=0)


class WorktreeBranch(_SchemaModel):
    name: str = Field(min_length=1)
    kind: WorktreeBranchKind


class WorktreesBranchesParams(_SchemaModel):
    repo_root: str = Field(min_length=1)
    include_repository_status: bool | None = Field(default=None)


class FsDirEntry(_SchemaModel):
    name: str = Field(min_length=1)
    path: str = Field(min_length=1)
    hidden: bool | None = Field(default=None)


class FsListDirParams(_SchemaModel):
    path: str | None = Field(default=None, min_length=1)
    node_id: str | None = Field(default=None, min_length=1)


class NodePairListParams(_SchemaModel):
    pass


class NodePairApproveParams(_SchemaModel):
    request_id: str = Field(min_length=1)


class NodePairRejectParams(_SchemaModel):
    request_id: str = Field(min_length=1)


class NodePairRemoveParams(_SchemaModel):
    node_id: str = Field(min_length=1)


class NodeRenameParams(_SchemaModel):
    node_id: str = Field(min_length=1)
    display_name: str = Field(min_length=1)


class NodeListParams(_SchemaModel):
    pass


class NodePluginToolDescriptor(_SchemaModel):
    plugin_id: str = Field(min_length=1)
    name: str = Field(min_length=1, max_length=64, pattern="^[A-Za-z][A-Za-z0-9_-]{0,63}$")
    description: str = Field(min_length=1)
    parameters: dict[str, Any] | None = Field(default=None)
    command: str | None = Field(default=None, min_length=1)
    mcp: dict[str, Any] | None = Field(default=None)


class NodeSkillDescriptor(_SchemaModel):
    name: str = Field(min_length=1, max_length=64, pattern="^(?!.*--)[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")
    description: str = Field(min_length=1, max_length=1024)
    content: str = Field(min_length=1, max_length=65536)


class NodePendingAckParams(_SchemaModel):
    ids: list[str] = Field(min_length=1)


class NodeDescribeParams(_SchemaModel):
    node_id: str = Field(min_length=1)


class NodeInvokeParams(_SchemaModel):
    node_id: str = Field(min_length=1)
    command: str = Field(min_length=1)
    params: Any | None = Field(default=None)
    timeout_ms: int | None = Field(default=None, ge=0)
    idempotency_key: str = Field(min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    turn_source_channel: str | None = Field(default=None)
    turn_source_to: str | None = Field(default=None)
    turn_source_account_id: str | None = Field(default=None)
    turn_source_thread_id: str | float | None = Field(default=None)


class NodeInvokeInputEvent(_SchemaModel):
    id: str = Field(min_length=1)
    node_id: str = Field(min_length=1)
    seq: int = Field(ge=0)
    payload_json: str = Field(max_length=16384)


class NodeInvokeProgressParams(_SchemaModel):
    invoke_id: str = Field(min_length=1)
    node_id: str = Field(min_length=1)
    seq: int = Field(ge=0)
    chunk: str = Field(max_length=16384)


class NodeInvokeResultParams(_SchemaModel):
    id: str = Field(min_length=1)
    node_id: str = Field(min_length=1)
    ok: bool
    payload: Any | None = Field(default=None)
    payload_json: str | None = Field(default=None)
    error: dict[str, Any] | None = Field(default=None)


class NodeInvokeRequestEvent(_SchemaModel):
    id: str = Field(min_length=1)
    node_id: str = Field(min_length=1)
    command: str = Field(min_length=1)
    params_json: str | None = Field(default=None)
    timeout_ms: int | None = Field(default=None, ge=0)
    idempotency_key: str | None = Field(default=None, min_length=1)


class NodeEventParams(_SchemaModel):
    event: str = Field(min_length=1)
    payload: Any | None = Field(default=None)
    payload_json: str | None = Field(default=None)


class NodeEventResult(_SchemaModel):
    ok: bool
    event: str = Field(min_length=1)
    handled: bool
    reason: str | None = Field(default=None, min_length=1)


class NodePendingDrainParams(_SchemaModel):
    max_items: int | None = Field(default=None, ge=1, le=10)


class NodePendingDrainResult(_SchemaModel):
    node_id: str = Field(min_length=1)
    revision: int = Field(ge=0)
    items: list[dict[str, Any]]
    has_more: bool


class NodePendingEnqueueParams(_SchemaModel):
    node_id: str = Field(min_length=1)
    type: NodePendingEnqueueType
    priority: NodePendingEnqueuePriority | None = Field(default=None)
    expires_in_ms: int | None = Field(default=None, ge=1000, le=86400000)
    wake: bool | None = Field(default=None)


class NodePendingEnqueueResult(_SchemaModel):
    node_id: str = Field(min_length=1)
    revision: int = Field(ge=0)
    queued: dict[str, Any]
    wake_triggered: bool


class PushTestParams(_SchemaModel):
    node_id: str = Field(min_length=1)
    title: str | None = Field(default=None)
    body: str | None = Field(default=None)
    environment: PushTestEnvironment | None = Field(default=None)


class PushTestResult(_SchemaModel):
    ok: bool
    status: int
    apns_id: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    token_suffix: str
    topic: str
    environment: PushTestEnvironment
    transport: PushTestTransport


class UiSplitCommand(_SchemaModel):
    kind: Literal["split"]
    direction: UiSplitCommandDirection
    session_key: str = Field(min_length=1)


class UiClosePaneCommand(_SchemaModel):
    kind: Literal["close-pane"]
    session_key: str = Field(min_length=1)


class UiFocusCommand(_SchemaModel):
    kind: Literal["focus"]
    session_key: str = Field(min_length=1)


class UiSidebarCommand(_SchemaModel):
    kind: Literal["sidebar"]
    visible: bool


class UiPanelCommand(_SchemaModel):
    kind: Literal["panel"]
    panel: UiPanelCommandPanel
    open: bool
    dock: UiPanelCommandDock | None = Field(default=None)
    terminal_session_id: str | None = Field(default=None, min_length=1)


class UiNavigateCommand(_SchemaModel):
    kind: Literal["navigate"]
    session_key: str = Field(min_length=1)


class UiCommandResult(_SchemaModel):
    ok: bool


class SecretsReloadParams(_SchemaModel):
    pass


class SecretsResolveParams(_SchemaModel):
    command_name: str = Field(min_length=1)
    target_ids: list[str]
    allowed_paths: list[str] | None = Field(default=None)
    forced_active_paths: list[str] | None = Field(default=None)
    optional_active_paths: list[str] | None = Field(default=None)
    provider_overrides: dict[str, Any] | None = Field(default=None)


class SecretsResolveAssignment(_SchemaModel):
    path: str | None = Field(default=None, min_length=1)
    path_segments: list[str]
    value: Any


class SessionsListParams(_SchemaModel):
    limit: int | None = Field(default=None, ge=1)
    offset: int | None = Field(default=None, ge=0)
    active_minutes: int | None = Field(default=None, ge=1)
    require_last_interaction: bool | None = Field(default=None)
    sort_by: SessionsListSortBy | None = Field(default=None)
    include_global: bool | None = Field(default=None)
    include_unknown: bool | None = Field(default=None)
    configured_agents_only: bool | None = Field(default=None)
    include_derived_titles: bool | None = Field(default=None)
    include_last_message: bool | None = Field(default=None)
    label: str | None = Field(default=None, min_length=1, max_length=512)
    board_face: SessionsListBoardFace | None = Field(default=None)
    creator_id: str | None = Field(default=None, min_length=1)
    spawned_by: str | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    search: str | None = Field(default=None)
    archived: bool | Literal["all"] | None = Field(default=None)


class SessionCatalogCapabilities(_SchemaModel):
    continue_session: bool
    archive: bool
    create_session: dict[str, Any] | None = Field(default=None)
    open_terminal: bool | None = Field(default=None)


class SessionCatalogPullRequestSummary(_SchemaModel):
    numbers: list[int] = Field(min_length=1, max_length=20)
    state: SessionCatalogPullRequestSummaryState


class SessionCatalogTranscriptItem(_SchemaModel):
    id: str | None = Field(default=None)
    type: SessionCatalogTranscriptItemType
    text: str | None = Field(default=None)
    timestamp: str | None = Field(default=None)
    model: str | None = Field(default=None)
    truncated: bool | None = Field(default=None)
    raw: Any | None = Field(default=None)


class SessionsCatalogListParams(_SchemaModel):
    catalog_id: str | None = Field(default=None, min_length=1)
    cursors: dict[str, Any] | None = Field(default=None)
    agent_id: str | None = Field(default=None, min_length=1)
    progress_id: str | None = Field(default=None, min_length=1, max_length=128)
    search: str | None = Field(default=None)
    limit_per_host: int | None = Field(default=None, ge=1)
    host_ids: list[str] | None = Field(default=None)


class SessionsCatalogReadParams(_SchemaModel):
    catalog_id: str = Field(min_length=1)
    host_id: str = Field(min_length=1)
    thread_id: str = Field(min_length=1)
    limit: int | None = Field(default=None, ge=1)
    cursor: str | None = Field(default=None)


class SessionsCatalogContinueParams(_SchemaModel):
    catalog_id: str = Field(min_length=1)
    host_id: str = Field(min_length=1)
    thread_id: str = Field(min_length=1)


class SessionsCatalogContinueResult(_SchemaModel):
    session_key: str = Field(min_length=1)


class SessionsCatalogArchiveParams(_SchemaModel):
    catalog_id: str = Field(min_length=1)
    host_id: str = Field(min_length=1)
    thread_id: str = Field(min_length=1)
    confirm_no_other_runner: Literal[True]


class SessionsCatalogArchiveResult(_SchemaModel):
    ok: Literal[True]


class SessionsCleanupParams(_SchemaModel):
    agent: str | None = Field(default=None, min_length=1)
    all_agents: bool | None = Field(default=None)
    enforce: bool | None = Field(default=None)
    active_key: str | None = Field(default=None, min_length=1)
    fix_missing: bool | None = Field(default=None)
    fix_dm_scope: bool | None = Field(default=None)


class SessionsPreviewParams(_SchemaModel):
    keys: list[str] = Field(min_length=1)
    limit: int | None = Field(default=None, ge=1)
    max_chars: int | None = Field(default=None, ge=20)


class SessionsDescribeParams(_SchemaModel):
    key: str = Field(min_length=1)
    include_derived_titles: bool | None = Field(default=None)
    include_last_message: bool | None = Field(default=None)


class SessionsResolveParams(_SchemaModel):
    key: str | None = Field(default=None, min_length=1)
    session_id: str | None = Field(default=None, min_length=1)
    label: str | None = Field(default=None, min_length=1, max_length=512)
    agent_id: str | None = Field(default=None, min_length=1)
    spawned_by: str | None = Field(default=None, min_length=1)
    include_global: bool | None = Field(default=None)
    include_unknown: bool | None = Field(default=None)
    allow_missing: bool | None = Field(default=None)


class SessionsSearchHit(_SchemaModel):
    session_key: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    message_id: str = Field(min_length=1)
    role: SessionsSearchHitRole
    timestamp: int = Field(ge=0)
    snippet: str
    score: float


class SessionsSearchParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    session_keys: list[str] | None = Field(default=None, min_length=1, max_length=200)
    query: str = Field(min_length=1, max_length=4096)
    limit: int | None = Field(default=None, ge=1, le=25)


class SessionCompactionCheckpoint(_SchemaModel):
    checkpoint_id: str = Field(min_length=1)
    session_key: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    created_at: int = Field(ge=0)
    reason: SessionCompactionCheckpointReason
    tokens_before: int | None = Field(default=None, ge=0)
    tokens_after: int | None = Field(default=None, ge=0)
    summary: str | None = Field(default=None)
    first_kept_entry_id: str | None = Field(default=None, min_length=1)
    pre_compaction: dict[str, Any]
    post_compaction: dict[str, Any]


class SessionOperationEvent(_SchemaModel):
    operation_id: str = Field(min_length=1)
    operation: Literal["compact"]
    phase: SessionOperationEventPhase
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    ts: int = Field(ge=0)
    completed: bool | None = Field(default=None)
    reason: str | None = Field(default=None)


class SessionCreatedActor(_SchemaModel):
    type: SessionCreatedActorType
    id: str | None = Field(default=None, min_length=1)
    label: str | None = Field(default=None, min_length=1)
    avatar_url: str | None = Field(default=None, min_length=1)


class SessionObserverPlanProgress(_SchemaModel):
    completed: int = Field(ge=0)
    total: int = Field(ge=0)


class SessionCompanionExchange(_SchemaModel):
    question: str = Field(min_length=1, max_length=400)
    answer: str = Field(min_length=1, max_length=1200)
    ts: int = Field(ge=0)


class SessionsCompanionAskParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    question: str = Field(min_length=1, max_length=400)


class SessionsCompanionAskResult(_SchemaModel):
    answer: str = Field(min_length=1, max_length=1200)
    ts: int = Field(ge=0)


class SessionsCompanionResetParams(_SchemaModel):
    session_key: str = Field(min_length=1)


class SessionsCompanionResetResult(_SchemaModel):
    ok: Literal[True]


class SessionsCompanionStateParams(_SchemaModel):
    session_key: str = Field(min_length=1)


class SessionsObserverVisibilityParams(_SchemaModel):
    visible: bool


class SessionsObserverVisibilityResult(_SchemaModel):
    ok: Literal[True]


class SessionSharingIdentity(_SchemaModel):
    type: SessionCreatedActorType
    id: str = Field(min_length=1)
    label: str | None = Field(default=None, min_length=1)
    avatar_url: str | None = Field(default=None, min_length=1)


class SessionMembersListParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class SessionMember(_SchemaModel):
    identity_id: str = Field(min_length=1)
    added_by: str = Field(min_length=1)
    added_at: int = Field(ge=0)


class SessionMemberAddParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    identity_id: str = Field(min_length=1)


class SessionMemberRemoveParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    identity_id: str = Field(min_length=1)


class SessionMemberMutationResult(_SchemaModel):
    ok: Literal[True]
    session_key: str = Field(min_length=1)
    identity_id: str = Field(min_length=1)


class SessionSuggestionsAddParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    text: str = Field(min_length=1, max_length=32768)


class SessionSuggestionsListParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class SessionTypingParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    session_id: str = Field(min_length=1)
    typing: bool


class SessionTypingResult(_SchemaModel):
    ok: Literal[True]
    broadcast: bool


class LocalSessionPlacement(_SchemaModel):
    state: Literal["local"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)


class RequestedSessionPlacement(_SchemaModel):
    state: Literal["requested"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)


class ProvisioningSessionPlacement(_SchemaModel):
    state: Literal["provisioning"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)
    environment_id: str | None = Field(default=None, min_length=1)


class SyncingSessionPlacement(_SchemaModel):
    state: Literal["syncing"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)
    environment_id: str = Field(min_length=1)
    worker_bundle_hash: str = Field(min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")


class StartingSessionPlacement(_SchemaModel):
    state: Literal["starting"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)
    environment_id: str = Field(min_length=1)
    worker_bundle_hash: str = Field(min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    workspace_base_manifest_ref: str = Field(min_length=1)
    remote_workspace_dir: str = Field(min_length=1)


class ActiveWorkerSessionPlacement(_SchemaModel):
    state: Literal["active"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)
    environment_id: str = Field(min_length=1)
    active_owner_epoch: int = Field(ge=1, le=9007199254740991)
    worker_bundle_hash: str = Field(min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    workspace_base_manifest_ref: str = Field(min_length=1)
    remote_workspace_dir: str = Field(min_length=1)
    last_transcript_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    last_live_event_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    workspace_result_conflict: dict[str, Any] | None = Field(default=None)


class DrainingSessionPlacement(_SchemaModel):
    state: Literal["draining"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)
    environment_id: str = Field(min_length=1)
    active_owner_epoch: int = Field(ge=1, le=9007199254740991)
    worker_bundle_hash: str = Field(min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    workspace_base_manifest_ref: str = Field(min_length=1)
    remote_workspace_dir: str = Field(min_length=1)
    last_transcript_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    last_live_event_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    workspace_result_conflict: dict[str, Any] | None = Field(default=None)


class ReconcilingSessionPlacement(_SchemaModel):
    state: Literal["reconciling"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)
    environment_id: str = Field(min_length=1)
    active_owner_epoch: int = Field(ge=1, le=9007199254740991)
    worker_bundle_hash: str = Field(min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    workspace_base_manifest_ref: str = Field(min_length=1)
    remote_workspace_dir: str = Field(min_length=1)
    last_transcript_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    last_live_event_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    workspace_result_conflict: dict[str, Any] | None = Field(default=None)


class ReclaimedSessionPlacement(_SchemaModel):
    state: Literal["reclaimed"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)
    environment_id: str | None = Field(default=None, min_length=1)
    active_owner_epoch: int | None = Field(default=None, ge=1, le=9007199254740991)
    workspace_base_manifest_ref: str | None = Field(default=None, min_length=1)
    remote_workspace_dir: str | None = Field(default=None, min_length=1)
    worker_bundle_hash: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    last_transcript_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    last_live_event_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    workspace_result_conflict: dict[str, Any] | None = Field(default=None)


class FailedSessionPlacement(_SchemaModel):
    state: Literal["failed"]
    generation: int = Field(ge=0, le=9007199254740991)
    created_at_ms: int = Field(ge=0, le=9007199254740991)
    updated_at_ms: int = Field(ge=0, le=9007199254740991)
    state_changed_at_ms: int = Field(ge=0, le=9007199254740991)
    environment_id: str | None = Field(default=None, min_length=1)
    active_owner_epoch: int | None = Field(default=None, ge=1, le=9007199254740991)
    workspace_base_manifest_ref: str | None = Field(default=None, min_length=1)
    remote_workspace_dir: str | None = Field(default=None, min_length=1)
    worker_bundle_hash: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    last_transcript_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    last_live_event_ack_cursor: int | None = Field(default=None, ge=0, le=9007199254740991)
    workspace_result_conflict: dict[str, Any] | None = Field(default=None)
    recovery_error: str = Field(min_length=1)


class SessionsDispatchParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    profile_id: str = Field(min_length=1)


class SessionsReclaimParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class SessionDiscussionInfoParams(_SchemaModel):
    session_key: str = Field(min_length=1)


class SessionDiscussionOpenParams(_SchemaModel):
    session_key: str = Field(min_length=1)


class SessionsCompactionListParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class SessionsCompactionGetParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    checkpoint_id: str = Field(min_length=1)


class SessionsCompactionBranchParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    checkpoint_id: str = Field(min_length=1)


class SessionsCompactionRestoreParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    checkpoint_id: str = Field(min_length=1)


class SessionsRewindParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    entry_id: str = Field(min_length=1)


class SessionsRewindResult(_SchemaModel):
    editor_text: str | None = Field(default=None)
    editor_attachments: list[dict[str, Any]] | None = Field(default=None)


class SessionsForkParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    entry_id: str = Field(min_length=1)


class SessionsForkResult(_SchemaModel):
    session_key: str = Field(min_length=1)
    editor_text: str | None = Field(default=None)
    editor_attachments: list[dict[str, Any]] | None = Field(default=None)


class SessionBranch(_SchemaModel):
    leaf_entry_id: str = Field(min_length=1)
    headline: str
    message_count: int = Field(ge=0)
    updated_at: str | None = Field(default=None, min_length=1)
    active: bool


class SessionsBranchesListParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class SessionsBranchesSwitchParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    leaf_entry_id: str = Field(min_length=1)


class SessionsBranchesSwitchResult(_SchemaModel):
    pass


class SessionsFilesListParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    path: str | None = Field(default=None)
    search: str | None = Field(default=None)


class SessionsFilesGetParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    path: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class SessionsFilesRevealParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class SessionsFilesRevealResult(_SchemaModel):
    ok: bool
    path: str | None = Field(default=None, min_length=1)
    error: str | None = Field(default=None, min_length=1)


class SessionsFilesSetParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    path: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    content: str
    expected_hash: str = Field(min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")


class SessionsDiffParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class SessionWorktreeInfo(_SchemaModel):
    id: str = Field(min_length=1)
    path: str = Field(min_length=1)
    branch: str = Field(min_length=1)


class SessionsSendParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    message: str
    thinking: str | None = Field(default=None)
    attachments: list[dict[str, Any]] | None = Field(default=None)
    timeout_ms: int | None = Field(default=None, ge=0)
    idempotency_key: str | None = Field(default=None, min_length=1)


class SessionsMessagesSubscribeParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    include_approvals: Literal[True] | None = Field(default=None)


class SessionsMessagesUnsubscribeParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class SessionsViewerPresenceSetParams(_SchemaModel):
    session_keys: list[str] = Field(max_length=32)


class SessionsViewerPresenceSetResult(_SchemaModel):
    session_keys: list[str] = Field(max_length=32)


class SessionsAbortParams(_SchemaModel):
    key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    clear_queued: bool | None = Field(default=None)


class SessionsPatchParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    expected_session_id: str | None = Field(default=None, min_length=1)
    expected_lifecycle_revision: str | None = Field(default=None, min_length=1)
    label: str | None = Field(default=None)
    category: str | None = Field(default=None)
    board_face: SessionsListBoardFace | None = Field(default=None)
    icon: str | None = Field(default=None)
    status_note: str | None = Field(default=None)
    attention: Literal["hand", "key", "alert", "flag", "lock", "hourglass"] | None = Field(default=None)
    ttl_minutes: int | None = Field(default=None, ge=1, le=120)
    archived: bool | None = Field(default=None)
    pinned: bool | None = Field(default=None)
    unread: bool | None = Field(default=None)
    thinking_level: str | None = Field(default=None)
    fast_mode: bool | None | Literal["auto"] = Field(default=None)
    tool_overrides: dict[str, Any] | None = Field(default=None)
    verbose_level: str | None = Field(default=None)
    trace_level: str | None = Field(default=None)
    reasoning_level: str | None = Field(default=None)
    response_usage: None | Literal["off", "tokens", "full", "on"] = Field(default=None)
    elevated_level: str | None = Field(default=None)
    exec_host: str | None = Field(default=None)
    exec_security: str | None = Field(default=None)
    exec_ask: str | None = Field(default=None)
    exec_node: str | None = Field(default=None)
    model: str | None = Field(default=None)
    completion_owner_session_key: str | None = Field(default=None)
    inherited_tool_policy_version: None | Literal[1] = Field(default=None)
    inherited_tool_allow: list[str] | None = Field(default=None)
    inherited_tool_deny: list[str] | None = Field(default=None)
    send_policy: None | Literal["allow", "deny"] = Field(default=None)
    group_activation: None | Literal["mention", "always"] = Field(default=None)


class SessionsPluginPatchParams(_SchemaModel):
    key: str = Field(min_length=1)
    plugin_id: str = Field(min_length=1)
    namespace: str = Field(min_length=1)
    value: Any | None = Field(default=None)
    unset: bool | None = Field(default=None)


class SessionsPluginPatchResult(_SchemaModel):
    ok: Literal[True]
    key: str = Field(min_length=1)
    value: Any | None = Field(default=None)


class SessionsResetParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    reason: SessionsResetReason | None = Field(default=None)


class SessionsDeleteParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    delete_transcript: bool | None = Field(default=None)
    expected_session_id: str | None = Field(default=None, min_length=1)
    expected_lifecycle_revision: str | None = Field(default=None, min_length=1)
    expected_session_updated_at: float | None = Field(default=None, ge=0)
    emit_lifecycle_hooks: bool | None = Field(default=None)
    archived_only: bool | None = Field(default=None)


class SessionGroup(_SchemaModel):
    name: str = Field(min_length=1, max_length=512)
    position: int = Field(ge=0)


class SessionsGroupsListParams(_SchemaModel):
    pass


class SessionsGroupsPutParams(_SchemaModel):
    names: list[str] = Field(max_length=200)
    section_order: list[str] | None = Field(default=None, max_length=232)


class SessionsGroupsRenameParams(_SchemaModel):
    name: str = Field(min_length=1, max_length=512)
    to: str = Field(min_length=1, max_length=512)


class SessionsGroupsDeleteParams(_SchemaModel):
    name: str = Field(min_length=1, max_length=512)


class SessionsCompactParams(_SchemaModel):
    key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    max_lines: int | None = Field(default=None, ge=1)


class SessionsUsageParams(_SchemaModel):
    key: str | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    agent_scope: Literal["all"] | None = Field(default=None)
    start_date: str | None = Field(default=None, pattern="^\\d{4}-\\d{2}-\\d{2}$")
    end_date: str | None = Field(default=None, pattern="^\\d{4}-\\d{2}-\\d{2}$")
    mode: SessionsUsageMode | None = Field(default=None)
    range: SessionsUsageRange | None = Field(default=None)
    group_by: SessionsUsageGroupBy | None = Field(default=None)
    include_historical: bool | None = Field(default=None)
    utc_offset: str | None = Field(default=None, pattern="^UTC[+-]\\d{1,2}(?::[0-5]\\d)?$")
    time_zone: str | None = Field(default=None, min_length=1)
    limit: int | None = Field(default=None, ge=1)
    include_context_weight: bool | None = Field(default=None)


class AuditActivityInboundMessageV1(_SchemaModel):
    event_type: Literal["inbound_message"]
    schema_version: int = Field(ge=1, le=1)
    event_id: str = Field(min_length=1)
    sequence: int = Field(ge=1)
    source_sequence: int = Field(ge=1)
    occurred_at: int = Field(ge=0)
    redaction: Literal["metadata_only"]
    channel: str = Field(min_length=1)
    conversation_kind: AuditActivityInboundMessageV1ConversationKind
    duration_ms: int | None = Field(default=None, ge=0)
    result_count: int | None = Field(default=None, ge=0)
    agent_id: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    account_ref: str | None = Field(default=None, pattern="^hmac-sha256:v1:[a-f0-9]{32}:[a-f0-9]{64}$")
    conversation_ref: str | None = Field(default=None, pattern="^hmac-sha256:v1:[a-f0-9]{32}:[a-f0-9]{64}$")
    message_ref: str | None = Field(default=None, pattern="^hmac-sha256:v1:[a-f0-9]{32}:[a-f0-9]{64}$")
    target_ref: str | None = Field(default=None, pattern="^hmac-sha256:v1:[a-f0-9]{32}:[a-f0-9]{64}$")
    kind: Literal["message"]
    action: Literal["message.inbound.processed"]
    direction: Literal["inbound"]
    actor: dict[str, Any]
    status: AuditActivityInboundMessageV1Status
    outcome: AuditActivityInboundMessageV1Outcome
    error_code: Literal["message_processing_failed"] | None = Field(default=None)
    reason_code: AuditActivityInboundMessageV1ReasonCode | None = Field(default=None)


class AuditActivityListParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    kind: AuditActivityListKind | None = Field(default=None)
    status: AuditActivityToolActionV1Status | None = Field(default=None)
    direction: AuditActivityListDirection | None = Field(default=None)
    channel: str | None = Field(default=None, min_length=1)
    after: int | None = Field(default=None, ge=0)
    before: int | None = Field(default=None, ge=0)
    limit: int | None = Field(default=None, ge=1, le=500)
    cursor: str | None = Field(default=None, min_length=1)


class AuditListParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    kind: AuditEventKind | None = Field(default=None)
    status: AuditActivityToolActionV1Status | None = Field(default=None)
    after: int | None = Field(default=None, ge=0)
    before: int | None = Field(default=None, ge=0)
    limit: int | None = Field(default=None, ge=1, le=500)
    cursor: str | None = Field(default=None, min_length=1)


class TaskSuggestion(_SchemaModel):
    id: str = Field(min_length=1, max_length=128)
    title: str = Field(min_length=1, max_length=60)
    prompt: str = Field(min_length=1, max_length=32768)
    tldr: str = Field(min_length=1, max_length=1024)
    cwd: str = Field(min_length=1, max_length=4096)
    session_key: str = Field(min_length=1, max_length=512)
    agent_id: str | None = Field(default=None, min_length=1, max_length=128)
    created_at: int = Field(ge=0)


class TaskSuggestionsAcceptParams(_SchemaModel):
    task_id: str = Field(min_length=1, max_length=128)


class TaskSuggestionsAcceptResult(_SchemaModel):
    task_id: str = Field(min_length=1, max_length=128)
    key: str = Field(min_length=1, max_length=512)


class TaskSuggestionsCreateParams(_SchemaModel):
    title: str = Field(min_length=1, max_length=60)
    prompt: str = Field(min_length=1, max_length=32768)
    tldr: str = Field(min_length=1, max_length=1024)
    cwd: str = Field(min_length=1, max_length=4096)
    session_key: str = Field(min_length=1, max_length=512)
    agent_id: str | None = Field(default=None, min_length=1, max_length=128)


class TaskSuggestionsDismissParams(_SchemaModel):
    task_id: str = Field(min_length=1, max_length=128)
    reason: str | None = Field(default=None, max_length=1024)


class TaskSuggestionsDismissResult(_SchemaModel):
    task_id: str = Field(min_length=1, max_length=128)
    dismissed: bool


class TaskSuggestionsListParams(_SchemaModel):
    session_key: str | None = Field(default=None, min_length=1, max_length=512)
    agent_id: str | None = Field(default=None, min_length=1, max_length=128)


class TaskSummary(_SchemaModel):
    id: str = Field(min_length=1)
    kind: str | None = Field(default=None)
    runtime: str | None = Field(default=None)
    status: TaskSummaryStatus
    title: str | None = Field(default=None)
    agent_id: str | None = Field(default=None)
    session_key: str | None = Field(default=None)
    child_session_key: str | None = Field(default=None)
    owner_key: str | None = Field(default=None)
    run_id: str | None = Field(default=None)
    task_id: str | None = Field(default=None)
    flow_id: str | None = Field(default=None)
    parent_task_id: str | None = Field(default=None)
    source_id: str | None = Field(default=None)
    created_at: str | int | None = Field(default=None)
    updated_at: str | int | None = Field(default=None)
    started_at: str | int | None = Field(default=None)
    ended_at: str | int | None = Field(default=None)
    tool_use_count: int | None = Field(default=None, ge=0)
    last_tool_name: str | None = Field(default=None)
    progress_summary: str | None = Field(default=None)
    terminal_summary: str | None = Field(default=None)
    error: str | None = Field(default=None)
    prompt: str | None = Field(default=None)


class TasksListParams(_SchemaModel):
    status: TaskSummaryStatus | list[TaskSummaryStatus] | None = Field(default=None)
    agent_id: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    limit: int | None = Field(default=None, ge=1, le=500)
    cursor: str | None = Field(default=None)


class TasksGetParams(_SchemaModel):
    task_id: str = Field(min_length=1)


class TasksCancelParams(_SchemaModel):
    task_id: str = Field(min_length=1)
    reason: str | None = Field(default=None)


class ConfigGetParams(_SchemaModel):
    pass


class ConfigSetParams(_SchemaModel):
    raw: str = Field(min_length=1)
    base_hash: str | None = Field(default=None, min_length=1)


class ConfigApplyParams(_SchemaModel):
    raw: str = Field(min_length=1)
    base_hash: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None)
    delivery_context: dict[str, Any] | None = Field(default=None)
    note: str | None = Field(default=None)
    restart_delay_ms: int | None = Field(default=None, ge=0)


class ConfigPatchParams(_SchemaModel):
    raw: str = Field(min_length=1)
    base_hash: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None)
    delivery_context: dict[str, Any] | None = Field(default=None)
    note: str | None = Field(default=None)
    restart_delay_ms: int | None = Field(default=None, ge=0)
    replace_paths: list[str] | None = Field(default=None, max_length=256)


class ConfigSchemaParams(_SchemaModel):
    pass


class ConfigSchemaLookupParams(_SchemaModel):
    path: str = Field(min_length=1, max_length=1024, pattern="^[A-Za-z0-9_./\\[\\]\\-*]+$")


class ConfigSchemaResponse(_SchemaModel):
    schema_: Any = Field(alias="schema")
    ui_hints: dict[str, Any]
    version: str = Field(min_length=1)
    generated_at: str = Field(min_length=1)


class ConfigSchemaLookupResult(_SchemaModel):
    path: str = Field(min_length=1)
    schema_: Any = Field(alias="schema")
    reload_kind: ConfigSchemaLookupReloadKind | None = Field(default=None)
    hint: dict[str, Any] | None = Field(default=None)
    hint_path: str | None = Field(default=None)
    children: list[dict[str, Any]]


class SystemAgentChatParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    message: str | None = Field(default=None)
    welcome_variant: SystemAgentChatWelcomeVariant | None = Field(default=None)
    reset: bool | None = Field(default=None)
    context: dict[str, Any] | None = Field(default=None)
    delegation: dict[str, Any] | None = Field(default=None)


class SystemAgentChatResult(_SchemaModel):
    session_id: str = Field(min_length=1)
    reply: str = Field(min_length=1)
    sensitive: bool | None = Field(default=None)
    wizard_input_pending: bool | None = Field(default=None)
    action: SystemAgentChatAction
    agent_draft: Literal["hatch"] | None = Field(default=None)
    agent_id: str | None = Field(default=None, min_length=1)
    needs_approval: bool | None = Field(default=None)
    proposal_id: str | None = Field(default=None, min_length=1)
    question: dict[str, Any] | None = Field(default=None)


class SystemAgentChatHistoryParams(_SchemaModel):
    limit: int | None = Field(default=None, ge=1, le=500)


class SystemAgentChatHistoryTurn(_SchemaModel):
    role: SessionsSearchHitRole
    text: str
    at: float


class SystemChangesListParams(_SchemaModel):
    limit: int | None = Field(default=None, ge=1, le=200)
    before_cursor: str | None = Field(default=None, min_length=1)


class SystemAgentSetupDetectParams(_SchemaModel):
    pass


class SystemAgentSetupDetectResult(_SchemaModel):
    candidates: list[dict[str, Any]]
    unavailable_candidates: list[dict[str, Any]] | None = Field(default=None)
    manual_providers: list[dict[str, Any]]
    auth_options: list[dict[str, Any]] | None = Field(default=None)
    recommended_installs: list[dict[str, Any]] | None = Field(default=None)
    workspace: str = Field(min_length=1)
    codex_app_server_detected: bool | None = Field(default=None)
    configured_model: str | None = Field(default=None)
    setup_complete: bool


class SystemAgentSetupVerifyParams(_SchemaModel):
    pass


class SystemAgentSetupActivateParams(_SchemaModel):
    kind: (
        str
        | Literal[
            "existing-model", "openai-api-key", "anthropic-api-key", "claude-cli", "codex-cli", "gemini-cli", "api-key"
        ]
    )
    model_ref: str | None = Field(default=None, min_length=1)
    auth_choice: str | None = Field(default=None)
    api_key: str | None = Field(default=None)
    workspace: str | None = Field(default=None)


class SystemAgentSetupActivateResult(_SchemaModel):
    ok: bool
    model_ref: str | None = Field(default=None)
    latency_ms: float | None = Field(default=None)
    lines: list[str] | None = Field(default=None)
    status: SystemAgentSetupActivateStatus | None = Field(default=None)
    error: str | None = Field(default=None)


class SystemAgentSetupAuthStartParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    auth_choice: str = Field(min_length=1)
    workspace: str | None = Field(default=None)


class WizardStartParams(_SchemaModel):
    mode: WorktreeBranchKind | None = Field(default=None)
    workspace: str | None = Field(default=None)
    install_daemon: bool | None = Field(default=None)
    flow: WizardStartFlow | None = Field(default=None)
    channel: str | None = Field(default=None, min_length=1)


class WizardNextParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    answer: dict[str, Any] | None = Field(default=None)


class WizardCancelParams(_SchemaModel):
    session_id: str = Field(min_length=1)


class WizardStatusParams(_SchemaModel):
    session_id: str = Field(min_length=1)


class WizardStep(_SchemaModel):
    id: str = Field(min_length=1)
    type: WizardStepType
    title: str | None = Field(default=None)
    message: str | None = Field(default=None)
    format: WizardStepFormat | None = Field(default=None)
    options: list[dict[str, Any]] | None = Field(default=None)
    initial_value: Any | None = Field(default=None)
    placeholder: str | None = Field(default=None)
    sensitive: bool | None = Field(default=None)
    executor: WizardStepExecutor | None = Field(default=None)
    external_url: str | None = Field(default=None)
    device_code: dict[str, Any] | None = Field(default=None)


class WizardStatusResult(_SchemaModel):
    status: SystemAgentSetupAuthStartStatus
    error: str | None = Field(default=None)


class TalkModeParams(_SchemaModel):
    enabled: bool
    phase: str | None = Field(default=None)


class TalkEvent(_SchemaModel):
    id: str = Field(min_length=1)
    type: TalkEventType
    session_id: str = Field(min_length=1)
    turn_id: str | None = Field(default=None)
    capture_id: str | None = Field(default=None)
    seq: int = Field(ge=1)
    timestamp: str = Field(min_length=1)
    mode: TalkEventMode
    transport: TalkEventTransport
    brain: TalkEventBrain
    provider: str | None = Field(default=None)
    final: bool | None = Field(default=None)
    call_id: str | None = Field(default=None)
    item_id: str | None = Field(default=None)
    parent_id: str | None = Field(default=None)
    payload: Any


class TalkCatalogParams(_SchemaModel):
    pass


class TalkCatalogResult(_SchemaModel):
    modes: list[TalkEventMode]
    transports: list[TalkEventTransport]
    brains: list[TalkEventBrain]
    speech: dict[str, Any]
    transcription: dict[str, Any]
    realtime: dict[str, Any]


class TalkClientCreateParams(_SchemaModel):
    session_key: str | None = Field(default=None, min_length=1)
    voice_session_id: str | None = Field(default=None, pattern="^[A-Za-z0-9_-]{1,128}$")
    provider: str | None = Field(default=None)
    model: str | None = Field(default=None)
    voice: str | None = Field(default=None)
    vad_threshold: float | None = Field(default=None)
    silence_duration_ms: int | None = Field(default=None, ge=1)
    prefix_padding_ms: int | None = Field(default=None, ge=0)
    reasoning_effort: str | None = Field(default=None)
    mode: TalkEventMode | None = Field(default=None)
    transport: TalkEventTransport | None = Field(default=None)
    brain: TalkEventBrain | None = Field(default=None)
    capabilities: list[Literal["camera-frame", "voice-transcript"]] | None = Field(default=None)


class TalkClientCloseParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    voice_session_id: str = Field(pattern="^[A-Za-z0-9_-]{1,128}$")


class TalkClientMutationResult(_SchemaModel):
    ok: Literal[True]


class TalkClientSteerParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    text: str = Field(min_length=1)
    mode: TalkClientSteerMode | None = Field(default=None)


class TalkAgentControlResult(_SchemaModel):
    ok: bool
    mode: TalkClientSteerMode
    session_key: str = Field(min_length=1)
    session_id: str | None = Field(default=None, min_length=1)
    active: bool
    queued: bool | None = Field(default=None)
    aborted: bool | None = Field(default=None)
    target: TalkAgentControlTarget | None = Field(default=None)
    reason: str | None = Field(default=None)
    message: str
    speak: bool
    show: bool
    suppress: bool
    provider_result: dict[str, Any] | None = Field(default=None)
    enqueued_at_ms: float | None = Field(default=None)
    delivered_at_ms: float | None = Field(default=None)


class TalkClientToolCallParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    voice_session_id: str | None = Field(default=None, pattern="^[A-Za-z0-9_-]{1,128}$")
    call_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    args: Any | None = Field(default=None)
    relay_session_id: str | None = Field(default=None, min_length=1)


class TalkClientToolCallResult(_SchemaModel):
    run_id: str = Field(min_length=1)
    idempotency_key: str = Field(min_length=1)


class TalkClientTranscriptParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    voice_session_id: str = Field(pattern="^[A-Za-z0-9_-]{1,128}$")
    entry_id: str = Field(pattern="^[A-Za-z0-9_-]{1,128}$")
    role: SessionsSearchHitRole
    text: str = Field(min_length=1)
    timestamp: float | None = Field(default=None)


class TalkConfigParams(_SchemaModel):
    include_secrets: bool | None = Field(default=None)


class TalkConfigResult(_SchemaModel):
    config: dict[str, Any]


class TalkSessionAppendAudioParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    audio_base64: str = Field(min_length=1)
    timestamp: float | None = Field(default=None)


class TalkSessionAcknowledgeMarkParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    mark_name: str = Field(min_length=1)


class TalkSessionCancelOutputParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    turn_id: str | None = Field(default=None)
    reason: str | None = Field(default=None)


class TalkSessionCancelTurnParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    turn_id: str | None = Field(default=None)
    reason: str | None = Field(default=None)


class TalkSessionCreateParams(_SchemaModel):
    session_key: str | None = Field(default=None)
    spawned_by: str | None = Field(default=None, min_length=1)
    provider: str | None = Field(default=None)
    model: str | None = Field(default=None)
    voice: str | None = Field(default=None)
    language: str | None = Field(default=None, pattern="^[a-z]{2}$")
    vad_threshold: float | None = Field(default=None)
    silence_duration_ms: int | None = Field(default=None, ge=1)
    prefix_padding_ms: int | None = Field(default=None, ge=0)
    reasoning_effort: str | None = Field(default=None)
    mode: TalkEventMode | None = Field(default=None)
    transport: TalkEventTransport | None = Field(default=None)
    brain: TalkEventBrain | None = Field(default=None)
    ttl_ms: int | None = Field(default=None, ge=1000, le=3600000)


class TalkSessionCreateResult(_SchemaModel):
    session_id: str = Field(min_length=1)
    provider: str | None = Field(default=None)
    mode: TalkEventMode
    transport: TalkEventTransport
    brain: TalkEventBrain
    relay_session_id: str | None = Field(default=None, min_length=1)
    transcription_session_id: str | None = Field(default=None, min_length=1)
    handoff_id: str | None = Field(default=None, min_length=1)
    room_id: str | None = Field(default=None, min_length=1)
    room_url: str | None = Field(default=None, min_length=1)
    token: str | None = Field(default=None, min_length=1)
    audio: Any | None = Field(default=None)
    model: str | None = Field(default=None)
    voice: str | None = Field(default=None)
    expires_at: float | None = Field(default=None)


class TalkSessionJoinParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    token: str = Field(min_length=1)


class TalkSessionTurnParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    turn_id: str | None = Field(default=None)


class TalkSessionSteerParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    text: str = Field(min_length=1)
    mode: TalkClientSteerMode | None = Field(default=None)


class TalkSessionSubmitToolResultParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    call_id: str = Field(min_length=1)
    result: Any
    options: dict[str, Any] | None = Field(default=None)


class TalkSessionCloseParams(_SchemaModel):
    session_id: str = Field(min_length=1)


class TalkSessionOkResult(_SchemaModel):
    ok: bool


class TalkSpeakParams(_SchemaModel):
    text: str = Field(min_length=1)
    voice_id: str | None = Field(default=None)
    model_id: str | None = Field(default=None)
    output_format: str | None = Field(default=None)
    speed: float | None = Field(default=None)
    rate_wpm: int | None = Field(default=None, ge=1)
    stability: float | None = Field(default=None)
    similarity: float | None = Field(default=None)
    style: float | None = Field(default=None)
    speaker_boost: bool | None = Field(default=None)
    seed: int | None = Field(default=None, ge=0)
    normalize: str | None = Field(default=None)
    language: str | None = Field(default=None)
    latency_tier: int | None = Field(default=None, ge=0)


class TalkSpeakResult(_SchemaModel):
    audio_base64: str = Field(min_length=1)
    provider: str = Field(min_length=1)
    output_format: str | None = Field(default=None)
    voice_compatible: bool | None = Field(default=None)
    mime_type: str | None = Field(default=None)
    file_extension: str | None = Field(default=None)


class TtsSpeakParams(_SchemaModel):
    text: str = Field(min_length=1)


class TtsSpeakResult(_SchemaModel):
    audio_base64: str = Field(min_length=1)
    provider: str = Field(min_length=1)
    output_format: str | None = Field(default=None)
    mime_type: str | None = Field(default=None)
    file_extension: str | None = Field(default=None)


class ChannelsStatusParams(_SchemaModel):
    probe: bool | None = Field(default=None)
    timeout_ms: int | None = Field(default=None, ge=0)
    channel: str | None = Field(default=None, min_length=1)


class ChannelsStatusResult(_SchemaModel):
    ts: int = Field(ge=0)
    channel_order: list[str]
    channel_labels: dict[str, Any]
    channel_detail_labels: dict[str, Any] | None = Field(default=None)
    channel_system_images: dict[str, Any] | None = Field(default=None)
    channel_meta: list[dict[str, Any]] | None = Field(default=None)
    channels: dict[str, Any]
    channel_accounts: dict[str, Any]
    channel_default_account_id: dict[str, Any]
    event_loop: dict[str, Any] | None = Field(default=None)
    partial: bool | None = Field(default=None)
    warnings: list[str] | None = Field(default=None)


class ChannelsPairingListParams(_SchemaModel):
    channel: str | None = Field(default=None, min_length=1)
    account_id: str | None = Field(default=None, min_length=1)


class ChannelsPairingListResult(_SchemaModel):
    accounts: list[dict[str, Any]]
    requests: list[dict[str, Any]]
    command_owner_configured: bool
    limits: dict[str, Any]


class ChannelsPairingApproveParams(_SchemaModel):
    channel: str = Field(min_length=1)
    account_id: str = Field(min_length=1)
    request_id: str = Field(min_length=1)
    notify: bool | None = Field(default=None)
    bootstrap_command_owner: bool | None = Field(default=None)


class ChannelsPairingApproveResult(_SchemaModel):
    request_id: str = Field(min_length=1)
    sender_id: str = Field(min_length=1)
    notification: ChannelsPairingApproveNotification
    command_owner_bootstrap: ChannelsPairingApproveCommandOwnerBootstrap


class ChannelsPairingDismissParams(_SchemaModel):
    channel: str = Field(min_length=1)
    account_id: str = Field(min_length=1)
    request_id: str = Field(min_length=1)


class ChannelsPairingDismissResult(_SchemaModel):
    request_id: str = Field(min_length=1)
    sender_id: str = Field(min_length=1)


class ChannelsStartParams(_SchemaModel):
    channel: str = Field(min_length=1)
    account_id: str | None = Field(default=None)


class ChannelsStopParams(_SchemaModel):
    channel: str = Field(min_length=1)
    account_id: str | None = Field(default=None)


class ChannelsLogoutParams(_SchemaModel):
    channel: str = Field(min_length=1)
    account_id: str | None = Field(default=None)


class WebLoginStartParams(_SchemaModel):
    force: bool | None = Field(default=None)
    timeout_ms: int | None = Field(default=None, ge=0)
    verbose: bool | None = Field(default=None)
    account_id: str | None = Field(default=None)


class WebLoginWaitParams(_SchemaModel):
    timeout_ms: int | None = Field(default=None, ge=0)
    account_id: str | None = Field(default=None)
    current_qr_data_url: str | None = Field(default=None, max_length=16384, pattern="^data:image/png;base64,")


class AgentsCreateParams(_SchemaModel):
    name: str = Field(min_length=1)
    workspace: str | None = Field(default=None, min_length=1)
    model: str | None = Field(default=None, min_length=1)
    emoji: str | None = Field(default=None)
    avatar: str | None = Field(default=None)


class AgentsCreateResult(_SchemaModel):
    ok: Literal[True]
    agent_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    workspace: str = Field(min_length=1)
    model: str | None = Field(default=None, min_length=1)


class AgentsUpdateParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    name: str | None = Field(default=None, min_length=1)
    workspace: str | None = Field(default=None, min_length=1)
    model: str | None = Field(default=None)
    emoji: str | None = Field(default=None)
    avatar: str | None = Field(default=None)


class AgentsUpdateResult(_SchemaModel):
    ok: Literal[True]
    agent_id: str = Field(min_length=1)


class AgentsDeleteParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    delete_files: bool | None = Field(default=None)


class AgentsDeleteResult(_SchemaModel):
    ok: Literal[True]
    agent_id: str = Field(min_length=1)
    removed_bindings: int = Field(ge=0)
    removed: list[dict[str, Any]] | None = Field(default=None)
    failed: list[dict[str, Any]] | None = Field(default=None)


class AgentsFileEntry(_SchemaModel):
    name: str = Field(min_length=1)
    path: str = Field(min_length=1)
    missing: bool
    expected_absent: bool | None = Field(default=None)
    size: int | None = Field(default=None, ge=0)
    updated_at_ms: int | None = Field(default=None, ge=0)
    content: str | None = Field(default=None)


class AgentsFilesListParams(_SchemaModel):
    agent_id: str = Field(min_length=1)


class AgentsFilesGetParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    name: str = Field(min_length=1)


class AgentsFilesSetParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    content: str


class AgentsWorkspaceEntry(_SchemaModel):
    path: str = Field(min_length=1)
    name: str = Field(min_length=1)
    kind: SessionFileBrowserEntryKind
    size: int | None = Field(default=None, ge=0)
    updated_at_ms: int | None = Field(default=None, ge=0)


class AgentsWorkspaceFile(_SchemaModel):
    path: str = Field(min_length=1)
    name: str = Field(min_length=1)
    size: int = Field(ge=0)
    updated_at_ms: int = Field(ge=0)
    mime_type: str = Field(min_length=1)
    encoding: SessionFileEntryContentEncoding
    content: str


class AgentsWorkspaceListParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    path: str | None = Field(default=None)
    offset: int | None = Field(default=None, ge=0)
    limit: int | None = Field(default=None, ge=1)


class AgentsWorkspaceGetParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    path: str = Field(min_length=1)


class ArtifactSummary(_SchemaModel):
    id: str = Field(min_length=1)
    type: str = Field(min_length=1)
    title: str = Field(min_length=1)
    mime_type: str | None = Field(default=None, min_length=1)
    size_bytes: int | None = Field(default=None, ge=0)
    session_key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    task_id: str | None = Field(default=None, min_length=1)
    message_seq: int | None = Field(default=None, ge=1)
    source: str | None = Field(default=None, min_length=1)
    download: dict[str, Any]


class ArtifactsListParams(_SchemaModel):
    session_key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    task_id: str | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)


class ArtifactsGetParams(_SchemaModel):
    session_key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    task_id: str | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    artifact_id: str = Field(min_length=1)


class ArtifactsDownloadParams(_SchemaModel):
    session_key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    task_id: str | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    artifact_id: str = Field(min_length=1)


class AgentsListParams(_SchemaModel):
    pass


class ModelChoice(_SchemaModel):
    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    provider: str = Field(min_length=1)
    alias: str | None = Field(default=None, min_length=1)
    available: bool | None = Field(default=None)
    context_window: int | None = Field(default=None, ge=1)
    reasoning: bool | None = Field(default=None)
    agent_runtime: dict[str, Any] | None = Field(default=None)
    api_key_supported: bool | None = Field(default=None)
    input: list[Literal["text", "image", "audio", "video", "document"]] | None = Field(default=None)


class ModelsAuthLogoutParams(_SchemaModel):
    provider: str = Field(min_length=1)
    profile_ids: list[str] | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None)


class ModelsAuthStatusParams(_SchemaModel):
    refresh: bool | None = Field(default=None)
    agent_id: str | None = Field(default=None)


class ModelsListParams(_SchemaModel):
    include_provider_capabilities: bool | None = Field(default=None)
    view: ModelsListView | None = Field(default=None)


class ModelsProbeParams(_SchemaModel):
    provider: str = Field(min_length=1)
    profile_id: str | None = Field(default=None, min_length=1)
    timeout_ms: int | None = Field(default=None, ge=1)
    agent_id: str | None = Field(default=None)


class CommandEntry(_SchemaModel):
    name: str = Field(min_length=1, max_length=200)
    native_name: str | None = Field(default=None, min_length=1, max_length=200)
    text_aliases: list[str] | None = Field(default=None, max_length=20)
    description: str = Field(max_length=2000)
    category: CommandEntryCategory | None = Field(default=None)
    source: CommandEntrySource
    skill_model_visible: bool | None = Field(default=None)
    scope: CommandEntryScope
    accepts_args: bool
    args: list[dict[str, Any]] | None = Field(default=None, max_length=20)


class CommandsListParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    provider: str | None = Field(default=None, min_length=1)
    scope: CommandEntryScope | None = Field(default=None)
    include_args: bool | None = Field(default=None)


class SkillsStatusParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)


class ToolsCatalogParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    include_plugins: bool | None = Field(default=None)


class ToolCatalogProfile(_SchemaModel):
    id: ToolCatalogProfileId
    label: str = Field(min_length=1)


class ToolCatalogEntry(_SchemaModel):
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    description: str
    source: ToolCatalogEntrySource
    plugin_id: str | None = Field(default=None, min_length=1)
    optional: bool | None = Field(default=None)
    risk: ToolCatalogEntryRisk | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    default_profiles: list[ToolCatalogProfileId]


class ToolsEffectiveParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    session_key: str = Field(min_length=1)


class ToolsEffectiveEntry(_SchemaModel):
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    description: str
    raw_description: str
    source: ToolsEffectiveEntrySource
    plugin_id: str | None = Field(default=None, min_length=1)
    channel_id: str | None = Field(default=None, min_length=1)
    mcp_server: str | None = Field(default=None, min_length=1)
    mcp_tool_name: str | None = Field(default=None, min_length=1)
    denied_by_session: Literal[True] | None = Field(default=None)
    risk: ToolCatalogEntryRisk | None = Field(default=None)
    tags: list[str] | None = Field(default=None)


class ToolsEffectiveNotice(_SchemaModel):
    id: str = Field(min_length=1)
    severity: ToolsEffectiveNoticeSeverity
    message: str
    servers: list[str] | None = Field(default=None)


class ToolsInvokeParams(_SchemaModel):
    name: str = Field(min_length=1)
    args: dict[str, Any] | None = Field(default=None)
    session_key: str | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    confirm: bool | None = Field(default=None)
    idempotency_key: str | None = Field(default=None, min_length=1)
    conversation_read_origin: Literal["direct-operator"] | None = Field(default=None)


class ToolsInvokeError(_SchemaModel):
    code: str = Field(min_length=1)
    message: str = Field(min_length=1)
    details: Any | None = Field(default=None)


class SkillsBinsParams(_SchemaModel):
    pass


class SkillsBinsResult(_SchemaModel):
    bins: list[str]


class SkillsSearchParams(_SchemaModel):
    query: str | None = Field(default=None, min_length=1)
    limit: int | None = Field(default=None, ge=1, le=100)


class SkillsSearchResult(_SchemaModel):
    results: list[dict[str, Any]]


class SkillsDetailParams(_SchemaModel):
    slug: str = Field(min_length=1)


class SkillsDetailResult(_SchemaModel):
    skill: dict[str, Any] | None
    latest_version: dict[str, Any] | None = Field(default=None)
    metadata: dict[str, Any] | None = Field(default=None)
    owner: dict[str, Any] | None = Field(default=None)


class SkillsCuratorActionParams(_SchemaModel):
    skill: str = Field(min_length=1)


class SkillsCuratorActionResult(_SchemaModel):
    skill_file: str = Field(min_length=1)
    skill_key: str = Field(min_length=1)
    skill_name: str = Field(min_length=1)
    state: SkillsCuratorActionState
    pinned: bool
    created_at_ms: float
    state_changed_at_ms: float
    last_used_at_ms: float | None
    use_count: float
    archived_reason: str | None


class SkillsCuratorStatusParams(_SchemaModel):
    pass


class SkillsProposalsListParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)


class SkillsProposalsListResult(_SchemaModel):
    schema_: Literal["openclaw.skill-workshop.proposals-manifest.v1"] = Field(alias="schema")
    updated_at: str = Field(min_length=1)
    proposals: list[dict[str, Any]]


class SkillsProposalEvaluateParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    proposal_id: str = Field(min_length=1)
    expected_revision_hash: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-fA-F0-9]{64}$")
    correlation_id: str | None = Field(default=None, min_length=1, max_length=256)


class SkillsProposalEventsListParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    proposal_id: str | None = Field(default=None, min_length=1)
    after_sequence: int | None = Field(default=None, ge=0)
    limit: int | None = Field(default=None, ge=1, le=200)


class SkillsProposalEventsListResult(_SchemaModel):
    events: list[dict[str, Any]] = Field(max_length=200)
    next_sequence: int | None = Field(default=None, ge=1)


class SkillsProposalHistoryStatusParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)


class SkillsProposalHistoryScanParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    direction: SkillsProposalHistoryScanDirection | None = Field(default=None)


class SkillsProposalHistoryScanResult(_SchemaModel):
    schema_: Literal["openclaw.skill-workshop.history-scan.v1"] = Field(alias="schema")
    has_scanned: bool
    reviewed_sessions: int = Field(ge=0)
    ideas_found: int = Field(ge=0)
    has_more: bool
    last_scan_reviewed: int = Field(ge=0)
    last_scan_ideas: int = Field(ge=0)
    last_scan_at: str | None = Field(default=None, min_length=1)
    oldest_reviewed_at: str | None = Field(default=None, min_length=1)
    newest_reviewed_at: str | None = Field(default=None, min_length=1)


class SkillsProposalInspectParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    proposal_id: str = Field(min_length=1)


class SkillsProposalCreateParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    content: str = Field(min_length=1, max_length=1048576)
    support_files: list[dict[str, Any]] | None = Field(default=None, max_length=64)
    goal: str | None = Field(default=None)
    evidence: str | None = Field(default=None)


class SkillsProposalUpdateParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    skill_name: str = Field(min_length=1)
    description: str | None = Field(default=None, min_length=1)
    content: str = Field(min_length=1, max_length=1048576)
    support_files: list[dict[str, Any]] | None = Field(default=None, max_length=64)
    goal: str | None = Field(default=None)
    evidence: str | None = Field(default=None)


class SkillsProposalReviseParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    proposal_id: str = Field(min_length=1)
    expected_revision_hash: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-fA-F0-9]{64}$")
    correlation_id: str | None = Field(default=None, min_length=1, max_length=256)
    content: str | None = Field(default=None, min_length=1, max_length=1048576)
    support_files: list[dict[str, Any]] | None = Field(default=None, max_length=64)
    description: str | None = Field(default=None, min_length=1)
    goal: str | None = Field(default=None)
    evidence: str | None = Field(default=None)


class SkillsProposalRequestRevisionParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    target_agent_id: str | None = Field(default=None, min_length=1)
    proposal_id: str = Field(min_length=1)
    expected_revision_hash: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-fA-F0-9]{64}$")
    instructions: str = Field(min_length=1, max_length=32768)
    session_key: str = Field(min_length=1)
    session_id: str | None = Field(default=None, min_length=1)
    idempotency_key: str = Field(min_length=1)


class SkillsProposalRequestRevisionResult(_SchemaModel):
    run_id: str = Field(min_length=1)
    status: SkillsProposalRequestRevisionStatus


class SkillsProposalActionParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    proposal_id: str = Field(min_length=1)
    expected_revision_hash: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-fA-F0-9]{64}$")
    correlation_id: str | None = Field(default=None, min_length=1, max_length=256)
    reason: str | None = Field(default=None)


class SkillsProposalRecordResult(_SchemaModel):
    schema_: Literal["openclaw.skill-workshop.proposal.v1"] = Field(alias="schema")
    id: str = Field(min_length=1)
    kind: SkillsProposalRecordKind
    status: SkillsProposalRecordStatus
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    created_at: str = Field(min_length=1)
    updated_at: str = Field(min_length=1)
    created_by: SkillsProposalRecordCreatedBy
    origin: dict[str, Any] | None = Field(default=None)
    proposed_version: str = Field(min_length=1)
    draft_file: Literal["PROPOSAL.md"]
    draft_hash: str = Field(min_length=1)
    support_files: list[dict[str, Any]] | None = Field(default=None, max_length=64)
    target: dict[str, Any]
    scan: dict[str, Any]
    goal: str | None = Field(default=None)
    evidence: str | None = Field(default=None)
    applied_at: str | None = Field(default=None, min_length=1)
    rejected_at: str | None = Field(default=None, min_length=1)
    quarantined_at: str | None = Field(default=None, min_length=1)
    stale_at: str | None = Field(default=None, min_length=1)
    status_reason: str | None = Field(default=None)
    evaluation: dict[str, Any] | None = Field(default=None)


class SkillsSecurityVerdictsParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)


class SkillsSecurityVerdictsResult(_SchemaModel):
    schema_: Literal["openclaw.skills.security-verdicts.v1"] = Field(alias="schema")
    items: list[dict[str, Any]]


class SkillsSkillCardParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    skill_key: str = Field(min_length=1)


class SkillsSkillCardResult(_SchemaModel):
    schema_: Literal["openclaw.skills.skill-card.v1"] = Field(alias="schema")
    skill_key: str = Field(min_length=1)
    path: str = Field(min_length=1)
    size_bytes: int = Field(ge=0)
    content: str


class SkillsUploadBeginParams(_SchemaModel):
    kind: Literal["skill-archive"]
    slug: str = Field(min_length=1)
    size_bytes: int = Field(ge=1)
    sha256: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-fA-F0-9]{64}$")
    force: bool | None = Field(default=None)
    idempotency_key: str | None = Field(default=None, min_length=1, max_length=2048)


class SkillsUploadChunkParams(_SchemaModel):
    upload_id: str = Field(min_length=1)
    offset: int = Field(ge=0)
    data_base64: str = Field(min_length=1, max_length=5592408)


class SkillsUploadCommitParams(_SchemaModel):
    upload_id: str = Field(min_length=1)
    sha256: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-fA-F0-9]{64}$")


class CronJob(_SchemaModel):
    id: str = Field(min_length=1)
    declaration_key: str | None = Field(default=None, min_length=1, max_length=200, pattern="\\S")
    display_name: str | None = Field(default=None, min_length=1, max_length=200, pattern="\\S")
    owner: dict[str, Any] | None = Field(default=None)
    scheduled_tool_policy: dict[str, Any] | None = Field(default=None)
    agent_id: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    name: str = Field(min_length=1)
    description: str | None = Field(default=None)
    enabled: bool
    delete_after_run: bool | None = Field(default=None)
    created_at_ms: int = Field(ge=0)
    updated_at_ms: int = Field(ge=0)
    config_revision: str | None = Field(default=None, min_length=1, max_length=128)
    schedule: dict[str, Any]
    pacing: dict[str, Any] | None = Field(default=None)
    trigger: dict[str, Any] | None = Field(default=None)
    session_target: str | Literal["main", "isolated", "current"]
    wake_mode: CronJobWakeMode
    payload: dict[str, Any]
    delivery: dict[str, Any] | None = Field(default=None)
    failure_alert: dict[str, Any] | Literal[False] | None = Field(default=None)
    state: dict[str, Any]
    next_run_at_ms: int | None = Field(default=None, ge=0)
    last_run_at_ms: int | None = Field(default=None, ge=0)
    last_run_status: CronJobLastRunStatus | None = Field(default=None)
    last_run_error: str | None = Field(default=None)
    last_delivered: bool | None = Field(default=None)
    last_delivery_status: CronJobLastDeliveryStatus | None = Field(default=None)
    last_delivery_error: str | None = Field(default=None)
    last_failure_notification_delivered: bool | None = Field(default=None)
    last_failure_notification_delivery_status: CronJobLastDeliveryStatus | None = Field(default=None)
    last_failure_notification_delivery_error: str | None = Field(default=None)


class CronListParams(_SchemaModel):
    include_disabled: bool | None = Field(default=None)
    limit: int | None = Field(default=None, ge=1, le=200)
    offset: int | None = Field(default=None, ge=0)
    query: str | None = Field(default=None)
    enabled: CronListEnabled | None = Field(default=None)
    schedule_kind: CronListScheduleKind | None = Field(default=None)
    last_run_status: CronListLastRunStatus | None = Field(default=None)
    sort_by: CronListSortBy | None = Field(default=None)
    sort_dir: CronListSortDir | None = Field(default=None)
    agent_id: str | None = Field(default=None, min_length=1)
    compact: bool | None = Field(default=None)
    include_delivery_previews: bool | None = Field(default=None)


class CronStatusParams(_SchemaModel):
    pass


class CronAddParams(_SchemaModel):
    name: str = Field(min_length=1)
    declaration_key: str | None = Field(default=None, min_length=1, max_length=200, pattern="\\S")
    display_name: str | None = Field(default=None, min_length=1, max_length=200, pattern="\\S")
    owner: dict[str, Any] | None = Field(default=None)
    agent_id: str | None = Field(default=None)
    session_key: str | None = Field(default=None)
    description: str | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    delete_after_run: bool | None = Field(default=None)
    schedule: dict[str, Any]
    pacing: dict[str, Any] | None = Field(default=None)
    trigger: dict[str, Any] | None = Field(default=None)
    session_target: str | Literal["main", "isolated", "current"]
    wake_mode: CronJobWakeMode
    payload: dict[str, Any]
    delivery: dict[str, Any] | None = Field(default=None)
    failure_alert: dict[str, Any] | Literal[False] | None = Field(default=None)


class CronRunsParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    scope: CronRunsScope | None = Field(default=None)
    id: str | None = Field(default=None, min_length=1, pattern="^[^/\\\\]+$")
    job_id: str | None = Field(default=None, min_length=1, pattern="^[^/\\\\]+$")
    run_id: str | None = Field(default=None, min_length=1)
    limit: int | None = Field(default=None, ge=1, le=200)
    offset: int | None = Field(default=None, ge=0)
    statuses: list[CronJobLastRunStatus] | None = Field(default=None, min_length=1, max_length=3)
    status: CronRunsStatus | None = Field(default=None)
    delivery_statuses: list[CronJobLastDeliveryStatus] | None = Field(default=None, min_length=1, max_length=4)
    delivery_status: CronJobLastDeliveryStatus | None = Field(default=None)
    query: str | None = Field(default=None)
    sort_dir: CronListSortDir | None = Field(default=None)


class CronScratchGetResult(_SchemaModel):
    scratch: dict[str, Any] | None
    current_revision: int = Field(ge=0)
    max_bytes: int = Field(ge=1)


class CronRunLogEntry(_SchemaModel):
    ts: int = Field(ge=0)
    job_id: str = Field(min_length=1)
    action: Literal["finished"]
    status: CronJobLastRunStatus | None = Field(default=None)
    error: str | None = Field(default=None)
    error_reason: CronRunLogEntryErrorReason | None = Field(default=None)
    summary: str | None = Field(default=None)
    diagnostics: dict[str, Any] | None = Field(default=None)
    delivered: bool | None = Field(default=None)
    delivery_status: CronJobLastDeliveryStatus | None = Field(default=None)
    delivery_error: str | None = Field(default=None)
    failure_notification_delivery: dict[str, Any] | None = Field(default=None)
    session_id: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    run_at_ms: int | None = Field(default=None, ge=0)
    duration_ms: int | None = Field(default=None, ge=0)
    next_run_at_ms: int | None = Field(default=None, ge=0)
    trigger_fired: bool | None = Field(default=None)
    model: str | None = Field(default=None)
    provider: str | None = Field(default=None)
    usage: dict[str, Any] | None = Field(default=None)
    job_name: str | None = Field(default=None)


class LogsTailParams(_SchemaModel):
    cursor: int | None = Field(default=None, ge=0)
    limit: int | None = Field(default=None, ge=1, le=5000)
    max_bytes: int | None = Field(default=None, ge=1, le=1000000)


class LogsTailResult(_SchemaModel):
    file: str = Field(min_length=1)
    cursor: int = Field(ge=0)
    size: int = Field(ge=0)
    lines: list[str]
    truncated: bool | None = Field(default=None)
    reset: bool | None = Field(default=None)


class MemoryMigrationSummary(_SchemaModel):
    total: int = Field(ge=0)
    planned: int = Field(ge=0)
    migrated: int = Field(ge=0)
    skipped: int = Field(ge=0)
    conflicts: int = Field(ge=0)
    errors: int = Field(ge=0)
    sensitive: int = Field(ge=0)


class MigrationsMemoryPlanParams(_SchemaModel):
    agent_id: str = Field(min_length=1)
    overwrite: bool | None = Field(default=None)


class MigrationsMemoryApplyParams(_SchemaModel):
    idempotency_key: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    provider_id: str = Field(min_length=1)
    plan_fingerprint: str = Field(min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    item_ids: list[str] = Field(min_length=1, max_length=2000)
    overwrite: bool | None = Field(default=None)


class TerminalOpenResult(_SchemaModel):
    session_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    shell: str = Field(min_length=1)
    cwd: str = Field(min_length=1)
    confined: bool
    title: str | None = Field(default=None, min_length=1)


class TerminalInputParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    data: str


class TerminalResizeParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    cols: int = Field(ge=1, le=2000)
    rows: int = Field(ge=1, le=2000)


class TerminalCloseParams(_SchemaModel):
    session_id: str = Field(min_length=1)


class TerminalAttachParams(_SchemaModel):
    session_id: str = Field(min_length=1)


class TerminalAttachResult(_SchemaModel):
    session_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    shell: str = Field(min_length=1)
    cwd: str = Field(min_length=1)
    confined: bool
    buffer: str
    seq: int | None = Field(default=None, ge=0)


class TerminalSessionInfo(_SchemaModel):
    session_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    shell: str = Field(min_length=1)
    cwd: str = Field(min_length=1)
    confined: bool
    attached: bool
    owner: str | Literal["conn"] | None = Field(default=None)
    created_at_ms: int = Field(ge=0)


class TerminalTextParams(_SchemaModel):
    session_id: str = Field(min_length=1)


class TerminalTextResult(_SchemaModel):
    text: str


class TerminalUploadParams(_SchemaModel):
    session_id: str = Field(min_length=1)
    name: str = Field(min_length=1, max_length=255)
    content_base64: str = Field(max_length=22369624)


class TerminalUploadResult(_SchemaModel):
    path: str = Field(min_length=1)
    size: int = Field(ge=0, le=16777216)


class TerminalAckResult(_SchemaModel):
    ok: bool


class TerminalDataEvent(_SchemaModel):
    session_id: str = Field(min_length=1)
    seq: int = Field(ge=0)
    data: str


class TerminalExitEvent(_SchemaModel):
    session_id: str = Field(min_length=1)
    exit_code: int | None = Field(default=None)
    signal: int | None = Field(default=None)
    reason: TerminalExitEventReason | None = Field(default=None)
    error: str | None = Field(default=None)


class SystemAgentApprovalPresentation(_SchemaModel):
    kind: Literal["system-agent"]
    title: str = Field(min_length=1, max_length=80)
    description: str = Field(min_length=1, max_length=512)
    proposal_hash: str = Field(pattern="^[a-f0-9]{64}$")
    agent_id: str | None = Field(default=None)
    allowed_decisions: list[Literal["allow-once", "deny"]] = Field(min_length=2)


class ApprovalGetParams(_SchemaModel):
    id: str = Field(min_length=1, pattern="^(?!\\.{1,2}$)(?:[^\\uD800-\\uDFFF]|[\\uD800-\\uDBFF][\\uDC00-\\uDFFF])+$")


class ExecApprovalsGetParams(_SchemaModel):
    pass


class ExecApprovalsSetParams(_SchemaModel):
    file: dict[str, Any]
    base_hash: str | None = Field(default=None, min_length=1)


class ExecApprovalsNodeGetParams(_SchemaModel):
    node_id: str = Field(min_length=1)


class ExecApprovalsNodeSnapshot(_SchemaModel):
    path: str | None = Field(default=None)
    exists: bool | None = Field(default=None)
    hash: str | None = Field(default=None)
    file: dict[str, Any] | None = Field(default=None)
    resolved_defaults: dict[str, Any] | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    base_hash: str | None = Field(default=None, min_length=1)
    default_action: ExecApprovalsNodeSnapshotDefaultAction | None = Field(default=None)
    rules: list[dict[str, Any]] | None = Field(default=None)
    constraints: dict[str, Any] | None = Field(default=None)
    message: str | None = Field(default=None)


class ExecApprovalsNodeSetParams(_SchemaModel):
    node_id: str = Field(min_length=1)
    file: dict[str, Any] | None = Field(default=None)
    native: dict[str, Any] | None = Field(default=None)
    base_hash: str | None = Field(default=None, min_length=1)


class ExecApprovalsSnapshot(_SchemaModel):
    path: str = Field(min_length=1)
    exists: bool
    hash: str = Field(min_length=1)
    file: dict[str, Any]


class ExecApprovalGetParams(_SchemaModel):
    id: str = Field(min_length=1)


class ExecApprovalRequestParams(_SchemaModel):
    id: str | None = Field(default=None, min_length=1)
    command: str | None = Field(default=None, min_length=1)
    command_argv: list[str] | None = Field(default=None)
    system_run_plan: dict[str, Any] | None = Field(default=None)
    env: dict[str, Any] | None = Field(default=None)
    cwd: str | None = Field(default=None)
    node_id: str | None = Field(default=None)
    host: str | None = Field(default=None)
    security: str | None = Field(default=None)
    ask: str | None = Field(default=None)
    warning_text: str | None = Field(default=None)
    unavailable_decisions: list[Literal["allow-always"]] | None = Field(default=None, min_length=1, max_length=1)
    command_spans: list[dict[str, Any]] | None = Field(default=None)
    agent_id: str | None = Field(default=None)
    resolved_path: str | None = Field(default=None)
    session_key: str | None = Field(default=None)
    session_id: str | None = Field(default=None)
    run_id: str | None = Field(default=None)
    tool_call_id: str | None = Field(default=None)
    turn_source_channel: str | None = Field(default=None)
    turn_source_to: str | None = Field(default=None)
    turn_source_account_id: str | None = Field(default=None)
    turn_source_thread_id: str | float | None = Field(default=None)
    approval_reviewer_device_ids: list[str] | None = Field(default=None)
    require_delivery_route: bool | None = Field(default=None)
    suppress_delivery: bool | None = Field(default=None)
    timeout_ms: int | None = Field(default=None, ge=1)
    two_phase: bool | None = Field(default=None)


class ExecApprovalResolveParams(_SchemaModel):
    id: str = Field(min_length=1)
    decision: str = Field(min_length=1)


class QuestionOption(_SchemaModel):
    label: str = Field(min_length=1)
    description: str | None = Field(default=None)


class QuestionAnswers(_SchemaModel):
    answers: dict[str, Any]


class QuestionRequestResult(_SchemaModel):
    id: str = Field(min_length=1)
    expires_at_ms: int = Field(ge=0)


class QuestionWaitAnswerParams(_SchemaModel):
    id: str = Field(min_length=1)
    timeout_ms: int | None = Field(default=None, ge=1)


class QuestionGetParams(_SchemaModel):
    id: str = Field(min_length=1)


class QuestionListParams(_SchemaModel):
    pass


class PluginApprovalRequestParams(_SchemaModel):
    plugin_id: str | None = Field(default=None, min_length=1)
    title: str = Field(min_length=1, max_length=80)
    description: str = Field(min_length=1, max_length=512)
    detail: str | None = Field(default=None, min_length=1, max_length=16384)
    severity: PluginApprovalRequestSeverity | None = Field(default=None)
    tool_name: str | None = Field(default=None)
    tool_call_id: str | None = Field(default=None)
    allowed_decisions: list[Literal["allow-once", "allow-always", "deny"]] | None = Field(
        default=None, min_length=1, max_length=3
    )
    agent_id: str | None = Field(default=None)
    session_key: str | None = Field(default=None)
    approval_reviewer_device_ids: list[str] | None = Field(default=None)
    turn_source_channel: str | None = Field(default=None)
    turn_source_to: str | None = Field(default=None)
    turn_source_account_id: str | None = Field(default=None)
    turn_source_thread_id: str | float | None = Field(default=None)
    timeout_ms: int | None = Field(default=None, ge=1, le=600000)
    two_phase: bool | None = Field(default=None)


class PluginApprovalResolveParams(_SchemaModel):
    id: str = Field(min_length=1)
    decision: str = Field(min_length=1)


class PluginCatalogClawHubInstall(_SchemaModel):
    source: Literal["clawhub"]
    package_name: str = Field(min_length=1)


class PluginCatalogOfficialInstall(_SchemaModel):
    source: Literal["official"]
    plugin_id: str = Field(min_length=1)


class PluginControlUiDescriptor(_SchemaModel):
    id: str = Field(min_length=1)
    plugin_id: str = Field(min_length=1)
    plugin_name: str | None = Field(default=None, min_length=1)
    surface: PluginControlUiDescriptorSurface
    label: str = Field(min_length=1)
    description: str | None = Field(default=None)
    placement: str | None = Field(default=None)
    schema_: Any | None = Field(default=None, alias="schema")
    required_scopes: list[str] | None = Field(default=None)


class PluginSearchPackage(_SchemaModel):
    name: str = Field(min_length=1)
    display_name: str = Field(min_length=1)
    family: PluginSearchPackageFamily
    channel: PluginSearchPackageChannel
    is_official: bool
    summary: str | None = Field(default=None)
    latest_version: str | None = Field(default=None, min_length=1)
    runtime_id: str | None = Field(default=None, min_length=1)
    downloads: float | None = Field(default=None, ge=0)
    verification_tier: str | None = Field(default=None, min_length=1)


class PluginsListParams(_SchemaModel):
    pass


class PluginsRefreshParams(_SchemaModel):
    pass


class PluginsRefreshResult(_SchemaModel):
    ok: Literal[True]


class PluginsSearchParams(_SchemaModel):
    query: str = Field(min_length=1)
    limit: int | None = Field(default=None, ge=1, le=100)


class PluginsSessionActionFailureResult(_SchemaModel):
    ok: Literal[False]
    error: str
    code: str | None = Field(default=None)
    details: Any | None = Field(default=None)


class PluginsSessionActionParams(_SchemaModel):
    plugin_id: str = Field(min_length=1)
    action_id: str = Field(min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    payload: Any | None = Field(default=None)


class PluginsSessionActionSuccessResult(_SchemaModel):
    ok: Literal[True]
    result: Any | None = Field(default=None)
    continue_agent: bool | None = Field(default=None)
    reply: Any | None = Field(default=None)


class PluginsSetEnabledParams(_SchemaModel):
    plugin_id: str = Field(min_length=1)
    enabled: bool


class PluginsUiDescriptorsParams(_SchemaModel):
    pass


class PluginsUninstallParams(_SchemaModel):
    plugin_id: str = Field(min_length=1)


class PluginsUninstallResult(_SchemaModel):
    ok: Literal[True]
    plugin_id: str = Field(min_length=1)
    restart_required: Literal[True]
    removed: list[str]
    warnings: list[str] | None = Field(default=None)


class DevicePairListParams(_SchemaModel):
    pass


class DevicePairApproveParams(_SchemaModel):
    request_id: str = Field(min_length=1)


class DevicePairRejectParams(_SchemaModel):
    request_id: str = Field(min_length=1)


class DevicePairRemoveParams(_SchemaModel):
    device_id: str = Field(min_length=1)


class DevicePairSetupCodeParams(_SchemaModel):
    public_url: str | None = Field(default=None, min_length=1)
    prefer_remote_url: bool | None = Field(default=None)
    include_qr: bool | None = Field(default=None)
    bootstrap_profile: DevicePairSetupCodeBootstrapProfile | None = Field(default=None)


class DevicePairSetupCodeResult(_SchemaModel):
    setup_code: str = Field(min_length=1)
    qr_data_url: str | None = Field(default=None, max_length=16384, pattern="^data:image/png;base64,")
    gateway_url: str = Field(min_length=1)
    gateway_urls: list[str] | None = Field(default=None, min_length=2, max_length=8)
    auth: DevicePairSetupCodeAuth
    url_source: str = Field(min_length=1)
    access: DevicePairSetupCodeAccess | None = Field(default=None)
    access_downgraded: bool | None = Field(default=None)


class DevicePairRenameParams(_SchemaModel):
    device_id: str = Field(min_length=1)
    label: str = Field(min_length=1, max_length=64)


class DeviceTokenRotateParams(_SchemaModel):
    device_id: str = Field(min_length=1)
    role: str = Field(min_length=1)
    scopes: list[str] | None = Field(default=None)


class DeviceTokenRevokeParams(_SchemaModel):
    device_id: str = Field(min_length=1)
    role: str = Field(min_length=1)


class DevicePairRequestedEvent(_SchemaModel):
    request_id: str = Field(min_length=1)
    device_id: str = Field(min_length=1)
    public_key: str = Field(min_length=1)
    display_name: str | None = Field(default=None, min_length=1)
    platform: str | None = Field(default=None, min_length=1)
    device_family: str | None = Field(default=None, min_length=1)
    client_id: str | None = Field(default=None, min_length=1)
    client_mode: str | None = Field(default=None, min_length=1)
    browser_origin: str | None = Field(default=None, min_length=1)
    role: str | None = Field(default=None, min_length=1)
    roles: list[str] | None = Field(default=None)
    scopes: list[str] | None = Field(default=None)
    remote_ip: str | None = Field(default=None, min_length=1)
    silent: bool | None = Field(default=None)
    is_repair: bool | None = Field(default=None)
    ts: int = Field(ge=0)


class DevicePairResolvedEvent(_SchemaModel):
    request_id: str = Field(min_length=1)
    device_id: str = Field(min_length=1)
    decision: str = Field(min_length=1)
    ts: int = Field(ge=0)


class ChatHistoryParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    limit: int | None = Field(default=None, ge=1, le=1000)
    offset: int | None = Field(default=None, ge=0)
    message_id: str | None = Field(default=None, min_length=1)
    session_id: str | None = Field(default=None, min_length=1)
    max_chars: int | None = Field(default=None, ge=1, le=500000)


class ChatMetadataParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)


class ChatMessageGetParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    message_id: str = Field(min_length=1)
    max_chars: int | None = Field(default=None, ge=1, le=2000000)


class ChatMessageGetResult(_SchemaModel):
    ok: bool
    message: Any | None = Field(default=None)
    unavailable_reason: ChatMessageGetUnavailableReason | None = Field(default=None)


class ChatToolTitlesParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    items: list[dict[str, Any]] = Field(min_length=1, max_length=24)


class ChatToolTitlesResult(_SchemaModel):
    titles: dict[str, Any]
    disabled: bool | None = Field(default=None)


class ChatSendParams(_SchemaModel):
    session_key: str = Field(min_length=1, max_length=512)
    agent_id: str | None = Field(default=None, min_length=1)
    session_id: str | None = Field(default=None, min_length=1)
    message: str
    thinking: str | None = Field(default=None)
    fast_mode: bool | Literal["auto"] | None = Field(default=None)
    fast_auto_on_seconds: int | None = Field(default=None, ge=1)
    queue_mode: ChatSendQueueMode | None = Field(default=None)
    deliver: bool | None = Field(default=None)
    originating_channel: str | None = Field(default=None)
    originating_to: str | None = Field(default=None)
    originating_account_id: str | None = Field(default=None)
    originating_thread_id: str | None = Field(default=None)
    reply_to_id: str | None = Field(default=None, min_length=1)
    attachments: list[dict[str, Any]] | None = Field(default=None)
    tool_bindings: dict[str, Any] | None = Field(default=None)
    timeout_ms: int | None = Field(default=None, ge=0)
    system_input_provenance: dict[str, Any] | None = Field(default=None)
    system_provenance_receipt: str | None = Field(default=None)
    suppress_command_interpretation: bool | None = Field(default=None)
    expected_leaf_entry_id: str | None = Field(default=None)
    expected_session_routing_contract: str | None = Field(default=None, min_length=1)
    idempotency_key: str = Field(default_factory=lambda: str(uuid4()), min_length=1)


class ChatAbortParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    preserve_side_runs: bool | None = Field(default=None)


class ChatInjectParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    message: str = Field(min_length=1)
    label: str | None = Field(default=None, max_length=100)


class ChatDeltaEvent(_SchemaModel):
    run_id: str = Field(min_length=1)
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    spawned_by: str | None = Field(default=None, min_length=1)
    seq: int = Field(ge=0)
    state: Literal["delta"]
    message: Any | None = Field(default=None)
    delta_text: str
    replace: bool | None = Field(default=None)
    usage: Any | None = Field(default=None)


class ChatFinalEvent(_SchemaModel):
    run_id: str = Field(min_length=1)
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    spawned_by: str | None = Field(default=None, min_length=1)
    seq: int = Field(ge=0)
    state: Literal["final"]
    message: Any | None = Field(default=None)
    usage: Any | None = Field(default=None)
    stop_reason: str | None = Field(default=None)
    yielded: Literal[True] | None = Field(default=None)


class ChatAbortedEvent(_SchemaModel):
    run_id: str = Field(min_length=1)
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    spawned_by: str | None = Field(default=None, min_length=1)
    seq: int = Field(ge=0)
    state: Literal["aborted"]
    message: Any | None = Field(default=None)
    error_message: str | None = Field(default=None)
    stop_reason: str | None = Field(default=None)


class ChatErrorEvent(_SchemaModel):
    run_id: str = Field(min_length=1)
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    spawned_by: str | None = Field(default=None, min_length=1)
    seq: int = Field(ge=0)
    state: Literal["error"]
    message: Any | None = Field(default=None)
    error_message: str | None = Field(default=None)
    error_kind: ChatErrorEventErrorKind | None = Field(default=None)
    usage: Any | None = Field(default=None)
    stop_reason: str | None = Field(default=None)


class UpdateStatusParams(_SchemaModel):
    pass


class UpdateRunParams(_SchemaModel):
    session_key: str | None = Field(default=None)
    delivery_context: dict[str, Any] | None = Field(default=None)
    note: str | None = Field(default=None)
    continuation_message: str | None = Field(default=None)
    restart_delay_ms: int | None = Field(default=None, ge=0)
    timeout_ms: int | None = Field(default=None, ge=1)


class TickEvent(_SchemaModel):
    ts: int = Field(ge=0)


class ShutdownEvent(_SchemaModel):
    reason: str = Field(min_length=1)
    restart_expected_ms: int | None = Field(default=None, ge=0)


class GatewayServer(_SchemaModel):
    version: str = Field(min_length=1)
    conn_id: str = Field(min_length=1)


class GatewayFeatures(_SchemaModel):
    methods: list[str]
    events: list[str]
    capabilities: list[str] | None = Field(default=None)


class ChatSendAck(_SchemaModel):
    run_id: str = Field(min_length=1)
    status: ChatSendStatus
    summary: str | None = Field(default=None)
    server_timing: dict[str, Any] | None = Field(default=None)


class BoardWidget(_SchemaModel):
    name: str = Field(pattern="^[a-z0-9][a-z0-9._-]{0,63}$")
    tab_id: str = Field(pattern="^[a-z0-9-]{1,40}$")
    title: str | None = Field(default=None, min_length=1, max_length=80)
    content_kind: BoardWidgetContentKind
    plugin_kind: str | None = Field(default=None, pattern="^[a-z0-9][a-z0-9-]{0,63}:[a-z0-9][a-z0-9._-]{0,63}$")
    props: dict[str, Any] | None = Field(default=None)
    presentation: BoardWidgetPresentation | None = Field(default=None)
    height_mode: BoardWidgetHeightMode | None = Field(default=None)
    size_w: int = Field(ge=1, le=12)
    size_h: int = Field(ge=1, le=20)
    position: int = Field(ge=0)
    grant_state: BoardWidgetGrantState
    revision: int = Field(ge=1)
    instance_id: str | None = Field(default=None, min_length=1)
    declared_summary: list[str] | None = Field(default=None)
    declared: BoardWidgetDeclared | None = Field(default=None)
    frame_url: str | None = Field(default=None)
    view_ticket: str | None = Field(default=None)
    view_ticket_ttl_ms: int | None = Field(default=None, ge=1)
    view_generation: str | None = Field(default=None, pattern="^[a-f0-9]{32}$")
    sandbox_url: str | None = Field(default=None)
    sandbox_port: int | None = Field(default=None, ge=1, le=65535)
    sandbox_origin: str | None = Field(default=None)


class BoardWidgetMcpAppContent(_SchemaModel):
    kind: Literal["mcp-app"]
    descriptor: BoardMcpAppDescriptor


class ResponseFrame(_SchemaModel):
    type: Literal["res"]
    id: str = Field(min_length=1)
    ok: bool
    payload: Any | None = Field(default=None)
    error: ErrorShape | None = Field(default=None)


class EventFrame(_SchemaModel):
    type: Literal["event"]
    event: str = Field(min_length=1)
    payload: Any | None = Field(default=None)
    seq: int | None = Field(default=None, ge=0)
    state_version: StateVersion | None = Field(default=None)


class Snapshot(_SchemaModel):
    presence: list[PresenceEntry]
    health: dict[str, Any]
    state_version: StateVersion
    uptime_ms: int = Field(ge=0)
    applied_config_hash: str | None = Field(default=None)
    config_path: str | None = Field(default=None, min_length=1)
    state_dir: str | None = Field(default=None, min_length=1)
    session_defaults: dict[str, Any] | None = Field(default=None)
    auth_mode: SnapshotAuthMode | None = Field(default=None)
    update_available: dict[str, Any] | None = Field(default=None)


class GatewaySuspendBlocker(_SchemaModel):
    kind: GatewaySuspendBlockerKind
    count: int = Field(ge=0)
    message: str
    task: GatewaySuspendTaskBlocker | None = Field(default=None)


class WorkerEnvironmentMetadata(_SchemaModel):
    provider_id: str = Field(min_length=1)
    lease_id: str | None = Field(default=None, min_length=1)
    state: WorkerEnvironmentState
    age_ms: int = Field(ge=0)
    idle_ms: int | None = Field(default=None, ge=0)
    attached_session_ids: list[str]
    tunnel_status: WorkerTunnelStatus


class ConversationListResult(_SchemaModel):
    conversations: list[ConversationListItem]


class WorktreesListResult(_SchemaModel):
    worktrees: list[WorktreeRecord]


class WorktreesBranchesResult(_SchemaModel):
    branches: list[WorktreeBranch]
    default_branch: str | None = Field(default=None, min_length=1)
    head_branch: str | None = Field(default=None, min_length=1)
    repository_status: WorktreeRepositoryStatus | None = Field(default=None)


class FsListDirResult(_SchemaModel):
    path: str = Field(min_length=1)
    parent: str | None = Field(default=None, min_length=1)
    home: str = Field(min_length=1)
    entries: list[FsDirEntry]


class NodePluginToolsUpdateParams(_SchemaModel):
    tools: list[NodePluginToolDescriptor]


class NodeSkillsUpdateParams(_SchemaModel):
    skills: list[NodeSkillDescriptor] = Field(max_length=64)


class NodePresenceAlivePayload(_SchemaModel):
    trigger: NodePresenceAliveReason
    sent_at_ms: int | None = Field(default=None, ge=0)
    display_name: str | None = Field(default=None, min_length=1)
    version: str | None = Field(default=None, min_length=1)
    platform: str | None = Field(default=None, min_length=1)
    device_family: str | None = Field(default=None, min_length=1)
    model_identifier: str | None = Field(default=None, min_length=1)
    push_transport: str | None = Field(default=None, min_length=1)


class SecretsResolveResult(_SchemaModel):
    ok: bool | None = Field(default=None)
    assignments: list[SecretsResolveAssignment] | None = Field(default=None)
    diagnostics: list[str] | None = Field(default=None)
    inactive_ref_paths: list[str] | None = Field(default=None)


class SessionCatalogDescriptor(_SchemaModel):
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    capabilities: SessionCatalogCapabilities


class SessionCatalogSession(_SchemaModel):
    thread_id: str = Field(min_length=1)
    name: str | None = Field(default=None)
    cwd: str | None = Field(default=None)
    status: str = Field(min_length=1)
    created_at: float | None = Field(default=None)
    updated_at: float | None = Field(default=None)
    recency_at: float | None = Field(default=None)
    source: str | None = Field(default=None)
    model_provider: str | None = Field(default=None)
    cli_version: str | None = Field(default=None)
    git_branch: str | None = Field(default=None)
    custom_group: str | None = Field(default=None)
    pull_request: SessionCatalogPullRequestSummary | None = Field(default=None)
    archived: bool
    session_key: str | None = Field(default=None, min_length=1)
    created_actor: SessionCreatedActor | None = Field(default=None)
    can_continue: bool
    can_archive: bool
    can_open_terminal: bool | None = Field(default=None)


class SessionsCatalogReadResult(_SchemaModel):
    host_id: str = Field(min_length=1)
    label: str | None = Field(default=None)
    thread_id: str = Field(min_length=1)
    items: list[SessionCatalogTranscriptItem]
    next_cursor: str | None = Field(default=None)


class SessionsSearchResult(_SchemaModel):
    results: list[SessionsSearchHit]
    indexing: bool | None = Field(default=None)
    truncated: bool | None = Field(default=None)


class SessionObserverDigest(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    revision: int = Field(ge=1)
    updated_at: int = Field(ge=0)
    headline: str = Field(min_length=1, max_length=120)
    assessment: str | None = Field(default=None, min_length=1, max_length=320)
    health: SessionObserverHealth
    plan_progress: SessionObserverPlanProgress | None = Field(default=None)


class SessionRow(_SchemaModel):
    key: str
    session_id: str | None = Field(default=None)
    incognito: Literal[True] | None = Field(default=None)
    kind: SessionRowKind
    label: str | None = Field(default=None)
    board_face: SessionsListBoardFace | None = Field(default=None)
    display_name: str | None = Field(default=None)
    derived_title: str | None = Field(default=None)
    last_message_preview: str | None = Field(default=None)
    channel: str | None = Field(default=None)
    chat_type: ConversationListItemKind | None = Field(default=None)
    updated_at: float | None = Field(default=None)
    archived: bool | None = Field(default=None)
    archived_at: float | None = Field(default=None)
    archived_by: SessionCreatedActor | None = Field(default=None)
    pinned: bool | None = Field(default=None)
    pinned_at: float | None = Field(default=None)
    icon: str | None = Field(default=None)
    unread: bool | None = Field(default=None)
    last_read_at: float | None = Field(default=None)
    last_activity_at: float | None = Field(default=None)
    last_interaction_at: float | None = Field(default=None)
    status: SessionRowStatus | None = Field(default=None)
    last_run_error: str | None = Field(default=None)
    active_leaf_entry_id: str | None = Field(default=None)
    spawned_by: str | None = Field(default=None)
    parent_session_key: str | None = Field(default=None)
    control_owner_session_key: str | None = Field(default=None)
    child_sessions: list[str] | None = Field(default=None)
    forked_from_parent: bool | None = Field(default=None)
    spawn_depth: float | None = Field(default=None)
    subagent_role: SessionRowSubagentRole | None = Field(default=None)
    subagent_control_scope: SessionRowSubagentControlScope | None = Field(default=None)
    swarm_group_id: str | None = Field(default=None)
    worktree: dict[str, Any] | None = Field(default=None)
    exec_node: str | None = Field(default=None)
    exec_cwd: str | None = Field(default=None)
    spawned_workspace_dir: str | None = Field(default=None)
    spawned_cwd: str | None = Field(default=None)
    created_via: SessionRowCreatedVia | None = Field(default=None)
    created_actor: SessionCreatedActor | None = Field(default=None)
    visibility: SessionVisibility | None = Field(default=None)
    sharing_role: SessionSharingRole | None = Field(default=None)
    created_at: float | None = Field(default=None)
    fork_source: dict[str, Any] | None = Field(default=None)
    previous_session_id: str | None = Field(default=None)
    input_tokens: float | None = Field(default=None)
    output_tokens: float | None = Field(default=None)
    total_tokens: float | None = Field(default=None)
    total_tokens_fresh: bool | None = Field(default=None)
    context_tokens: float | None = Field(default=None)
    estimated_cost_usd: float | None = Field(default=None)
    model: str | None = Field(default=None)
    model_provider: str | None = Field(default=None)
    tool_overrides: dict[str, Any] | None = Field(default=None)


class SessionsCompanionStateResult(_SchemaModel):
    exchanges: list[SessionCompanionExchange] = Field(max_length=24)


class SessionVisibilitySetParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    visibility: SessionVisibility


class SessionVisibilitySetResult(_SchemaModel):
    ok: Literal[True]
    session_key: str = Field(min_length=1)
    visibility: SessionVisibility


class SessionMembersListResult(_SchemaModel):
    session_key: str = Field(min_length=1)
    owner: SessionSharingIdentity | None = Field(default=None)
    members: list[SessionMember]
    identities: list[SessionSharingIdentity]
    role: SessionSharingRole
    allowed_visibilities: list[SessionVisibility]


class SessionSharingEvent(_SchemaModel):
    action: SessionSharingAction
    session_key: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    actor: SessionSharingIdentity
    visibility: SessionVisibility | None = Field(default=None)
    identity_id: str | None = Field(default=None, min_length=1)
    ts: int = Field(ge=0)


class SessionSuggestion(_SchemaModel):
    id: str = Field(min_length=1)
    session_key: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    author: SessionSharingIdentity
    text: str = Field(min_length=1, max_length=32768)
    created_at: int = Field(ge=0)
    state: SessionSuggestionState


class SessionSuggestionsResolveParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    id: str = Field(min_length=1)
    resolution: SessionSuggestionResolution


class SessionTypingEvent(_SchemaModel):
    session_key: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    agent_id: str = Field(min_length=1)
    actor: SessionSharingIdentity
    typing: bool
    ts: int = Field(ge=0)


class SessionsDispatchResult(_SchemaModel):
    ok: Literal[True]
    key: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    placement: ActiveWorkerSessionPlacement


class SessionsReclaimResult(_SchemaModel):
    ok: Literal[True]
    key: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    placement: ReclaimedSessionPlacement


class SessionDiscussionInfo(_SchemaModel):
    state: SessionDiscussionState
    embed_url: str | None = Field(default=None)
    open_url: str | None = Field(default=None)


class SessionDiscussionInfoResult(_SchemaModel):
    state: SessionDiscussionState
    embed_url: str | None = Field(default=None)
    open_url: str | None = Field(default=None)


class SessionDiscussionOpenResult(_SchemaModel):
    state: SessionDiscussionState
    embed_url: str | None = Field(default=None)
    open_url: str | None = Field(default=None)


class SessionsCompactionListResult(_SchemaModel):
    ok: Literal[True]
    key: str = Field(min_length=1)
    checkpoints: list[SessionCompactionCheckpoint]


class SessionsCompactionGetResult(_SchemaModel):
    ok: Literal[True]
    key: str = Field(min_length=1)
    checkpoint: SessionCompactionCheckpoint


class SessionsCompactionBranchResult(_SchemaModel):
    ok: Literal[True]
    source_key: str = Field(min_length=1)
    key: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    checkpoint: SessionCompactionCheckpoint
    entry: dict[str, Any]


class SessionsCompactionRestoreResult(_SchemaModel):
    ok: Literal[True]
    key: str = Field(min_length=1)
    session_id: str = Field(min_length=1)
    checkpoint: SessionCompactionCheckpoint
    entry: dict[str, Any]


class SessionsBranchesListResult(_SchemaModel):
    branches: list[SessionBranch]


class SessionFileBrowserEntry(_SchemaModel):
    path: str
    name: str = Field(min_length=1)
    kind: SessionFileBrowserEntryKind
    session_kind: SessionFileRelevance | None = Field(default=None)
    size: int | None = Field(default=None, ge=0)
    updated_at_ms: int | None = Field(default=None, ge=0)


class SessionFileEntry(_SchemaModel):
    path: str = Field(min_length=1)
    workspace_path: str | None = Field(default=None, min_length=1)
    name: str = Field(min_length=1)
    kind: SessionFileKind
    missing: bool
    size: int | None = Field(default=None, ge=0)
    updated_at_ms: int | None = Field(default=None, ge=0)
    content: str | None = Field(default=None)
    hash: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    mime_type: str | None = Field(default=None, min_length=1)
    content_encoding: SessionFileEntryContentEncoding | None = Field(default=None)
    preview_kind: SessionFilePreviewKind | None = Field(default=None)


class SessionDiffFile(_SchemaModel):
    path: str = Field(min_length=1)
    old_path: str | None = Field(default=None, min_length=1)
    status: SessionDiffFileStatus
    additions: int = Field(ge=0)
    deletions: int = Field(ge=0)
    binary: bool | None = Field(default=None)
    untracked: bool | None = Field(default=None)
    patch: str | None = Field(default=None)
    truncated: bool | None = Field(default=None)


class SessionsCreateParams(_SchemaModel):
    key: str | None = Field(default=None, min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    label: str | None = Field(default=None, min_length=1, max_length=512)
    model: str | None = Field(default=None, min_length=1)
    thinking_level: str | None = Field(default=None, min_length=1)
    incognito: bool | None = Field(default=None)
    visibility: SessionVisibility | None = Field(default=None)
    catalog_id: str | None = Field(default=None, min_length=1)
    parent_session_key: str | None = Field(default=None, min_length=1)
    spawn_depth: int | None = Field(default=None, ge=1)
    fork: bool | None = Field(default=None)
    emit_command_hooks: bool | None = Field(default=None)
    succeeds_parent: bool | None = Field(default=None)
    task: str | None = Field(default=None)
    message: str | None = Field(default=None)
    attachments: list[dict[str, Any]] | None = Field(default=None)
    worktree: bool | None = Field(default=None)
    worktree_base_ref: str | None = Field(default=None, min_length=1)
    worktree_name: str | None = Field(default=None, pattern="^[a-z0-9][a-z0-9-]{0,63}$")
    exec_node: str | None = Field(default=None, min_length=1)
    cwd: str | None = Field(default=None, min_length=1)


class SessionsCreateResult(_SchemaModel):
    ok: Literal[True]
    key: str = Field(min_length=1)
    session_id: str | None = Field(default=None, min_length=1)
    entry: dict[str, Any] | None = Field(default=None)
    run_started: bool | None = Field(default=None)
    run_id: str | None = Field(default=None, min_length=1)
    message_seq: int | None = Field(default=None, ge=1)
    run_error: ErrorShape | None = Field(default=None)
    worktree: SessionWorktreeInfo | None = Field(default=None)


class SessionsGroupsListResult(_SchemaModel):
    groups: list[SessionGroup]
    section_order: list[str] | None = Field(default=None, max_length=232)


class SessionsGroupsMutationResult(_SchemaModel):
    ok: Literal[True]
    groups: list[SessionGroup]
    section_order: list[str] | None = Field(default=None, max_length=232)
    updated_sessions: int | None = Field(default=None, ge=0)


class AuditActivityAgentRunV1(_SchemaModel):
    event_type: Literal["agent_run"]
    schema_version: int = Field(ge=1, le=1)
    event_id: str = Field(min_length=1)
    sequence: int = Field(ge=1)
    source_sequence: int = Field(ge=1)
    occurred_at: int = Field(ge=0)
    redaction: Literal["metadata_only"]
    actor: dict[str, Any]
    agent_id: str = Field(min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    session_id: str | None = Field(default=None, min_length=1)
    run_id: str = Field(min_length=1)
    kind: Literal["agent_run"]
    action: AuditActivityAgentRunV1Action
    status: AuditActivityAgentRunV1Status
    error_code: AuditActivityAgentRunV1ErrorCode | None = Field(default=None)


class AuditActivityToolActionV1(_SchemaModel):
    event_type: Literal["tool_action"]
    schema_version: int = Field(ge=1, le=1)
    event_id: str = Field(min_length=1)
    sequence: int = Field(ge=1)
    source_sequence: int = Field(ge=1)
    occurred_at: int = Field(ge=0)
    redaction: Literal["metadata_only"]
    actor: dict[str, Any]
    agent_id: str = Field(min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    session_id: str | None = Field(default=None, min_length=1)
    run_id: str = Field(min_length=1)
    kind: Literal["tool_action"]
    tool_call_id: str | None = Field(default=None, min_length=1)
    tool_name: str | None = Field(default=None, min_length=1)
    action: AuditActivityToolActionV1Action
    status: AuditActivityToolActionV1Status
    error_code: AuditActivityToolActionV1ErrorCode | None = Field(default=None)


class AuditActivityOutboundMessageV1(_SchemaModel):
    event_type: Literal["outbound_message"]
    schema_version: int = Field(ge=1, le=1)
    event_id: str = Field(min_length=1)
    sequence: int = Field(ge=1)
    source_sequence: int = Field(ge=1)
    occurred_at: int = Field(ge=0)
    redaction: Literal["metadata_only"]
    channel: str = Field(min_length=1)
    conversation_kind: AuditActivityInboundMessageV1ConversationKind
    duration_ms: int | None = Field(default=None, ge=0)
    result_count: int | None = Field(default=None, ge=0)
    agent_id: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    account_ref: str | None = Field(default=None, pattern="^hmac-sha256:v1:[a-f0-9]{32}:[a-f0-9]{64}$")
    conversation_ref: str | None = Field(default=None, pattern="^hmac-sha256:v1:[a-f0-9]{32}:[a-f0-9]{64}$")
    message_ref: str | None = Field(default=None, pattern="^hmac-sha256:v1:[a-f0-9]{32}:[a-f0-9]{64}$")
    target_ref: str | None = Field(default=None, pattern="^hmac-sha256:v1:[a-f0-9]{32}:[a-f0-9]{64}$")
    kind: Literal["message"]
    action: Literal["message.outbound.finished"]
    direction: Literal["outbound"]
    actor: dict[str, Any]
    delivery_kind: AuditActivityOutboundMessageV1DeliveryKind | None = Field(default=None)
    status: AuditActivityOutboundMessageV1Status
    outcome: AuditActivityOutboundMessageV1Outcome
    error_code: AuditActivityOutboundMessageV1ErrorCode | None = Field(default=None)
    reason_code: AuditActivityOutboundMessageV1ReasonCode | None = Field(default=None)
    failure_stage: AuditActivityOutboundMessageV1FailureStage | None = Field(default=None)


class AuditEvent(_SchemaModel):
    event_id: str = Field(min_length=1)
    sequence: int = Field(ge=1)
    source_sequence: int = Field(ge=1)
    occurred_at: int = Field(ge=0)
    kind: AuditEventKind
    action: AuditEventAction
    status: AuditActivityToolActionV1Status
    error_code: AuditEventErrorCode | None = Field(default=None)
    actor: dict[str, Any]
    agent_id: str = Field(min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    session_id: str | None = Field(default=None, min_length=1)
    run_id: str = Field(min_length=1)
    tool_call_id: str | None = Field(default=None, min_length=1)
    tool_name: str | None = Field(default=None, min_length=1)
    redaction: Literal["metadata_only"]


class TaskSuggestionsCreateResult(_SchemaModel):
    task_id: str = Field(min_length=1, max_length=128)
    suggestion: TaskSuggestion


class TaskSuggestionsListResult(_SchemaModel):
    suggestions: list[TaskSuggestion]


class TasksListResult(_SchemaModel):
    tasks: list[TaskSummary]
    next_cursor: str | None = Field(default=None)


class TasksGetResult(_SchemaModel):
    task: TaskSummary


class TasksCancelResult(_SchemaModel):
    found: bool
    cancelled: bool
    reason: str | None = Field(default=None)
    task: TaskSummary | None = Field(default=None)


class SystemAgentChatHistoryResult(_SchemaModel):
    turns: list[SystemAgentChatHistoryTurn]


class SystemChangeEntry(_SchemaModel):
    id: str = Field(min_length=1)
    at: float
    kind: SystemChangeKind
    source: SystemChangeSource
    summary: str
    changed_paths: list[str] | None = Field(default=None)
    invalid: bool | None = Field(default=None)
    opaque_change: bool | None = Field(default=None)


class SystemAgentSetupAuthStartResult(_SchemaModel):
    session_id: str = Field(min_length=1)
    done: bool
    step: WizardStep | None = Field(default=None)
    status: SystemAgentSetupAuthStartStatus | None = Field(default=None)
    error: str | None = Field(default=None)
    channels: list[str] | None = Field(default=None)
    accounts: list[dict[str, Any]] | None = Field(default=None)


class WizardNextResult(_SchemaModel):
    done: bool
    step: WizardStep | None = Field(default=None)
    status: SystemAgentSetupAuthStartStatus | None = Field(default=None)
    error: str | None = Field(default=None)
    channels: list[str] | None = Field(default=None)
    accounts: list[dict[str, Any]] | None = Field(default=None)


class WizardStartResult(_SchemaModel):
    session_id: str = Field(min_length=1)
    done: bool
    step: WizardStep | None = Field(default=None)
    status: SystemAgentSetupAuthStartStatus | None = Field(default=None)
    error: str | None = Field(default=None)
    channels: list[str] | None = Field(default=None)
    accounts: list[dict[str, Any]] | None = Field(default=None)


class TalkSessionJoinResult(_SchemaModel):
    id: str = Field(min_length=1)
    room_id: str = Field(min_length=1)
    room_url: str = Field(min_length=1)
    session_key: str = Field(min_length=1)
    session_id: str | None = Field(default=None)
    channel: str | None = Field(default=None)
    target: str | None = Field(default=None)
    provider: str | None = Field(default=None)
    model: str | None = Field(default=None)
    voice: str | None = Field(default=None)
    mode: TalkEventMode
    transport: TalkEventTransport
    brain: TalkEventBrain
    created_at: float
    expires_at: float
    room: dict[str, Any]


class TalkSessionTurnResult(_SchemaModel):
    ok: bool
    turn_id: str | None = Field(default=None)
    events: list[TalkEvent] | None = Field(default=None)


class AgentSummary(_SchemaModel):
    id: str = Field(min_length=1)
    kind: AgentKind | None = Field(default=None)
    name: str | None = Field(default=None, min_length=1)
    identity: dict[str, Any] | None = Field(default=None)
    workspace: str | None = Field(default=None, min_length=1)
    workspace_git: bool | None = Field(default=None)
    model: dict[str, Any] | None = Field(default=None)
    agent_runtime: dict[str, Any] | None = Field(default=None)
    thinking_levels: list[dict[str, Any]] | None = Field(default=None)
    thinking_options: list[str] | None = Field(default=None)
    thinking_default: str | None = Field(default=None, min_length=1)


class AgentsFilesListResult(_SchemaModel):
    agent_id: str = Field(min_length=1)
    workspace: str = Field(min_length=1)
    files: list[AgentsFileEntry]


class AgentsFilesGetResult(_SchemaModel):
    agent_id: str = Field(min_length=1)
    workspace: str = Field(min_length=1)
    file: AgentsFileEntry


class AgentsFilesSetResult(_SchemaModel):
    ok: Literal[True]
    agent_id: str = Field(min_length=1)
    workspace: str = Field(min_length=1)
    file: AgentsFileEntry


class AgentsWorkspaceListResult(_SchemaModel):
    agent_id: str = Field(min_length=1)
    path: str
    parent_path: str | None = Field(default=None)
    entries: list[AgentsWorkspaceEntry]
    total_entries: int = Field(ge=0)
    offset: int = Field(ge=0)


class AgentsWorkspaceGetResult(_SchemaModel):
    agent_id: str = Field(min_length=1)
    file: AgentsWorkspaceFile


class ArtifactsListResult(_SchemaModel):
    artifacts: list[ArtifactSummary]


class ArtifactsGetResult(_SchemaModel):
    artifact: ArtifactSummary


class ArtifactsDownloadResult(_SchemaModel):
    artifact: ArtifactSummary
    encoding: Literal["base64"] | None = Field(default=None)
    data: str | None = Field(default=None)
    url: str | None = Field(default=None, min_length=1)
    expires_at: str | None = Field(default=None, min_length=1)


class ModelsListResult(_SchemaModel):
    models: list[ModelChoice]


class ModelsProbeTargetResult(_SchemaModel):
    profile_id: str | None = Field(default=None, min_length=1)
    label: str = Field(min_length=1)
    status: AuthProbeStatus
    latency_ms: int | None = Field(default=None, ge=0)
    error: str | None = Field(default=None)


class CommandsListResult(_SchemaModel):
    commands: list[CommandEntry] = Field(max_length=500)


class ToolCatalogGroup(_SchemaModel):
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    source: ToolCatalogEntrySource
    plugin_id: str | None = Field(default=None, min_length=1)
    tools: list[ToolCatalogEntry]


class ToolsEffectiveGroup(_SchemaModel):
    id: ToolsEffectiveEntrySource
    label: str = Field(min_length=1)
    source: ToolsEffectiveEntrySource
    tools: list[ToolsEffectiveEntry]


class ToolsInvokeResult(_SchemaModel):
    ok: bool
    tool_name: str = Field(min_length=1)
    output: Any | None = Field(default=None)
    requires_approval: bool | None = Field(default=None)
    approval_id: str | None = Field(default=None, min_length=1)
    source: str | Literal["core", "plugin", "mcp", "channel"] | None = Field(default=None)
    error: ToolsInvokeError | None = Field(default=None)


class SkillsCuratorStatusResult(_SchemaModel):
    last_attempt_at_ms: float | None
    last_success_at_ms: float | None
    last_error: str | None
    counts: dict[str, Any]
    skills: list[SkillsCuratorActionResult]
    overlaps: list[dict[str, Any]]


class SkillsProposalEvaluateResult(_SchemaModel):
    record: SkillsProposalRecordResult
    evaluation: dict[str, Any]


class SkillsProposalInspectResult(_SchemaModel):
    record: SkillsProposalRecordResult
    revision_hash: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-fA-F0-9]{64}$")
    content: str
    support_files: list[dict[str, Any]] | None = Field(default=None, max_length=64)


class SkillsProposalApplyResult(_SchemaModel):
    record: SkillsProposalRecordResult
    target_skill_file: str = Field(min_length=1)


class CronDeclarativeAddResult(_SchemaModel):
    created: bool
    updated: bool | None = Field(default=None)
    job: CronJob


class MemoryMigrationItem(_SchemaModel):
    id: str = Field(min_length=1)
    status: MemoryMigrationItemStatus
    source: str | None = Field(default=None, min_length=1)
    target: str | None = Field(default=None, min_length=1)
    message: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    details: dict[str, Any] | None = Field(default=None)


class TerminalOpenParams(_SchemaModel):
    agent_id: str | None = Field(default=None, min_length=1)
    catalog: SessionsCatalogContinueParams | None = Field(default=None)
    cols: int = Field(ge=1, le=2000)
    rows: int = Field(ge=1, le=2000)


class TerminalListResult(_SchemaModel):
    sessions: list[TerminalSessionInfo]


class ExecApprovalPresentation(_SchemaModel):
    kind: Literal["exec"]
    command_text: str = Field(min_length=1)
    command_preview: str | None = Field(default=None)
    warning_text: str | None = Field(default=None)
    host: str | None = Field(default=None)
    node_id: str | None = Field(default=None)
    agent_id: str | None = Field(default=None)
    allowed_decisions: list[ApprovalDecision] = Field(min_length=1, max_length=3)


class PluginApprovalPresentation(_SchemaModel):
    kind: Literal["plugin"]
    title: str = Field(min_length=1, max_length=80)
    description: str = Field(min_length=1, max_length=512)
    detail: str | None = Field(default=None, min_length=1, max_length=16384)
    severity: PluginApprovalSeverity
    plugin_id: str | None = Field(default=None)
    tool_name: str | None = Field(default=None)
    agent_id: str | None = Field(default=None)
    allowed_decisions: list[ApprovalDecision] = Field(min_length=1, max_length=3)


class ApprovalHistoryParams(_SchemaModel):
    cursor: str | None = Field(default=None, min_length=1, max_length=512)
    limit: int | None = Field(default=None, ge=1, le=100)
    kind: ApprovalKind | None = Field(default=None)


class ApprovalResolveParams(_SchemaModel):
    id: str = Field(min_length=1, pattern="^(?!\\.{1,2}$)(?:[^\\uD800-\\uDFFF]|[\\uD800-\\uDBFF][\\uDC00-\\uDFFF])+$")
    kind: ApprovalKind
    decision: ApprovalDecision


class Question(_SchemaModel):
    question_id: str = Field(pattern="^[a-z][a-z0-9_]*$")
    header: str = Field(max_length=12)
    question: str = Field(min_length=1)
    options: list[QuestionOption] = Field(max_length=4)
    multi_select: bool | None = Field(default=None)
    is_other: bool | None = Field(default=None)
    is_secret: bool | None = Field(default=None)


class QuestionRequestQuestion(_SchemaModel):
    question_id: str = Field(pattern="^[a-z][a-z0-9_]*$")
    header: str = Field(max_length=12)
    question: str = Field(min_length=1)
    options: list[QuestionOption] = Field(max_length=4)
    multi_select: bool | None = Field(default=None)
    is_other: bool | None = Field(default=None)
    is_secret: bool | None = Field(default=None)


class PluginSearchResultEntry(_SchemaModel):
    score: float
    package: PluginSearchPackage


class PluginsUiDescriptorsResult(_SchemaModel):
    ok: Literal[True]
    descriptors: list[PluginControlUiDescriptor]


class ChatStatusEvent(_SchemaModel):
    run_id: str = Field(min_length=1)
    session_key: str = Field(min_length=1)
    agent_id: str | None = Field(default=None, min_length=1)
    spawned_by: str | None = Field(default=None, min_length=1)
    seq: int = Field(ge=0)
    state: Literal["status"]
    phase: ChatRunStartupPhase


class GatewayPolicy(_SchemaModel):
    max_payload: int = Field(ge=1)
    max_buffered_bytes: int = Field(ge=1)
    tick_interval_ms: int = Field(ge=1)
    allowed_session_visibilities: list[SessionVisibility] | None = Field(default=None)
    has_multiple_session_sharing_identities: bool | None = Field(default=None)


class BoardSnapshot(_SchemaModel):
    session_key: str = Field(min_length=1)
    revision: int = Field(ge=0)
    tabs: list[BoardTab]
    widgets: list[BoardWidget]


class BoardUpdateParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    ops: list[
        BoardTabCreateOp
        | BoardTabUpdateOp
        | BoardTabDeleteOp
        | BoardTabsReorderOp
        | BoardWidgetMoveOp
        | BoardWidgetResizeOp
        | BoardWidgetRemoveOp
    ]


class BoardWidgetPutParams(_SchemaModel):
    session_key: str = Field(min_length=1)
    name: str = Field(pattern="^[a-z0-9][a-z0-9._-]{0,63}$")
    title: str | None = Field(default=None, min_length=1, max_length=80)
    content: BoardWidgetHtmlContent | BoardWidgetMcpAppPutContent | BoardWidgetPluginContent | BoardCanvasDocumentSource
    presentation: BoardWidgetPresentation | None = Field(default=None)
    height_mode: BoardWidgetHeightMode | None = Field(default=None)
    placement: dict[str, Any] | None = Field(default=None)
    declared: BoardWidgetDeclared | None = Field(default=None)


class BoardCommandEvent(_SchemaModel):
    session_key: str = Field(min_length=1)
    command: BoardFocusTabCommand | BoardSetChatDockCommand


class HelloOk(_SchemaModel):
    type: Literal["hello-ok"]
    protocol: int = Field(ge=1)
    server: GatewayServer
    features: GatewayFeatures
    snapshot: Snapshot
    control_ui_tabs: list[dict[str, Any]] | None = Field(default=None)
    control_ui_widget_kinds: list[dict[str, Any]] | None = Field(default=None)
    plugin_surface_urls: dict[str, Any] | None = Field(default=None)
    device_auth_migration: dict[str, Any] | None = Field(default=None)
    auth: dict[str, Any]
    policy: GatewayPolicy


class GatewaySuspendPrepareBusyResult(_SchemaModel):
    status: Literal["busy"]
    reason: GatewaySuspendPrepareBusyReason
    retry_after_ms: int = Field(ge=0)
    active_count: int = Field(ge=0)
    blockers: list[GatewaySuspendBlocker]


class GatewaySuspendPrepareReadyResult(_SchemaModel):
    status: Literal["ready"]
    suspension_id: str = Field(min_length=1, max_length=128, pattern="\\S")
    expires_at_ms: int = Field(ge=0)
    active_count: int = Field(ge=0)
    blockers: list[GatewaySuspendBlocker]


class EnvironmentSummary(_SchemaModel):
    id: str = Field(min_length=1)
    type: str = Field(min_length=1)
    label: str | None = Field(default=None, min_length=1)
    status: EnvironmentStatus
    capabilities: list[str] | None = Field(default=None)
    worker: WorkerEnvironmentMetadata | None = Field(default=None)


class EnvironmentsCreateResult(_SchemaModel):
    id: str = Field(min_length=1)
    type: str = Field(min_length=1)
    label: str | None = Field(default=None, min_length=1)
    status: EnvironmentStatus
    capabilities: list[str] | None = Field(default=None)
    worker: WorkerEnvironmentMetadata | None = Field(default=None)


class EnvironmentsDestroyResult(_SchemaModel):
    id: str = Field(min_length=1)
    type: str = Field(min_length=1)
    label: str | None = Field(default=None, min_length=1)
    status: EnvironmentStatus
    capabilities: list[str] | None = Field(default=None)
    worker: WorkerEnvironmentMetadata | None = Field(default=None)


class EnvironmentsStatusResult(_SchemaModel):
    id: str = Field(min_length=1)
    type: str = Field(min_length=1)
    label: str | None = Field(default=None, min_length=1)
    status: EnvironmentStatus
    capabilities: list[str] | None = Field(default=None)
    worker: WorkerEnvironmentMetadata | None = Field(default=None)


class UiCommandParams(_SchemaModel):
    command: (
        UiSplitCommand | UiClosePaneCommand | UiFocusCommand | UiSidebarCommand | UiPanelCommand | UiNavigateCommand
    )
    session_key: str | None = Field(default=None, min_length=1)


class SessionCatalogHost(_SchemaModel):
    host_id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    kind: SessionCatalogHostKind
    connected: bool
    node_id: str | None = Field(default=None, min_length=1)
    sessions: list[SessionCatalogSession]
    next_cursor: str | None = Field(default=None)
    error: dict[str, Any] | None = Field(default=None)


class SessionSuggestionsAddResult(_SchemaModel):
    suggestion: SessionSuggestion


class SessionSuggestionsListResult(_SchemaModel):
    suggestions: list[SessionSuggestion]
    role: SessionSharingRole


class SessionSuggestionsResolveResult(_SchemaModel):
    suggestion: SessionSuggestion


class SessionSuggestionEvent(_SchemaModel):
    action: SessionSuggestionAction
    suggestion: SessionSuggestion


class SessionFileBrowserResult(_SchemaModel):
    path: str
    parent_path: str | None = Field(default=None)
    search: str | None = Field(default=None)
    entries: list[SessionFileBrowserEntry]
    truncated: bool | None = Field(default=None)


class SessionsFilesGetResult(_SchemaModel):
    session_key: str = Field(min_length=1)
    root: str | None = Field(default=None, min_length=1)
    file: SessionFileEntry


class SessionsFilesSetResult(_SchemaModel):
    session_key: str = Field(min_length=1)
    root: str | None = Field(default=None, min_length=1)
    file: SessionFileEntry


class SessionsDiffResult(_SchemaModel):
    session_key: str = Field(min_length=1)
    root: str | None = Field(default=None, min_length=1)
    branch: str | None = Field(default=None, min_length=1)
    base_ref: str | None = Field(default=None, min_length=1)
    files: list[SessionDiffFile]
    additions: int = Field(ge=0)
    deletions: int = Field(ge=0)
    truncated: bool | None = Field(default=None)
    unavailable_reason: SessionsDiffUnavailableReason | None = Field(default=None)


class AuditListResult(_SchemaModel):
    events: list[AuditEvent]
    next_cursor: str | None = Field(default=None, min_length=1)


class SystemChangesListResult(_SchemaModel):
    entries: list[SystemChangeEntry]
    next_cursor: str | None = Field(default=None, min_length=1)


class AgentsListResult(_SchemaModel):
    default_id: str = Field(min_length=1)
    main_key: str = Field(min_length=1)
    scope: AgentsListScope
    agents: list[AgentSummary]


class ModelsProbeResult(_SchemaModel):
    provider: str = Field(min_length=1)
    status: AuthProbeStatus
    latency_ms: int | None = Field(default=None, ge=0)
    error: str | None = Field(default=None)
    results: list[ModelsProbeTargetResult]


class ToolsCatalogResult(_SchemaModel):
    agent_id: str = Field(min_length=1)
    profiles: list[ToolCatalogProfile]
    groups: list[ToolCatalogGroup]


class ToolsEffectiveResult(_SchemaModel):
    agent_id: str = Field(min_length=1)
    profile: str = Field(min_length=1)
    groups: list[ToolsEffectiveGroup]
    notices: list[ToolsEffectiveNotice] | None = Field(default=None)


class MemoryMigrationProviderPlan(_SchemaModel):
    provider_id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    description: str | None = Field(default=None)
    plan_fingerprint: str | None = Field(default=None, min_length=64, max_length=64, pattern="^[a-f0-9]{64}$")
    found: bool
    source: str | None = Field(default=None, min_length=1)
    target: str | None = Field(default=None, min_length=1)
    confidence: ToolCatalogEntryRisk | None = Field(default=None)
    message: str | None = Field(default=None)
    error: str | None = Field(default=None)
    summary: MemoryMigrationSummary
    items: list[MemoryMigrationItem] = Field(max_length=2000)
    warnings: list[str] | None = Field(default=None)


class MigrationsMemoryApplyResult(_SchemaModel):
    provider_id: str = Field(min_length=1)
    source: str = Field(min_length=1)
    target: str | None = Field(default=None, min_length=1)
    summary: MemoryMigrationSummary
    items: list[MemoryMigrationItem] = Field(max_length=2000)
    warnings: list[str] | None = Field(default=None)
    backup_path: str | None = Field(default=None, min_length=1)
    report_dir: str | None = Field(default=None, min_length=1)


class QuestionRecord(_SchemaModel):
    id: str = Field(min_length=1)
    questions: list[Question] = Field(min_length=1, max_length=3)
    agent_id: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    created_at_ms: int = Field(ge=0)
    expires_at_ms: int = Field(ge=0)
    status: QuestionStatus
    answers: QuestionAnswers | None = Field(default=None)
    resolved_by: str | None = Field(default=None, min_length=1)


class QuestionRequestParams(_SchemaModel):
    id: str | None = Field(default=None, min_length=1)
    questions: list[Question] = Field(min_length=1, max_length=3)
    agent_id: str | None = Field(default=None, min_length=1)
    session_key: str | None = Field(default=None, min_length=1)
    run_id: str | None = Field(default=None, min_length=1)
    timeout_ms: int | None = Field(default=None, ge=1)


class PluginCatalogEntry(_SchemaModel):
    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    package_name: str | None = Field(default=None, min_length=1)
    description: str | None = Field(default=None)
    version: str | None = Field(default=None, min_length=1)
    kind: list[str] | None = Field(default=None)
    origin: str | None = Field(default=None, min_length=1)
    installed: bool
    enabled: bool
    state: PluginCatalogEntryState
    featured: bool | None = Field(default=None)
    featured_at: int | None = Field(default=None, ge=0)
    order: float | None = Field(default=None)
    has_icon: bool | None = Field(default=None)
    install: PluginCatalogClawHubInstall | PluginCatalogOfficialInstall | None = Field(default=None)
    error: str | None = Field(default=None)
    category: str | None = Field(default=None, min_length=1)
    removable: bool | None = Field(default=None)


class PluginsSearchResult(_SchemaModel):
    results: list[PluginSearchResultEntry]


class EnvironmentsListResult(_SchemaModel):
    environments: list[EnvironmentSummary]
    profiles: list[dict[str, Any]] | None = Field(default=None)


class SessionCatalog(_SchemaModel):
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    capabilities: SessionCatalogCapabilities
    hosts: list[SessionCatalogHost]
    error: dict[str, Any] | None = Field(default=None)


class SessionsFilesListResult(_SchemaModel):
    session_key: str = Field(min_length=1)
    root: str | None = Field(default=None, min_length=1)
    git_checkout: bool | None = Field(default=None)
    files: list[SessionFileEntry]
    browser: SessionFileBrowserResult | None = Field(default=None)


class AuditActivityListResult(_SchemaModel):
    events: list[
        AuditActivityAgentRunV1
        | AuditActivityToolActionV1
        | AuditActivityInboundMessageV1
        | AuditActivityOutboundMessageV1
    ]
    next_cursor: str | None = Field(default=None, min_length=1)


class MigrationsMemoryPlanResult(_SchemaModel):
    agent_id: str = Field(min_length=1)
    workspace: str = Field(min_length=1)
    providers: list[MemoryMigrationProviderPlan]


class PendingApprovalSnapshot(_SchemaModel):
    id: str = Field(min_length=1, pattern="^(?!\\.{1,2}$)(?:[^\\uD800-\\uDFFF]|[\\uD800-\\uDBFF][\\uDC00-\\uDFFF])+$")
    url_path: str = Field(min_length=1)
    created_at_ms: int = Field(ge=0)
    expires_at_ms: int = Field(ge=0)
    presentation: ExecApprovalPresentation | PluginApprovalPresentation | SystemAgentApprovalPresentation
    status: Literal["pending"]


class AllowedApprovalSnapshot(_SchemaModel):
    id: str = Field(min_length=1, pattern="^(?!\\.{1,2}$)(?:[^\\uD800-\\uDFFF]|[\\uD800-\\uDBFF][\\uDC00-\\uDFFF])+$")
    url_path: str = Field(min_length=1)
    created_at_ms: int = Field(ge=0)
    expires_at_ms: int = Field(ge=0)
    presentation: ExecApprovalPresentation | PluginApprovalPresentation | SystemAgentApprovalPresentation
    resolved_at_ms: int = Field(ge=0)
    source: dict[str, Any] | None = Field(default=None)
    resolver: dict[str, Any] | None = Field(default=None)
    status: Literal["allowed"]
    decision: ApprovalAllowDecision
    reason: ApprovalAllowedReason


class DeniedApprovalSnapshot(_SchemaModel):
    id: str = Field(min_length=1, pattern="^(?!\\.{1,2}$)(?:[^\\uD800-\\uDFFF]|[\\uD800-\\uDBFF][\\uDC00-\\uDFFF])+$")
    url_path: str = Field(min_length=1)
    created_at_ms: int = Field(ge=0)
    expires_at_ms: int = Field(ge=0)
    presentation: ExecApprovalPresentation | PluginApprovalPresentation | SystemAgentApprovalPresentation
    resolved_at_ms: int = Field(ge=0)
    source: dict[str, Any] | None = Field(default=None)
    resolver: dict[str, Any] | None = Field(default=None)
    status: Literal["denied"]
    decision: Literal["deny"]
    reason: ApprovalDeniedReason


class ExpiredApprovalSnapshot(_SchemaModel):
    id: str = Field(min_length=1, pattern="^(?!\\.{1,2}$)(?:[^\\uD800-\\uDFFF]|[\\uD800-\\uDBFF][\\uDC00-\\uDFFF])+$")
    url_path: str = Field(min_length=1)
    created_at_ms: int = Field(ge=0)
    expires_at_ms: int = Field(ge=0)
    presentation: ExecApprovalPresentation | PluginApprovalPresentation | SystemAgentApprovalPresentation
    resolved_at_ms: int = Field(ge=0)
    source: dict[str, Any] | None = Field(default=None)
    resolver: dict[str, Any] | None = Field(default=None)
    status: Literal["expired"]
    reason: ApprovalExpiredReason


class CancelledApprovalSnapshot(_SchemaModel):
    id: str = Field(min_length=1, pattern="^(?!\\.{1,2}$)(?:[^\\uD800-\\uDFFF]|[\\uD800-\\uDBFF][\\uDC00-\\uDFFF])+$")
    url_path: str = Field(min_length=1)
    created_at_ms: int = Field(ge=0)
    expires_at_ms: int = Field(ge=0)
    presentation: ExecApprovalPresentation | PluginApprovalPresentation | SystemAgentApprovalPresentation
    resolved_at_ms: int = Field(ge=0)
    source: dict[str, Any] | None = Field(default=None)
    resolver: dict[str, Any] | None = Field(default=None)
    status: Literal["cancelled"]
    reason: ApprovalCancelledReason


class QuestionGetResult(_SchemaModel):
    question: QuestionRecord


class QuestionListResult(_SchemaModel):
    questions: list[QuestionRecord]


class PluginsInstallResult(_SchemaModel):
    ok: Literal[True]
    plugin: PluginCatalogEntry
    restart_required: Literal[True]
    warnings: list[str] | None = Field(default=None)


class PluginsListResult(_SchemaModel):
    plugins: list[PluginCatalogEntry]
    diagnostics: list[Any]
    mutation_allowed: bool


class PluginsSetEnabledResult(_SchemaModel):
    ok: Literal[True]
    plugin: PluginCatalogEntry
    restart_required: bool
    warnings: list[str] | None = Field(default=None)


class SessionsCatalogListResult(_SchemaModel):
    catalogs: list[SessionCatalog]


class PendingSessionApprovalEvent(_SchemaModel):
    session_key: str = Field(min_length=1)
    source_session_key: str | None = Field(default=None, min_length=1)
    updated_at_ms: int = Field(ge=0)
    phase: Literal["pending"]
    approval: PendingApprovalSnapshot


class SessionApprovalReplay(_SchemaModel):
    session_key: str = Field(min_length=1)
    updated_at_ms: int = Field(ge=0)
    approvals: list[PendingApprovalSnapshot]
    truncated: bool


class ApprovalGetResult(_SchemaModel):
    approval: (
        PendingApprovalSnapshot
        | AllowedApprovalSnapshot
        | DeniedApprovalSnapshot
        | ExpiredApprovalSnapshot
        | CancelledApprovalSnapshot
    )


class ApprovalHistoryResult(_SchemaModel):
    items: list[AllowedApprovalSnapshot | DeniedApprovalSnapshot | ExpiredApprovalSnapshot | CancelledApprovalSnapshot]
    next_cursor: str | None = Field(default=None, min_length=1, max_length=512)


class ApprovalResolveResult(_SchemaModel):
    applied: bool
    approval: AllowedApprovalSnapshot | DeniedApprovalSnapshot | ExpiredApprovalSnapshot | CancelledApprovalSnapshot


class TerminalSessionApprovalEvent(_SchemaModel):
    session_key: str = Field(min_length=1)
    source_session_key: str | None = Field(default=None, min_length=1)
    updated_at_ms: int = Field(ge=0)
    phase: Literal["terminal"]
    approval: AllowedApprovalSnapshot | DeniedApprovalSnapshot | ExpiredApprovalSnapshot | CancelledApprovalSnapshot


type BoardEventParams = dict[str, Any]


type BoardActionParams = dict[str, Any]


type NodePresenceActivityPayload = dict[str, Any]


type SystemAgentSetupVerifyResult = dict[str, Any]


type TalkClientCreateResult = dict[str, Any]


type SkillsInstallParams = dict[str, Any]


type SkillsUpdateParams = dict[str, Any]


type CronUpdateParams = dict[str, Any]


type CronRunParams = dict[str, Any]


type CronScratchSetParams = dict[str, Any]


type CronScratchSetResult = dict[str, Any]


type BoardOp = (
    BoardTabCreateOp
    | BoardTabUpdateOp
    | BoardTabDeleteOp
    | BoardTabsReorderOp
    | BoardWidgetMoveOp
    | BoardWidgetResizeOp
    | BoardWidgetRemoveOp
)


type BoardWidgetPutContent = (
    BoardWidgetHtmlContent | BoardWidgetMcpAppPutContent | BoardWidgetPluginContent | BoardCanvasDocumentSource
)


type BoardCommand = BoardFocusTabCommand | BoardSetChatDockCommand


type GatewayErrorDetails = (
    MissingScopeErrorDetails | McpAppViewExpiredErrorDetails | UnknownAgentIdErrorDetails | WizardNotFoundErrorDetails
)


type GatewaySuspendStatusResult = GatewaySuspendStatusRunningResult | GatewaySuspendStatusReadyResult


type ConversationTurnResult = dict[str, Any]


type UiCommand = (
    UiSplitCommand | UiClosePaneCommand | UiFocusCommand | UiSidebarCommand | UiPanelCommand | UiNavigateCommand
)


type SessionPlacement = (
    LocalSessionPlacement
    | RequestedSessionPlacement
    | ProvisioningSessionPlacement
    | SyncingSessionPlacement
    | StartingSessionPlacement
    | ActiveWorkerSessionPlacement
    | DrainingSessionPlacement
    | ReconcilingSessionPlacement
    | ReclaimedSessionPlacement
    | FailedSessionPlacement
)


type TaskSuggestionEvent = dict[str, Any]


type CronGetParams = WorktreesRestoreParams | dict[str, Any]


type CronRemoveParams = WorktreesRestoreParams | dict[str, Any]


type CronScratchGetParams = WorktreesRestoreParams | dict[str, Any]


type TerminalEvent = TerminalDataEvent | TerminalExitEvent


type QuestionWaitAnswerResult = dict[str, Any]


type QuestionResolveParams = dict[str, Any]


type QuestionResolveResult = dict[str, Any]


type QuestionResolvedEvent = dict[str, Any]


type PluginCatalogInstallAction = PluginCatalogClawHubInstall | PluginCatalogOfficialInstall


type PluginsInstallParams = dict[str, Any] | PluginCatalogOfficialInstall


type PluginsSessionActionResult = PluginsSessionActionSuccessResult | PluginsSessionActionFailureResult


type BoardWidgetContent = BoardWidgetHtmlContent | BoardWidgetMcpAppContent | BoardWidgetPluginContent


type GatewayFrame = RequestFrame | ResponseFrame | EventFrame


type AuditActivityEventV1 = (
    AuditActivityAgentRunV1 | AuditActivityToolActionV1 | AuditActivityInboundMessageV1 | AuditActivityOutboundMessageV1
)


type CronAddResult = CronJob | CronDeclarativeAddResult


type ApprovalPresentation = ExecApprovalPresentation | PluginApprovalPresentation | SystemAgentApprovalPresentation


type ChatEvent = ChatStatusEvent | ChatDeltaEvent | ChatFinalEvent | ChatAbortedEvent | ChatErrorEvent


type GatewaySuspendPrepareResult = GatewaySuspendPrepareBusyResult | GatewaySuspendPrepareReadyResult


type ApprovalSnapshot = (
    PendingApprovalSnapshot
    | AllowedApprovalSnapshot
    | DeniedApprovalSnapshot
    | ExpiredApprovalSnapshot
    | CancelledApprovalSnapshot
)


type TerminalApprovalSnapshot = (
    AllowedApprovalSnapshot | DeniedApprovalSnapshot | ExpiredApprovalSnapshot | CancelledApprovalSnapshot
)


type SessionApprovalEvent = PendingSessionApprovalEvent | TerminalSessionApprovalEvent


_EVENT_ADAPTERS: dict[str, TypeAdapter[Any]] = {}


def parse_generated_event(event: str, payload: Any) -> Any:
    adapter = _EVENT_ADAPTERS.get(event)
    return payload if adapter is None else adapter.validate_python(payload)


__all__ = [
    "BoardTab",
    "BoardWidgetDeclared",
    "BoardTabCreateOp",
    "BoardTabUpdateOp",
    "BoardTabDeleteOp",
    "BoardTabsReorderOp",
    "BoardWidgetMoveOp",
    "BoardWidgetResizeOp",
    "BoardWidgetRemoveOp",
    "BoardMcpAppDescriptor",
    "BoardWidgetHtmlContent",
    "BoardWidgetMcpAppPutContent",
    "BoardWidgetPluginContent",
    "BoardCanvasDocumentSource",
    "BoardGetParams",
    "BoardWidgetGrantParams",
    "BoardWidgetAppViewParams",
    "BoardWidgetAppViewResult",
    "BoardEventParams",
    "BoardPromptAuthorizeParams",
    "BoardDataReadParams",
    "BoardActionParams",
    "BoardChangedEvent",
    "BoardFocusTabCommand",
    "BoardSetChatDockCommand",
    "AuthProbeStatus",
    "ConnectParams",
    "WorkerAdmissionHandshake",
    "RequestFrame",
    "PresenceEntry",
    "StateVersion",
    "ErrorShape",
    "MissingScopeErrorDetails",
    "McpAppViewExpiredErrorDetails",
    "UnknownAgentIdErrorDetails",
    "WizardNotFoundErrorDetails",
    "GatewaySuspendTaskBlocker",
    "GatewaySuspendPrepareParams",
    "GatewaySuspendStatusParams",
    "GatewaySuspendStatusRunningResult",
    "GatewaySuspendStatusReadyResult",
    "GatewaySuspendResumeParams",
    "GatewaySuspendResumeResult",
    "EnvironmentStatus",
    "WorkerEnvironmentState",
    "WorkerTunnelStatus",
    "EnvironmentsCreateParams",
    "EnvironmentsDestroyParams",
    "EnvironmentsListParams",
    "EnvironmentsStatusParams",
    "SystemInfoParams",
    "SystemInfoResult",
    "AgentEvent",
    "ConversationSendParams",
    "ConversationSendResult",
    "ConversationListItem",
    "ConversationListParams",
    "ConversationTurnCancelParams",
    "ConversationTurnCancelResult",
    "ConversationTurnParams",
    "ConversationTurnReply",
    "MessageActionParams",
    "SendParams",
    "PollParams",
    "AgentParams",
    "AgentIdentityParams",
    "AgentIdentityResult",
    "AgentWaitParams",
    "WakeParams",
    "WorktreeRecord",
    "WorktreesListParams",
    "WorktreesCreateParams",
    "WorktreesRemoveParams",
    "WorktreesRemoveResult",
    "WorktreesRestoreParams",
    "WorktreesGcParams",
    "WorktreesGcResult",
    "WorktreeBranch",
    "WorktreeRepositoryStatus",
    "WorktreesBranchesParams",
    "FsDirEntry",
    "FsListDirParams",
    "NodePairListParams",
    "NodePairApproveParams",
    "NodePairRejectParams",
    "NodePairRemoveParams",
    "NodeRenameParams",
    "NodeListParams",
    "NodePluginToolDescriptor",
    "NodeSkillDescriptor",
    "NodePendingAckParams",
    "NodeDescribeParams",
    "NodeInvokeParams",
    "NodeInvokeInputEvent",
    "NodeInvokeProgressParams",
    "NodeInvokeResultParams",
    "NodeInvokeRequestEvent",
    "NodeEventParams",
    "NodeEventResult",
    "NodePresenceAliveReason",
    "NodePresenceActivityPayload",
    "NodePendingDrainParams",
    "NodePendingDrainResult",
    "NodePendingEnqueueParams",
    "NodePendingEnqueueResult",
    "PushTestParams",
    "PushTestResult",
    "UiSplitCommand",
    "UiClosePaneCommand",
    "UiFocusCommand",
    "UiSidebarCommand",
    "UiPanelCommand",
    "UiNavigateCommand",
    "UiCommandResult",
    "SecretsReloadParams",
    "SecretsResolveParams",
    "SecretsResolveAssignment",
    "SessionsListParams",
    "SessionCatalogCapabilities",
    "SessionCatalogPullRequestSummary",
    "SessionCatalogTranscriptItem",
    "SessionsCatalogListParams",
    "SessionsCatalogReadParams",
    "SessionsCatalogContinueParams",
    "SessionsCatalogContinueResult",
    "SessionsCatalogArchiveParams",
    "SessionsCatalogArchiveResult",
    "SessionsCleanupParams",
    "SessionsPreviewParams",
    "SessionsDescribeParams",
    "SessionsResolveParams",
    "SessionsSearchHit",
    "SessionsSearchParams",
    "SessionCompactionCheckpoint",
    "SessionOperationEvent",
    "SessionCreatedActor",
    "SessionObserverHealth",
    "SessionObserverPlanProgress",
    "SessionCompanionExchange",
    "SessionsCompanionAskParams",
    "SessionsCompanionAskResult",
    "SessionsCompanionResetParams",
    "SessionsCompanionResetResult",
    "SessionsCompanionStateParams",
    "SessionsObserverVisibilityParams",
    "SessionsObserverVisibilityResult",
    "SessionVisibility",
    "SessionSharingIdentity",
    "SessionSharingRole",
    "SessionMembersListParams",
    "SessionMember",
    "SessionMemberAddParams",
    "SessionMemberRemoveParams",
    "SessionMemberMutationResult",
    "SessionSharingAction",
    "SessionSuggestionState",
    "SessionSuggestionAction",
    "SessionSuggestionResolution",
    "SessionSuggestionsAddParams",
    "SessionSuggestionsListParams",
    "SessionTypingParams",
    "SessionTypingResult",
    "SessionPlacementState",
    "LocalSessionPlacement",
    "RequestedSessionPlacement",
    "ProvisioningSessionPlacement",
    "SyncingSessionPlacement",
    "StartingSessionPlacement",
    "ActiveWorkerSessionPlacement",
    "DrainingSessionPlacement",
    "ReconcilingSessionPlacement",
    "ReclaimedSessionPlacement",
    "FailedSessionPlacement",
    "SessionsDispatchParams",
    "SessionsReclaimParams",
    "SessionDiscussionState",
    "SessionDiscussionInfoParams",
    "SessionDiscussionOpenParams",
    "SessionsCompactionListParams",
    "SessionsCompactionGetParams",
    "SessionsCompactionBranchParams",
    "SessionsCompactionRestoreParams",
    "SessionsRewindParams",
    "SessionsRewindResult",
    "SessionsForkParams",
    "SessionsForkResult",
    "SessionBranch",
    "SessionsBranchesListParams",
    "SessionsBranchesSwitchParams",
    "SessionsBranchesSwitchResult",
    "SessionFileKind",
    "SessionFilePreviewKind",
    "SessionFileRelevance",
    "SessionsFilesListParams",
    "SessionsFilesGetParams",
    "SessionsFilesRevealParams",
    "SessionsFilesRevealResult",
    "SessionsFilesSetParams",
    "SessionDiffFileStatus",
    "SessionsDiffParams",
    "SessionWorktreeInfo",
    "SessionsSendParams",
    "SessionsMessagesSubscribeParams",
    "SessionsMessagesUnsubscribeParams",
    "SessionsViewerPresenceSetParams",
    "SessionsViewerPresenceSetResult",
    "SessionsAbortParams",
    "SessionsPatchParams",
    "SessionsPluginPatchParams",
    "SessionsPluginPatchResult",
    "SessionsResetParams",
    "SessionsDeleteParams",
    "SessionGroup",
    "SessionsGroupsListParams",
    "SessionsGroupsPutParams",
    "SessionsGroupsRenameParams",
    "SessionsGroupsDeleteParams",
    "SessionsCompactParams",
    "SessionsUsageParams",
    "AuditActivityInboundMessageV1",
    "AuditActivityListParams",
    "AuditListParams",
    "TaskSuggestion",
    "TaskSuggestionResolution",
    "TaskSuggestionsAcceptParams",
    "TaskSuggestionsAcceptResult",
    "TaskSuggestionsCreateParams",
    "TaskSuggestionsDismissParams",
    "TaskSuggestionsDismissResult",
    "TaskSuggestionsListParams",
    "TaskSummary",
    "TasksListParams",
    "TasksGetParams",
    "TasksCancelParams",
    "ConfigGetParams",
    "ConfigSetParams",
    "ConfigApplyParams",
    "ConfigPatchParams",
    "ConfigSchemaParams",
    "ConfigSchemaLookupParams",
    "ConfigSchemaResponse",
    "ConfigSchemaLookupResult",
    "SystemAgentChatParams",
    "SystemAgentChatResult",
    "SystemAgentChatHistoryParams",
    "SystemAgentChatHistoryTurn",
    "SystemChangeKind",
    "SystemChangeSource",
    "SystemChangesListParams",
    "SystemAgentSetupDetectParams",
    "SystemAgentSetupDetectResult",
    "SystemAgentSetupVerifyParams",
    "SystemAgentSetupVerifyResult",
    "SystemAgentSetupActivateParams",
    "SystemAgentSetupActivateResult",
    "SystemAgentSetupAuthStartParams",
    "WizardStartParams",
    "WizardNextParams",
    "WizardCancelParams",
    "WizardStatusParams",
    "WizardStep",
    "WizardStatusResult",
    "TalkModeParams",
    "TalkEvent",
    "TalkCatalogParams",
    "TalkCatalogResult",
    "TalkClientCreateParams",
    "TalkClientCreateResult",
    "TalkClientCloseParams",
    "TalkClientMutationResult",
    "TalkClientSteerParams",
    "TalkAgentControlResult",
    "TalkClientToolCallParams",
    "TalkClientToolCallResult",
    "TalkClientTranscriptParams",
    "TalkConfigParams",
    "TalkConfigResult",
    "TalkSessionAppendAudioParams",
    "TalkSessionAcknowledgeMarkParams",
    "TalkSessionCancelOutputParams",
    "TalkSessionCancelTurnParams",
    "TalkSessionCreateParams",
    "TalkSessionCreateResult",
    "TalkSessionJoinParams",
    "TalkSessionTurnParams",
    "TalkSessionSteerParams",
    "TalkSessionSubmitToolResultParams",
    "TalkSessionCloseParams",
    "TalkSessionOkResult",
    "TalkSpeakParams",
    "TalkSpeakResult",
    "TtsSpeakParams",
    "TtsSpeakResult",
    "ChannelsStatusParams",
    "ChannelsStatusResult",
    "ChannelsPairingListParams",
    "ChannelsPairingListResult",
    "ChannelsPairingApproveParams",
    "ChannelsPairingApproveResult",
    "ChannelsPairingDismissParams",
    "ChannelsPairingDismissResult",
    "ChannelsStartParams",
    "ChannelsStopParams",
    "ChannelsLogoutParams",
    "WebLoginStartParams",
    "WebLoginWaitParams",
    "AgentKind",
    "AgentsCreateParams",
    "AgentsCreateResult",
    "AgentsUpdateParams",
    "AgentsUpdateResult",
    "AgentsDeleteParams",
    "AgentsDeleteResult",
    "AgentsFileEntry",
    "AgentsFilesListParams",
    "AgentsFilesGetParams",
    "AgentsFilesSetParams",
    "AgentsWorkspaceEntry",
    "AgentsWorkspaceFile",
    "AgentsWorkspaceListParams",
    "AgentsWorkspaceGetParams",
    "ArtifactSummary",
    "ArtifactsListParams",
    "ArtifactsGetParams",
    "ArtifactsDownloadParams",
    "AgentsListParams",
    "ModelChoice",
    "ModelsAuthLogoutParams",
    "ModelsAuthStatusParams",
    "ModelsListParams",
    "ModelsProbeParams",
    "CommandEntry",
    "CommandsListParams",
    "SkillsStatusParams",
    "ToolsCatalogParams",
    "ToolCatalogProfile",
    "ToolCatalogEntry",
    "ToolsEffectiveParams",
    "ToolsEffectiveEntry",
    "ToolsEffectiveNotice",
    "ToolsInvokeParams",
    "ToolsInvokeError",
    "SkillsBinsParams",
    "SkillsBinsResult",
    "SkillsSearchParams",
    "SkillsSearchResult",
    "SkillsDetailParams",
    "SkillsDetailResult",
    "SkillsCuratorActionParams",
    "SkillsCuratorActionResult",
    "SkillsCuratorStatusParams",
    "SkillsProposalsListParams",
    "SkillsProposalsListResult",
    "SkillsProposalEvaluateParams",
    "SkillsProposalEventsListParams",
    "SkillsProposalEventsListResult",
    "SkillsProposalHistoryStatusParams",
    "SkillsProposalHistoryScanParams",
    "SkillsProposalHistoryScanResult",
    "SkillsProposalInspectParams",
    "SkillsProposalCreateParams",
    "SkillsProposalUpdateParams",
    "SkillsProposalReviseParams",
    "SkillsProposalRequestRevisionParams",
    "SkillsProposalRequestRevisionResult",
    "SkillsProposalActionParams",
    "SkillsProposalRecordResult",
    "SkillsSecurityVerdictsParams",
    "SkillsSecurityVerdictsResult",
    "SkillsSkillCardParams",
    "SkillsSkillCardResult",
    "SkillsUploadBeginParams",
    "SkillsUploadChunkParams",
    "SkillsUploadCommitParams",
    "SkillsInstallParams",
    "SkillsUpdateParams",
    "CronJob",
    "CronListParams",
    "CronStatusParams",
    "CronAddParams",
    "CronUpdateParams",
    "CronRunParams",
    "CronRunsParams",
    "CronScratchGetResult",
    "CronScratchSetParams",
    "CronScratchSetResult",
    "CronRunLogEntry",
    "LogsTailParams",
    "LogsTailResult",
    "MemoryMigrationItemStatus",
    "MemoryMigrationSummary",
    "MigrationsMemoryPlanParams",
    "MigrationsMemoryApplyParams",
    "TerminalOpenResult",
    "TerminalInputParams",
    "TerminalResizeParams",
    "TerminalCloseParams",
    "TerminalAttachParams",
    "TerminalAttachResult",
    "TerminalSessionInfo",
    "TerminalTextParams",
    "TerminalTextResult",
    "TerminalUploadParams",
    "TerminalUploadResult",
    "TerminalAckResult",
    "TerminalDataEvent",
    "TerminalExitEvent",
    "ApprovalKind",
    "ApprovalDecision",
    "ApprovalAllowDecision",
    "ApprovalAllowedReason",
    "ApprovalDeniedReason",
    "ApprovalExpiredReason",
    "ApprovalCancelledReason",
    "PluginApprovalSeverity",
    "SystemAgentApprovalPresentation",
    "ApprovalTerminalReason",
    "ApprovalGetParams",
    "ExecApprovalsGetParams",
    "ExecApprovalsSetParams",
    "ExecApprovalsNodeGetParams",
    "ExecApprovalsNodeSnapshot",
    "ExecApprovalsNodeSetParams",
    "ExecApprovalsSnapshot",
    "ExecApprovalGetParams",
    "ExecApprovalRequestParams",
    "ExecApprovalResolveParams",
    "QuestionOption",
    "QuestionAnswers",
    "QuestionStatus",
    "QuestionRequestResult",
    "QuestionWaitAnswerParams",
    "QuestionGetParams",
    "QuestionListParams",
    "PluginApprovalRequestParams",
    "PluginApprovalResolveParams",
    "PluginCatalogClawHubInstall",
    "PluginCatalogOfficialInstall",
    "PluginControlUiDescriptor",
    "PluginSearchPackage",
    "PluginsListParams",
    "PluginsRefreshParams",
    "PluginsRefreshResult",
    "PluginsSearchParams",
    "PluginsSessionActionFailureResult",
    "PluginsSessionActionParams",
    "PluginsSessionActionSuccessResult",
    "PluginsSetEnabledParams",
    "PluginsUiDescriptorsParams",
    "PluginsUninstallParams",
    "PluginsUninstallResult",
    "DevicePairListParams",
    "DevicePairApproveParams",
    "DevicePairRejectParams",
    "DevicePairRemoveParams",
    "DevicePairSetupCodeParams",
    "DevicePairSetupCodeResult",
    "DevicePairRenameParams",
    "DeviceTokenRotateParams",
    "DeviceTokenRevokeParams",
    "DevicePairRequestedEvent",
    "DevicePairResolvedEvent",
    "ChatHistoryParams",
    "ChatMetadataParams",
    "ChatMessageGetParams",
    "ChatMessageGetResult",
    "ChatToolTitlesParams",
    "ChatToolTitlesResult",
    "ChatSendParams",
    "ChatAbortParams",
    "ChatInjectParams",
    "ChatRunStartupPhase",
    "ChatDeltaEvent",
    "ChatFinalEvent",
    "ChatAbortedEvent",
    "ChatErrorEvent",
    "UpdateStatusParams",
    "UpdateRunParams",
    "TickEvent",
    "ShutdownEvent",
    "GatewayServer",
    "GatewayFeatures",
    "ChatSendAck",
    "BoardWidget",
    "BoardOp",
    "BoardWidgetMcpAppContent",
    "BoardWidgetPutContent",
    "BoardCommand",
    "ResponseFrame",
    "EventFrame",
    "Snapshot",
    "GatewayErrorDetails",
    "GatewaySuspendBlocker",
    "GatewaySuspendStatusResult",
    "WorkerEnvironmentMetadata",
    "ConversationListResult",
    "ConversationTurnResult",
    "WorktreesListResult",
    "WorktreesBranchesResult",
    "FsListDirResult",
    "NodePluginToolsUpdateParams",
    "NodeSkillsUpdateParams",
    "NodePresenceAlivePayload",
    "UiCommand",
    "SecretsResolveResult",
    "SessionCatalogDescriptor",
    "SessionCatalogSession",
    "SessionsCatalogReadResult",
    "SessionsSearchResult",
    "SessionObserverDigest",
    "SessionRow",
    "SessionsCompanionStateResult",
    "SessionVisibilitySetParams",
    "SessionVisibilitySetResult",
    "SessionMembersListResult",
    "SessionSharingEvent",
    "SessionSuggestion",
    "SessionSuggestionsResolveParams",
    "SessionTypingEvent",
    "SessionPlacement",
    "SessionsDispatchResult",
    "SessionsReclaimResult",
    "SessionDiscussionInfo",
    "SessionDiscussionInfoResult",
    "SessionDiscussionOpenResult",
    "SessionsCompactionListResult",
    "SessionsCompactionGetResult",
    "SessionsCompactionBranchResult",
    "SessionsCompactionRestoreResult",
    "SessionsBranchesListResult",
    "SessionFileBrowserEntry",
    "SessionFileEntry",
    "SessionDiffFile",
    "SessionsCreateParams",
    "SessionsCreateResult",
    "SessionsGroupsListResult",
    "SessionsGroupsMutationResult",
    "AuditActivityAgentRunV1",
    "AuditActivityToolActionV1",
    "AuditActivityOutboundMessageV1",
    "AuditEvent",
    "TaskSuggestionEvent",
    "TaskSuggestionsCreateResult",
    "TaskSuggestionsListResult",
    "TasksListResult",
    "TasksGetResult",
    "TasksCancelResult",
    "SystemAgentChatHistoryResult",
    "SystemChangeEntry",
    "SystemAgentSetupAuthStartResult",
    "WizardNextResult",
    "WizardStartResult",
    "TalkSessionJoinResult",
    "TalkSessionTurnResult",
    "AgentSummary",
    "AgentsFilesListResult",
    "AgentsFilesGetResult",
    "AgentsFilesSetResult",
    "AgentsWorkspaceListResult",
    "AgentsWorkspaceGetResult",
    "ArtifactsListResult",
    "ArtifactsGetResult",
    "ArtifactsDownloadResult",
    "ModelsListResult",
    "ModelsProbeTargetResult",
    "CommandsListResult",
    "ToolCatalogGroup",
    "ToolsEffectiveGroup",
    "ToolsInvokeResult",
    "SkillsCuratorStatusResult",
    "SkillsProposalEvaluateResult",
    "SkillsProposalInspectResult",
    "SkillsProposalApplyResult",
    "CronGetParams",
    "CronDeclarativeAddResult",
    "CronRemoveParams",
    "CronScratchGetParams",
    "MemoryMigrationItem",
    "TerminalOpenParams",
    "TerminalListResult",
    "TerminalEvent",
    "ExecApprovalPresentation",
    "PluginApprovalPresentation",
    "ApprovalHistoryParams",
    "ApprovalResolveParams",
    "Question",
    "QuestionRequestQuestion",
    "QuestionWaitAnswerResult",
    "QuestionResolveParams",
    "QuestionResolveResult",
    "QuestionResolvedEvent",
    "PluginCatalogInstallAction",
    "PluginSearchResultEntry",
    "PluginsInstallParams",
    "PluginsSessionActionResult",
    "PluginsUiDescriptorsResult",
    "ChatStatusEvent",
    "GatewayPolicy",
    "BoardSnapshot",
    "BoardWidgetContent",
    "BoardUpdateParams",
    "BoardWidgetPutParams",
    "BoardCommandEvent",
    "HelloOk",
    "GatewayFrame",
    "GatewaySuspendPrepareBusyResult",
    "GatewaySuspendPrepareReadyResult",
    "EnvironmentSummary",
    "EnvironmentsCreateResult",
    "EnvironmentsDestroyResult",
    "EnvironmentsStatusResult",
    "UiCommandParams",
    "SessionCatalogHost",
    "SessionSuggestionsAddResult",
    "SessionSuggestionsListResult",
    "SessionSuggestionsResolveResult",
    "SessionSuggestionEvent",
    "SessionFileBrowserResult",
    "SessionsFilesGetResult",
    "SessionsFilesSetResult",
    "SessionsDiffResult",
    "AuditActivityEventV1",
    "AuditListResult",
    "SystemChangesListResult",
    "AgentsListResult",
    "ModelsProbeResult",
    "ToolsCatalogResult",
    "ToolsEffectiveResult",
    "CronAddResult",
    "MemoryMigrationProviderPlan",
    "MigrationsMemoryApplyResult",
    "ApprovalPresentation",
    "QuestionRecord",
    "QuestionRequestParams",
    "PluginCatalogEntry",
    "PluginsSearchResult",
    "ChatEvent",
    "GatewaySuspendPrepareResult",
    "EnvironmentsListResult",
    "SessionCatalog",
    "SessionsFilesListResult",
    "AuditActivityListResult",
    "MigrationsMemoryPlanResult",
    "PendingApprovalSnapshot",
    "AllowedApprovalSnapshot",
    "DeniedApprovalSnapshot",
    "ExpiredApprovalSnapshot",
    "CancelledApprovalSnapshot",
    "QuestionGetResult",
    "QuestionListResult",
    "PluginsInstallResult",
    "PluginsListResult",
    "PluginsSetEnabledResult",
    "SessionsCatalogListResult",
    "ApprovalSnapshot",
    "TerminalApprovalSnapshot",
    "PendingSessionApprovalEvent",
    "SessionApprovalReplay",
    "ApprovalGetResult",
    "ApprovalHistoryResult",
    "ApprovalResolveResult",
    "TerminalSessionApprovalEvent",
    "SessionApprovalEvent",
    "BoardTabChatDock",
    "BoardWidgetContentKind",
    "BoardWidgetPresentation",
    "BoardWidgetHeightMode",
    "BoardWidgetGrantState",
    "BoardWidgetGrantDecision",
    "SnapshotAuthMode",
    "GatewaySuspendTaskBlockerRuntime",
    "GatewaySuspendBlockerKind",
    "GatewaySuspendPrepareBusyReason",
    "ConversationSendStatus",
    "ConversationListItemKind",
    "MessageActionInboundTurnKind",
    "AgentPromptMode",
    "AgentBootstrapContextMode",
    "AgentBootstrapContextRunKind",
    "AgentSessionEffects",
    "AgentSourceReplyDeliveryMode",
    "AgentIdentityAvatarStatus",
    "WakeMode",
    "WorktreeRecordOwnerKind",
    "WorktreeBranchKind",
    "NodePendingEnqueueType",
    "NodePendingEnqueuePriority",
    "PushTestEnvironment",
    "PushTestTransport",
    "UiSplitCommandDirection",
    "UiPanelCommandPanel",
    "UiPanelCommandDock",
    "SessionsListSortBy",
    "SessionsListBoardFace",
    "SessionCatalogPullRequestSummaryState",
    "SessionCatalogHostKind",
    "SessionCatalogTranscriptItemType",
    "SessionsSearchHitRole",
    "SessionCompactionCheckpointReason",
    "SessionOperationEventPhase",
    "SessionCreatedActorType",
    "SessionRowKind",
    "SessionRowStatus",
    "SessionRowSubagentRole",
    "SessionRowSubagentControlScope",
    "SessionRowCreatedVia",
    "SessionFileBrowserEntryKind",
    "SessionFileEntryContentEncoding",
    "SessionsDiffUnavailableReason",
    "SessionsResetReason",
    "SessionsUsageMode",
    "SessionsUsageRange",
    "SessionsUsageGroupBy",
    "AuditActivityAgentRunV1Action",
    "AuditActivityAgentRunV1Status",
    "AuditActivityAgentRunV1ErrorCode",
    "AuditActivityToolActionV1Action",
    "AuditActivityToolActionV1Status",
    "AuditActivityToolActionV1ErrorCode",
    "AuditActivityInboundMessageV1ConversationKind",
    "AuditActivityInboundMessageV1Status",
    "AuditActivityInboundMessageV1Outcome",
    "AuditActivityInboundMessageV1ReasonCode",
    "AuditActivityOutboundMessageV1DeliveryKind",
    "AuditActivityOutboundMessageV1Status",
    "AuditActivityOutboundMessageV1Outcome",
    "AuditActivityOutboundMessageV1ErrorCode",
    "AuditActivityOutboundMessageV1ReasonCode",
    "AuditActivityOutboundMessageV1FailureStage",
    "AuditActivityListKind",
    "AuditActivityListDirection",
    "AuditEventKind",
    "AuditEventAction",
    "AuditEventErrorCode",
    "TaskSummaryStatus",
    "ConfigSchemaLookupReloadKind",
    "SystemAgentChatWelcomeVariant",
    "SystemAgentChatAction",
    "SystemAgentSetupActivateStatus",
    "SystemAgentSetupAuthStartStatus",
    "WizardStartFlow",
    "WizardStepType",
    "WizardStepFormat",
    "WizardStepExecutor",
    "TalkEventType",
    "TalkEventMode",
    "TalkEventTransport",
    "TalkEventBrain",
    "TalkClientSteerMode",
    "TalkAgentControlTarget",
    "ChannelsPairingApproveNotification",
    "ChannelsPairingApproveCommandOwnerBootstrap",
    "AgentsListScope",
    "ModelsListView",
    "CommandEntryCategory",
    "CommandEntrySource",
    "CommandEntryScope",
    "ToolCatalogProfileId",
    "ToolCatalogEntrySource",
    "ToolCatalogEntryRisk",
    "ToolsEffectiveEntrySource",
    "ToolsEffectiveNoticeSeverity",
    "SkillsCuratorActionState",
    "SkillsProposalHistoryScanDirection",
    "SkillsProposalRequestRevisionStatus",
    "SkillsProposalRecordKind",
    "SkillsProposalRecordStatus",
    "SkillsProposalRecordCreatedBy",
    "CronJobWakeMode",
    "CronJobLastRunStatus",
    "CronJobLastDeliveryStatus",
    "CronListEnabled",
    "CronListScheduleKind",
    "CronListLastRunStatus",
    "CronListSortBy",
    "CronListSortDir",
    "CronRunsScope",
    "CronRunsStatus",
    "CronRunLogEntryErrorReason",
    "TerminalExitEventReason",
    "ExecApprovalsNodeSnapshotDefaultAction",
    "PluginApprovalRequestSeverity",
    "PluginCatalogEntryState",
    "PluginControlUiDescriptorSurface",
    "PluginSearchPackageFamily",
    "PluginSearchPackageChannel",
    "DevicePairSetupCodeBootstrapProfile",
    "DevicePairSetupCodeAuth",
    "DevicePairSetupCodeAccess",
    "ChatMessageGetUnavailableReason",
    "ChatSendQueueMode",
    "ChatErrorEventErrorKind",
    "ChatSendStatus",
    "parse_generated_event",
]
