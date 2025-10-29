# ADR-0002: Provider Adapter Pattern for AI Integrations

## Status
Accepted

*Date: 2024-01-20*

## Context

GenOps AI needs to capture governance telemetry from various AI providers (OpenAI, Anthropic, Bedrock, etc.) and frameworks (LangChain, LlamaIndex, etc.). Each provider has different:

- **API structures** (REST, streaming, async/sync)
- **Cost models** (per-token, per-request, tiered pricing)  
- **Authentication patterns** (API keys, OAuth, IAM roles)
- **Response formats** (JSON structures, metadata fields)
- **Error handling** approaches

The instrumentation must be:
- **Non-invasive** - minimal changes to existing application code
- **Accurate** - precise cost calculation and token counting
- **Consistent** - uniform telemetry regardless of provider
- **Maintainable** - easy to add new providers and update pricing

Three main approaches were considered:
1. **Monkey patching** - Runtime modification of provider libraries
2. **Proxy/middleware** - Intercept HTTP requests/responses
3. **Adapter pattern** - Wrapper classes that implement consistent interfaces

## Decision

We will use the **Provider Adapter Pattern** for AI provider integrations.

Each provider will have a dedicated adapter module that:
- **Wraps the native SDK** with governance instrumentation
- **Implements consistent telemetry** across all providers
- **Handles provider-specific quirks** (pricing, token counting, metadata)
- **Provides a unified interface** for common operations
- **Maintains backward compatibility** with existing application code

Architecture:
```python
# Provider-specific adapter
from genops.providers.openai import instrument_openai

# Returns instrumented client with governance telemetry
client = instrument_openai(api_key="sk-...")

# Normal usage - telemetry added transparently
response = client.chat.completions.create(...)
```

## Alternatives Considered

### Monkey Patching Approach
```python
# Automatically instruments all imports
import genops.auto_instrument
import openai  # Now automatically instrumented

client = openai.OpenAI()  # Telemetry added transparently
```

**Pros:**
- Zero code changes required
- Works with any existing codebase
- Automatic discovery of provider usage

**Cons:**
- Fragile - breaks with provider SDK updates
- Hard to debug when instrumentation fails
- Version compatibility nightmare across providers
- Difficult to handle provider-specific customization

### Proxy/Middleware Approach
```python
# HTTP-level interception
genops.configure_http_proxy("https://api.openai.com")

# All HTTP calls automatically captured
client = openai.OpenAI()  # Unchanged code
```

**Pros:**
- Language and SDK agnostic
- Works with any HTTP-based provider
- No SDK version dependencies

**Cons:**
- Requires complex HTTP parsing logic
- Missing semantic context (model names, token counts)
- Difficult to extract structured telemetry from HTTP bodies
- Performance overhead of HTTP interception

## Consequences

### Positive
- **Explicit instrumentation**: Clear where governance is active
- **Provider-specific optimization**: Accurate cost models and token counting
- **Type safety**: Full IDE support and compile-time checking  
- **Debugging friendly**: Clear stack traces through adapter code
- **Version stability**: Adapter can handle SDK changes gracefully
- **Customization**: Easy to add provider-specific governance features

### Negative
- **Code changes required**: Applications must use instrumented clients
- **Maintenance overhead**: Each provider needs dedicated adapter maintenance
- **Version coupling**: Adapters must track provider SDK releases
- **Discovery challenge**: Developers must find and use correct adapter

### Neutral
- **Learning curve**: Developers need to understand adapter usage patterns
- **Documentation burden**: Each adapter needs usage examples and migration guides
- **Testing complexity**: Must test against multiple provider SDK versions

## Implementation Notes

### Adapter Structure
```
genops/providers/
├── openai/
│   ├── __init__.py       # instrument_openai()
│   ├── client.py         # Instrumented client wrapper
│   ├── cost_calculator.py # OpenAI pricing logic
│   └── token_counter.py  # OpenAI token counting
├── anthropic/
├── bedrock/
└── base/
    └── adapter.py        # Base adapter interface
```

### Key Principles
1. **Preserve native API**: Instrumented clients should be drop-in replacements
2. **Fail gracefully**: Instrumentation errors shouldn't break AI operations  
3. **Configurable telemetry**: Allow disabling/customizing governance features
4. **Provider parity**: Consistent telemetry schema across all adapters

### Migration Strategy
1. **Start with major providers**: OpenAI, Anthropic, Bedrock
2. **Community contributions**: Template and tools for adding new providers
3. **Deprecation path**: Clear upgrade path when provider SDKs change
4. **Auto-instrumentation option**: Future consideration for monkey patching as opt-in

## References

- [Adapter Pattern - Gang of Four](https://en.wikipedia.org/wiki/Adapter_pattern)
- [OpenAI Python SDK](https://github.com/openai/openai-python) 
- [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- [AWS Bedrock SDK](https://docs.aws.amazon.com/bedrock/)
- [OpenTelemetry Instrumentation Guidelines](https://opentelemetry.io/docs/specs/otel/trace/sdk/#span-processor)

---

*Author: GenOps AI Team*  
*Reviewers: Provider Integration Working Group*