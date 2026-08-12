import hashlib

import pytest

from openclaw_codegen.generator import schema


def test_validate_schema_digest_returns_matching_digest() -> None:
    raw = b'{"a": 1}'
    digest = hashlib.sha256(raw).hexdigest()
    assert schema._validate_schema_digest(raw, {"sha256": digest}) == digest


def test_validate_schema_digest_rejects_mismatch() -> None:
    with pytest.raises(RuntimeError, match="schema SHA-256 mismatch"):
        schema._validate_schema_digest(b"data", {"sha256": "deadbeef"})


def test_operation_overrides_must_name_a_known_model() -> None:
    with pytest.raises(RuntimeError, match=r"operation override a.params names unknown model 'Missing'"):
        schema._validate_operation_overrides({"a": {"params": "Missing"}}, {"AParams": {}})


def test_operation_overrides_accept_external_and_defined_models() -> None:
    overrides = {"a": {"params": "AParams", "result": "some_module:External"}}
    schema._validate_operation_overrides(overrides, {"AParams": {}})
