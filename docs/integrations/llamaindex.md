# LlamaIndex Integration Guide

**Complete reference for integrating GenOps AI governance with LlamaIndex RAG applications**

This guide provides comprehensive documentation for all GenOps LlamaIndex features, from basic cost tracking to advanced production deployment patterns.

## Overview

GenOps provides complete governance for LlamaIndex applications including:

- **🔍 RAG Pipeline Tracking** - Monitor embeddings, retrieval, and synthesis costs
- **🤖 Agent Workflow Governance** - Track multi-step agent operations and tool usage
- **💰 Multi-Provider Cost Management** - Optimize across OpenAI, Anthropic, Google, and local models
- **🏷️ Team Attribution** - Attribute costs to teams, projects, and customers
- **⚡ Performance Monitoring** - Track latency, quality, and success rates
- **🛡️ Budget Controls** - Set limits, alerts, and automatic cost enforcement
- **📊 OpenTelemetry Integration** - Export to your existing observability stack

## Quick Start

> **🚀 New to GenOps?** Start with the [5-Minute Quickstart Guide](../llamaindex-quickstart.md) for an instant working example, then return here for comprehensive reference.

### Installation

```bash
pip install genops-ai[llamaindex]

# Or with specific LlamaIndex components
pip install genops-ai llama-index llama-index-llms-openai llama-index-embeddings-openai
```

### Basic Setup

```python
from genops.providers.llamaindex import auto_instrument
from llama_index.core import Settings, VectorStoreIndex, Document

# Enable automatic instrumentation
auto_instrument()

# Configure your LLM and embedding models
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding()

# Your existing LlamaIndex code now includes GenOps tracking
documents = [Document(text="Your content here")]
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query("Your question")
# Costs automatically tracked and exported
```

## Core Components

### 1. GenOpsLlamaIndexAdapter

The main adapter class for comprehensive LlamaIndex instrumentation.

```python
from genops.providers.llamaindex import instrument_llamaindex

# Create adapter with governance defaults
adapter = instrument_llamaindex(
    team="ai-research",
    project="rag-system",
    customer_id="internal-demo"
)

# Track queries with team attribution
response = adapter.track_query(
    query_engine,
    "What is LlamaIndex?",
    team="ai-research",
    project="document-qa"
)

# Track agent conversations
agent_response = adapter.track_chat(
    agent,
    "Help me analyze this document",
    customer_id="enterprise-123"
)
```

#### Key Methods

- **`track_query()`** - Track query engine operations with cost attribution
- **`track_chat()`** - Track agent chat interactions with conversation context
- **`instrument_query_engine()`** - Add instrumentation to existing query engines
- **`instrument_agent()`** - Add instrumentation to existing agents
- **`get_operation_summary()`** - Get comprehensive operation statistics

### 2. Cost Aggregation and Budgeting

```python
from genops.providers.llamaindex import create_llamaindex_cost_context

# Track operations within a cost context
with create_llamaindex_cost_context("rag_demo", budget_limit=5.0) as context:
    
    # Multiple operations tracked together
    response1 = query_engine.query("Question 1")
    response2 = query_engine.query("Question 2") 
    
    # Get detailed cost breakdown
    summary = context.get_current_summary()
    print(f"Total Cost: ${summary.total_cost:.4f}")
    print(f"Embedding Cost: ${summary.cost_breakdown.embedding_cost:.4f}")
    print(f"Synthesis Cost: ${summary.cost_breakdown.synthesis_cost:.4f}")
```

#### Cost Tracking Features

- **Component-level costs** - Separate tracking for embeddings, retrieval, synthesis
- **Provider comparison** - Compare costs across OpenAI, Anthropic, Google
- **Budget enforcement** - Automatic limits and alerts
- **Cost forecasting** - Predict future spending based on usage patterns

### 3. Multi-Provider Cost Optimization

```python
from genops.providers.llamaindex import multi_provider_cost_tracking

# Track costs across multiple providers
tracker = multi_provider_cost_tracking(
    providers=['openai', 'anthropic', 'google'],
    budget_per_provider={
        'openai': 10.0,
        'anthropic': 15.0, 
        'google': 5.0
    },
    enable_cost_optimization=True,
    team="ai-research",
    project="multi-provider-rag"
)

# Get optimization recommendations
recommendation = tracker.get_cost_optimization_recommendation()
print(f"Best provider: {recommendation['best_provider']}")
print(f"Potential savings: ${recommendation['potential_savings']:.4f}")
```

### 4. RAG Pipeline Monitoring

```python
from genops.providers.llamaindex import create_rag_monitor

# Advanced RAG pipeline monitoring
rag_monitor = create_rag_monitor(
    enable_quality_metrics=True,
    enable_cost_tracking=True,
    enable_performance_profiling=True
)

# Monitor complete RAG operation
with rag_monitor.monitor_rag_operation("complex_query", team="research") as monitor:
    response = query_engine.query("Complex question requiring deep analysis")
    
    # Get detailed analytics
    analytics = rag_monitor.get_analytics()
    print(f"Retrieval Relevance: {analytics.avg_retrieval_relevance:.3f}")
    print(f"Response Quality: {analytics.avg_response_quality:.3f}")
    print(f"Average Latency: {analytics.avg_response_time_ms:.0f}ms")
```

## Advanced Features

### Agent Workflow Governance

Track complex multi-step agent operations:

```python
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool

# Create agent with tools
def calculator(operation: str, a: float, b: float) -> float:
    """Perform mathematical operations."""
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    # ... more operations

calc_tool = FunctionTool.from_defaults(fn=calculator)
agent = ReActAgent.from_tools([calc_tool], llm=Settings.llm)

# Track agent operations with governance
instrumented_agent = adapter.instrument_agent(
    agent,
    team="ai-agents",
    project="customer-support",
    tools_cost_tracking=True
)

# Track multi-step conversation
response = adapter.track_chat(
    instrumented_agent,
    "Calculate the compound interest on $10,000 at 5% for 3 years",
    customer_id="premium-customer-456",
    conversation_id="session-789"
)
```

### Production-Grade Error Handling

GenOps includes circuit breakers and graceful degradation:

```python
# Track queries with fallback providers
response = adapter.track_query(
    query_engine,
    "Important production query",
    fallback_providers=["anthropic", "google"],
    team="production",
    project="customer-facing-qa"
)

# System automatically falls back if primary provider fails
health_status = adapter.get_system_health()
print(f"Healthy providers: {health_status['healthy_providers']}")
```

### Real-Time Budget Enforcement

```python
from genops.providers.llamaindex import LlamaIndexCostAggregator

# Create aggregator with real-time enforcement
aggregator = LlamaIndexCostAggregator(
    context_name="production_rag",
    budget_limit=50.0,
    enable_alerts=True
)

# Check budget before expensive operations
operation_cost = 0.05  # Estimated cost
enforcement = aggregator.enforce_budget_constraints(
    operation_cost, 
    customer_id="enterprise-customer"
)

if enforcement["allowed"]:
    # Proceed with operation
    response = query_engine.query(expensive_query)
else:
    # Use alternative approach
    print(f"Operation blocked: {enforcement['reason']}")
    if enforcement["alternative_suggestion"]:
        print(f"Suggestion: {enforcement['alternative_suggestion']}")
```

### Quality Monitoring and Optimization

```python
# Monitor retrieval quality and optimize
with rag_monitor.monitor_rag_operation("quality_test") as monitor:
    # Configure quality thresholds
    monitor.set_quality_thresholds(
        min_retrieval_relevance=0.7,
        min_response_quality=0.8,
        max_response_time_ms=3000
    )
    
    response = query_engine.query("Test query for quality monitoring")
    
    # Get quality metrics
    quality_report = monitor.get_quality_report()
    
    if quality_report.below_threshold:
        print("⚠️ Quality below threshold:")
        for issue in quality_report.issues:
            print(f"  - {issue}")
        
        # Get optimization recommendations
        recommendations = monitor.get_optimization_recommendations()
        for rec in recommendations:
            print(f"💡 {rec}")
```

## Configuration and Customization

### Environment Variables

```bash
# Required: At least one AI provider API key
export OPENAI_API_KEY="sk-your-openai-key"
export ANTHROPIC_API_KEY="sk-ant-your-anthropic-key"
export GOOGLE_API_KEY="your-google-api-key"

# Optional: OpenTelemetry configuration
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
export OTEL_RESOURCE_ATTRIBUTES="service.name=genops-llamaindex"

# Optional: GenOps configuration
export GENOPS_ENVIRONMENT="production"
export GENOPS_TELEMETRY_ENABLED="true"
export GENOPS_COST_TRACKING_ENABLED="true"
```

### Custom Configuration

```python
from genops.providers.llamaindex import GenOpsLlamaIndexAdapter

# Create adapter with custom configuration
adapter = GenOpsLlamaIndexAdapter(
    telemetry_enabled=True,
    cost_tracking_enabled=True,
    debug=False,
    # Governance defaults
    team="default-team",
    project="default-project",
    environment="production",
    # Error handling configuration
    enable_graceful_degradation=True,
    retry_config=RetryConfig(max_retries=3, base_delay=1.0),
    # Budget controls
    default_budget_limit=100.0,
    enable_budget_alerts=True
)
```

## Production Deployment Patterns

### Kubernetes Integration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: genops-llamaindex-app
spec:
  template:
    spec:
      containers:
      - name: app
        image: your-app:latest
        env:
        - name: GENOPS_TELEMETRY_ENABLED
          value: "true"
        - name: GENOPS_ENVIRONMENT
          value: "production"
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: "http://otel-collector:4317"
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: ai-secrets
              key: openai-key
```

### Monitoring and Alerting

```python
# Set up comprehensive monitoring
from genops.providers.llamaindex import ProductionRAGDeployment, ProductionConfig

config = ProductionConfig(
    daily_budget_limit=100.0,
    max_response_time_ms=3000.0,
    target_availability=0.999,
    enable_circuit_breakers=True,
    enable_graceful_degradation=True
)

deployment = ProductionRAGDeployment(config)

# Monitor production traffic
with deployment.track_request("customer-123", "complex_query") as request:
    response = adapter.track_query(
        query_engine,
        user_query,
        customer_id="customer-123",
        priority="high"
    )
    request["cost"] = response.cost
    request["latency"] = response.latency

# Get production metrics
metrics = deployment.get_production_metrics()
alerts = deployment.check_all_alerts(metrics)
```

## Testing and Validation

### Setup Validation

```python
from genops.providers.llamaindex.validation import validate_setup, print_validation_result

# Comprehensive setup validation
result = validate_setup()

if result.success:
    print("✅ GenOps LlamaIndex setup is ready!")
else:
    print_validation_result(result, detailed=True)
```

### Cost Testing

```python
# Test cost calculations in development
from genops.providers.llamaindex import create_llamaindex_cost_context

with create_llamaindex_cost_context("cost_test", budget_limit=1.0) as context:
    # Test different query types
    simple_response = query_engine.query("Simple question")
    complex_response = query_engine.query("Complex multi-part analysis question")
    
    summary = context.get_current_summary()
    
    print(f"Simple query cost: ${summary.cost_breakdown.synthesis_cost / 2:.6f}")
    print(f"Complex query cost: ${summary.cost_breakdown.synthesis_cost / 2:.6f}")
    print(f"Embedding cost: ${summary.cost_breakdown.embedding_cost:.6f}")
```

## Troubleshooting

### Common Issues

**Import Errors**
```bash
# Fix LlamaIndex import issues
pip install llama-index>=0.10.0
pip install llama-index-llms-openai llama-index-embeddings-openai

# For Anthropic support
pip install llama-index-llms-anthropic

# For Google support  
pip install llama-index-llms-gemini
```

**Configuration Issues**
```python
# Ensure LlamaIndex is properly configured
from llama_index.core import Settings

# Both LLM and embedding model must be set
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding()

# Verify settings
print(f"LLM configured: {Settings.llm is not None}")
print(f"Embedding configured: {Settings.embed_model is not None}")
```

**API Key Issues**
```python
import os

# Check API key configuration
providers = {
    "OpenAI": os.getenv("OPENAI_API_KEY"),
    "Anthropic": os.getenv("ANTHROPIC_API_KEY"),
    "Google": os.getenv("GOOGLE_API_KEY")
}

configured_providers = {name: bool(key) for name, key in providers.items()}
print("Configured providers:", configured_providers)
```

**Telemetry Issues**
```python
# Debug telemetry export
import os

otel_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")
if otel_endpoint:
    print(f"Telemetry endpoint: {otel_endpoint}")
else:
    print("No telemetry endpoint configured (data stays local)")
```

### Performance Optimization

**Embedding Optimization**
```python
# Use caching for repeated embeddings
from genops.providers.llamaindex import create_rag_monitor

rag_monitor = create_rag_monitor(enable_embedding_cache=True)

# Monitor embedding efficiency
analytics = rag_monitor.get_embedding_analytics()
print(f"Cache hit rate: {analytics.cache_hit_rate:.1%}")
print(f"Embedding cost savings: ${analytics.cost_savings:.4f}")
```

**Provider Selection**
```python
# Optimize provider selection based on query complexity
def select_provider_by_complexity(query: str) -> str:
    if len(query) < 100:
        return "google"  # Cheapest for simple queries
    elif len(query) < 500:
        return "openai"  # Balanced cost/quality
    else:
        return "anthropic"  # Best for complex queries

provider = select_provider_by_complexity(user_query)
response = adapter.track_query(
    query_engine,
    user_query,
    provider=provider,
    cost_optimization=True
)
```

## API Reference

### Classes

- **`GenOpsLlamaIndexAdapter`** - Main instrumentation adapter
- **`LlamaIndexCostAggregator`** - Cost tracking and budgeting
- **`LlamaIndexRAGInstrumentor`** - RAG pipeline monitoring
- **`ProviderHealthMonitor`** - Multi-provider health management

### Functions

- **`instrument_llamaindex()`** - Create configured adapter
- **`auto_instrument()`** - Enable global auto-instrumentation
- **`create_llamaindex_cost_context()`** - Cost tracking context manager
- **`multi_provider_cost_tracking()`** - Multi-provider optimization
- **`create_rag_monitor()`** - RAG quality monitoring

### Context Managers

- **`create_llamaindex_cost_context()`** - Track costs within scope
- **`monitor_rag_operation()`** - Monitor RAG pipeline quality
- **`track_request()`** - Production request tracking

## Examples

Complete working examples are available in the [`examples/llamaindex/`](../../examples/llamaindex/) directory:

- **`hello_genops_minimal.py`** - 30-second quickstart
- **`auto_instrumentation.py`** - Zero-code integration
- **`rag_pipeline_tracking.py`** - Comprehensive RAG monitoring
- **`embedding_cost_optimization.py`** - Embedding efficiency
- **`advanced_agent_governance.py`** - Agent workflow tracking
- **`multi_modal_rag.py`** - Complex RAG patterns
- **`production_rag_deployment.py`** - Enterprise deployment

## Support and Community

- **Documentation**: [GenOps AI Docs](https://docs.genops.ai)
- **Examples**: [GitHub Examples](https://github.com/KoshiHQ/GenOps-AI/tree/main/examples/llamaindex)
- **Issues**: [GitHub Issues](https://github.com/KoshiHQ/GenOps-AI/issues)
- **Discussions**: [Community Forum](https://github.com/KoshiHQ/GenOps-AI/discussions)

---

## 📚 Navigation & Next Steps

**🎯 Getting Started:**
- **[5-Minute Quickstart](../llamaindex-quickstart.md)** - Copy-paste examples to get running immediately
- **[Examples Directory](../../examples/llamaindex/)** - Step-by-step practical tutorials with clear progression

**🏗️ Production Deployment:**
- **[Security Best Practices](../security-best-practices.md)** - Enterprise security, compliance, and API key management
- **[CI/CD Integration Guide](../ci-cd-integration.md)** - Automated testing, budget gates, and deployment pipelines

**🤝 Community & Support:**
- **[GitHub Repository](https://github.com/KoshiHQ/GenOps-AI)** - Source code and latest updates
- **[Community Discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)** - Questions, ideas, and community help
- **[Issue Tracker](https://github.com/KoshiHQ/GenOps-AI/issues)** - Bug reports and feature requests

**Ready to implement production GenOps governance for your LlamaIndex applications? Start with the [quickstart guide](../llamaindex-quickstart.md) or jump into the [examples](../../examples/llamaindex/)!**