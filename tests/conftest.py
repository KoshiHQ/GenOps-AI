"""Pytest configuration and shared fixtures for GenOps AI tests."""

from collections.abc import Generator
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

try:
    from opentelemetry.test.spantestutil import SpanRecorder
except ImportError:
    # Fallback implementation for SpanRecorder

    from opentelemetry.sdk.trace import Span

    class SpanRecorder:
        """Simple span recorder for testing."""

        def __init__(self):
            self._spans: list[Span] = []

        def export(self, spans):
            self._spans.extend(spans)
            return None

        def shutdown(self):
            pass

        def on_start(self, span, parent_context):
            pass

        def on_end(self, span):
            self._spans.append(span)

        def get_finished_spans(self):
            return list(self._spans)

        def get_spans(self):
            """Alias for get_finished_spans for compatibility."""
            return self.get_finished_spans()

        def clear(self):
            self._spans.clear()


from opentelemetry.sdk.resources import Resource

from genops.core.policy import PolicyConfig, PolicyResult
from genops.core.telemetry import GenOpsTelemetry


@pytest.fixture
def mock_otel_setup() -> Generator[SpanRecorder, None, None]:
    """Set up in-memory OpenTelemetry for isolated testing."""
    # Get existing tracer provider or create new one
    current_tracer_provider = trace.get_tracer_provider()

    if not hasattr(current_tracer_provider, "add_span_processor"):
        # Create a tracer provider with test resource only if none exists
        resource = Resource.create({"service.name": "genops-test"})
        tracer_provider = TracerProvider(resource=resource)
        trace.set_tracer_provider(tracer_provider)
    else:
        tracer_provider = current_tracer_provider

    # Set up span recorder for verification
    span_recorder = SpanRecorder()
    span_processor = SimpleSpanProcessor(span_recorder)
    tracer_provider.add_span_processor(span_processor)

    yield span_recorder

    # Cleanup
    span_recorder.clear()


@pytest.fixture
def telemetry(mock_otel_setup) -> GenOpsTelemetry:
    """Provide a GenOpsTelemetry instance with mock OpenTelemetry."""
    return GenOpsTelemetry("genops-test")


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client for testing without API calls."""
    mock_client = MagicMock()

    # Mock chat completion response
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Test AI response"
    mock_response.usage.prompt_tokens = 10
    mock_response.usage.completion_tokens = 5
    mock_response.usage.total_tokens = 15
    mock_response.model = "gpt-3.5-turbo"

    mock_client.chat.completions.create.return_value = mock_response

    return mock_client


@pytest.fixture
def mock_anthropic_client():
    """Mock Anthropic client for testing without API calls."""
    mock_client = MagicMock()

    # Mock message response
    mock_response = MagicMock()
    mock_response.content = [MagicMock()]
    mock_response.content[0].text = "Test Claude response"
    mock_response.usage.input_tokens = 12
    mock_response.usage.output_tokens = 8
    mock_response.model = "claude-3-sonnet-20240229"

    mock_client.messages.create.return_value = mock_response

    return mock_client


@pytest.fixture
def sample_messages() -> list[dict[str, str]]:
    """Provide sample chat messages for testing."""
    return [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is machine learning?"},
    ]


@pytest.fixture
def sample_policy_config() -> PolicyConfig:
    """Provide a sample policy configuration."""
    return PolicyConfig(
        name="test_cost_limit",
        description="Test cost limit policy",
        enforcement_level=PolicyResult.BLOCKED,
        conditions={"max_cost": 1.0},
    )


@pytest.fixture
def sample_policies() -> list[PolicyConfig]:
    """Provide sample policy configurations for testing."""
    return [
        PolicyConfig(
            name="cost_limit",
            description="Limit AI operation costs",
            enforcement_level=PolicyResult.BLOCKED,
            conditions={"max_cost": 5.0},
        ),
        PolicyConfig(
            name="rate_limit",
            description="Rate limit AI operations",
            enforcement_level=PolicyResult.RATE_LIMITED,
            conditions={"max_requests": 100, "time_window": 3600},
        ),
        PolicyConfig(
            name="content_filter",
            description="Filter inappropriate content",
            enforcement_level=PolicyResult.WARNING,
            conditions={"blocked_patterns": ["violence", "explicit"]},
        ),
    ]


@pytest.fixture
def governance_attributes() -> dict[str, Any]:
    """Provide sample governance attributes."""
    return {
        "team": "ai-platform",
        "project": "chatbot-service",
        "environment": "testing",
        "feature": "conversation",
        "customer_id": "test-customer-123",
        "cost_center": "engineering",
        "model": "gpt-3.5-turbo",
        "provider": "openai",
    }


@pytest.fixture
def cost_data() -> dict[str, Any]:
    """Provide sample cost calculation data."""
    return {
        "input_tokens": 100,
        "output_tokens": 50,
        "total_tokens": 150,
        "model": "gpt-3.5-turbo",
        "cost_per_input_token": 0.0005,
        "cost_per_output_token": 0.0015,
        "total_cost": 0.125,
    }


@pytest.fixture
def mock_span_recorder(mock_otel_setup) -> SpanRecorder:
    """Provide direct access to span recorder for assertions."""
    return mock_otel_setup


class SpanAssertions:
    """Helper class for making assertions about OpenTelemetry spans."""

    @staticmethod
    def assert_span_exists(spans: list, name: str) -> Any:
        """Assert that a span with the given name exists."""
        matching_spans = [s for s in spans if s.name == name]
        assert len(matching_spans) > 0, f"No span found with name '{name}'"
        return matching_spans[0]

    @staticmethod
    def assert_span_attribute(span: Any, key: str, expected_value: Any = None):
        """Assert that a span has a specific attribute."""
        attributes = getattr(span, "attributes", {})
        assert key in attributes, f"Attribute '{key}' not found in span"

        if expected_value is not None:
            actual_value = attributes[key]
            assert actual_value == expected_value, (
                f"Attribute '{key}': expected '{expected_value}', got '{actual_value}'"
            )

    @staticmethod
    def assert_governance_attributes(span: Any, expected_attrs: dict[str, Any]):
        """Assert that a span contains expected governance attributes."""
        for key, expected_value in expected_attrs.items():
            genops_key = f"genops.{key}" if not key.startswith("genops.") else key
            SpanAssertions.assert_span_attribute(span, genops_key, expected_value)


@pytest.fixture
def span_assertions() -> SpanAssertions:
    """Provide span assertion helper."""
    return SpanAssertions()


# Mock provider patches for isolated testing
@pytest.fixture
def mock_openai_import():
    """Mock OpenAI import for testing without dependency."""
    with patch("genops.providers.openai.HAS_OPENAI", True):
        with patch("genops.providers.openai.OpenAI") as mock_openai_class:
            yield mock_openai_class


@pytest.fixture
def mock_anthropic_import():
    """Mock Anthropic import for testing without dependency."""
    with patch("genops.providers.anthropic.HAS_ANTHROPIC", True):
        with patch("genops.providers.anthropic.Anthropic") as mock_anthropic_class:
            yield mock_anthropic_class


# Test data generators
class TestDataGenerator:
    """Generate test data for various scenarios."""

    @staticmethod
    def generate_chat_messages(count: int = 3) -> list[dict[str, str]]:
        """Generate sample chat messages."""
        messages = []
        for i in range(count):
            role = "user" if i % 2 == 0 else "assistant"
            content = f"Test message {i + 1} from {role}"
            messages.append({"role": role, "content": content})
        return messages

    @staticmethod
    def generate_policy_violations() -> list[dict[str, Any]]:
        """Generate sample policy violation scenarios."""
        return [
            {
                "policy": "cost_limit",
                "violation_type": "cost_exceeded",
                "cost": 10.0,
                "limit": 5.0,
                "metadata": {"model": "gpt-4", "tokens": 2000},
            },
            {
                "policy": "content_filter",
                "violation_type": "blocked_content",
                "content": "This contains violence",
                "patterns": ["violence"],
                "metadata": {"severity": "high"},
            },
            {
                "policy": "rate_limit",
                "violation_type": "rate_exceeded",
                "requests": 150,
                "limit": 100,
                "time_window": 3600,
                "metadata": {"user_id": "test-user"},
            },
        ]


@pytest.fixture
def test_data_generator() -> TestDataGenerator:
    """Provide test data generator."""
    return TestDataGenerator()


# Cleanup fixture to ensure test isolation
@pytest.fixture
def cleanup_test_state():
    """Ensure clean state between tests."""
    yield

    # Clean up instrumentation without breaking telemetry
    from genops.auto_instrumentation import GenOpsInstrumentor

    if hasattr(GenOpsInstrumentor, "_instance") and GenOpsInstrumentor._instance:
        instrumentor = GenOpsInstrumentor._instance
        if instrumentor and instrumentor._initialized:
            try:
                instrumentor.uninstrument()
            except Exception:
                pass  # Ignore cleanup errors
        # Only reset initialization flag, not the instance itself
        GenOpsInstrumentor._initialized = False


# Flowise-specific test fixtures and utilities

# Test configuration constants for Flowise
TEST_FLOWISE_BASE_URL = "http://localhost:3000"
TEST_FLOWISE_API_KEY = "test-api-key-12345"
TEST_CHATFLOW_ID = "test-chatflow-abc123"

# Sample Flowise test data
SAMPLE_CHATFLOWS = [
    {"id": "customer-support", "name": "Customer Support Assistant"},
    {"id": "sales-assistant", "name": "Sales Assistant"},
    {"id": "technical-help", "name": "Technical Help Desk"},
    {"id": "general-qa", "name": "General Q&A Bot"}
]

SAMPLE_FLOWISE_RESPONSES = [
    {"text": "Hello! How can I help you today?"},
    {"text": "I understand you're asking about artificial intelligence. Let me explain..."},
    {"text": "Based on your question, here are some key points to consider..."},
    {"text": "Is there anything else you'd like to know about this topic?"}
]


@pytest.fixture
def flowise_base_url():
    """Provide test Flowise base URL."""
    return TEST_FLOWISE_BASE_URL


@pytest.fixture
def flowise_api_key():
    """Provide test Flowise API key."""
    return TEST_FLOWISE_API_KEY


@pytest.fixture
def test_chatflow_id():
    """Provide test chatflow ID."""
    return TEST_CHATFLOW_ID


@pytest.fixture
def sample_chatflows():
    """Provide sample chatflow data."""
    return SAMPLE_CHATFLOWS.copy()


@pytest.fixture
def sample_flowise_responses():
    """Provide sample Flowise response data."""
    return SAMPLE_FLOWISE_RESPONSES.copy()


@pytest.fixture
def mock_successful_flowise_get():
    """Mock successful Flowise GET requests."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = SAMPLE_CHATFLOWS
    mock_response.elapsed.total_seconds.return_value = 0.15
    return mock_response


@pytest.fixture  
def mock_successful_flowise_post():
    """Mock successful Flowise POST requests."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = SAMPLE_FLOWISE_RESPONSES[0]
    return mock_response


@pytest.fixture
def mock_failed_flowise_request():
    """Mock failed Flowise requests."""
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    return mock_response


@pytest.fixture
def mock_auth_error_flowise_request():
    """Mock authentication error Flowise requests."""
    mock_response = MagicMock()
    mock_response.status_code = 401
    mock_response.text = "Unauthorized"
    return mock_response


@pytest.fixture
def sample_flowise_governance_config():
    """Provide sample Flowise governance configuration."""
    return {
        "team": "test-engineering",
        "project": "flowise-integration-tests",
        "customer_id": "test-customer-789",
        "environment": "test",
        "cost_center": "eng-ai-testing",
        "feature": "chatflow-automation"
    }


@pytest.fixture
def mock_flowise_server(mock_successful_flowise_get, mock_successful_flowise_post):
    """Complete mock Flowise server with GET and POST endpoints."""
    with patch('requests.get', return_value=mock_successful_flowise_get) as mock_get:
        with patch('requests.post', return_value=mock_successful_flowise_post) as mock_post:
            yield {
                'get': mock_get,
                'post': mock_post,
                'get_response': mock_successful_flowise_get,
                'post_response': mock_successful_flowise_post
            }


class MockFlowiseServer:
    """Mock Flowise server for integration testing."""
    
    def __init__(self):
        self.chatflows = SAMPLE_CHATFLOWS.copy()
        self.responses = SAMPLE_FLOWISE_RESPONSES.copy()
        self.request_count = 0
        self.sessions = {}
        
    def get_chatflows_response(self):
        """Get mock chatflows response."""
        self.request_count += 1
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.chatflows
        mock_response.elapsed.total_seconds.return_value = 0.1
        return mock_response
    
    def predict_flow_response(self, request_data: dict):
        """Get mock prediction response based on request data."""
        self.request_count += 1
        
        # Simulate session-aware responses
        session_id = request_data.get('sessionId')
        if session_id:
            if session_id not in self.sessions:
                self.sessions[session_id] = []
            self.sessions[session_id].append(request_data.get('question', ''))
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        
        # Vary response based on request
        response_idx = len(self.sessions.get(session_id, [])) - 1 if session_id else 0
        response_idx = min(response_idx, len(self.responses) - 1)
        
        mock_response.json.return_value = self.responses[response_idx]
        return mock_response
    
    def simulate_error(self, error_type="server_error"):
        """Simulate various error conditions."""
        mock_response = MagicMock()
        
        if error_type == "server_error":
            mock_response.status_code = 500
            mock_response.text = "Internal Server Error"
        elif error_type == "auth_error":
            mock_response.status_code = 401
            mock_response.text = "Unauthorized"
        elif error_type == "not_found":
            mock_response.status_code = 404
            mock_response.text = "Not Found"
        elif error_type == "rate_limit":
            mock_response.status_code = 429
            mock_response.text = "Rate Limited"
        
        return mock_response


@pytest.fixture
def mock_flowise_server_instance():
    """Provide MockFlowiseServer instance."""
    return MockFlowiseServer()


# Utility functions for Flowise test assertions
def assert_valid_flowise_adapter(adapter):
    """Assert that a Flowise adapter is properly configured."""
    assert adapter is not None
    assert hasattr(adapter, 'base_url')
    assert hasattr(adapter, 'team')
    assert hasattr(adapter, 'project')
    assert adapter.base_url
    assert adapter.team
    assert adapter.project


def assert_valid_flowise_validation_result(result):
    """Assert that a Flowise validation result is properly structured."""
    assert result is not None
    assert hasattr(result, 'is_valid')
    assert hasattr(result, 'issues')
    assert hasattr(result, 'summary')
    assert isinstance(result.is_valid, bool)
    assert isinstance(result.issues, list)
    assert isinstance(result.summary, str)
