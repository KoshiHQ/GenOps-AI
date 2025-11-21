# Flowise Integration Guide

**Complete integration guide for Flowise visual AI workflow platform with GenOps governance and cost tracking.**

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)  
- [Quick Setup](#quick-setup)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Cost Tracking](#cost-tracking)
- [Advanced Patterns](#advanced-patterns)
- [Production Deployment](#production-deployment)
- [Troubleshooting](#troubleshooting)
- [Examples](#examples)

---

## Overview

### What is Flowise?

Flowise is an open-source, low-code platform for building customized AI agents and chatflows using LangChain. It provides:

- **Visual Flow Builder**: Drag-and-drop interface for creating AI workflows
- **Multi-Provider Support**: Works with OpenAI, Anthropic, Hugging Face, and other providers  
- **RAG Capabilities**: Built-in support for vector databases and document processing
- **API Integration**: REST APIs for integrating flows into applications
- **Self-Hosted or Cloud**: Deploy locally or use Flowise Cloud

### GenOps Integration Benefits

The GenOps-Flowise integration provides comprehensive governance for your Flowise deployments:

✅ **Automatic Cost Tracking**: Real-time cost calculation across all underlying LLM providers  
✅ **Team Attribution**: Multi-tenant cost allocation and project tracking  
✅ **Usage Monitoring**: Token consumption, execution metrics, and performance analysis  
✅ **Multi-Provider Aggregation**: Unified cost view across OpenAI, Anthropic, etc.  
✅ **OpenTelemetry Export**: Standard telemetry for existing observability stacks  
✅ **Zero-Code Auto-Instrumentation**: Works with existing Flowise applications  
✅ **Enterprise Governance**: Policy enforcement and compliance monitoring  

### Integration Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│   Your App      │    │   GenOps         │    │   Observability     │
│                 │    │   Flowise        │    │   Platform          │
│ ┌─────────────┐ │    │   Integration    │    │                     │
│ │   Flowise   │ │───▶│                  │───▶│  • Datadog          │
│ │   API Calls │ │    │ ┌──────────────┐ │    │  • Grafana          │
│ └─────────────┘ │    │ │ Auto-Instr.  │ │    │  • Honeycomb        │
│                 │    │ │ Layer        │ │    │  • Custom Dashbd    │
│ ┌─────────────┐ │    │ └──────────────┘ │    │                     │
│ │   Manual    │ │    │                  │    │ ┌─────────────────┐ │
│ │   Adapter   │ │───▶│ ┌──────────────┐ │    │ │  Cost Reports   │ │ 
│ └─────────────┘ │    │ │ Cost Calc.   │ │    │ │  Usage Analytics│ │
└─────────────────┘    │ │ Engine       │ │    │ │  Team Dashboards│ │
                       │ └──────────────┘ │    │ └─────────────────┘ │
                       └──────────────────┘    └─────────────────────┘
```

---

## Architecture

### Core Components

#### 1. GenOpsFlowiseAdapter

Main adapter class providing governance-enabled Flowise API access:

```python
from genops.providers.flowise import GenOpsFlowiseAdapter

adapter = GenOpsFlowiseAdapter(
    base_url="http://localhost:3000",
    api_key="your-api-key",  # Optional for local development
    team="ai-team",
    project="customer-support",
    environment="production"
)

# Execute chatflow with full governance tracking
response = adapter.predict_flow(
    chatflow_id="abc123",
    question="What are your business hours?",
    sessionId="user-456"
)
```

#### 2. Auto-Instrumentation Engine

Transparent instrumentation layer that requires zero code changes:

```python
from genops.providers.flowise import auto_instrument

# Enable automatic tracking for all Flowise API calls
auto_instrument(team="your-team", project="your-project")

# Your existing code works unchanged
import requests
response = requests.post(
    "http://localhost:3000/api/v1/prediction/chatflow-id",
    json={"question": "Hello!"}
)
```

#### 3. Cost Calculation Engine

Multi-provider cost aggregation with Flowise-specific pricing:

```python
from genops.providers.flowise_pricing import FlowiseCostCalculator

calculator = FlowiseCostCalculator(pricing_tier="cloud_pro")
cost = calculator.calculate_execution_cost(
    "chatflow-123",
    "Customer Support Bot", 
    underlying_provider_calls=[
        {'provider': 'openai', 'model': 'gpt-4', 'input_tokens': 100, 'output_tokens': 50}
    ]
)
```

#### 4. Validation and Diagnostics

Comprehensive setup validation and troubleshooting:

```python
from genops.providers.flowise_validation import validate_flowise_setup, print_validation_result

result = validate_flowise_setup()
print_validation_result(result)
```

---

## Quick Setup

### Installation

```bash
pip install genops requests
```

### Environment Variables

Set up your environment for automatic configuration:

```bash
# Flowise Configuration
export FLOWISE_BASE_URL="http://localhost:3000"  # Your Flowise instance
export FLOWISE_API_KEY="your-api-key"           # Optional for local dev

# Governance Configuration
export GENOPS_TEAM="ai-team"
export GENOPS_PROJECT="customer-support"
export GENOPS_ENVIRONMENT="production"
export GENOPS_CUSTOMER_ID="customer-123"  # Optional
export GENOPS_COST_CENTER="engineering"   # Optional

# OpenTelemetry Export (choose your platform)
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.datadoghq.com"
export OTEL_EXPORTER_OTLP_HEADERS="dd-api-key=your-datadog-key"
```

### Auto-Instrumentation (Recommended)

Enable automatic tracking for all Flowise API calls:

```python
from genops.providers.flowise import auto_instrument

# Enable with environment variable configuration
auto_instrument()

# Or configure explicitly
auto_instrument(
    base_url="http://localhost:3000",
    team="ai-team", 
    project="customer-support",
    environment="production"
)

# Your existing Flowise code now has governance tracking!
```

### Manual Instrumentation (Advanced)

For more control over the integration:

```python
from genops.providers.flowise import instrument_flowise

flowise = instrument_flowise(
    base_url="http://localhost:3000",
    api_key="your-api-key",
    team="ai-team",
    project="customer-support"
)

# Execute flows with explicit governance
response = flowise.predict_flow(
    chatflow_id="abc123",
    question="What are your business hours?",
    team="specific-team",  # Override default
    customer_id="customer-456"  # Per-customer attribution
)
```

---

## Configuration

### Adapter Configuration

#### Basic Configuration

```python
from genops.providers.flowise import GenOpsFlowiseAdapter

# Minimum configuration
adapter = GenOpsFlowiseAdapter()  # Uses environment variables

# Explicit configuration
adapter = GenOpsFlowiseAdapter(
    base_url="https://your-flowise.example.com",
    api_key="fl-your-api-key-here",
    team="ai-engineering",
    project="chatbot-v2"
)
```

#### Advanced Configuration

```python
adapter = GenOpsFlowiseAdapter(
    # Connection settings
    base_url="https://your-flowise.example.com",
    api_key="fl-your-api-key-here",
    
    # Governance attributes (per CLAUDE.md standards)
    team="ai-engineering",
    project="customer-support-bot",
    environment="production",
    cost_center="product-engineering", 
    customer_id="enterprise-customer-123",
    feature="multilingual-support",
    
    # Custom attributes
    deployment_region="us-west-2",
    service_tier="premium"
)
```

### Auto-Instrumentation Configuration

#### Basic Auto-Instrumentation

```python
from genops.providers.flowise import auto_instrument

# Environment-based configuration
auto_instrument()

# Explicit configuration
auto_instrument(
    base_url="http://localhost:3000",
    team="ai-team",
    project="customer-support"
)
```

#### Advanced Auto-Instrumentation

```python
auto_instrument(
    # Connection configuration
    base_url="https://your-flowise.example.com", 
    api_key="fl-your-api-key-here",
    
    # Default governance attributes
    team="ai-engineering",
    project="customer-support-v2",
    environment="production",
    cost_center="product-team",
    
    # Instrumentation options
    enable_console_export=True,  # Show telemetry in console (dev)
    sample_rate=1.0,            # Sample 100% of requests
    
    # Custom tags
    application="customer-support",
    version="v2.1.0"
)
```

### Environment Variable Reference

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `FLOWISE_BASE_URL` | Flowise instance URL | `http://localhost:3000` | Yes |
| `FLOWISE_API_KEY` | Flowise API key | `fl-abc123...` | No (local dev) |
| `GENOPS_TEAM` | Team for cost attribution | `ai-engineering` | Recommended |
| `GENOPS_PROJECT` | Project identifier | `customer-support` | Recommended |
| `GENOPS_ENVIRONMENT` | Environment (dev/staging/prod) | `production` | Recommended |
| `GENOPS_CUSTOMER_ID` | Customer identifier | `customer-123` | Optional |
| `GENOPS_COST_CENTER` | Cost center for billing | `engineering` | Optional |
| `GENOPS_FEATURE` | Feature identifier | `multilingual` | Optional |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OpenTelemetry endpoint | `https://api.datadoghq.com` | Optional |
| `OTEL_EXPORTER_OTLP_HEADERS` | OTel headers | `dd-api-key=key` | Optional |

---

## API Reference

### GenOpsFlowiseAdapter

#### Constructor

```python
GenOpsFlowiseAdapter(
    base_url: str = "http://localhost:3000",
    api_key: Optional[str] = None,
    team: Optional[str] = None,
    project: Optional[str] = None,
    environment: Optional[str] = None,
    cost_center: Optional[str] = None,
    customer_id: Optional[str] = None,
    feature: Optional[str] = None,
    **kwargs
) -> GenOpsFlowiseAdapter
```

**Parameters:**
- `base_url`: Flowise instance URL (defaults to localhost)
- `api_key`: Flowise API key (auto-detected from `FLOWISE_API_KEY`)
- `team`: Team for cost attribution (auto-detected from `GENOPS_TEAM`)
- `project`: Project identifier (auto-detected from `GENOPS_PROJECT`) 
- `environment`: Environment name (auto-detected from `GENOPS_ENVIRONMENT`)
- `cost_center`: Cost center (auto-detected from `GENOPS_COST_CENTER`)
- `customer_id`: Customer ID (auto-detected from `GENOPS_CUSTOMER_ID`)
- `feature`: Feature identifier (auto-detected from `GENOPS_FEATURE`)
- `**kwargs`: Additional governance attributes

#### Methods

##### predict_flow()

Execute a Flowise chatflow with governance tracking.

```python
predict_flow(
    chatflow_id: str,
    question: str,
    sessionId: Optional[str] = None,
    overrideConfig: Optional[Dict] = None,
    history: Optional[List[Dict]] = None,
    stream: bool = False,
    **kwargs
) -> Any
```

**Parameters:**
- `chatflow_id`: Unique identifier for the chatflow
- `question`: Input question/prompt for the flow
- `sessionId`: Optional session identifier for conversation continuity
- `overrideConfig`: Optional configuration overrides for the flow
- `history`: Optional conversation history
- `stream`: Enable streaming response (if supported)
- `**kwargs`: Additional governance attributes for this execution

**Example:**
```python
response = adapter.predict_flow(
    chatflow_id="customer-support-v1",
    question="What are your business hours?",
    sessionId="user-session-123",
    overrideConfig={
        "temperature": 0.7,
        "maxTokens": 150
    },
    history=[
        {"role": "user", "message": "Hello"},
        {"role": "assistant", "message": "Hi! How can I help you today?"}
    ],
    # Override governance attributes for this specific call
    customer_id="premium-customer-456",
    feature="business-hours-inquiry"
)

print(f"Response: {response.get('text', 'No response')}")
```

##### get_chatflows()

Get list of available chatflows.

```python
get_chatflows(**kwargs) -> List[Dict]
```

**Example:**
```python
chatflows = adapter.get_chatflows()
for flow in chatflows:
    print(f"Flow: {flow['name']} (ID: {flow['id']})")
```

##### get_chatflow()

Get details of a specific chatflow.

```python
get_chatflow(chatflow_id: str, **kwargs) -> Dict
```

**Example:**
```python
flow_details = adapter.get_chatflow("customer-support-v1")
print(f"Flow name: {flow_details['name']}")
print(f"Flow category: {flow_details.get('category', 'Unknown')}")
```

##### get_chat_messages()

Get chat message history for a chatflow and session.

```python
get_chat_messages(
    chatflow_id: str,
    session_id: Optional[str] = None,
    **kwargs
) -> List[Dict]
```

**Example:**
```python
messages = adapter.get_chat_messages("customer-support-v1", "user-session-123")
for msg in messages:
    print(f"{msg.get('role', 'unknown')}: {msg.get('message', '')}")
```

##### delete_chat_messages()

Delete chat message history.

```python
delete_chat_messages(
    chatflow_id: str,
    session_id: Optional[str] = None,
    **kwargs
) -> Dict
```

**Example:**
```python
# Delete all messages for a chatflow
adapter.delete_chat_messages("customer-support-v1")

# Delete messages for a specific session
adapter.delete_chat_messages("customer-support-v1", "user-session-123")
```

### Auto-Instrumentation Functions

#### auto_instrument()

Enable automatic instrumentation for all Flowise API calls.

```python
auto_instrument(
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    team: Optional[str] = None,
    project: Optional[str] = None,
    environment: Optional[str] = None,
    enable_console_export: bool = False,
    **config
) -> bool
```

**Returns:** `True` if instrumentation was successful, `False` otherwise.

**Example:**
```python
from genops.providers.flowise import auto_instrument

success = auto_instrument(
    base_url="http://localhost:3000",
    team="ai-team",
    project="chatbot-v2",
    enable_console_export=True  # Show telemetry in console for debugging
)

if success:
    print("✅ Auto-instrumentation enabled")
else:
    print("❌ Auto-instrumentation failed")
```

#### disable_auto_instrument()

Disable auto-instrumentation and restore original HTTP methods.

```python
disable_auto_instrument() -> bool
```

**Example:**
```python
from genops.providers.flowise import disable_auto_instrument

if disable_auto_instrument():
    print("Auto-instrumentation disabled")
```

### Validation Functions

#### validate_flowise_setup()

Comprehensive Flowise setup validation.

```python
from genops.providers.flowise_validation import validate_flowise_setup

validate_flowise_setup(
    base_url: Optional[str] = None,
    api_key: Optional[str] = None,
    timeout: int = 10
) -> ValidationResult
```

**Example:**
```python
result = validate_flowise_setup()
if result.is_valid:
    print("✅ Setup is valid")
    print(f"Found {len(result.available_chatflows)} chatflows")
else:
    for issue in result.issues:
        if issue.severity == "error":
            print(f"❌ {issue.component}: {issue.message}")
```

#### print_validation_result()

Print validation results in user-friendly format.

```python
from genops.providers.flowise_validation import print_validation_result

result = validate_flowise_setup()
print_validation_result(result)
```

#### quick_test_flow()

Quick test of a Flowise chatflow.

```python
from genops.providers.flowise_validation import quick_test_flow

result = quick_test_flow(
    chatflow_id="customer-support-v1",
    question="Test question",
    base_url="http://localhost:3000"
)

if result['success']:
    print(f"✅ Flow test successful: {result['response']}")
else:
    print(f"❌ Flow test failed: {result['error']}")
```

---

## Cost Tracking

### Overview

The Flowise integration provides comprehensive cost tracking across multiple dimensions:

- **Flowise Platform Costs**: Execution costs based on your Flowise pricing tier
- **Underlying Provider Costs**: Aggregated costs from OpenAI, Anthropic, etc.
- **Token Usage**: Input/output token tracking for cost optimization
- **Multi-Provider Attribution**: Cost breakdown by LLM provider
- **Team/Project Attribution**: Cost allocation for internal billing

### Cost Calculation Architecture

```python
from genops.providers.flowise_pricing import FlowiseCostCalculator

# Initialize cost calculator
calculator = FlowiseCostCalculator(
    pricing_tier="cloud_pro",  # or "self_hosted", "cloud_free", etc.
    monthly_execution_count=15000  # For overage calculation
)

# Calculate cost for a single execution
cost = calculator.calculate_execution_cost(
    flow_id="customer-support-v1",
    flow_name="Customer Support Chatbot",
    underlying_provider_calls=[
        {
            'provider': 'openai',
            'model': 'gpt-4',
            'input_tokens': 150,
            'output_tokens': 75,
            'cost': 0.0135  # Pre-calculated or will be estimated
        },
        {
            'provider': 'anthropic', 
            'model': 'claude-3-sonnet',
            'input_tokens': 200,
            'output_tokens': 100,
            'cost': 0.009
        }
    ],
    execution_duration_ms=2340
)

print(f"Total cost: ${cost.total_cost:.6f}")
print(f"Flowise platform cost: ${cost.base_execution_cost:.6f}")
print(f"Provider costs: {cost.provider_costs}")
```

### Flowise Pricing Tiers

The integration supports multiple Flowise deployment models:

#### Self-Hosted (Default)

```python
calculator = FlowiseCostCalculator(pricing_tier="self_hosted")
```

- **Platform Cost**: $0.00 (no Flowise platform fees)
- **Provider Costs**: Full cost of underlying LLM providers
- **Best For**: Teams running their own Flowise instance

#### Flowise Cloud Tiers

```python
# Free tier
calculator = FlowiseCostCalculator(pricing_tier="cloud_free")

# Starter plan
calculator = FlowiseCostCalculator(pricing_tier="cloud_starter") 

# Professional plan
calculator = FlowiseCostCalculator(pricing_tier="cloud_pro")

# Enterprise plan
calculator = FlowiseCostCalculator(pricing_tier="cloud_enterprise")
```

### Real-Time Cost Tracking

#### With Auto-Instrumentation

When using auto-instrumentation, costs are automatically calculated for every flow execution:

```python
from genops.providers.flowise import auto_instrument

# Enable auto-instrumentation with cost tracking
auto_instrument(
    team="ai-team",
    project="customer-support",
    pricing_tier="cloud_pro"  # Optional: specify your pricing tier
)

# Your existing code - costs are automatically tracked
import requests
response = requests.post(
    "http://localhost:3000/api/v1/prediction/customer-support-v1",
    json={"question": "What are your business hours?"}
)

# Cost data is automatically sent to your observability platform
```

#### With Manual Adapter

```python
from genops.providers.flowise import instrument_flowise

flowise = instrument_flowise(
    team="ai-team",
    project="customer-support"
)

# Every execution includes automatic cost calculation
response = flowise.predict_flow(
    "customer-support-v1",
    "What are your business hours?",
    customer_id="customer-123"  # For per-customer cost attribution
)

# Cost telemetry is automatically exported
```

### Cost Analysis and Reporting

#### Monthly Cost Analysis

```python
from genops.providers.flowise_pricing import FlowiseCostCalculator

calculator = FlowiseCostCalculator(pricing_tier="cloud_pro")

# Simulate a month of execution costs
execution_costs = []
for execution in monthly_executions:  # Your execution data
    cost = calculator.calculate_execution_cost(
        execution['flow_id'],
        execution['flow_name'],
        execution['provider_calls']
    )
    execution_costs.append(cost)

# Analyze monthly costs
analysis = calculator.calculate_monthly_costs(execution_costs)

print(f"Total monthly cost: ${analysis['total_cost']:.2f}")
print(f"Total executions: {analysis['total_executions']}")
print(f"Average cost per execution: ${analysis['average_cost_per_execution']:.4f}")

print("\nCosts by flow:")
for flow, cost in analysis['costs_by_flow'].items():
    print(f"  {flow}: ${cost:.2f}")

print("\nCosts by provider:")
for provider, cost in analysis['costs_by_provider'].items():
    print(f"  {provider}: ${cost:.2f}")
```

#### Cost Optimization Analysis

```python
from genops.providers.flowise_pricing import analyze_cost_optimization_opportunities

# Analyze execution costs for optimization opportunities
optimization = analyze_cost_optimization_opportunities(execution_costs)

print(f"Total potential savings: ${optimization['total_potential_savings']:.2f}")
print(f"Current total cost: ${optimization['total_analyzed_cost']:.2f}")

print("\nOptimization recommendations:")
for rec in optimization['recommendations']:
    print(f"• {rec['suggestion']}")
    print(f"  Potential savings: {rec['potential_savings_percent']}%")
```

#### Monthly Spend Estimation

```python
# Estimate monthly costs based on expected usage
estimate = calculator.estimate_monthly_spend(
    expected_executions_per_month=50000,
    average_tokens_per_execution=800,
    provider_distribution={
        'openai': 0.6,    # 60% of requests use OpenAI
        'anthropic': 0.3, # 30% use Anthropic
        'gemini': 0.1     # 10% use Gemini
    }
)

print(f"Estimated monthly cost: ${estimate['total_estimated_cost']:.2f}")
print(f"Flowise platform cost: ${estimate['flowise_platform_cost']:.2f}")
print(f"Provider costs: ${estimate['total_provider_costs']:.2f}")

print("\nProvider cost breakdown:")
for provider, cost in estimate['provider_cost_breakdown'].items():
    print(f"  {provider}: ${cost:.2f}")
```

### Cost Attribution Patterns

#### Team-Based Attribution

```python
# Different teams using the same Flowise instance
marketing_response = flowise.predict_flow(
    "content-generation-v1",
    "Write a product description for our new feature",
    team="marketing",
    project="product-launch-q3"
)

support_response = flowise.predict_flow(
    "customer-support-v1", 
    "How do I reset my password?",
    team="customer-support",
    project="helpdesk-automation"
)

# Costs are automatically attributed to the respective teams
```

#### Customer-Based Attribution

```python
# Multi-tenant SaaS with per-customer cost tracking
for customer in customers:
    response = flowise.predict_flow(
        "customer-chatbot-v1",
        customer['question'],
        customer_id=customer['id'],
        team="saas-platform",
        project="customer-ai-assistant"
    )
    
# Generate per-customer cost reports from telemetry data
```

#### Feature-Based Attribution

```python
# Track costs by feature for product analytics
multilingual_response = flowise.predict_flow(
    "translation-flow-v1",
    "Translate this to Spanish: Hello, how are you?",
    feature="multilingual-support",
    team="product",
    project="globalization"
)

summarization_response = flowise.predict_flow(
    "document-summary-v1",
    "Summarize this document: ...",
    feature="document-summarization", 
    team="product",
    project="knowledge-management"
)
```

---

## Advanced Patterns

### Multi-Flow Orchestration

#### Sequential Flow Execution

```python
from genops.providers.flowise import instrument_flowise
from genops.core.context import with_governance_context

flowise = instrument_flowise(
    team="ai-orchestration",
    project="complex-workflows"
)

# Execute multiple flows in sequence with shared context
with with_governance_context(
    session_id="complex-workflow-123",
    customer_id="enterprise-customer-456"
) as context:
    
    # Step 1: Document analysis
    analysis = flowise.predict_flow(
        "document-analyzer-v1",
        f"Analyze this document: {document_content}",
        feature="document-analysis"
    )
    
    # Step 2: Extract key information
    extraction = flowise.predict_flow(
        "information-extractor-v1",
        f"Extract key information from: {analysis['text']}",
        feature="information-extraction"
    )
    
    # Step 3: Generate summary
    summary = flowise.predict_flow(
        "summary-generator-v1", 
        f"Generate executive summary: {extraction['text']}",
        feature="summary-generation"
    )
    
    print(f"Workflow session {context.session_id} completed")
    print(f"Total cost: ${context.total_cost:.4f}")
```

#### Parallel Flow Execution

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def execute_parallel_flows(flowise, document_batch):
    """Execute multiple flows in parallel for batch processing."""
    
    def process_document(doc):
        return flowise.predict_flow(
            "document-processor-v1",
            f"Process this document: {doc['content']}",
            customer_id=doc['customer_id'],
            feature="batch-processing"
        )
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Process multiple documents in parallel
        futures = [
            executor.submit(process_document, doc) 
            for doc in document_batch
        ]
        
        results = []
        for future in futures:
            try:
                result = future.result(timeout=30)
                results.append(result)
            except Exception as e:
                print(f"Flow execution failed: {e}")
                results.append(None)
    
    return results

# Usage
document_batch = [
    {"content": "Document 1 content...", "customer_id": "customer-123"},
    {"content": "Document 2 content...", "customer_id": "customer-456"},
    {"content": "Document 3 content...", "customer_id": "customer-789"}
]

results = asyncio.run(execute_parallel_flows(flowise, document_batch))
print(f"Processed {len([r for r in results if r])} documents successfully")
```

### Error Handling and Resilience

#### Retry Logic with Exponential Backoff

```python
import time
import random
from typing import Optional, Dict, Any

def execute_flow_with_retry(
    flowise: GenOpsFlowiseAdapter,
    chatflow_id: str,
    question: str,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    **kwargs
) -> Optional[Dict[str, Any]]:
    """Execute flow with exponential backoff retry logic."""
    
    for attempt in range(max_retries + 1):
        try:
            response = flowise.predict_flow(
                chatflow_id,
                question,
                **kwargs
            )
            return response
            
        except requests.exceptions.ConnectionError as e:
            if attempt == max_retries:
                raise e
            delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
            print(f"Connection failed, retrying in {delay:.2f}s (attempt {attempt + 1})")
            time.sleep(delay)
            
        except requests.exceptions.HTTPError as e:
            if e.response and e.response.status_code == 429:  # Rate limit
                if attempt == max_retries:
                    raise e
                delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
                print(f"Rate limited, retrying in {delay:.2f}s (attempt {attempt + 1})")
                time.sleep(delay)
            else:
                # Don't retry on other HTTP errors
                raise e
                
        except Exception as e:
            # Don't retry on unexpected errors
            raise e
    
    return None

# Usage
try:
    response = execute_flow_with_retry(
        flowise,
        "customer-support-v1",
        "What are your business hours?",
        max_retries=3,
        team="customer-support",
        customer_id="customer-123"
    )
    print(f"Response: {response['text']}")
except Exception as e:
    print(f"Flow execution failed after retries: {e}")
```

#### Circuit Breaker Pattern

```python
from datetime import datetime, timedelta
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open" 
    HALF_OPEN = "half_open"

class FlowiseCircuitBreaker:
    """Circuit breaker for Flowise API calls to prevent cascade failures."""
    
    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 60.0,
        expected_exception: type = Exception
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.expected_exception = expected_exception
        
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection."""
        
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit breaker is OPEN - too many failures")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
            
        except self.expected_exception as e:
            self._on_failure()
            raise e
    
    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset."""
        return (
            self.last_failure_time and
            datetime.now() - self.last_failure_time >= timedelta(seconds=self.recovery_timeout)
        )
    
    def _on_success(self):
        """Handle successful execution."""
        self.failure_count = 0
        self.state = CircuitState.CLOSED
    
    def _on_failure(self):
        """Handle failed execution."""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN

# Usage
circuit_breaker = FlowiseCircuitBreaker(
    failure_threshold=3,
    recovery_timeout=30.0,
    expected_exception=requests.RequestException
)

def protected_flow_execution(chatflow_id: str, question: str, **kwargs):
    """Execute flow with circuit breaker protection."""
    return circuit_breaker.call(
        flowise.predict_flow,
        chatflow_id,
        question,
        **kwargs
    )

# Execute with protection
try:
    response = protected_flow_execution(
        "customer-support-v1",
        "What are your business hours?",
        team="customer-support"
    )
    print(f"Response: {response['text']}")
except Exception as e:
    print(f"Circuit breaker prevented execution: {e}")
```

### Advanced Governance Patterns

#### Multi-Tenant Cost Isolation

```python
class MultiTenantFlowiseManager:
    """Manage Flowise access for multiple tenants with cost isolation."""
    
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key
        self.tenant_adapters = {}
    
    def get_tenant_adapter(self, tenant_id: str, **tenant_config) -> GenOpsFlowiseAdapter:
        """Get or create adapter for a specific tenant."""
        
        if tenant_id not in self.tenant_adapters:
            self.tenant_adapters[tenant_id] = GenOpsFlowiseAdapter(
                base_url=self.base_url,
                api_key=self.api_key,
                customer_id=tenant_id,
                team=tenant_config.get('team', f'tenant-{tenant_id}'),
                project=tenant_config.get('project', 'multi-tenant-app'),
                **tenant_config
            )
        
        return self.tenant_adapters[tenant_id]
    
    def execute_for_tenant(
        self,
        tenant_id: str,
        chatflow_id: str,
        question: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Execute flow for a specific tenant with automatic cost attribution."""
        
        adapter = self.get_tenant_adapter(tenant_id)
        return adapter.predict_flow(
            chatflow_id,
            question,
            customer_id=tenant_id,  # Ensure tenant attribution
            **kwargs
        )
    
    def get_tenant_cost_summary(self, tenant_id: str, time_period_hours: int = 24) -> Dict:
        """Get cost summary for a specific tenant."""
        # This would integrate with your telemetry backend to fetch cost data
        # Implementation depends on your observability platform
        pass

# Usage
tenant_manager = MultiTenantFlowiseManager(
    base_url="http://localhost:3000",
    api_key="your-api-key"
)

# Execute flows for different tenants
tenant_a_response = tenant_manager.execute_for_tenant(
    "tenant-a",
    "customer-support-v1", 
    "What are your business hours?",
    team="tenant-a-support"
)

tenant_b_response = tenant_manager.execute_for_tenant(
    "tenant-b",
    "customer-support-v1",
    "How do I cancel my subscription?", 
    team="tenant-b-support"
)

# Costs are automatically isolated by tenant_id
```

#### Budget Enforcement

```python
from decimal import Decimal
from datetime import datetime, timedelta

class FlowiseBudgetEnforcer:
    """Enforce budget limits for Flowise executions."""
    
    def __init__(
        self,
        daily_budget: Decimal,
        monthly_budget: Decimal,
        cost_calculator: FlowiseCostCalculator
    ):
        self.daily_budget = daily_budget
        self.monthly_budget = monthly_budget
        self.cost_calculator = cost_calculator
        
        # Track spending (in production, this would be persisted)
        self.daily_spend = Decimal('0.0')
        self.monthly_spend = Decimal('0.0')
        self.last_reset_date = datetime.now().date()
    
    def check_budget_before_execution(
        self,
        estimated_cost: Decimal,
        team: str,
        project: str
    ) -> Dict[str, Any]:
        """Check if execution would exceed budget limits."""
        
        self._reset_counters_if_needed()
        
        projected_daily = self.daily_spend + estimated_cost
        projected_monthly = self.monthly_spend + estimated_cost
        
        if projected_daily > self.daily_budget:
            return {
                'allowed': False,
                'reason': 'daily_budget_exceeded',
                'current_daily_spend': float(self.daily_spend),
                'daily_budget': float(self.daily_budget),
                'estimated_cost': float(estimated_cost)
            }
        
        if projected_monthly > self.monthly_budget:
            return {
                'allowed': False,
                'reason': 'monthly_budget_exceeded', 
                'current_monthly_spend': float(self.monthly_spend),
                'monthly_budget': float(self.monthly_budget),
                'estimated_cost': float(estimated_cost)
            }
        
        return {
            'allowed': True,
            'remaining_daily_budget': float(self.daily_budget - projected_daily),
            'remaining_monthly_budget': float(self.monthly_budget - projected_monthly)
        }
    
    def record_execution_cost(self, actual_cost: Decimal):
        """Record actual cost after execution."""
        self.daily_spend += actual_cost
        self.monthly_spend += actual_cost
    
    def _reset_counters_if_needed(self):
        """Reset daily counter if it's a new day."""
        today = datetime.now().date()
        if today != self.last_reset_date:
            self.daily_spend = Decimal('0.0')
            self.last_reset_date = today
            
            # Reset monthly counter if it's a new month
            if today.day == 1:
                self.monthly_spend = Decimal('0.0')

class BudgetEnforcedFlowiseAdapter(GenOpsFlowiseAdapter):
    """Flowise adapter with budget enforcement."""
    
    def __init__(
        self,
        daily_budget: float,
        monthly_budget: float,
        pricing_tier: str = "self_hosted",
        **kwargs
    ):
        super().__init__(**kwargs)
        
        cost_calculator = FlowiseCostCalculator(pricing_tier=pricing_tier)
        self.budget_enforcer = FlowiseBudgetEnforcer(
            daily_budget=Decimal(str(daily_budget)),
            monthly_budget=Decimal(str(monthly_budget)),
            cost_calculator=cost_calculator
        )
    
    def predict_flow(self, chatflow_id: str, question: str, **kwargs) -> Any:
        """Execute flow with budget enforcement."""
        
        # Estimate cost before execution
        estimated_tokens = len(question.split()) * 1.3 * 2  # Rough estimate for input + output
        estimated_cost = Decimal('0.001') + (Decimal(str(estimated_tokens)) * Decimal('0.000002'))
        
        # Check budget
        budget_check = self.budget_enforcer.check_budget_before_execution(
            estimated_cost,
            kwargs.get('team', 'unknown'),
            kwargs.get('project', 'unknown')
        )
        
        if not budget_check['allowed']:
            raise Exception(
                f"Budget limit exceeded: {budget_check['reason']}. "
                f"Estimated cost: ${budget_check['estimated_cost']:.4f}"
            )
        
        # Execute flow
        response = super().predict_flow(chatflow_id, question, **kwargs)
        
        # Record actual cost (this would be calculated from the response)
        # For now, use the estimated cost
        self.budget_enforcer.record_execution_cost(estimated_cost)
        
        return response

# Usage
budget_flowise = BudgetEnforcedFlowiseAdapter(
    base_url="http://localhost:3000",
    daily_budget=50.0,   # $50 per day
    monthly_budget=1000.0,  # $1000 per month
    pricing_tier="cloud_pro",
    team="ai-team",
    project="customer-support"
)

try:
    response = budget_flowise.predict_flow(
        "customer-support-v1",
        "What are your business hours?"
    )
    print(f"Response: {response['text']}")
except Exception as e:
    print(f"Budget enforcement blocked execution: {e}")
```

---

## Production Deployment

### Container Deployment

#### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV FLOWISE_BASE_URL="http://flowise:3000"
ENV GENOPS_TEAM="production"
ENV GENOPS_ENVIRONMENT="production"

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "from genops.providers.flowise_validation import validate_flowise_setup; \
                 result = validate_flowise_setup(); \
                 exit(0 if result.is_valid else 1)"

EXPOSE 8000

CMD ["python", "app.py"]
```

#### Docker Compose

```yaml
version: '3.8'

services:
  flowise:
    image: flowiseai/flowise:latest
    restart: unless-stopped
    environment:
      - PORT=3000
      - FLOWISE_USERNAME=admin
      - FLOWISE_PASSWORD=1234
    ports:
      - "3000:3000"
    volumes:
      - flowise_data:/root/.flowise
    networks:
      - flowise-network

  app:
    build: .
    restart: unless-stopped
    environment:
      # Flowise configuration
      - FLOWISE_BASE_URL=http://flowise:3000
      - FLOWISE_API_KEY=${FLOWISE_API_KEY}
      
      # Governance configuration
      - GENOPS_TEAM=production-team
      - GENOPS_PROJECT=customer-support
      - GENOPS_ENVIRONMENT=production
      
      # OpenTelemetry export
      - OTEL_EXPORTER_OTLP_ENDPOINT=${OTEL_ENDPOINT}
      - OTEL_EXPORTER_OTLP_HEADERS=authorization=Bearer ${OTEL_TOKEN}
      
    depends_on:
      - flowise
    networks:
      - flowise-network
    ports:
      - "8000:8000"

volumes:
  flowise_data:

networks:
  flowise-network:
    driver: bridge
```

### Kubernetes Deployment

#### ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: flowise-genops-config
data:
  FLOWISE_BASE_URL: "http://flowise-service:3000"
  GENOPS_TEAM: "production-team"
  GENOPS_PROJECT: "customer-support"
  GENOPS_ENVIRONMENT: "production"
  OTEL_EXPORTER_OTLP_ENDPOINT: "http://tempo:4317"
```

#### Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: flowise-genops-secrets
type: Opaque
stringData:
  FLOWISE_API_KEY: "fl-your-api-key-here"
  OTEL_EXPORTER_OTLP_HEADERS: "authorization=Bearer your-otel-token"
```

#### Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flowise-genops-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: flowise-genops-app
  template:
    metadata:
      labels:
        app: flowise-genops-app
    spec:
      containers:
      - name: app
        image: your-registry/flowise-genops-app:latest
        ports:
        - containerPort: 8000
        envFrom:
        - configMapRef:
            name: flowise-genops-config
        - secretRef:
            name: flowise-genops-secrets
        
        # Resource limits
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi" 
            cpu: "500m"
        
        # Health checks
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 30
        
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
        
        # Graceful shutdown
        lifecycle:
          preStop:
            exec:
              command: ["/bin/sh", "-c", "sleep 15"]
        
      # Enable horizontal pod autoscaling
      terminationGracePeriodSeconds: 30
```

#### Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: flowise-genops-service
spec:
  selector:
    app: flowise-genops-app
  ports:
  - name: http
    port: 80
    targetPort: 8000
  type: ClusterIP
```

#### HorizontalPodAutoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: flowise-genops-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: flowise-genops-app
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

### Environment-Specific Configurations

#### Development Environment

```python
# dev_config.py
from genops.providers.flowise import auto_instrument

# Development setup with console output
auto_instrument(
    base_url="http://localhost:3000",
    team="development",
    project="flowise-integration",
    environment="development",
    enable_console_export=True,  # See telemetry in console
    pricing_tier="self_hosted"   # Local development
)
```

#### Staging Environment

```python
# staging_config.py  
from genops.providers.flowise import auto_instrument

# Staging setup with observability export
auto_instrument(
    base_url=os.getenv("FLOWISE_BASE_URL"),
    api_key=os.getenv("FLOWISE_API_KEY"),
    team="staging",
    project="flowise-integration",
    environment="staging",
    pricing_tier="cloud_starter"
)
```

#### Production Environment

```python
# prod_config.py
from genops.providers.flowise import auto_instrument

# Production setup with full governance
auto_instrument(
    base_url=os.getenv("FLOWISE_BASE_URL"),
    api_key=os.getenv("FLOWISE_API_KEY"),
    team=os.getenv("GENOPS_TEAM"),
    project=os.getenv("GENOPS_PROJECT"),
    environment="production",
    cost_center=os.getenv("GENOPS_COST_CENTER"),
    pricing_tier=os.getenv("FLOWISE_PRICING_TIER", "cloud_pro")
)
```

### Monitoring and Alerting

#### Custom Health Check Endpoint

```python
from flask import Flask, jsonify
from genops.providers.flowise_validation import validate_flowise_setup

app = Flask(__name__)

@app.route('/health')
def health_check():
    """Health check endpoint for load balancers."""
    try:
        result = validate_flowise_setup(timeout=5)
        if result.is_valid:
            return jsonify({
                'status': 'healthy',
                'flowise_url': result.flowise_url,
                'chatflows_available': len(result.available_chatflows or [])
            }), 200
        else:
            return jsonify({
                'status': 'unhealthy',
                'errors': [issue.message for issue in result.issues if issue.severity == 'error']
            }), 503
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 503

@app.route('/ready')
def readiness_check():
    """Readiness check endpoint for Kubernetes."""
    try:
        # Quick validation
        result = validate_flowise_setup(timeout=2)
        if result.is_valid:
            return jsonify({'status': 'ready'}), 200
        else:
            return jsonify({'status': 'not ready'}), 503
    except Exception:
        return jsonify({'status': 'not ready'}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

#### Prometheus Metrics

```python
from prometheus_client import Counter, Histogram, Gauge, generate_latest
import time

# Define metrics
flowise_requests_total = Counter(
    'flowise_requests_total',
    'Total number of Flowise requests',
    ['chatflow_id', 'status', 'team', 'project']
)

flowise_request_duration_seconds = Histogram(
    'flowise_request_duration_seconds',
    'Time spent on Flowise requests',
    ['chatflow_id', 'team', 'project']
)

flowise_cost_usd_total = Counter(
    'flowise_cost_usd_total',
    'Total cost of Flowise requests in USD',
    ['chatflow_id', 'provider', 'team', 'project']
)

flowise_active_sessions = Gauge(
    'flowise_active_sessions',
    'Number of active Flowise sessions'
)

class MetricsFlowiseAdapter(GenOpsFlowiseAdapter):
    """Flowise adapter with Prometheus metrics."""
    
    def predict_flow(self, chatflow_id: str, question: str, **kwargs) -> Any:
        team = kwargs.get('team', self.governance_attrs.get('team', 'unknown'))
        project = kwargs.get('project', self.governance_attrs.get('project', 'unknown'))
        
        # Track request
        start_time = time.time()
        
        try:
            response = super().predict_flow(chatflow_id, question, **kwargs)
            
            # Record successful request
            flowise_requests_total.labels(
                chatflow_id=chatflow_id,
                status='success',
                team=team,
                project=project
            ).inc()
            
            return response
            
        except Exception as e:
            # Record failed request
            flowise_requests_total.labels(
                chatflow_id=chatflow_id,
                status='error',
                team=team, 
                project=project
            ).inc()
            raise
            
        finally:
            # Record duration
            duration = time.time() - start_time
            flowise_request_duration_seconds.labels(
                chatflow_id=chatflow_id,
                team=team,
                project=project
            ).observe(duration)

@app.route('/metrics')
def metrics():
    """Prometheus metrics endpoint."""
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}
```

### Performance Optimization

#### Connection Pooling

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class OptimizedFlowiseAdapter(GenOpsFlowiseAdapter):
    """Flowise adapter with connection pooling and retry logic."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Configure connection pooling
        self.session = requests.Session()
        
        # Retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        # HTTP adapter with connection pooling
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=20,  # Number of connection pools
            pool_maxsize=20,      # Max connections per pool
            pool_block=False      # Don't block when pool is full
        )
        
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Set timeouts
        self.session.timeout = (5.0, 30.0)  # (connect, read)
        
        # Configure headers
        if self.api_key:
            self.session.headers.update({
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "User-Agent": "GenOps-Flowise-Integration/1.0"
            })
```

#### Async Support

```python
import asyncio
import aiohttp
from typing import Optional, Dict, Any

class AsyncFlowiseAdapter:
    """Async Flowise adapter for high-performance applications."""
    
    def __init__(
        self,
        base_url: str = "http://localhost:3000",
        api_key: Optional[str] = None,
        max_connections: int = 100,
        **governance_attrs
    ):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.governance_attrs = governance_attrs
        self.max_connections = max_connections
        self._session = None
    
    async def __aenter__(self):
        """Async context manager entry."""
        connector = aiohttp.TCPConnector(limit=self.max_connections)
        timeout = aiohttp.ClientTimeout(total=30)
        
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        self._session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            headers=headers
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self._session:
            await self._session.close()
    
    async def predict_flow(
        self,
        chatflow_id: str,
        question: str,
        **kwargs
    ) -> Dict[str, Any]:
        """Async flow execution."""
        
        if not self._session:
            raise RuntimeError("Use async context manager: async with AsyncFlowiseAdapter() as adapter")
        
        url = f"{self.base_url}/api/v1/prediction/{chatflow_id}"
        data = {"question": question}
        
        # Add optional parameters
        if "sessionId" in kwargs:
            data["sessionId"] = kwargs["sessionId"]
        if "overrideConfig" in kwargs:
            data["overrideConfig"] = kwargs["overrideConfig"]
        
        async with self._session.post(url, json=data) as response:
            response.raise_for_status()
            return await response.json()

# Usage
async def process_multiple_flows():
    """Process multiple flows concurrently."""
    
    questions = [
        "What are your business hours?",
        "How do I reset my password?", 
        "What's your return policy?",
        "Do you offer customer support?",
        "How can I track my order?"
    ]
    
    async with AsyncFlowiseAdapter(
        base_url="http://localhost:3000",
        team="customer-support",
        project="async-processing"
    ) as adapter:
        
        # Execute all flows concurrently
        tasks = [
            adapter.predict_flow("customer-support-v1", question)
            for question in questions
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"Question {i+1} failed: {result}")
            else:
                print(f"Question {i+1}: {result.get('text', 'No response')}")

# Run async processing
asyncio.run(process_multiple_flows())
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Connection Issues

**Issue**: `Cannot connect to Flowise at http://localhost:3000`

**Solutions**:
```python
# Check if Flowise is running
from genops.providers.flowise_validation import validate_flowise_setup

result = validate_flowise_setup()
if not result.is_valid:
    for issue in result.issues:
        print(f"{issue.severity}: {issue.message}")
        print(f"Fix: {issue.fix_suggestion}")
```

**Common causes**:
- Flowise not running: `docker run -d --name flowise -p 3000:3000 flowiseai/flowise`
- Wrong URL: Check `FLOWISE_BASE_URL` environment variable
- Network issues: Test with `curl http://localhost:3000/api/v1/chatflows`

#### 2. Authentication Issues

**Issue**: `Authentication failed with Flowise API`

**Solutions**:
```python
# Test API key
import requests

response = requests.get(
    "http://localhost:3000/api/v1/chatflows",
    headers={"Authorization": "Bearer YOUR_API_KEY"}
)
print(f"Status: {response.status_code}")
if response.status_code != 200:
    print(f"Error: {response.text}")
```

**Common causes**:
- Invalid API key: Generate new key in Flowise UI
- Missing API key for production: Set `FLOWISE_API_KEY` environment variable  
- Local development: API key may not be required for localhost

#### 3. Chatflow Not Found

**Issue**: `Flowise resource not found: /api/v1/prediction/chatflow-id`

**Solutions**:
```python
# List available chatflows
flowise = instrument_flowise()
chatflows = flowise.get_chatflows()
for flow in chatflows:
    print(f"ID: {flow.get('id')} - Name: {flow.get('name')}")
```

**Common causes**:
- Wrong chatflow ID: Copy ID from Flowise UI
- Chatflow deleted: Recreate or use different flow
- Case sensitivity: IDs are case-sensitive

#### 4. Auto-Instrumentation Not Working

**Issue**: Auto-instrumentation enabled but no telemetry data

**Debugging**:
```python
from genops.providers.flowise import auto_instrument

# Enable with console output for debugging
success = auto_instrument(
    team="debug-team",
    project="debug-project",
    enable_console_export=True
)

print(f"Auto-instrumentation successful: {success}")

# Make a test request
import requests
response = requests.post(
    "http://localhost:3000/api/v1/prediction/your-chatflow-id",
    json={"question": "Test"}
)

# You should see telemetry output in console
```

**Common causes**:
- Wrong URL pattern: Auto-instrumentation only tracks requests to Flowise API endpoints
- Import order: Enable auto-instrumentation before importing requests
- Multiple sessions: Some HTTP clients create new sessions

#### 5. Cost Calculation Issues

**Issue**: Costs showing as $0.00 or incorrect values

**Debugging**:
```python
from genops.providers.flowise_pricing import calculate_flow_execution_cost

# Test cost calculation
cost = calculate_flow_execution_cost(
    "test-flow",
    "Test Flow",
    [
        {
            'provider': 'openai',
            'model': 'gpt-4', 
            'input_tokens': 100,
            'output_tokens': 50
        }
    ],
    pricing_tier="self_hosted"
)

print(f"Total cost: ${cost.total_cost:.6f}")
print(f"Provider costs: {cost.provider_costs}")
print(f"Base cost: ${cost.base_execution_cost:.6f}")
```

**Common causes**:
- Missing provider call data: Ensure underlying LLM calls are tracked
- Wrong pricing tier: Verify your Flowise deployment model
- Token counting: Verify token estimation is working

### Debugging Tools

#### Validation Script

```python
#!/usr/bin/env python3
"""Comprehensive Flowise integration debugging script."""

import os
import sys
from genops.providers.flowise_validation import validate_flowise_setup, print_validation_result
from genops.providers.flowise import auto_instrument

def debug_flowise_integration():
    """Run comprehensive debugging checks."""
    
    print("🔍 GenOps Flowise Integration Debug")
    print("=" * 50)
    
    # 1. Environment check
    print("\n1. Environment Variables:")
    env_vars = [
        'FLOWISE_BASE_URL', 'FLOWISE_API_KEY',
        'GENOPS_TEAM', 'GENOPS_PROJECT', 'GENOPS_ENVIRONMENT'
    ]
    
    for var in env_vars:
        value = os.getenv(var)
        if value:
            # Mask API key for security
            if 'KEY' in var and len(value) > 10:
                masked = value[:4] + '*' * (len(value) - 8) + value[-4:]
                print(f"  ✅ {var}: {masked}")
            else:
                print(f"  ✅ {var}: {value}")
        else:
            print(f"  ❌ {var}: Not set")
    
    # 2. Validation
    print("\n2. Flowise Setup Validation:")
    result = validate_flowise_setup()
    print_validation_result(result)
    
    if not result.is_valid:
        print("\n❌ Cannot proceed - fix validation issues first")
        return False
    
    # 3. Auto-instrumentation test
    print("\n3. Auto-Instrumentation Test:")
    try:
        success = auto_instrument(
            team="debug-team",
            project="debug-test",
            enable_console_export=True
        )
        
        if success:
            print("  ✅ Auto-instrumentation enabled successfully")
        else:
            print("  ❌ Auto-instrumentation failed")
            return False
            
    except Exception as e:
        print(f"  ❌ Auto-instrumentation error: {e}")
        return False
    
    # 4. Test request
    print("\n4. Test Request:")
    if result.available_chatflows:
        print("  Available chatflows for testing:")
        for i, flow in enumerate(result.available_chatflows[:3]):
            print(f"    {i+1}. {flow}")
        
        print("\n  To test with a specific chatflow:")
        print("  from genops.providers.flowise_validation import quick_test_flow")
        print("  result = quick_test_flow('your-chatflow-id')")
    else:
        print("  ❌ No chatflows available for testing")
    
    # 5. Cost calculation test
    print("\n5. Cost Calculation Test:")
    try:
        from genops.providers.flowise_pricing import calculate_flow_execution_cost
        
        cost = calculate_flow_execution_cost(
            "test-flow",
            "Test Flow",
            [{'provider': 'openai', 'model': 'gpt-4', 'input_tokens': 100, 'output_tokens': 50}]
        )
        
        print(f"  ✅ Cost calculation working: ${cost.total_cost:.6f}")
        
    except Exception as e:
        print(f"  ❌ Cost calculation error: {e}")
    
    print("\n✅ Debug complete!")
    return True

if __name__ == "__main__":
    debug_flowise_integration()
```

#### Integration Test Suite

```python
"""Integration test suite for Flowise integration."""

import unittest
import os
from genops.providers.flowise import instrument_flowise, auto_instrument
from genops.providers.flowise_validation import validate_flowise_setup
from genops.providers.flowise_pricing import FlowiseCostCalculator

class TestFlowiseIntegration(unittest.TestCase):
    """Integration tests for Flowise."""
    
    def setUp(self):
        """Set up test environment."""
        self.base_url = os.getenv('FLOWISE_BASE_URL', 'http://localhost:3000')
        self.api_key = os.getenv('FLOWISE_API_KEY')
        
    def test_validation(self):
        """Test setup validation."""
        result = validate_flowise_setup(self.base_url, self.api_key)
        self.assertTrue(result.is_valid, f"Validation failed: {result.issues}")
    
    def test_adapter_creation(self):
        """Test adapter creation."""
        adapter = instrument_flowise(
            base_url=self.base_url,
            api_key=self.api_key,
            team="test-team",
            project="test-project"
        )
        self.assertIsNotNone(adapter)
        
    def test_chatflows_list(self):
        """Test chatflows listing."""
        adapter = instrument_flowise(base_url=self.base_url, api_key=self.api_key)
        chatflows = adapter.get_chatflows()
        self.assertIsInstance(chatflows, list)
        
    def test_auto_instrumentation(self):
        """Test auto-instrumentation setup."""
        success = auto_instrument(
            base_url=self.base_url,
            api_key=self.api_key,
            team="test-team"
        )
        self.assertTrue(success)
    
    def test_cost_calculation(self):
        """Test cost calculation."""
        calculator = FlowiseCostCalculator()
        cost = calculator.calculate_execution_cost(
            "test-flow",
            "Test Flow",
            [{'provider': 'openai', 'model': 'gpt-4', 'input_tokens': 100, 'output_tokens': 50}]
        )
        self.assertGreater(cost.total_cost, 0)

if __name__ == '__main__':
    unittest.main()
```

### Performance Monitoring

#### Response Time Tracking

```python
import time
import statistics
from collections import defaultdict

class PerformanceTracker:
    """Track performance metrics for Flowise operations."""
    
    def __init__(self):
        self.metrics = defaultdict(list)
    
    def track_execution(self, operation: str, duration: float, success: bool):
        """Track execution metrics."""
        self.metrics[f"{operation}_duration"].append(duration)
        self.metrics[f"{operation}_success"].append(1 if success else 0)
    
    def get_summary(self) -> dict:
        """Get performance summary."""
        summary = {}
        
        for metric, values in self.metrics.items():
            if 'duration' in metric:
                summary[metric] = {
                    'count': len(values),
                    'avg': statistics.mean(values),
                    'min': min(values),
                    'max': max(values),
                    'p95': statistics.quantiles(values, n=20)[18] if len(values) >= 20 else max(values)
                }
            elif 'success' in metric:
                summary[metric] = {
                    'total': len(values),
                    'successful': sum(values),
                    'success_rate': sum(values) / len(values) if values else 0
                }
        
        return summary

# Usage
tracker = PerformanceTracker()

def tracked_flow_execution(adapter, chatflow_id: str, question: str, **kwargs):
    """Execute flow with performance tracking."""
    start_time = time.time()
    
    try:
        result = adapter.predict_flow(chatflow_id, question, **kwargs)
        duration = time.time() - start_time
        tracker.track_execution('predict_flow', duration, True)
        return result
        
    except Exception as e:
        duration = time.time() - start_time
        tracker.track_execution('predict_flow', duration, False)
        raise

# After running tests
summary = tracker.get_summary()
for metric, stats in summary.items():
    print(f"{metric}: {stats}")
```

---

## Examples

The GenOps Flowise integration includes comprehensive examples demonstrating real-world usage patterns:

### Example Overview

| Example | Complexity | Description |
|---------|------------|-------------|
| [01_basic_flow_execution.py](../../examples/flowise/01_basic_flow_execution.py) | ⭐ Basic | Simple chatflow execution with governance |
| [02_session_management.py](../../examples/flowise/02_session_management.py) | ⭐ Basic | Multi-turn conversation handling |
| [03_cost_tracking.py](../../examples/flowise/03_cost_tracking.py) | ⭐⭐ Intermediate | Cost calculation and tracking |
| [04_multi_provider_aggregation.py](../../examples/flowise/04_multi_provider_aggregation.py) | ⭐⭐ Intermediate | Multi-provider cost aggregation |
| [05_multi_tenant_saas.py](../../examples/flowise/05_multi_tenant_saas.py) | ⭐⭐ Intermediate | Multi-tenant SaaS patterns |
| [06_enterprise_governance.py](../../examples/flowise/06_enterprise_governance.py) | ⭐⭐⭐ Advanced | Enterprise governance with policy enforcement |
| [07_production_monitoring.py](../../examples/flowise/07_production_monitoring.py) | ⭐⭐⭐ Advanced | Production monitoring and alerting |
| [08_async_high_performance.py](../../examples/flowise/08_async_high_performance.py) | ⭐⭐⭐ Advanced | Async high-performance processing |

### Quick Start Examples

**Basic Flow Execution:**
```python
# From examples/flowise/01_basic_flow_execution.py
from genops.providers.flowise import instrument_flowise

# Create governed adapter
flowise = instrument_flowise(
    team="your-team",
    project="your-project"
)

# Execute flow with governance
response = flowise.predict_flow(
    chatflow_id="your-chatflow-id",
    question="What are your business hours?"
)
print(f"Response: {response['text']}")
```

**Session Management:**
```python
# From examples/flowise/02_session_management.py
session_id = "user-123"

# Multi-turn conversation
questions = [
    "Hello, I need help with my account",
    "I forgot my password", 
    "How do I reset it?"
]

for question in questions:
    response = flowise.predict_flow(
        chatflow_id="support-flow",
        question=question,
        sessionId=session_id  # Maintains conversation context
    )
    print(f"Q: {question}")
    print(f"A: {response['text']}\n")
```

**Cost Tracking:**
```python  
# From examples/flowise/03_cost_tracking.py
from genops.providers.flowise_pricing import FlowiseCostCalculator

calculator = FlowiseCostCalculator()

# Calculate execution cost
cost = calculator.calculate_execution_cost(
    chatflow_id="customer-support",
    chatflow_name="Customer Support Bot", 
    underlying_provider_calls=[
        {
            'provider': 'openai',
            'model': 'gpt-4',
            'input_tokens': 100,
            'output_tokens': 50
        }
    ]
)

print(f"Total cost: ${cost.total_cost:.6f}")
print(f"Per-provider breakdown: {cost.provider_costs}")
```

### Production Examples

**Enterprise Governance:**
```python
# From examples/flowise/06_enterprise_governance.py  
from genops.providers.flowise import instrument_flowise

# Enterprise configuration
flowise = instrument_flowise(
    base_url="https://flowise.company.com",
    api_key="prod-api-key",
    team="customer-success",
    project="support-chatbot",
    customer_id="enterprise-client-001", 
    environment="production",
    cost_center="support-operations"
)

# Governance tracking includes:
# - Cost attribution per customer
# - Budget monitoring and alerts  
# - Compliance policy enforcement
# - Performance SLA monitoring
```

**High-Performance Async:**
```python
# From examples/flowise/08_async_high_performance.py
import asyncio
from genops.providers.flowise import AsyncFlowiseClient

async def process_requests():
    async with AsyncFlowiseClient(base_url="http://localhost:3000") as client:
        
        # Process multiple requests concurrently
        tasks = []
        for i in range(100):
            task = client.predict_flow(
                chatflow_id="high-volume-flow",
                question=f"Process request {i}"
            )
            tasks.append(task)
        
        # Execute all requests concurrently
        results = await asyncio.gather(*tasks)
        return results

# Run async processing
results = asyncio.run(process_requests())
```

### Running the Examples

1. **Install dependencies:**
   ```bash
   pip install genops requests aiohttp flask prometheus_client
   ```

2. **Set environment variables:**
   ```bash
   export FLOWISE_BASE_URL="http://localhost:3000"
   export FLOWISE_API_KEY="your-api-key"  # Optional for local
   export GENOPS_TEAM="your-team"
   export GENOPS_PROJECT="your-project"
   ```

3. **Run specific examples:**
   ```bash
   # Basic examples
   python examples/flowise/01_basic_flow_execution.py
   python examples/flowise/02_session_management.py
   
   # Advanced examples  
   python examples/flowise/06_enterprise_governance.py
   python examples/flowise/08_async_high_performance.py --benchmark
   ```

All examples include detailed comments, error handling, and real-world patterns you can adapt for your specific use case.

---

## Next Steps

### Recommended Learning Path

1. **Start with the [5-minute quickstart](../flowise-quickstart.md)** to get basic integration working
2. **Explore [working examples](../../examples/flowise/)** to see real-world patterns  
3. **Review this comprehensive guide** for advanced features and production deployment
4. **Set up observability dashboards** using your preferred platform (Datadog, Grafana, etc.)
5. **Implement cost tracking and governance** for your specific use cases

### Additional Resources

- **🔍 Validation Tools**: Use `validate_flowise_setup()` regularly to ensure proper configuration
- **📊 Cost Analysis**: Implement `FlowiseCostCalculator` for budget tracking and optimization  
- **🚀 Auto-Instrumentation**: Start with zero-code setup, migrate to manual control as needed
- **📈 Observability**: Export telemetry to your existing monitoring stack
- **🏗️ Production**: Follow the deployment patterns for container and Kubernetes environments

### Contributing

Found issues or want to contribute improvements? See our [Contributing Guide](../../CONTRIBUTING.md) for:
- Bug reporting process
- Feature request guidelines  
- Development setup
- Testing requirements
- Code review process

---

**You now have comprehensive Flowise governance tracking with GenOps!** 🎉

This integration provides enterprise-grade cost tracking, team attribution, and observability for your Flowise AI workflows while maintaining the simplicity and flexibility that makes Flowise powerful.