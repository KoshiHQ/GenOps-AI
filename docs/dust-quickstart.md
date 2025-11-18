# Dust Quickstart

Get GenOps governance telemetry running with your Dust AI workflows in under 5 minutes.

## 🚀 Quick Setup

### 1. Install GenOps with Dust Support

```bash
pip install genops[dust]
```

### 2. Set Environment Variables

```bash
export DUST_API_KEY="your_dust_api_key"
export DUST_WORKSPACE_ID="your_workspace_id" 
export OTEL_SERVICE_NAME="my-dust-app"
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"  # Optional
```

### 3. Validate Your Setup (Recommended)

Before proceeding, verify your configuration works:

```python
from genops.providers.dust_validation import quick_validate, validate_setup, print_validation_result

# Quick check
if quick_validate():
    print("✅ Dust integration ready!")
else:
    # Detailed diagnostics
    result = validate_setup()
    print_validation_result(result)
```

### 4. Enable Auto-Instrumentation (Zero Code Changes)

```python
import genops

# This one line enables telemetry for all Dust operations
genops.auto_instrument()

# Your existing Dust API code works unchanged!
import os
import requests

headers = {
    "Authorization": f"Bearer {os.getenv('DUST_API_KEY')}",
    "Content-Type": "application/json"
}

# Create conversation - automatically tracked with governance!
response = requests.post(
    f"https://dust.tt/api/v1/w/{os.getenv('DUST_WORKSPACE_ID')}/conversations",
    json={"title": "Customer Support", "visibility": "private"},
    headers=headers
)
```

**That's it!** Your Dust application now captures:
- ✅ Conversation and message costs with attribution
- ✅ Agent execution performance tracking
- ✅ Data source search analytics
- ✅ Complete request/response telemetry

## 💰 Add Cost Attribution

For per-team/customer billing, add governance attributes:

```python
from genops.providers.dust import instrument_dust

# Create instrumented Dust client with governance
dust = instrument_dust(
    api_key=os.getenv("DUST_API_KEY"),
    workspace_id=os.getenv("DUST_WORKSPACE_ID"),
    team="customer-success",           # Cost attribution  
    project="support-automation",      # Project tracking
    environment="production"           # Environment separation
)

# All operations automatically inherit governance attributes
conversation = dust.create_conversation(
    title="Customer Inquiry",
    customer_id="cust-123"           # Per-customer billing
)
```


## 📊 View Your Data

Your telemetry data flows to any OpenTelemetry-compatible backend:

- **Jaeger**: Distributed tracing with conversation flows
- **Datadog**: Cost dashboards and performance monitoring  
- **Grafana**: Custom governance analytics
- **Console**: Local development with `enable_console_export=True`

## 🚀 Next Steps

- **30-minute exploration**: See [integration guide](integrations/dust.md) for advanced features
- **Production deployment**: Check [production patterns example](../examples/dust/production_patterns.py)
- **Cost optimization**: Run [cost analysis example](../examples/dust/cost_optimization.py)

## 🆘 Need Help?

- Run `python examples/dust/setup_validation.py` for detailed diagnostics
- Check the [troubleshooting guide](integrations/dust.md#troubleshooting)
- Join our [community support](https://github.com/KoshiHQ/GenOps-AI/issues)

**Developer Experience Validation**: A developer with no prior GenOps knowledge should be productive within 5 minutes of following this guide.