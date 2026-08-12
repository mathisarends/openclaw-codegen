import inspect
import json
import subprocess
import sys
from enum import StrEnum
from pathlib import Path
from typing import Any, get_args

import pytest
from pydantic import ValidationError

from openclaw_codegen.generated.clients import AgentsClient, ChatClient, SessionsClient, UsageClient
from openclaw_codegen.generated.clients import chat as chat_client
from openclaw_codegen.generated.clients import sessions as sessions_client
from openclaw_codegen.generated.clients.chat import ChatMethod
from openclaw_codegen.generated.clients.sessions import SessionsMethod
from openclaw_codegen.generated.events import parse_event_payload
from openclaw_codegen.generated.protocol import (
    ChatFinalEvent,
    ChatHistoryParams,
    ChatSendAck,
    ChatSendQueueMode,
    SessionDiscussionState,
    SessionsFilesListResult,
    SessionVisibility,
)

_PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def test_generated_files_are_current() -> None:
    subprocess.run(
        [sys.executable, str(_PACKAGE_ROOT / "scripts" / "generate.py"), "--check"],
        check=True,
    )


def test_generation_report_covers_schema() -> None:
    report = json.loads((_PACKAGE_ROOT / "schema" / "generation-report.json").read_text(encoding="utf-8"))
    assert report["counts"]["definitions"] == 659
    assert report["counts"]["methods"] == 350
    assert report["counts"]["generated_domains"] == 55
    assert report["counts"]["generated_operations"] == 350
    assert "chat.history" in report["unresolved_methods"]["schema_gap"]
    assert report["unresolved_methods"]["naming_mismatch"]["skills.curator.pin"] == {
        "params": "SkillsCuratorActionParams",
        "result": "SkillsCuratorActionResult",
    }
    assert report["normalized_matches"]["conversations.list"] == {
        "params": "ConversationListParams",
        "result": "ConversationListResult",
    }


def test_generated_constraints_and_aliases() -> None:
    params = ChatHistoryParams(session_key="agent:main:main", limit=1000)
    assert params.model_dump(by_alias=True, exclude_none=True) == {
        "sessionKey": "agent:main:main",
        "limit": 1000,
    }
    with pytest.raises(ValidationError):
        ChatHistoryParams(session_key="agent:main:main", limit=1001)

    acknowledgement = ChatSendAck(run_id="run-1", status="started")
    assert acknowledgement.model_dump(by_alias=True, exclude_none=True) == {
        "runId": "run-1",
        "status": "started",
    }


def test_client_methods_expose_flat_keyword_only_inputs() -> None:
    parameters = inspect.signature(ChatClient.send).parameters
    assert "params" not in parameters
    assert all(parameter.kind is not inspect.Parameter.VAR_KEYWORD for parameter in parameters.values())
    assert parameters["session_key"].kind is inspect.Parameter.KEYWORD_ONLY
    assert ChatSendQueueMode in get_args(parameters["queue_mode"].annotation)
    assert hasattr(ChatClient, "get_message")
    assert not hasattr(chat_client, "ChatMessageClient")
    assert hasattr(SessionsClient, "list_files")
    assert not hasattr(sessions_client, "SessionsFilesClient")


def test_methods_without_a_schema_contract_expose_a_params_passthrough() -> None:
    parameters = inspect.signature(UsageClient.cost).parameters
    assert parameters["params"].kind is inspect.Parameter.KEYWORD_ONLY
    assert parameters["params"].default is None
    assert parameters["params"].annotation == dict[str, Any] | None
    assert inspect.signature(UsageClient.cost).return_annotation is Any


def test_generated_clients_are_flat_modules() -> None:
    generated = _PACKAGE_ROOT / "openclaw_codegen" / "generated"
    assert (generated / "clients" / "chat.py").is_file()
    assert (generated / "clients" / "sessions.py").is_file()
    assert (generated / "clients" / "agents.py").is_file()
    assert not (generated / "chat").is_dir()
    assert AgentsClient.__module__ == "openclaw_codegen.generated.clients.agents"
    assert (generated / "protocol.py").is_file()


def test_string_value_sets_are_str_enums_and_nested_names_are_specific() -> None:
    assert issubclass(SessionVisibility, StrEnum)
    assert issubclass(SessionDiscussionState, StrEnum)
    assert inspect.signature(SessionsClient.list_files).return_annotation is SessionsFilesListResult
    assert ChatMethod.MESSAGE_GET == "chat.message.get"
    assert SessionsMethod.FILES_LIST == "sessions.files.list"


def test_known_event_payload_is_typed_and_unknown_event_stays_raw() -> None:
    payload = {"runId": "run-1", "sessionKey": "session-1", "seq": 1, "state": "final"}
    parsed = parse_event_payload("chat", payload)
    assert isinstance(parsed, ChatFinalEvent)

    unknown = {"new": "shape"}
    assert parse_event_payload("plugin.new-event", unknown) is unknown
