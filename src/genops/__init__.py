"""GenOps AI - OpenTelemetry-native governance for AI."""

__version__ = "0.1.0"

# Core instrumentation functions
from genops.core.context_manager import track
from genops.core.policy import enforce_policy
from genops.core.telemetry import GenOpsTelemetry
from genops.core.tracker import track_usage

# Auto-instrumentation system
from genops.auto_instrumentation import init, uninstrument, status, get_default_attributes

__all__ = [
    # Core functions
    "track_usage",
    "track", 
    "enforce_policy",
    "GenOpsTelemetry",
    # Auto-instrumentation
    "init",
    "uninstrument", 
    "status",
    "get_default_attributes",
]
