import pytest

from openclaw_codegen.exceptions import (
    OpenClawClientError,
    OpenClawGatewayError,
    OpenClawNotConnectedError,
    OpenClawProtocolError,
)
from openclaw_codegen.generated.protocol import ErrorShape


@pytest.mark.parametrize(
    "exception_type",
    [OpenClawProtocolError, OpenClawNotConnectedError, OpenClawGatewayError],
)
def test_client_exceptions_are_openclaw_codegen_errors(exception_type: type[Exception]) -> None:
    assert issubclass(exception_type, OpenClawClientError)


def test_gateway_error_exposes_code_and_message_from_the_error_shape() -> None:
    error = OpenClawGatewayError(ErrorShape(code="FORBIDDEN", message="missing scope"))
    assert error.code == "FORBIDDEN"
    assert str(error) == "FORBIDDEN: missing scope"
    assert error.retryable is None


def test_gateway_error_exposes_retryable_when_the_gateway_reports_it() -> None:
    error = OpenClawGatewayError(ErrorShape(code="UNAVAILABLE", message="try again", retryable=True))
    assert error.retryable is True
