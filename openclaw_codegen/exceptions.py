from openclaw_codegen.generated.protocol import ErrorShape


class OpenClawClientError(Exception):
    """Base exception raised by the OpenClaw client."""


class OpenClawProtocolError(OpenClawClientError):
    """The peer sent a frame that violates the expected gateway protocol."""


class OpenClawCompatibilityWarning(UserWarning):
    """The gateway may not match the schema version used by this client."""


class OpenClawNotConnectedError(OpenClawClientError):
    """An operation requires an active gateway connection."""


class OpenClawGatewayError(OpenClawClientError):
    """A gateway RPC returned an error response."""

    def __init__(self, error: ErrorShape) -> None:
        super().__init__(f"{error.code}: {error.message}")
        self.error = error

    @property
    def code(self) -> str:
        return self.error.code

    @property
    def retryable(self) -> bool | None:
        return self.error.retryable
