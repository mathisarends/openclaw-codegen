import platform

import pytest
from pydantic import ValidationError

from openclaw_codegen.connection import PROTOCOL_VERSION, ConnectChallenge, GatewayAuth, GatewayClientInfo


def test_protocol_version_is_pinned() -> None:
    assert PROTOCOL_VERSION == 4


def test_gateway_client_info_defaults_and_camel_case_dump() -> None:
    info = GatewayClientInfo()
    assert info.id == "gateway-client"
    assert info.mode == "backend"
    assert info.version == "0.1.0"
    assert info.platform == platform.system()
    assert info.display_name is None
    assert info.instance_id is None
    assert info.model_dump(by_alias=True, exclude_none=True) == {
        "id": "gateway-client",
        "version": "0.1.0",
        "platform": platform.system(),
        "mode": "backend",
    }


def test_gateway_client_info_rejects_unknown_fields_and_wrong_id() -> None:
    with pytest.raises(ValidationError):
        GatewayClientInfo(id="something-else")
    with pytest.raises(ValidationError):
        GatewayClientInfo(unexpected="value")


def test_gateway_auth_defaults_to_no_credentials_and_uses_camel_case_alias() -> None:
    auth = GatewayAuth(device_token="token-1")
    assert auth.token is None
    assert auth.password is None
    assert auth.model_dump(by_alias=True, exclude_none=True) == {"deviceToken": "token-1"}


@pytest.mark.parametrize(
    ("nonce", "ts"),
    [
        ("", 1737264000000),
        ("nonce", -1),
    ],
)
def test_connect_challenge_rejects_invalid_nonce_or_timestamp(nonce: str, ts: int) -> None:
    with pytest.raises(ValidationError):
        ConnectChallenge(nonce=nonce, ts=ts)


def test_connect_challenge_accepts_a_valid_payload() -> None:
    challenge = ConnectChallenge(nonce="nonce", ts=0)
    assert challenge.nonce == "nonce"
    assert challenge.ts == 0
