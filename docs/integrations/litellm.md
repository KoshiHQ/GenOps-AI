# LiteLLM Integration Guide

Complete integration guide for LiteLLM + GenOps - the highest-leverage GenOps integration providing unified governance across 100+ LLM providers through a single instrumentation layer.

## Table of Contents

- [Strategic Overview](#strategic-overview)
- [Quick Start](#quick-start)  
- [Installation](#installation)
- [Integration Patterns](#integration-patterns)
- [API Reference](#api-reference)
- [Advanced Configuration](#advanced-configuration)
- [Production Deployment](#production-deployment)
- [Performance Optimization](#performance-optimization)
- [Troubleshooting](#troubleshooting)
- [Examples](#examples)

## Strategic Overview

### Why LiteLLM + GenOps is Game-Changing

**Single Integration → Massive Coverage**: One GenOps integration covers 100+ LLM providers through LiteLLM's unified interface.

```
Traditional Approach:           LiteLLM + GenOps Approach:
─────────────────────           ──────────────────────────

Your App                       Your App
  ↓   ↓   ↓   ↓                   ↓
OpenAI Anthropic Google Azure   GenOps LiteLLM (1 integration)
(4 separate integrations)        ↓
                               100+ LLM Providers
```

### Supported Providers (100+)

**Major Providers**: OpenAI, Anthropic, Google Gemini, Azure OpenAI, AWS Bedrock, Cohere, Mistral, Perplexity, Together AI, Fireworks AI, Anyscale, DeepInfra

**Open Source Models**: Ollama, HuggingFace Inference, Replicate, Together AI, RunPod

**Enterprise Platforms**: Azure ML, AWS SageMaker, Google Vertex AI, IBM watsonx

[See complete provider list →](https://docs.litellm.ai/docs/providers)

## Quick Start

**5-minute setup** - see [LiteLLM Quickstart →](../litellm-quickstart.md)

## Installation

### Basic Installation

```bash
pip install litellm genops[litellm]
```

### Development Installation

```bash
# Install with dev dependencies
pip install litellm genops[litellm,dev]

# Or from source
git clone https://github.com/your-org/genops
cd genops
pip install -e .[litellm,dev]
```

### Docker Installation

```dockerfile
FROM python:3.11-slim

RUN pip install litellm genops[litellm]

# Your app code
COPY . /app
WORKDIR /app

CMD ["python", "your_app.py"]
```

### Validation

Verify your installation:

```bash
python -c "
from genops.providers.litellm_validation import validate_litellm_setup, print_validation_result
result = validate_litellm_setup(quick=True)
print_validation_result(result)
"
```

## Integration Patterns

### 1. Zero-Code Auto-Instrumentation (Recommended)

**Best for**: Existing LiteLLM applications, minimal code changes

```python
import litellm
from genops.providers.litellm import auto_instrument

# Enable governance across ALL providers
auto_instrument(
    team="your-team",
    project="your-project",
    environment="production",
    daily_budget_limit=1000.0,
    governance_policy="enforced"
)

# Your existing LiteLLM code works unchanged
response = litellm.completion(
    model="gpt-4",  # Or any of 100+ models
    messages=[{"role": "user", "content": "Hello!"}]
)
# ✅ Automatic governance tracking!
```

### 2. Manual Context Managers

**Best for**: Fine-grained control, specific request attribution

```python
import litellm
from genops.providers.litellm import track_completion

with track_completion(
    model="claude-3-sonnet",
    team="research-team", 
    project="ai-analysis",
    customer_id="customer-123"
) as context:
    
    response = litellm.completion(
        model="claude-3-sonnet",
        messages=[{"role": "user", "content": "Analyze this data..."}]
    )
    
    # Access tracking data
    print(f"Cost: ${context.cost:.6f}")
    print(f"Tokens: {context.total_tokens}")
```

### 3. Conditional Instrumentation

**Best for**: Business logic-driven tracking, performance optimization

```python
from genops.providers.litellm import auto_instrument, track_completion

def process_user_request(user_tier, request_type):
    if user_tier == "enterprise":
        # Detailed tracking for enterprise customers
        with track_completion(
            model="gpt-4",
            team="enterprise-support",
            project="premium-ai",
            customer_id=f"enterprise-{user.id}",
            custom_tags={
                "tier": user_tier,
                "request_type": request_type,
                "detailed_tracking": True
            }
        ) as context:
            response = litellm.completion(...)
    
    else:
        # Lightweight tracking for other users
        response = litellm.completion(...)  # Uses auto-instrumentation
    
    return response
```

### 4. Multi-Provider Optimization

**Best for**: Cost optimization, provider redundancy

```python
from genops.providers.litellm import auto_instrument, get_cost_summary

# Enable cost tracking
auto_instrument(team="cost-optimization", project="multi-provider")

def get_cheapest_equivalent_model(use_case: str):
    """Select cheapest model for equivalent quality."""
    
    equivalent_models = {
        "fast_chat": [
            ("gpt-3.5-turbo", "openai"),
            ("claude-3-haiku", "anthropic"), 
            ("gemini-pro", "google")
        ],
        "reasoning": [
            ("gpt-4", "openai"),
            ("claude-3-sonnet", "anthropic"),
            ("gemini-1.5-pro", "google")
        ]
    }
    
    # Get historical cost data
    cost_summary = get_cost_summary(group_by="provider")
    
    # Select based on cost efficiency
    models = equivalent_models.get(use_case, [])
    # ... optimization logic
    
    return selected_model

# Use optimized model selection
optimal_model = get_cheapest_equivalent_model("fast_chat")
response = litellm.completion(model=optimal_model, messages=[...])
```

## API Reference

### Core Functions

#### `auto_instrument()`

Enable automatic governance across all LiteLLM requests.

```python
def auto_instrument(
    team: str = "default-team",
    project: str = "default-project", 
    environment: str = "development",
    customer_id: Optional[str] = None,
    daily_budget_limit: float = 100.0,
    governance_policy: str = "advisory",
    enable_cost_tracking: bool = True,
    **kwargs
) -> bool
```

**Parameters:**
- `team`: Team identifier for cost attribution and access control
- `project`: Project identifier for governance grouping
- `environment`: Deployment environment (`development`, `staging`, `production`)
- `customer_id`: Optional customer attribution for billing
- `daily_budget_limit`: Daily spending limit in USD
- `governance_policy`: `"advisory"` (warnings) or `"enforced"` (blocking)
- `enable_cost_tracking`: Enable detailed cost calculation
- `**kwargs`: Additional custom attributes

**Returns:**
- `bool`: True if instrumentation successful, False otherwise

#### `instrument_litellm()`

Factory function for creating instrumented LiteLLM instances.

```python
def instrument_litellm(
    team: str,
    project: str,
    **governance_attrs
) -> 'InstrumentedLiteLLM'
```

**Example:**
```python
from genops.providers.litellm import instrument_litellm

# Create instrumented instance
llm = instrument_litellm(
    team="ai-team",
    project="chat-bot",
    customer_id="customer-456"
)

# Use like normal LiteLLM
response = llm.completion(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

#### `track_completion()`

Context manager for manual request tracking.

```python
@contextmanager
def track_completion(
    model: str,
    team: str,
    project: str,
    environment: str = "development",
    customer_id: Optional[str] = None,
    **kwargs
) -> LiteLLMTrackingContext
```

#### `multi_provider_cost_tracking()`

Unified cost tracking across multiple providers.

```python
def multi_provider_cost_tracking(
    providers: List[str],
    time_range: str = "1d",
    group_by: str = "provider"
) -> Dict[str, Any]
```

**Example:**
```python
from genops.providers.litellm import multi_provider_cost_tracking

# Get cost breakdown across providers
costs = multi_provider_cost_tracking(
    providers=["openai", "anthropic", "google"],
    time_range="7d",
    group_by="provider"
)

print(f"OpenAI: ${costs['cost_by_provider']['openai']:.2f}")
print(f"Anthropic: ${costs['cost_by_provider']['anthropic']:.2f}")
```

### Usage Statistics Functions

#### `get_usage_stats()`

Get current session usage statistics.

```python
def get_usage_stats() -> Dict[str, Any]
```

**Returns:**
```python
{
    "total_requests": int,
    "total_cost": float,
    "total_tokens": int,
    "provider_usage": {
        "provider_name": {
            "requests": int,
            "cost": float, 
            "tokens": int,
            "models": List[str]
        }
    },
    "instrumentation_active": bool,
    "instrumentation_config": Dict[str, Any]
}
```

#### `get_cost_summary()`

Get detailed cost summary with grouping options.

```python
def get_cost_summary(
    group_by: str = "provider",
    time_range: Optional[str] = None
) -> Dict[str, Any]
```

**Parameters:**
- `group_by`: Group costs by `"provider"`, `"team"`, `"project"`, or `"customer"`
- `time_range`: Time range filter (e.g., `"1h"`, `"1d"`, `"7d"`)

#### `reset_usage_stats()`

Reset usage statistics (useful for testing).

```python
def reset_usage_stats() -> None
```

### Validation Functions

#### `validate_setup()`

Validate LiteLLM + GenOps integration setup.

```python
def validate_setup(
    quick: bool = False,
    test_connectivity: bool = False
) -> ValidationResult
```

## Advanced Configuration

### Governance Policies

Configure different governance policies for different environments:

```python
# Development - Advisory mode
auto_instrument(
    team="dev-team",
    environment="development", 
    governance_policy="advisory",
    daily_budget_limit=10.0
)

# Production - Enforced mode
auto_instrument(
    team="prod-team",
    environment="production",
    governance_policy="enforced",
    daily_budget_limit=1000.0
)
```

### Custom Cost Tracking

Override default cost calculation:

```python
from genops.providers.litellm import auto_instrument

def custom_cost_calculator(provider, model, input_tokens, output_tokens):
    """Custom cost calculation logic."""
    # Your custom pricing logic
    return calculated_cost

auto_instrument(
    team="custom-billing",
    project="special-pricing",
    custom_cost_calculator=custom_cost_calculator
)
```

### Performance Optimization

#### Sampling Configuration

For high-volume applications, use sampling:

```python
auto_instrument(
    team="high-volume",
    project="production-api",
    sampling_rate=0.1,  # Track 10% of requests
    enable_cost_tracking=True  # Always track costs
)
```

#### Async Telemetry Export

Minimize application overhead:

```python
auto_instrument(
    team="performance",
    project="low-latency",
    async_export=True,
    export_batch_size=100,
    export_interval_seconds=30
)
```

### Multi-Tenant Configuration

Configure per-tenant governance:

```python
def configure_tenant_governance(tenant_id: str, plan: str):
    """Configure governance per tenant."""
    
    tenant_config = {
        "free": {"budget": 10.0, "policy": "enforced"},
        "pro": {"budget": 100.0, "policy": "advisory"},
        "enterprise": {"budget": 1000.0, "policy": "advisory"}
    }
    
    config = tenant_config.get(plan, tenant_config["free"])
    
    return auto_instrument(
        team=f"tenant-{tenant_id}",
        project="saas-platform",
        customer_id=tenant_id,
        daily_budget_limit=config["budget"],
        governance_policy=config["policy"]
    )

# Use with requests
tenant_governance = configure_tenant_governance("tenant-123", "enterprise")
response = litellm.completion(model="gpt-4", messages=[...])
```

## Production Deployment

### High Availability Patterns

#### Multi-Provider Fallback

```python
import litellm
from genops.providers.litellm import auto_instrument

# Configure fallback providers
litellm.set_verbose = False
litellm.fallbacks = [
    {"gpt-4": "claude-3-sonnet"},
    {"claude-3-sonnet": "gemini-1.5-pro"}
]

auto_instrument(
    team="production",
    project="ha-service",
    governance_policy="enforced"
)

def robust_completion(messages, primary_model="gpt-4"):
    """Completion with automatic fallback."""
    try:
        return litellm.completion(model=primary_model, messages=messages)
    except Exception as e:
        # LiteLLM handles fallback automatically
        # GenOps tracks all attempts
        raise e
```

#### Circuit Breaker Pattern

```python
from genops.providers.litellm import auto_instrument
import time

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "closed"  # closed, open, half-open
    
    def call(self, func, *args, **kwargs):
        if self.state == "open":
            if time.time() - self.last_failure_time < self.timeout:
                raise Exception("Circuit breaker is OPEN")
            else:
                self.state = "half-open"
        
        try:
            result = func(*args, **kwargs)
            if self.state == "half-open":
                self.state = "closed"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.state = "open"
            
            raise e

# Usage
circuit_breaker = CircuitBreaker()
auto_instrument(team="resilient", project="circuit-breaker")

def protected_completion(messages):
    return circuit_breaker.call(
        litellm.completion,
        model="gpt-4",
        messages=messages
    )
```

### Container Deployment

#### Docker

```dockerfile
FROM python:3.11-slim

# Install dependencies
RUN pip install litellm genops[litellm]

# Copy application
COPY . /app
WORKDIR /app

# Set governance configuration
ENV GENOPS_TEAM="production"
ENV GENOPS_PROJECT="containerized-ai"
ENV GENOPS_ENVIRONMENT="production"

# Health check endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from genops.providers.litellm_validation import validate_litellm_setup; validate_litellm_setup(quick=True)"

CMD ["python", "app.py"]
```

#### Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: genops-litellm-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: genops-litellm
  template:
    metadata:
      labels:
        app: genops-litellm
    spec:
      containers:
      - name: app
        image: your-app:latest
        env:
        - name: GENOPS_TEAM
          value: "k8s-production"
        - name: GENOPS_PROJECT  
          value: "scalable-ai"
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: llm-api-keys
              key: openai-key
        resources:
          limits:
            memory: "512Mi"
            cpu: "500m"
          requests:
            memory: "256Mi"
            cpu: "250m"
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
```

### Monitoring and Observability

#### OpenTelemetry Export

```python
from genops.providers.litellm import auto_instrument
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configure OpenTelemetry
trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(endpoint="http://your-otel-collector:4317")
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Enable GenOps with OTel export
auto_instrument(
    team="monitored",
    project="otel-export",
    export_to_otel=True,
    otel_service_name="litellm-service"
)
```

#### Custom Metrics Export

```python
from genops.providers.litellm import auto_instrument, get_usage_stats
import time
import json

def export_metrics_to_datadog():
    """Export GenOps metrics to DataDog."""
    stats = get_usage_stats()
    
    metrics = {
        "genops.litellm.requests.total": stats["total_requests"],
        "genops.litellm.cost.total": stats["total_cost"],
        "genops.litellm.tokens.total": stats["total_tokens"]
    }
    
    # Send to your monitoring system
    # datadog.api.Metric.send(metrics)
    
# Run periodic export
import threading
def periodic_export():
    while True:
        export_metrics_to_datadog()
        time.sleep(60)

threading.Thread(target=periodic_export, daemon=True).start()
```

## Performance Optimization

### Latency Optimization

#### Provider Selection by Latency

```python
from genops.providers.litellm import auto_instrument
import time

# Track latency per provider
provider_latencies = {
    "openai": [],
    "anthropic": [], 
    "google": []
}

def select_fastest_provider(equivalent_models):
    """Select provider with lowest average latency."""
    avg_latencies = {}
    
    for provider, latencies in provider_latencies.items():
        if latencies:
            avg_latencies[provider] = sum(latencies) / len(latencies)
    
    if not avg_latencies:
        return equivalent_models[0]  # Default fallback
    
    fastest_provider = min(avg_latencies, key=avg_latencies.get)
    
    for model, provider in equivalent_models:
        if provider == fastest_provider:
            return model
    
    return equivalent_models[0][0]  # Fallback

# Usage
equivalent_models = [
    ("gpt-3.5-turbo", "openai"),
    ("claude-3-haiku", "anthropic"),
    ("gemini-pro", "google")
]

optimal_model = select_fastest_provider(equivalent_models)
```

#### Connection Pooling

```python
import litellm
from genops.providers.litellm import auto_instrument

# Configure connection pooling
litellm.modify_params = True
litellm.drop_params = True
litellm.set_verbose = False

# Connection pool settings
session_config = {
    "pool_connections": 10,
    "pool_maxsize": 10,
    "max_retries": 3
}

auto_instrument(
    team="optimized",
    project="connection-pool",
    session_config=session_config
)
```

### Cost Optimization Strategies

#### Dynamic Model Selection

```python
from genops.providers.litellm import auto_instrument, get_cost_summary

def cost_aware_model_selection(complexity_score: float, budget_remaining: float):
    """Select model based on complexity and budget."""
    
    # Model tiers by cost and capability
    models = [
        {"model": "gpt-3.5-turbo", "cost_multiplier": 1.0, "min_complexity": 0.0},
        {"model": "gpt-4", "cost_multiplier": 20.0, "min_complexity": 0.7},
        {"model": "claude-3-sonnet", "cost_multiplier": 15.0, "min_complexity": 0.6},
        {"model": "gemini-pro", "cost_multiplier": 2.0, "min_complexity": 0.3}
    ]
    
    # Filter by complexity requirements
    suitable_models = [
        m for m in models 
        if m["min_complexity"] <= complexity_score
    ]
    
    # Select cheapest suitable model within budget
    affordable_models = [
        m for m in suitable_models
        if (budget_remaining * m["cost_multiplier"]) > 0.01  # Min viable cost
    ]
    
    if affordable_models:
        return min(affordable_models, key=lambda x: x["cost_multiplier"])["model"]
    else:
        return "gpt-3.5-turbo"  # Budget fallback

# Usage
auto_instrument(team="cost-optimized", project="smart-selection")

task_complexity = analyze_task_complexity(user_input)
remaining_budget = get_remaining_daily_budget()
optimal_model = cost_aware_model_selection(task_complexity, remaining_budget)

response = litellm.completion(model=optimal_model, messages=[...])
```

## Troubleshooting

### Common Issues

#### Installation Issues

**❌ "LiteLLM not found"**
```bash
pip install litellm
# Or for specific version
pip install litellm==1.35.0
```

**❌ "GenOps LiteLLM provider not available"**
```bash
pip install genops[litellm]
# Or upgrade
pip install --upgrade genops[litellm]
```

#### API Key Issues

**❌ "No LLM provider API keys configured"**

Set at least one provider API key:
```bash
# OpenAI (most common)
export OPENAI_API_KEY="sk-your-key"

# Or Anthropic
export ANTHROPIC_API_KEY="sk-ant-your-key"

# Or Google
export GOOGLE_API_KEY="your-google-key"

# See all providers: https://docs.litellm.ai/docs/providers
```

**❌ "Invalid API key" errors**

Verify your keys work directly:
```bash
# Test OpenAI key
curl -H "Authorization: Bearer $OPENAI_API_KEY" \
     https://api.openai.com/v1/models

# Test Anthropic key  
curl -H "x-api-key: $ANTHROPIC_API_KEY" \
     https://api.anthropic.com/v1/messages
```

#### Callback System Issues

**❌ "Callback registration failed"**

Update LiteLLM to latest version:
```bash
pip install --upgrade litellm
```

Check callback support:
```python
import litellm
print(f"LiteLLM version: {litellm.__version__}")
print(f"Has callbacks: {hasattr(litellm, 'success_callback')}")
```

#### Performance Issues

**❌ High latency with instrumentation**

Enable async export:
```python
auto_instrument(
    team="performance",
    project="async-export",
    async_export=True,
    export_batch_size=100
)
```

Use sampling for high-volume:
```python
auto_instrument(
    team="high-volume",
    project="sampled",
    sampling_rate=0.1  # Track 10% of requests
)
```

### Diagnostic Tools

#### Setup Validation

Run comprehensive validation:
```bash
cd examples/litellm
python setup_validation.py
```

Quick validation:
```bash
python setup_validation.py --quick
```

With connectivity tests:
```bash
python setup_validation.py --test
```

#### Debug Mode

Enable verbose logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)

from genops.providers.litellm import auto_instrument
auto_instrument(team="debug", project="troubleshooting")

# LiteLLM debug
import litellm
litellm.set_verbose = True
```

#### Cost Tracking Verification

Verify cost calculations:
```python
from genops.providers.litellm import get_usage_stats, get_cost_summary

# Check current stats
stats = get_usage_stats()
print(f"Total cost: ${stats['total_cost']:.6f}")

# Detailed breakdown
summary = get_cost_summary(group_by="provider")
for provider, cost in summary['cost_by_provider'].items():
    print(f"{provider}: ${cost:.6f}")
```

### Getting Help

#### Documentation

- **[5-Minute Quickstart →](../litellm-quickstart.md)** - Get started immediately
- **[Examples →](../../examples/litellm/)** - 7 progressive examples  
- **[LiteLLM Docs →](https://docs.litellm.ai/)** - Provider-specific configuration

#### Validation and Testing

```bash
# Validate environment
python examples/litellm/setup_validation.py

# Test all examples
cd examples/litellm
for example in *.py; do 
    echo "Testing $example..."
    python "$example" || echo "Failed: $example"
done
```

#### Community Support

- **GitHub Issues**: [Report integration issues](https://github.com/your-org/genops/issues)
- **LiteLLM Support**: [LiteLLM documentation](https://docs.litellm.ai/)
- **Provider Issues**: Check provider-specific troubleshooting

## Examples

### Progressive Learning Path

Our examples are designed for progressive mastery:

#### **🟢 Foundation (15 minutes)**
- **[`setup_validation.py`](../../examples/litellm/setup_validation.py)** - Validate your environment
- **[`auto_instrumentation.py`](../../examples/litellm/auto_instrumentation.py)** - Zero-code demo
- **[`basic_tracking.py`](../../examples/litellm/basic_tracking.py)** - Manual tracking patterns

#### **🔵 Optimization (45 minutes)**
- **[`multi_provider_costs.py`](../../examples/litellm/multi_provider_costs.py)** - Cost analysis
- **[`cost_optimization.py`](../../examples/litellm/cost_optimization.py)** - Smart model selection
- **[`budget_management.py`](../../examples/litellm/budget_management.py)** - Budget controls

#### **🟡 Production (90 minutes)**
- **[`production_patterns.py`](../../examples/litellm/production_patterns.py)** - Enterprise deployment
- **[`compliance_monitoring.py`](../../examples/litellm/compliance_monitoring.py)** - Audit & compliance
- **[`performance_optimization.py`](../../examples/litellm/performance_optimization.py)** - Scaling patterns

### Running Examples

```bash
cd examples/litellm

# Always start with validation
python setup_validation.py

# Foundation examples
python auto_instrumentation.py
python basic_tracking.py

# Cost optimization examples  
python multi_provider_costs.py
python cost_optimization.py

# Production examples
python production_patterns.py
python compliance_monitoring.py
```

## Conclusion

LiteLLM + GenOps provides the highest-leverage AI governance integration available:

- **Single Integration** → Coverage across 100+ LLM providers
- **Zero Vendor Lock-in** → Provider-agnostic cost optimization
- **Enterprise Ready** → Production patterns, compliance, monitoring
- **Developer First** → 5-minute setup to production deployment

**Next Steps:**
1. **[Try the 5-minute quickstart →](../litellm-quickstart.md)**
2. **[Explore progressive examples →](../../examples/litellm/)**
3. **[Deploy to production →](#production-deployment)**

The single instrumentation layer for ecosystem-wide AI governance.