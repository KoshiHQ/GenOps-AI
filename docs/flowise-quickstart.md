# Flowise Integration - 5-Minute Quickstart

**⚡ Get Flowise governance tracking working in under 5 minutes with zero code changes to your existing application.**

## Why This Matters

**Without GenOps governance:**
- ❌ No visibility into AI costs per team/project  
- ❌ Cannot track which customers are driving costs
- ❌ No budget controls or cost optimization insights
- ❌ Difficult to debug performance issues
- ❌ Manual reporting and scattered cost data

**With GenOps governance:**
- ✅ Automatic cost attribution and tracking
- ✅ Per-customer billing and analytics  
- ✅ Budget alerts and optimization insights
- ✅ Complete observability and performance monitoring
- ✅ Unified dashboard across all AI tools

## What This Gives You

- **Automatic cost tracking** for all Flowise chatflow executions  
- **Team attribution** and project-level cost breakdowns
- **Usage monitoring** with token counting and performance metrics
- **Zero-code setup** - your existing Flowise code works unchanged
- **OpenTelemetry export** compatible with Datadog, Grafana, Honeycomb, etc.

## Prerequisites & Timeline

**⚡ True 5-Minute Setup (if you already have):**
- Python 3.9+ with `pip install genops requests`
- Flowise instance running with at least one chatflow created
- Your chatflow ID ready (see "Finding Your Chatflow ID" below)

**🕐 First-Time Setup Timeline:**
- **5 minutes**: If you have Flowise + chatflows already
- **15 minutes**: If you need to set up Flowise and create your first chatflow
- **2 minutes**: If you just need to install GenOps

## Quick Validation (Do This First!)

Before starting the setup, let's make sure everything is ready:

```python
from genops.providers.flowise_validation import validate_flowise_setup, print_validation_result

# Quick validation check
result = validate_flowise_setup()
print_validation_result(result)

if result.is_valid:
    print("✅ Ready for 5-minute setup!")
else:
    print("❌ Fix issues above first, then continue")
```

## Finding Your Chatflow ID

You'll need your chatflow ID for the examples below. Here's how to find it:

### Method 1: From Flowise UI
1. Open your Flowise UI (usually `http://localhost:3000`)
2. Navigate to "Chatflows" 
3. Click on your desired chatflow
4. Copy the ID from the URL: `/chatflow/YOUR-CHATFLOW-ID-HERE`

### Method 2: Using Code
```python
from genops.providers.flowise import instrument_flowise

flowise = instrument_flowise()
chatflows = flowise.get_chatflows()

print("Available chatflows:")
for flow in chatflows:
    print(f"  Name: {flow['name']}")
    print(f"  ID: {flow['id']}")
    print()
```

💡 **Tip**: Copy one of these chatflow IDs - you'll need it in the next steps!

## Step 1: Enable Auto-Instrumentation (1 line of code)

Add this **single line** at the start of your application:

```python
from genops.providers.flowise import auto_instrument

# Enable governance tracking (zero-code setup)
auto_instrument(team="your-team", project="your-project")
```

### What Does Auto-Instrumentation Actually Do?

When you call `auto_instrument()`, GenOps automatically:

1. **🔍 Intercepts HTTP requests** to your Flowise instance  
2. **📊 Adds governance metadata** (team, project, costs, performance)
3. **💰 Calculates costs** based on token usage and underlying LLM provider pricing
4. **📤 Exports telemetry** to your observability platform (Datadog, Grafana, etc.)
5. **✨ Preserves your existing code** - zero changes needed to your current Flowise calls

**That's it!** All your existing Flowise API calls will now be automatically tracked.

## Step 2: Your Existing Code Works Unchanged

Your current Flowise code continues to work exactly as before:

```python
import requests

# Your existing Flowise code - no changes needed!
response = requests.post(
    "http://localhost:3000/api/v1/prediction/PASTE-YOUR-CHATFLOW-ID-HERE",
    json={
        "question": "What are the business hours?",
        "sessionId": "user-123"  # Optional: for conversation context
    }
)

result = response.json()
print(f"Answer: {result.get('text', 'No response')}")
```

## Complete Working Example (Copy & Paste Ready!)

Here's a complete example you can run right now:

```python
from genops.providers.flowise import auto_instrument
import requests

# Step 1: Enable tracking (one line!)
auto_instrument(team="your-team", project="your-project")

# Step 2: Your existing Flowise code works unchanged
# 🚨 Replace 'YOUR-CHATFLOW-ID' with your actual chatflow ID from above
response = requests.post(
    "http://localhost:3000/api/v1/prediction/YOUR-CHATFLOW-ID",
    json={
        "question": "Hello! What can you help me with today?",
        "sessionId": "demo-session-123"
    }
)

if response.status_code == 200:
    result = response.json()
    print(f"✅ Response: {result.get('text', 'No response text found')}")
    print(f"🎯 Governance tracking is now active!")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
    print("💡 Check your chatflow ID and Flowise URL")
```

**💡 What to replace:**
- `YOUR-CHATFLOW-ID`: Use the chatflow ID you found in the previous step  
- `"your-team"` and `"your-project"`: Use your actual team and project names

## Step 3: See Your Tracking Data (immediate results)

The auto-instrumentation automatically captures detailed telemetry:

```json
{
  "trace_id": "abc123",
  "span_name": "flowise.flow_predict", 
  "attributes": {
    "operation_type": "ai.flow_execution",
    "provider": "flowise",
    "chatflow_id": "your-chatflow-id",
    "tokens_estimated_input": 26,
    "tokens_estimated_output": 45,
    "cost_estimated_usd": 0.00142,
    "team": "your-team", 
    "project": "your-project",
    "customer_id": null,
    "environment": "development",
    "execution_duration_ms": 2340,
    "session_id": "demo-session-123"
  }
}
```

### What This Tracking Data Tells You:

- **💰 Cost Attribution**: How much each request costs (`cost_estimated_usd`)
- **⏱️ Performance**: How long each request takes (`execution_duration_ms`)
- **📊 Usage**: Token consumption for input/output (`tokens_estimated_*`)
- **🏷️ Organization**: Which team, project, customer caused the cost
- **🔗 Context**: Session tracking for conversation flows (`session_id`)

## Step 4: View Your Data (choose your platform)

**Local Console Output** (for development):
```python
auto_instrument(
    team="your-team", 
    project="your-project",
    enable_console_export=True  # See telemetry in console
)
```

**Export to Observability Platforms**:
```bash
# For Datadog
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.datadoghq.com"
export OTEL_EXPORTER_OTLP_HEADERS="dd-api-key=your-key"

# For Grafana/Tempo  
export OTEL_EXPORTER_OTLP_ENDPOINT="http://tempo:4317"

# For Honeycomb
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io"
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=your-key"
```

## Environment Configuration (recommended)

Set these environment variables for automatic configuration:

```bash
# Flowise connection
export FLOWISE_BASE_URL="http://localhost:3000"  # Your Flowise URL
export FLOWISE_API_KEY="your-api-key"           # Optional for local dev

# Governance attribution
export GENOPS_TEAM="your-team"
export GENOPS_PROJECT="your-project"
export GENOPS_ENVIRONMENT="development"  # or staging, production
```

Then use without parameters:
```python
from genops.providers.flowise import auto_instrument
auto_instrument()  # Uses environment variables automatically
```

## Troubleshooting (if needed)

**Connection Issues:**
```python
# Test your Flowise connection
from genops.providers.flowise_validation import quick_test_flow

result = quick_test_flow("your-chatflow-id")
if result['success']:
    print("✅ Flowise is working!")
else:
    print(f"❌ Issue: {result['error']}")
```

**Common Issues:**
- **"Cannot connect to Flowise"** → Check if Flowise is running at the URL
- **"Authentication failed"** → Verify your API key (or remove for local dev)
- **"Chatflow not found"** → Check your chatflow ID in the Flowise UI

## What's Next?

Your Flowise governance is now active! You'll see:

✅ **Cost Tracking**: Every flow execution cost is calculated and tracked  
✅ **Team Attribution**: Costs are attributed to your specified team and project  
✅ **Usage Monitoring**: Token usage, execution duration, and performance metrics  
✅ **Multi-Provider Support**: Costs from underlying LLM providers (OpenAI, Anthropic, etc.)  

## Advanced Usage (optional)

**Manual Instrumentation** (for more control):
```python
from genops.providers.flowise import instrument_flowise

flowise = instrument_flowise(
    team="ai-team",
    project="customer-support", 
    environment="production"
)

# More explicit API usage
response = flowise.predict_flow(
    "chatflow-123",
    "What are your business hours?",
    sessionId="user-456"
)
```

**Cost Analysis**:
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
print(f"Execution cost: ${cost.total_cost:.6f}")
```

## Resources

- **📚 Complete Guide**: [Full Flowise Integration Documentation](integrations/flowise.md)
- **🎯 Examples**: [7 Production Examples](../examples/flowise/)
- **🔧 Validation**: Run `validate_flowise_setup()` anytime to check your setup
- **📊 Observability**: Works with all OpenTelemetry-compatible platforms

---

**✨ That's it!** Your Flowise applications now have enterprise-grade governance tracking with zero code changes to your existing flows.

Need help? Check the [full integration guide](integrations/flowise.md) or see [working examples](../examples/flowise/).