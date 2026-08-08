"""Generated direct RPC client accessors. Do not edit manually."""

from functools import cached_property
from typing import cast

from openclaw_codegen.generated.clients import (
    AgentClient,
    AgentsClient,
    ApprovalClient,
    ArtifactsClient,
    AssistantClient,
    AttachClient,
    AuditClient,
    BoardClient,
    ChannelsClient,
    ChatClient,
    CommandsClient,
    ConfigClient,
    ControlUiClient,
    ConversationsClient,
    CronClient,
    DeviceClient,
    DiagnosticsClient,
    DoctorClient,
    EnvironmentsClient,
    ExecClient,
    FsClient,
    GatewayClient,
    LogsClient,
    McpClient,
    MemoryClient,
    MessageClient,
    MigrationsClient,
    ModelsClient,
    NativeHookClient,
    NodeClient,
    OpenclawClient,
    PluginClient,
    PluginsClient,
    PushClient,
    QuestionClient,
    RootClient,
    SecretsClient,
    SessionClient,
    SessionsClient,
    SkillsClient,
    SystemClient,
    TalkClient,
    TasksClient,
    TaskSuggestionsClient,
    TerminalClient,
    ToolsClient,
    TtsClient,
    UiClient,
    UpdateClient,
    UsageClient,
    UsersClient,
    VoicewakeClient,
    WebClient,
    WizardClient,
    WorktreesClient,
)
from openclaw_codegen.generated.clients._requester import Requester


class OpenClawClients:
    """Typed, lazily-created RPC clients for an OpenClaw requester."""

    @property
    def _requester(self) -> Requester:
        return cast(Requester, self)

    @cached_property
    def root(self) -> RootClient:
        return RootClient(self._requester)

    @cached_property
    def diagnostics(self) -> DiagnosticsClient:
        return DiagnosticsClient(self._requester)

    @cached_property
    def doctor(self) -> DoctorClient:
        return DoctorClient(self._requester)

    @cached_property
    def logs(self) -> LogsClient:
        return LogsClient(self._requester)

    @cached_property
    def channels(self) -> ChannelsClient:
        return ChannelsClient(self._requester)

    @cached_property
    def usage(self) -> UsageClient:
        return UsageClient(self._requester)

    @cached_property
    def tts(self) -> TtsClient:
        return TtsClient(self._requester)

    @cached_property
    def config(self) -> ConfigClient:
        return ConfigClient(self._requester)

    @cached_property
    def exec(self) -> ExecClient:
        return ExecClient(self._requester)

    @cached_property
    def question(self) -> QuestionClient:
        return QuestionClient(self._requester)

    @cached_property
    def plugin(self) -> PluginClient:
        return PluginClient(self._requester)

    @cached_property
    def plugins(self) -> PluginsClient:
        return PluginsClient(self._requester)

    @cached_property
    def openclaw(self) -> OpenclawClient:
        return OpenclawClient(self._requester)

    @cached_property
    def wizard(self) -> WizardClient:
        return WizardClient(self._requester)

    @cached_property
    def talk(self) -> TalkClient:
        return TalkClient(self._requester)

    @cached_property
    def commands(self) -> CommandsClient:
        return CommandsClient(self._requester)

    @cached_property
    def models(self) -> ModelsClient:
        return ModelsClient(self._requester)

    @cached_property
    def tools(self) -> ToolsClient:
        return ToolsClient(self._requester)

    @cached_property
    def mcp(self) -> McpClient:
        return McpClient(self._requester)

    @cached_property
    def board(self) -> BoardClient:
        return BoardClient(self._requester)

    @cached_property
    def audit(self) -> AuditClient:
        return AuditClient(self._requester)

    @cached_property
    def users(self) -> UsersClient:
        return UsersClient(self._requester)

    @cached_property
    def tasks(self) -> TasksClient:
        return TasksClient(self._requester)

    @cached_property
    def task_suggestions(self) -> TaskSuggestionsClient:
        return TaskSuggestionsClient(self._requester)

    @cached_property
    def environments(self) -> EnvironmentsClient:
        return EnvironmentsClient(self._requester)

    @cached_property
    def worktrees(self) -> WorktreesClient:
        return WorktreesClient(self._requester)

    @cached_property
    def fs(self) -> FsClient:
        return FsClient(self._requester)

    @cached_property
    def agents(self) -> AgentsClient:
        return AgentsClient(self._requester)

    @cached_property
    def sessions(self) -> SessionsClient:
        return SessionsClient(self._requester)

    @cached_property
    def artifacts(self) -> ArtifactsClient:
        return ArtifactsClient(self._requester)

    @cached_property
    def skills(self) -> SkillsClient:
        return SkillsClient(self._requester)

    @cached_property
    def update(self) -> UpdateClient:
        return UpdateClient(self._requester)

    @cached_property
    def voicewake(self) -> VoicewakeClient:
        return VoicewakeClient(self._requester)

    @cached_property
    def secrets(self) -> SecretsClient:
        return SecretsClient(self._requester)

    @cached_property
    def node(self) -> NodeClient:
        return NodeClient(self._requester)

    @cached_property
    def device(self) -> DeviceClient:
        return DeviceClient(self._requester)

    @cached_property
    def cron(self) -> CronClient:
        return CronClient(self._requester)

    @cached_property
    def gateway(self) -> GatewayClient:
        return GatewayClient(self._requester)

    @cached_property
    def message(self) -> MessageClient:
        return MessageClient(self._requester)

    @cached_property
    def conversations(self) -> ConversationsClient:
        return ConversationsClient(self._requester)

    @cached_property
    def agent(self) -> AgentClient:
        return AgentClient(self._requester)

    @cached_property
    def chat(self) -> ChatClient:
        return ChatClient(self._requester)

    @cached_property
    def terminal(self) -> TerminalClient:
        return TerminalClient(self._requester)

    @cached_property
    def assistant(self) -> AssistantClient:
        return AssistantClient(self._requester)

    @cached_property
    def push(self) -> PushClient:
        return PushClient(self._requester)

    @cached_property
    def attach(self) -> AttachClient:
        return AttachClient(self._requester)

    @cached_property
    def native_hook(self) -> NativeHookClient:
        return NativeHookClient(self._requester)

    @cached_property
    def web(self) -> WebClient:
        return WebClient(self._requester)

    @cached_property
    def control_ui(self) -> ControlUiClient:
        return ControlUiClient(self._requester)

    @cached_property
    def system(self) -> SystemClient:
        return SystemClient(self._requester)

    @cached_property
    def approval(self) -> ApprovalClient:
        return ApprovalClient(self._requester)

    @cached_property
    def migrations(self) -> MigrationsClient:
        return MigrationsClient(self._requester)

    @cached_property
    def ui(self) -> UiClient:
        return UiClient(self._requester)

    @cached_property
    def session(self) -> SessionClient:
        return SessionClient(self._requester)

    @cached_property
    def memory(self) -> MemoryClient:
        return MemoryClient(self._requester)


__all__ = ["OpenClawClients"]
