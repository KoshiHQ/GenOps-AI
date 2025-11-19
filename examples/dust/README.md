# Dust AI Examples

This directory contains examples demonstrating how to use GenOps with Dust AI for governance, cost tracking, and observability.

## Examples Overview

- **`basic_tracking.py`** - Basic Dust operations with GenOps tracking
- **`auto_instrumentation.py`** - Zero-code auto-instrumentation setup
- **`setup_validation.py`** - Validate your Dust integration setup
- **`cost_optimization.py`** - Cost tracking and optimization strategies
- **`production_patterns.py`** - Enterprise-ready deployment patterns
- **`advanced_features.py`** - Advanced governance and monitoring features

## Prerequisites

1. **Install Dependencies**
   ```bash
   pip install genops[dust]
   ```

2. **Set Environment Variables**
   ```bash
   export DUST_API_KEY="your_dust_api_key"
   export DUST_WORKSPACE_ID="your_workspace_id"
   
   # Optional: OpenTelemetry configuration
   export OTEL_SERVICE_NAME="dust-examples"
   export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
   
   # Optional: Governance attributes
   export GENOPS_TEAM="ai-team"
   export GENOPS_PROJECT="examples"
   export GENOPS_ENVIRONMENT="development"
   ```

3. **Get Dust Credentials**
   - Sign up at [dust.tt](https://dust.tt)
   - Create a workspace
   - Generate an API key from your workspace settings

## Quick Start

Run the basic example to verify your setup:

```bash
python basic_tracking.py
```

For auto-instrumentation (zero code changes):

```bash
python auto_instrumentation.py
```

Validate your setup:

```bash
python setup_validation.py
```

## Running Examples

Each example is self-contained and demonstrates specific GenOps capabilities with Dust:

```bash
# Basic tracking
python basic_tracking.py

# Cost analysis
python cost_optimization.py

# Production patterns
python production_patterns.py

# Advanced features
python advanced_features.py
```

## Example Categories

### Basic Integration
- Simple conversation creation and message sending
- Basic governance attribute usage
- Cost attribution patterns

### Cost Management
- Subscription cost calculation
- Usage-based cost estimation
- Budget monitoring and alerts
- Cost optimization insights

### Production Deployment
- Enterprise governance patterns
- Multi-customer attribution
- Policy enforcement
- Compliance audit trails

### Advanced Features
- Custom telemetry and metrics
- Complex workflow orchestration
- Error handling and retry logic
- Performance monitoring

## Common Patterns

### Customer Context Management

```python
from genops.core.context import set_customer_context
from genops.providers.dust import instrument_dust

dust = instrument_dust(
    api_key=os.getenv("DUST_API_KEY"),
    workspace_id=os.getenv("DUST_WORKSPACE_ID")
)

# Automatic customer attribution
with set_customer_context(customer_id="cust-123", team="support"):
    conversation = dust.create_conversation(title="Support Chat")
    # Inherits customer_id and team automatically
```

### Cost Tracking

```python
from genops.providers.dust_pricing import calculate_dust_cost

# Calculate operation costs
cost = calculate_dust_cost(
    operation_type="conversation",
    operation_count=10,
    user_count=5,
    plan_type="pro"
)
print(f"Estimated monthly cost: €{cost.total_cost}")
```

### Validation and Setup

```python
from genops.providers.dust_validation import validate_setup, print_validation_result

# Comprehensive setup validation
result = validate_setup()
print_validation_result(result)

if result.is_valid:
    print("✅ Ready to use Dust with GenOps!")
else:
    print("❌ Setup needs attention")
```

## Observability

All examples automatically generate OpenTelemetry traces and metrics. View them in your observability platform:

- **Traces**: `dust.*` operations with governance attributes
- **Metrics**: Cost, usage, and performance metrics
- **Logs**: Structured logs with correlation IDs

## Support

If you encounter issues:

1. Run `python setup_validation.py` to check your configuration
2. Enable debug logging: `export GENOPS_LOG_LEVEL=DEBUG`
3. Check the [troubleshooting guide](../../docs/integrations/dust.md#troubleshooting)
4. Open an issue on GitHub

## Contributing

Have an example that would help others? Please contribute!

1. Create a new example file
2. Add clear documentation and comments
3. Test with different Dust configurations
4. Submit a pull request

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for details.