# Helicone AI Gateway Integration Guide

## Overview

The GenOps Helicone adapter provides comprehensive governance telemetry for Helicone AI Gateway applications, including:

- **Multi-provider AI gateway access** with unified tracking for 100+ models
- **Cross-provider cost optimization** with intelligent routing strategies
- **Gateway performance analytics** with latency and success rate monitoring
- **Unified cost intelligence** across OpenAI, Anthropic, Vertex AI, Groq, and more
- **Policy enforcement** with governance attribute propagation
- **Real-time budget tracking** with automatic cost aggregation

## Quick Start

### Installation

```bash
pip install genops[helicone]
```

### Basic Setup

The simplest way to add GenOps tracking to your Helicone AI Gateway application:

```python
from genops.providers.helicone import instrument_helicone

# Initialize GenOps Helicone adapter
adapter = instrument_helicone(
    helicone_api_key="your_helicone_key",
    provider_keys={
        "openai": "your_openai_key",
        "anthropic": "your_anthropic_key"
    }
)

# Multi-provider chat with automatic tracking
response = adapter.chat(
    message="Explain quantum computing",
    provider="openai",  # or "anthropic", "vertex", etc.
    model="gpt-4",
    team="research-team",
    project="quantum-ai",
    customer_id="customer_123"
)
```

### Auto-Instrumentation (Recommended)

For zero-code setup, enable auto-instrumentation:

```python
from genops import init

# Automatically instrument all supported providers including Helicone
init()

# Your existing AI code automatically gets governance telemetry
# Works with any framework that uses Helicone gateway
```

## Core Features

### 1. Multi-Provider Chat Completion

Access multiple AI providers through unified interface with comprehensive tracking:

```python
from genops.providers.helicone import GenOpsHeliconeAdapter

adapter = GenOpsHeliconeAdapter(
    helicone_api_key="your_helicone_key",
    provider_keys={
        "openai": "your_openai_key",
        "anthropic": "your_anthropic_key",
        "vertex": "your_vertex_credentials",
        "groq": "your_groq_key"
    }
)

# Single message across multiple providers
response = adapter.multi_provider_chat(
    message="What is the future of AI?",
    providers=["openai", "anthropic"],
    model_preferences={
        "openai": "gpt-4", 
        "anthropic": "claude-3-sonnet"
    },
    routing_strategy="cost_optimized",
    
    # Governance attributes
    team="ai-research",
    project="future-studies",
    environment="production"
)
```

**Telemetry Captured:**
- Request/response timing across all providers
- Token usage and cost calculation per provider
- Gateway routing decisions and performance
- Provider selection rationale and optimization
- Success/error rates by provider and model
- Governance attribute propagation

### 2. Intelligent Routing Strategies

Optimize AI requests with intelligent routing:

```python
# Cost-optimized routing
response = adapter.chat(
    message="Simple task",
    providers=["openai", "groq"],  # Groq often cheaper
    routing_strategy="cost_optimized"
)

# Performance-optimized routing
response = adapter.chat(
    message="Complex reasoning task", 
    providers=["openai", "anthropic"],
    routing_strategy="performance_optimized"
)

# Failover routing for reliability
response = adapter.chat(
    message="Critical business query",
    providers=["openai", "anthropic", "vertex"],
    routing_strategy="failover"
)

# Quality-optimized routing
response = adapter.chat(
    message="Creative writing task",
    providers=["openai", "anthropic"],
    routing_strategy="quality_optimized"
)
```

### 3. Real-time Cost Aggregation

Track costs across all providers in real-time:

```python
from genops.providers.helicone import multi_provider_cost_tracking

# Start cost tracking session
with multi_provider_cost_tracking(session_id="batch_analysis") as tracker:
    
    # Multiple provider calls tracked automatically
    response1 = adapter.chat("Task 1", provider="openai")
    response2 = adapter.chat("Task 2", provider="anthropic") 
    response3 = adapter.chat("Task 3", provider="groq")
    
    # Get real-time cost summary
    summary = tracker.get_session_summary()
    print(f"Total session cost: ${summary.total_cost:.4f}")
    print(f"Cost by provider: {summary.cost_by_provider}")
    print(f"Gateway fees: ${summary.gateway_fees:.4f}")
```

### 4. Advanced Provider Management

Handle complex multi-provider scenarios:

```python
# Provider availability checking
adapter.validate_providers()  # Check all configured providers

# Provider-specific model selection
response = adapter.chat(
    message="Complex analysis task",
    provider_preferences={
        "openai": {"model": "gpt-4", "weight": 0.7},
        "anthropic": {"model": "claude-3-opus", "weight": 0.3}
    },
    fallback_strategy="round_robin"
)

# Budget-constrained operations
response = adapter.chat(
    message="Budget-sensitive task",
    max_cost=0.05,  # Maximum $0.05 per request
    providers=["groq", "openai"],  # Ordered by cost preference
    routing_strategy="cost_optimized"
)
```

## Configuration

### Environment Variables

The adapter automatically reads from environment variables:

```bash
# Required
export HELICONE_API_KEY="your_helicone_key"

# Provider keys (at least one required)
export OPENAI_API_KEY="your_openai_key"
export ANTHROPIC_API_KEY="your_anthropic_key" 
export GROQ_API_KEY="your_groq_key"
export VERTEX_AI_CREDENTIALS="path/to/credentials.json"

# Optional: GenOps configuration
export GENOPS_SERVICE_NAME="my-ai-service"
export GENOPS_ENVIRONMENT="production"
```

### Manual Configuration

For programmatic configuration:

```python
from genops.providers.helicone import GenOpsHeliconeAdapter

adapter = GenOpsHeliconeAdapter(
    helicone_api_key="your_helicone_key",
    provider_keys={
        "openai": "your_openai_key",
        "anthropic": "your_anthropic_key",
        "groq": "your_groq_key"
    },
    
    # GenOps configuration
    default_attributes={
        "team": "ai-platform",
        "environment": "production",
        "cost_center": "engineering"
    },
    
    # Helicone gateway settings
    gateway_url="https://ai-gateway.helicone.ai",  # Default
    timeout_seconds=30,
    retry_attempts=3,
    
    # Cost tracking settings
    enable_cost_tracking=True,
    cost_currency="USD"
)
```

## Cost Intelligence Features

### 1. Provider Cost Comparison

Compare costs across providers for identical tasks:

```python
from genops.providers.helicone import compare_provider_costs

# Compare cost for same task across providers
comparison = compare_provider_costs(
    message="Analyze this data and provide insights",
    providers=["openai", "anthropic", "groq"],
    model_preferences={
        "openai": "gpt-4",
        "anthropic": "claude-3-sonnet", 
        "groq": "mixtral-8x7b"
    }
)

print(f"Cheapest option: {comparison.cheapest_provider}")
print(f"Cost savings: ${comparison.max_savings:.4f}")
print(f"Cost breakdown: {comparison.cost_by_provider}")
```

### 2. Migration Cost Analysis

Analyze costs when migrating between providers:

```python
from genops.providers.helicone import estimate_migration_costs

# Estimate cost impact of provider migration
migration_analysis = estimate_migration_costs(
    current_provider="openai",
    current_model="gpt-3.5-turbo",
    target_providers=["anthropic", "groq"],
    target_models=["claude-3-haiku", "mixtral-8x7b"],
    historical_usage={"requests_per_day": 1000, "avg_tokens": 500}
)

print(f"Current monthly cost: ${migration_analysis.current_monthly_cost:.2f}")
print(f"Projected savings: ${migration_analysis.projected_savings:.2f}")
```

### 3. Budget Management

Set and enforce spending limits:

```python
# Set budget limits
adapter.set_budget_limits(
    daily_limit=100.0,    # $100 per day
    monthly_limit=2500.0, # $2500 per month
    per_team_limits={
        "research": 500.0,
        "product": 1500.0
    }
)

# Budget-aware requests (will fail if over budget)
try:
    response = adapter.chat(
        message="Expensive analysis task",
        team="research",
        enforce_budget=True
    )
except BudgetExceededError as e:
    print(f"Request blocked: {e.message}")
    print(f"Current usage: ${e.current_usage:.2f}")
    print(f"Budget limit: ${e.budget_limit:.2f}")
```

## Validation and Troubleshooting

### Setup Validation

Validate your Helicone integration:

```python
from genops.providers.helicone_validation import validate_setup, print_validation_result

# Comprehensive setup validation
result = validate_setup(include_performance_tests=True)
print_validation_result(result, detailed=True)
```

**Example validation output:**
```
🔍 GenOps Helicone Setup Validation

✅ Helicone API Key: Valid
✅ Provider Keys: 3/3 configured (OpenAI, Anthropic, Groq)
✅ Gateway Connectivity: Healthy (45ms avg latency)
✅ Cost Tracking: Enabled and functioning
⚠️  Self-hosted Gateway: Not configured (using cloud gateway)

🎯 Quick Performance Test:
✅ OpenAI via Helicone: 892ms (cost: $0.0024)
✅ Anthropic via Helicone: 1.1s (cost: $0.0019)
✅ Groq via Helicone: 312ms (cost: $0.0008)

✅ Overall Status: PASSED (with 1 warning)

💡 Recommendations:
- Consider self-hosted gateway for production workloads
- Groq shows best cost/performance ratio for this test
```

### Common Issues

**Issue: Gateway timeouts**
```python
# Increase timeout for complex requests
adapter = GenOpsHeliconeAdapter(
    timeout_seconds=60,  # Increase from default 30s
    retry_attempts=5
)
```

**Issue: Rate limiting**
```python
# Configure rate limiting
adapter.configure_rate_limits(
    requests_per_minute=100,
    burst_allowance=20,
    backoff_strategy="exponential"
)
```

**Issue: Cost tracking accuracy**
```python
# Enable detailed cost debugging
adapter.enable_cost_debugging(
    log_all_requests=True,
    validate_pricing=True,
    alert_on_unexpected_costs=True
)
```

## Advanced Usage

### 1. Custom Routing Logic

Implement custom routing strategies:

```python
def custom_routing_strategy(providers, message, context):
    """Custom routing based on message complexity and time of day."""
    import datetime
    
    # Use cheaper providers during off-hours
    current_hour = datetime.datetime.now().hour
    if 22 <= current_hour or current_hour <= 6:  # Night hours
        return "groq"  # Cheapest option
    
    # Use high-quality providers for complex tasks
    if len(message.split()) > 100:  # Complex message
        return "anthropic"  # Best reasoning
    
    return "openai"  # Default for simple tasks

# Register and use custom strategy
adapter.register_routing_strategy("custom", custom_routing_strategy)

response = adapter.chat(
    message="Your message here",
    routing_strategy="custom"
)
```

### 2. Webhook Integration

Set up webhooks for cost alerts and monitoring:

```python
# Configure cost alerts
adapter.configure_webhooks(
    cost_alert_webhook="https://your-api.com/cost-alerts",
    performance_webhook="https://your-api.com/performance",
    triggers={
        "high_cost": {"threshold": 10.0, "timeframe": "hourly"},
        "slow_response": {"threshold": 5000, "unit": "ms"},
        "error_rate": {"threshold": 0.05, "unit": "percentage"}
    }
)
```

### 3. Enterprise Features

For enterprise deployments:

```python
# Self-hosted gateway configuration
adapter = GenOpsHeliconeAdapter(
    gateway_url="https://your-helicone-gateway.company.com",
    auth_mode="oauth2",
    oauth_config={
        "client_id": "your_client_id",
        "client_secret": "your_client_secret",
        "token_url": "https://auth.company.com/token"
    },
    
    # Enterprise governance
    compliance_mode=True,
    audit_logging=True,
    data_residency="us-east-1"
)
```

## Best Practices

### 1. Provider Selection

- **Cost-sensitive workloads**: Start with Groq, fallback to OpenAI
- **High-quality reasoning**: Use Anthropic Claude or OpenAI GPT-4
- **Speed-critical applications**: Consider Groq or optimized OpenAI models
- **Enterprise compliance**: Prefer providers with strong data governance

### 2. Cost Optimization

```python
# Good: Use appropriate models for task complexity
response = adapter.chat(
    message="Simple question",
    provider="groq",  # Cheaper for simple tasks
    model="mixtral-8x7b"
)

# Better: Let intelligent routing decide
response = adapter.chat(
    message="Simple question", 
    routing_strategy="cost_optimized",
    providers=["groq", "openai"]  # Ordered by preference
)

# Best: Combine with budget enforcement
response = adapter.chat(
    message="Simple question",
    routing_strategy="cost_optimized", 
    max_cost=0.01,  # Hard limit
    team="cost-sensitive-team"
)
```

### 3. Error Handling

```python
from genops.providers.helicone import HeliconeError, ProviderError

try:
    response = adapter.multi_provider_chat(
        message="Your query",
        providers=["openai", "anthropic"],
        routing_strategy="failover"
    )
except ProviderError as e:
    print(f"Provider failed: {e.provider} - {e.error_message}")
    # Automatic failover to backup provider
except HeliconeError as e:
    print(f"Gateway error: {e.error_message}")
    # Handle gateway-specific issues
```

## Performance Considerations

### Async Support

For high-throughput applications:

```python
import asyncio
from genops.providers.helicone import GenOpsHeliconeAsyncAdapter

async def process_batch():
    adapter = GenOpsHeliconeAsyncAdapter()
    
    # Process multiple requests concurrently
    tasks = [
        adapter.chat_async(f"Process item {i}", provider="groq")
        for i in range(100)
    ]
    
    responses = await asyncio.gather(*tasks)
    return responses
```

### Caching

Enable response caching for repeated queries:

```python
adapter.enable_caching(
    cache_provider="redis",  # or "memory", "disk"
    cache_ttl=3600,  # 1 hour
    cache_key_strategy="content_hash"  # or "exact_match"
)
```

## Monitoring and Observability

The adapter automatically exports OpenTelemetry metrics compatible with your existing observability stack:

### Grafana Dashboard

```yaml
# Example Grafana queries for Helicone metrics
- name: "AI Gateway Requests/sec"
  query: rate(genops_helicone_requests_total[5m])

- name: "Average Response Time by Provider" 
  query: avg by (provider) (genops_helicone_request_duration_ms)

- name: "Cost per Hour by Team"
  query: sum by (team) (increase(genops_helicone_cost_usd[1h]))
```

### Custom Metrics

Export custom metrics for your specific use cases:

```python
adapter.register_custom_metrics([
    {
        "name": "business_value_score",
        "type": "gauge", 
        "description": "Business value score for AI responses"
    }
])

# Use in requests
response = adapter.chat(
    message="Business critical analysis",
    custom_metrics={"business_value_score": 0.95}
)
```

For detailed setup instructions and additional examples, see the [Helicone Quickstart Guide](../helicone-quickstart.md).