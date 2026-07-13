class GeoAgentError(Exception):
    """Base exception for the geo agent."""


class CapabilityError(GeoAgentError):
    """Raised when a capability is unavailable."""

