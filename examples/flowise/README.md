# Flowise Integration Examples

**Production-ready examples demonstrating GenOps governance patterns with Flowise AI workflows.**

## Examples Overview

| Example | Description | Complexity | Use Case |
|---------|-------------|------------|----------|
| [Basic Flow Execution](01_basic_flow_execution.py) | Simple chatflow execution with governance | ⭐ Beginner | Getting started |
| [Auto-Instrumentation](02_auto_instrumentation.py) | Zero-code instrumentation setup | ⭐ Beginner | Quick setup |
| [Multi-Flow Orchestration](03_multi_flow_orchestration.py) | Sequential flow execution with context | ⭐⭐ Intermediate | Complex workflows |
| [Cost Optimization](04_cost_optimization.py) | Cost tracking and optimization analysis | ⭐⭐ Intermediate | Budget management |
| [Multi-Tenant SaaS](05_multi_tenant_saas.py) | Multi-tenant cost isolation | ⭐⭐⭐ Advanced | SaaS platforms |
| [Enterprise Governance](06_enterprise_governance.py) | Full governance with budget enforcement | ⭐⭐⭐ Advanced | Enterprise deployment |
| [Production Monitoring](07_production_monitoring.py) | Comprehensive monitoring and alerting | ⭐⭐⭐ Advanced | Production operations |
| [Async High-Performance](08_async_high_performance.py) | High-throughput async processing | ⭐⭐⭐ Advanced | High-scale applications |

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install genops requests flask prometheus_client aiohttp
   ```

2. **Set Environment Variables**:
   ```bash
   export FLOWISE_BASE_URL="http://localhost:3000"
   export FLOWISE_API_KEY="your-api-key"  # Optional for local development
   export GENOPS_TEAM="your-team"
   export GENOPS_PROJECT="flowise-examples"
   ```

3. **Start with Basic Example**:
   ```bash
   python 01_basic_flow_execution.py
   ```

## Prerequisites

- **Flowise Instance**: Running locally or in cloud
  ```bash
  # Quick local setup with Docker
  docker run -d --name flowise -p 3000:3000 flowiseai/flowise
  ```

- **Sample Chatflows**: Create at least one chatflow in Flowise UI
- **GenOps Package**: `pip install genops`

## Example Categories

### 🌟 Beginner Examples

Perfect for getting started with Flowise governance:

- **Basic Flow Execution**: Simple chatflow execution with telemetry
- **Auto-Instrumentation**: Zero-code setup for existing applications

### 🌟🌟 Intermediate Examples  

Practical patterns for real applications:

- **Multi-Flow Orchestration**: Complex workflows with multiple flows
- **Cost Optimization**: Budget tracking and cost analysis

### 🌟🌟🌟 Advanced Examples

Enterprise-grade patterns for production:

- **Multi-Tenant SaaS**: Customer isolation and per-tenant billing
- **Enterprise Governance**: Policy enforcement and compliance
- **Production Monitoring**: Comprehensive observability setup
- **Async High-Performance**: Scalable async processing

## Running Examples

### Individual Examples

```bash
# Run specific example
python examples/flowise/01_basic_flow_execution.py

# Run with custom configuration
FLOWISE_BASE_URL="http://your-flowise.com" python 02_auto_instrumentation.py
```

### All Examples Test Suite

```bash
# Run all examples (requires working Flowise instance)
python -m pytest examples/flowise/ -v
```

### Docker Environment

```bash
# Run examples in Docker environment
docker-compose -f examples/flowise/docker-compose.yml up
```

## Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `FLOWISE_BASE_URL` | Flowise instance URL | `http://localhost:3000` | Yes |
| `FLOWISE_API_KEY` | Flowise API key | None | No (local dev) |
| `GENOPS_TEAM` | Team for governance | `flowise-examples` | Recommended |
| `GENOPS_PROJECT` | Project identifier | `examples` | Recommended |
| `GENOPS_ENVIRONMENT` | Environment name | `development` | Optional |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | Telemetry endpoint | None | Optional |

### Sample Configuration File

```python
# config.py
import os

FLOWISE_CONFIG = {
    'base_url': os.getenv('FLOWISE_BASE_URL', 'http://localhost:3000'),
    'api_key': os.getenv('FLOWISE_API_KEY'),
    'team': os.getenv('GENOPS_TEAM', 'flowise-examples'),
    'project': os.getenv('GENOPS_PROJECT', 'examples'),
    'environment': os.getenv('GENOPS_ENVIRONMENT', 'development')
}

# Export for use in examples
__all__ = ['FLOWISE_CONFIG']
```

## Integration Patterns

### Pattern 1: Auto-Instrumentation (Recommended)

```python
from genops.providers.flowise import auto_instrument

# Enable once at application startup
auto_instrument(team="your-team", project="your-project")

# All existing Flowise code is automatically tracked
import requests
response = requests.post(f"{flowise_url}/api/v1/prediction/{chatflow_id}", ...)
```

### Pattern 2: Manual Adapter

```python
from genops.providers.flowise import instrument_flowise

flowise = instrument_flowise(team="your-team", project="your-project")
response = flowise.predict_flow(chatflow_id, "Your question")
```

### Pattern 3: Context Manager

```python
from genops.core.context import with_governance_context

with with_governance_context(customer_id="customer-123") as context:
    response = flowise.predict_flow(chatflow_id, question)
    print(f"Total cost: ${context.total_cost:.4f}")
```

## Observability Integration

### Datadog Dashboard

```python
# Export telemetry to Datadog
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.datadoghq.com"
export OTEL_EXPORTER_OTLP_HEADERS="dd-api-key=your-datadog-key"

# Run any example - telemetry will appear in Datadog
python 01_basic_flow_execution.py
```

### Grafana Integration

```python
# Export to Grafana/Tempo
export OTEL_EXPORTER_OTLP_ENDPOINT="http://tempo:4317"

# Run examples with Grafana monitoring
python 07_production_monitoring.py
```

### Custom Dashboards

See [Production Monitoring Example](07_production_monitoring.py) for:
- Prometheus metrics collection
- Custom dashboard setup  
- Alert configuration
- Health check endpoints

## Testing

### Unit Tests

```bash
# Run example-specific tests
python -m pytest examples/flowise/tests/ -v
```

### Integration Tests

```bash
# Run full integration tests (requires live Flowise)
python -m pytest examples/flowise/tests/test_integration.py -v
```

### Performance Tests

```bash
# Run performance benchmarks
python examples/flowise/08_async_high_performance.py --benchmark
```

## Troubleshooting

### Common Issues

1. **Connection Refused**
   ```bash
   # Check if Flowise is running
   curl http://localhost:3000/api/v1/chatflows
   ```

2. **No Chatflows Available**
   ```bash
   # Create a sample chatflow in Flowise UI
   # Or check available flows:
   python -c "
   from examples.flowise.config import FLOWISE_CONFIG
   from genops.providers.flowise import instrument_flowise
   flowise = instrument_flowise(**FLOWISE_CONFIG)
   print(flowise.get_chatflows())
   "
   ```

3. **Authentication Issues**
   ```bash
   # For local development, API key is usually not required
   unset FLOWISE_API_KEY
   python 01_basic_flow_execution.py
   ```

### Debug Mode

```bash
# Enable debug logging
export GENOPS_LOG_LEVEL="DEBUG"
python examples/flowise/01_basic_flow_execution.py
```

### Validation

```bash
# Validate setup before running examples
python -c "
from genops.providers.flowise_validation import validate_and_print
validate_and_print()
"
```

## Contributing

### Adding New Examples

1. **Follow naming convention**: `##_descriptive_name.py`
2. **Include docstring**: Describe purpose and complexity
3. **Add error handling**: Graceful failure with helpful messages
4. **Document dependencies**: List any additional packages needed
5. **Test thoroughly**: Ensure example works in clean environment

### Example Template

```python
#!/usr/bin/env python3
"""
Example: [Brief Description]

Complexity: ⭐⭐ [Beginner/Intermediate/Advanced]

This example demonstrates [specific functionality and use case].

Prerequisites:
- Flowise instance running
- [Any specific chatflow requirements]
- [Additional dependencies if needed]

Usage:
    python ##_example_name.py

Environment Variables:
    FLOWISE_BASE_URL: Flowise instance URL
    FLOWISE_API_KEY: API key (optional for local dev)
"""

import os
import logging
from genops.providers.flowise import instrument_flowise

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Main example function."""
    try:
        # Example implementation
        pass
    except Exception as e:
        logger.error(f"Example failed: {e}")
        return False
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
```

## Resources

- **📚 Integration Guide**: [Complete Flowise Documentation](../../docs/integrations/flowise.md)
- **⚡ Quick Start**: [5-Minute Setup Guide](../../docs/flowise-quickstart.md)
- **🔍 Validation**: Use `validate_flowise_setup()` to check configuration
- **💬 Support**: [GitHub Issues](https://github.com/KoshiHQ/GenOps-AI/issues) for questions

---

**Ready to explore Flowise governance patterns?** Start with the basic examples and work your way up to advanced enterprise patterns! 🚀