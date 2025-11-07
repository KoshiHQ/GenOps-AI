# Langfuse LLM Observability Integration Guide

## Overview

The GenOps Langfuse adapter provides comprehensive governance integration for Langfuse LLM observability platform, including:

- **Enhanced LLM Observability** with governance attribute propagation to all traces
- **Cost Intelligence Integration** with precise cost tracking and team attribution
- **Policy Compliance Enforcement** with budget controls and governance automation
- **Evaluation Governance** with LLM evaluation tracking and cost oversight
- **Enterprise-Ready Patterns** with production deployment and monitoring capabilities
- **Zero-Code Auto-Instrumentation** with seamless integration for existing applications

## Quick Start

### Installation

```bash
pip install genops[langfuse]
```

### Basic Setup

The simplest way to add GenOps governance to your Langfuse observability:

```python
from genops.providers.langfuse import instrument_langfuse

# Initialize GenOps Langfuse integration
adapter = instrument_langfuse(
    langfuse_public_key="pk-lf-your-public-key",
    langfuse_secret_key="sk-lf-your-secret-key",
    team="ai-team",
    project="llm-observability"
)

# Enhanced tracing with governance
with adapter.trace_with_governance(
    name="enhanced_analysis",
    customer_id="enterprise_123",
    cost_center="research"
) as trace:
    
    response = adapter.generation_with_cost_tracking(
        prompt="Analyze market trends...",
        model="gpt-4",
        max_cost=0.50,  # Budget enforcement
        team="research-team",
        project="market-analysis"
    )
```

### Auto-Instrumentation (Recommended)

For zero-code setup, enable auto-instrumentation:

```python
from genops import init
from genops.providers.langfuse import instrument_langfuse

# Automatically enhance all Langfuse operations with governance
instrument_langfuse(
    team="auto-instrumented",
    project="zero-code-governance"
)

# Your existing Langfuse code automatically gets governance
from langfuse.decorators import observe

@observe()
def my_llm_function():
    # Automatically enhanced with cost tracking and governance
    return openai.chat.completions.create(...)
```

## Core Features

### 1. Enhanced Tracing with Governance

Extend Langfuse traces with comprehensive governance attributes:

```python
from genops.providers.langfuse import GenOpsLangfuseAdapter

adapter = GenOpsLangfuseAdapter(
    langfuse_public_key="pk-lf-your-key",
    langfuse_secret_key="sk-lf-your-key",
    team="observability-team",
    project="enhanced-tracing"
)

# Context manager for complex workflows
with adapter.trace_with_governance(
    name="complex_workflow",
    customer_id="customer_456",
    cost_center="ai-research",
    feature="sentiment-analysis"
) as trace:
    
    # Multiple operations within governed trace
    preprocessing = adapter.generation_with_cost_tracking(
        prompt="Clean and prepare this data...",
        model="gpt-3.5-turbo",
        max_cost=0.10
    )
    
    analysis = adapter.generation_with_cost_tracking(
        prompt="Perform sentiment analysis...",
        model="gpt-4",
        max_cost=0.25
    )
    
    summary = adapter.generation_with_cost_tracking(
        prompt="Summarize findings...",
        model="gpt-3.5-turbo",
        max_cost=0.05
    )
```

**Telemetry Captured:**
- Enhanced Langfuse traces with GenOps governance metadata
- Cost attribution per operation with team/project breakdown
- Policy compliance status and violation tracking
- Performance metrics with governance context
- Budget utilization and remaining limits

### 2. LLM Evaluation with Governance

Integrate governance with Langfuse's evaluation capabilities:

```python
from genops.providers.langfuse import GenOpsLangfuseAdapter

adapter = GenOpsLangfuseAdapter(
    team="evaluation-team",
    budget_limits={"daily": 50.0, "monthly": 1000.0}
)

# Custom evaluation function
def quality_evaluator():
    return {
        "score": 0.92,
        "comment": "High quality response with accurate information"
    }

# Run evaluation with governance tracking
evaluation_result = adapter.evaluate_with_governance(
    trace_id="trace-12345",
    evaluation_name="response_quality",
    evaluator_function=quality_evaluator,
    customer_id="enterprise_789",
    cost_center="quality-assurance"
)

print(f"Evaluation score: {evaluation_result['score']}")
print(f"Evaluation cost tracked for: {evaluation_result['governance']['team']}")
print(f"Duration: {evaluation_result['duration_ms']}ms")
```

### 3. Cost Intelligence and Budget Management

Advanced cost tracking with policy enforcement:

```python
from genops.providers.langfuse import GenOpsLangfuseAdapter, GovernancePolicy

adapter = GenOpsLangfuseAdapter(
    team="cost-conscious-team",
    budget_limits={
        "daily": 100.0,     # $100 daily limit
        "monthly": 2500.0,  # $2500 monthly limit
    },
    policy_mode=GovernancePolicy.ENFORCED  # Block violations
)

# Budget-aware operations
try:
    response = adapter.generation_with_cost_tracking(
        prompt="Expensive analysis task...",
        model="gpt-4",
        max_cost=5.0,  # Per-operation limit
        team="research",
        customer_id="enterprise_client"
    )
    
    print(f"Operation cost: ${response.usage.cost:.6f}")
    print(f"Team: {response.usage.team}")
    print(f"Budget remaining: ${response.usage.budget_remaining:.2f}")
    
except ValueError as e:
    print(f"Operation blocked: {e}")
    # Handle budget violation
```

### 4. Advanced Governance Patterns

Production-ready governance automation:

```python
from genops.providers.langfuse import GenOpsLangfuseAdapter
import os

adapter = GenOpsLangfuseAdapter(
    # Production configuration
    team=os.getenv("TEAM_NAME", "production"),
    project=os.getenv("PROJECT_NAME", "main-app"),
    environment=os.getenv("ENVIRONMENT", "production"),
    
    # Enterprise governance
    budget_limits={
        "daily": float(os.getenv("DAILY_BUDGET", "200.0")),
        "monthly": float(os.getenv("MONTHLY_BUDGET", "5000.0"))
    },
    policy_mode=GovernancePolicy.ENFORCED,
    enable_governance=True
)

# Production workflow with comprehensive governance
def production_llm_workflow(customer_request):
    with adapter.trace_with_governance(
        name="production_request",
        customer_id=customer_request.customer_id,
        feature=customer_request.feature,
        priority=customer_request.priority
    ) as trace:
        
        # Multi-step workflow with governance at each step
        steps = [
            ("validation", "Validate user input", 0.02),
            ("processing", "Process request", 0.15),
            ("analysis", "Perform analysis", 0.30),
            ("response", "Generate response", 0.10)
        ]
        
        results = {}
        for step_name, prompt, max_cost in steps:
            try:
                result = adapter.generation_with_cost_tracking(
                    prompt=f"{prompt}: {customer_request.content}",
                    model="gpt-4",
                    max_cost=max_cost,
                    operation=step_name
                )
                results[step_name] = result
                
            except Exception as e:
                # Handle governance violations or failures
                trace.update(metadata={
                    "error": str(e),
                    "failed_step": step_name,
                    "governance_status": "violation"
                })
                raise
        
        return results
```

## Configuration

### Environment Variables

The adapter automatically reads from environment variables:

```bash
# Required Langfuse configuration
export LANGFUSE_PUBLIC_KEY="pk-lf-your-public-key"
export LANGFUSE_SECRET_KEY="sk-lf-your-secret-key"
export LANGFUSE_BASE_URL="https://cloud.langfuse.com"  # Optional

# LLM provider keys (at least one required)
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"

# Optional: GenOps governance configuration
export GENOPS_SERVICE_NAME="my-observability-service"
export GENOPS_ENVIRONMENT="production"
```

### Manual Configuration

For programmatic configuration:

```python
from genops.providers.langfuse import GenOpsLangfuseAdapter, GovernancePolicy

adapter = GenOpsLangfuseAdapter(
    # Langfuse configuration
    langfuse_public_key="pk-lf-your-key",
    langfuse_secret_key="sk-lf-your-key",
    langfuse_base_url="https://your-instance.langfuse.com",
    
    # GenOps governance
    team="advanced-ai",
    project="observability-platform", 
    environment="production",
    
    # Budget and policy configuration
    budget_limits={
        "hourly": 25.0,
        "daily": 200.0,
        "monthly": 5000.0
    },
    policy_mode=GovernancePolicy.ENFORCED,
    enable_governance=True
)
```

## Advanced Features

### 1. Custom Cost Models

Define custom cost models for specialized pricing:

```python
adapter = GenOpsLangfuseAdapter(
    team="custom-pricing"
)

# Override default cost calculation
adapter.cost_per_token.update({
    "custom-model": {
        "input": 0.00005,
        "output": 0.00015
    }
})

# Use custom model with governance
response = adapter.generation_with_cost_tracking(
    prompt="Custom model analysis...",
    model="custom-model",
    max_cost=1.0
)
```

### 2. Multi-Team Cost Attribution

Advanced cost attribution across teams:

```python
# Team-specific adapters with shared governance
teams = ["research", "product", "engineering"]
adapters = {}

for team in teams:
    adapters[team] = GenOpsLangfuseAdapter(
        team=team,
        project="multi-team-platform",
        budget_limits={f"{team}_daily": 100.0}
    )

# Route operations to appropriate team adapter
def route_request(request, team):
    adapter = adapters[team]
    
    with adapter.trace_with_governance(
        name=f"{team}_request",
        customer_id=request.customer_id,
        priority=request.priority
    ) as trace:
        
        return adapter.generation_with_cost_tracking(
            prompt=request.prompt,
            model=request.model,
            team=team,
            max_cost=request.budget
        )
```

### 3. Integration with Enterprise Systems

Connect with enterprise monitoring and alerting:

```python
from genops.providers.langfuse import GenOpsLangfuseAdapter

class EnterpriseAdapter(GenOpsLangfuseAdapter):
    """Extended adapter with enterprise integrations."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize enterprise connections
        self.alerting_client = self._init_alerting()
        self.metrics_client = self._init_metrics()
    
    def _send_cost_alert(self, cost, limit):
        """Send cost alert to enterprise systems."""
        self.alerting_client.send_alert({
            "type": "budget_warning",
            "team": self.team,
            "cost": cost,
            "limit": limit,
            "timestamp": time.time()
        })
    
    def _export_metrics(self, metrics):
        """Export governance metrics to enterprise monitoring."""
        self.metrics_client.gauge("genops.langfuse.cost", metrics.cost, 
                                 tags={"team": self.team})
        self.metrics_client.counter("genops.langfuse.operations", 
                                   tags={"team": self.team})

# Use enterprise adapter
adapter = EnterpriseAdapter(
    team="enterprise-ai",
    budget_limits={"daily": 500.0}
)
```

## Validation and Troubleshooting

### Setup Validation

Validate your Langfuse integration:

```python
from genops.providers.langfuse_validation import validate_setup, print_validation_result

# Comprehensive setup validation
result = validate_setup(include_performance_tests=True)
print_validation_result(result, detailed=True)
```

**Example validation output:**
```
🔍 GenOps + Langfuse Integration Validation

✅ Overall Status: PASSED

📊 Test Summary:
   Total Tests: 5
   ✅ Passed: 4
   ❌ Failed: 0
   ⚠️  Warnings: 1
   ⏭️  Skipped: 0

📋 Detailed Results:
   ✅ Langfuse Installation: Langfuse package successfully imported (45ms)
   ✅ Langfuse Configuration: Langfuse configuration valid (12ms)
   ✅ Langfuse Connectivity: Successfully connected to Langfuse API (289ms)
   ✅ GenOps Integration: GenOps Langfuse integration working correctly (67ms)
   ⚠️  Performance Baseline: Performance baseline acceptable (156ms)

💡 Recommendations:
   1. Langfuse integration is ready - proceed with examples and production usage
```

### Common Issues

**Issue: Authentication failures**
```python
# Check API key configuration
from genops.providers.langfuse_validation import validate_langfuse_configuration

result = validate_langfuse_configuration()
if result.status != "PASSED":
    print(f"Configuration issue: {result.fix_suggestion}")
```

**Issue: Cost tracking accuracy**
```python
# Enable detailed cost debugging
adapter = GenOpsLangfuseAdapter(
    enable_governance=True
)

# Monitor cost calculations
response = adapter.generation_with_cost_tracking(
    prompt="Test prompt",
    model="gpt-3.5-turbo"
)
print(f"Detailed cost breakdown: {response.usage}")
```

**Issue: Performance optimization**
```python
# Optimize for high-throughput scenarios
adapter = GenOpsLangfuseAdapter(
    team="high-performance",
    # Reduce governance overhead for performance
    enable_governance=False  # For non-production workloads
)
```

## Best Practices

### 1. Governance Attribute Strategy

```python
# Good: Consistent governance attributes
response = adapter.generation_with_cost_tracking(
    prompt="Analysis task",
    model="gpt-4",
    team="research",           # Consistent team naming
    project="market-analysis", # Clear project identification
    customer_id="enterprise_123",  # Customer attribution
    cost_center="ai-research", # Financial tracking
    feature="sentiment-analysis"  # Feature-level tracking
)

# Better: Use environment variables for consistency
import os

response = adapter.generation_with_cost_tracking(
    prompt="Analysis task",
    model="gpt-4",
    team=os.getenv("TEAM_NAME"),
    project=os.getenv("PROJECT_NAME"),
    customer_id=request.customer_id
)
```

### 2. Budget Management

```python
# Good: Per-team budget limits
team_adapters = {
    "research": GenOpsLangfuseAdapter(
        team="research", 
        budget_limits={"daily": 200.0}
    ),
    "product": GenOpsLangfuseAdapter(
        team="product",
        budget_limits={"daily": 100.0}
    )
}

# Better: Dynamic budget allocation
def get_team_budget(team, time_period="daily"):
    base_budgets = {"research": 200.0, "product": 100.0}
    # Adjust based on usage patterns, time of day, etc.
    return base_budgets.get(team, 50.0)

adapter = GenOpsLangfuseAdapter(
    team="dynamic-team",
    budget_limits={"daily": get_team_budget("research")}
)
```

### 3. Error Handling

```python
from genops.providers.langfuse import GenOpsLangfuseAdapter
import logging

logger = logging.getLogger(__name__)

def robust_llm_operation(prompt, model):
    try:
        with adapter.trace_with_governance(
            name="robust_operation"
        ) as trace:
            
            response = adapter.generation_with_cost_tracking(
                prompt=prompt,
                model=model,
                max_cost=1.0
            )
            
            return response
            
    except ValueError as e:
        # Handle budget/policy violations
        logger.warning(f"Governance violation: {e}")
        # Implement fallback strategy
        return fallback_response(prompt)
        
    except Exception as e:
        # Handle other errors
        logger.error(f"LLM operation failed: {e}")
        raise
```

## Performance Considerations

### Async Support

For high-throughput applications:

```python
import asyncio
from genops.providers.langfuse import GenOpsLangfuseAdapter

adapter = GenOpsLangfuseAdapter(team="async-processing")

async def process_batch(prompts):
    """Process multiple requests concurrently with governance."""
    tasks = []
    
    for i, prompt in enumerate(prompts):
        # Create async context for each operation
        task = asyncio.create_task(
            async_generation_with_governance(prompt, f"batch_item_{i}")
        )
        tasks.append(task)
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results

async def async_generation_with_governance(prompt, operation_id):
    """Async LLM operation with governance."""
    # Implement async version of generation_with_cost_tracking
    # This would use async Langfuse client when available
    pass
```

### Caching Strategy

Optimize performance with intelligent caching:

```python
from functools import lru_cache
import hashlib

class CachedLangfuseAdapter(GenOpsLangfuseAdapter):
    """Adapter with intelligent caching for governance metadata."""
    
    @lru_cache(maxsize=1000)
    def _get_cached_governance_attrs(self, team, project, customer_id):
        """Cache frequently used governance attribute combinations."""
        return {
            "team": team,
            "project": project,
            "customer_id": customer_id,
            "cached": True
        }
    
    def generation_with_cost_tracking(self, prompt, **kwargs):
        # Use cached governance attributes for better performance
        governance_key = (
            kwargs.get("team", self.team),
            kwargs.get("project", self.project),
            kwargs.get("customer_id")
        )
        
        cached_attrs = self._get_cached_governance_attrs(*governance_key)
        kwargs.update(cached_attrs)
        
        return super().generation_with_cost_tracking(prompt, **kwargs)
```

## Monitoring and Observability

### Custom Metrics Export

Export governance metrics to monitoring systems:

```python
from genops.providers.langfuse import GenOpsLangfuseAdapter
import time

class MonitoredAdapter(GenOpsLangfuseAdapter):
    """Adapter with enhanced monitoring capabilities."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.metrics_collector = self._init_metrics()
    
    def generation_with_cost_tracking(self, *args, **kwargs):
        start_time = time.time()
        
        try:
            response = super().generation_with_cost_tracking(*args, **kwargs)
            
            # Export success metrics
            self.metrics_collector.counter("genops.langfuse.requests.success",
                                         tags={"team": self.team})
            self.metrics_collector.histogram("genops.langfuse.cost",
                                           response.usage.cost,
                                           tags={"team": self.team})
            
            return response
            
        except Exception as e:
            # Export error metrics
            self.metrics_collector.counter("genops.langfuse.requests.error",
                                         tags={"team": self.team, "error": type(e).__name__})
            raise
            
        finally:
            duration = time.time() - start_time
            self.metrics_collector.histogram("genops.langfuse.duration",
                                           duration * 1000,  # Convert to ms
                                           tags={"team": self.team})
```

For detailed setup instructions and additional examples, see the [Langfuse Quickstart Guide](../langfuse-quickstart.md).