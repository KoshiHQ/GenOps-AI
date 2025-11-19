# Dust AI Integration Guide

[Dust](https://dust.tt) is a platform to create custom AI agents that can read your company knowledge and perform actions via built-in and custom tools. This guide shows how to add GenOps governance and cost tracking to your Dust AI workflows.

## Quick Start

### Installation

Install GenOps with Dust support:

```bash
pip install genops[dust]
```

### Environment Setup

Set your Dust credentials:

```bash
export DUST_API_KEY="your_dust_api_key"
export DUST_WORKSPACE_ID="your_workspace_id"

# Optional: OpenTelemetry configuration
export OTEL_SERVICE_NAME="my-dust-app"
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"

# Optional: Governance attributes
export GENOPS_TEAM="ai-team"
export GENOPS_PROJECT="customer-support"
export GENOPS_ENVIRONMENT="production"
```

### Basic Usage

```python
import genops
from genops.providers.dust import instrument_dust

# Initialize GenOps
genops.init()

# Create instrumented Dust adapter
dust = instrument_dust(
    api_key="your_dust_api_key",
    workspace_id="your_workspace_id",
    team="ai-team",
    project="customer-support"
)

# Create a conversation with governance tracking
conversation = dust.create_conversation(
    title="Customer Support Chat",
    visibility="private",
    customer_id="cust-123"
)

# Send messages with cost attribution
response = dust.send_message(
    conversation_id=conversation["conversation"]["sId"],
    content="Help me understand the pricing plans",
    feature="pricing-inquiry",
    user_id="user-456"
)

# Run an agent with governance tracking
agent_result = dust.run_agent(
    agent_id="agent-abc123",
    inputs={"query": "Find pricing documentation"},
    project="customer-support",
    cost_center="support-ops"
)
```

## Advanced Features

### Cost Tracking and Optimization

```python
from genops.providers.dust_pricing import calculate_dust_cost, get_dust_pricing_info

# Calculate costs for operations
cost_breakdown = calculate_dust_cost(
    operation_type="conversation",
    operation_count=50,
    estimated_tokens=25000,
    user_count=10,
    plan_type="pro"
)

print(f"Monthly cost: €{cost_breakdown.total_cost:.2f}")
print(f"Cost per user: €{cost_breakdown.total_cost / cost_breakdown.user_count:.2f}")

# Get current pricing information
pricing = get_dust_pricing_info()
print(f"Pro plan: €{pricing.pro_monthly_per_user}/user/month")
```

### Data Source Management

```python
# Create and track data sources
datasource = dust.create_datasource(
    name="support-docs",
    description="Customer support documentation",
    visibility="workspace",
    provider_id="webcrawler",
    team="support",
    project="knowledge-base"
)

# Search with governance tracking
search_results = dust.search_datasources(
    query="refund policy",
    data_sources=["support-docs"],
    top_k=5,
    customer_id="cust-789",
    feature="policy-lookup"
)
```

### Enterprise Workflow Patterns

```python
import genops
from genops.providers.dust import instrument_dust
from genops.core.context import set_customer_context

dust = instrument_dust(
    api_key=os.getenv("DUST_API_KEY"),
    workspace_id=os.getenv("DUST_WORKSPACE_ID")
)

# Customer-specific context management
def handle_customer_inquiry(customer_id: str, inquiry: str):
    with set_customer_context(
        customer_id=customer_id,
        team="customer-success",
        environment="production"
    ):
        # Create conversation with automatic customer attribution
        conversation = dust.create_conversation(
            title=f"Inquiry from {customer_id}",
            visibility="private"
        )
        
        # Send message with inherited context
        response = dust.send_message(
            conversation_id=conversation["conversation"]["sId"],
            content=inquiry
        )
        
        return response

# Multi-agent workflow with cost tracking
def complex_support_workflow(query: str):
    # Agent 1: Initial classification
    classification = dust.run_agent(
        agent_id="classifier-agent",
        inputs={"query": query},
        feature="query-classification"
    )
    
    # Agent 2: Specialized response based on classification
    category = classification.get("run", {}).get("results", [{}])[0].get("category", "general")
    
    response = dust.run_agent(
        agent_id=f"{category}-agent",
        inputs={"query": query, "category": category},
        feature="specialized-response"
    )
    
    return response
```

## Validation and Setup

Validate your Dust integration:

```python
from genops.providers.dust_validation import validate_setup, print_validation_result

# Validate setup
result = validate_setup(
    api_key="your_dust_api_key",
    workspace_id="your_workspace_id"
)

# Print detailed results
print_validation_result(result)

# Quick validation check
from genops.providers.dust_validation import quick_validate
if quick_validate():
    print("✅ Dust integration ready!")
else:
    print("❌ Setup needs attention")
```

## Production Deployment

### Kubernetes Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dust-app
spec:
  template:
    spec:
      containers:
      - name: app
        env:
        - name: DUST_API_KEY
          valueFrom:
            secretKeyRef:
              name: dust-secrets
              key: api-key
        - name: DUST_WORKSPACE_ID
          valueFrom:
            secretKeyRef:
              name: dust-secrets
              key: workspace-id
        - name: OTEL_SERVICE_NAME
          value: "dust-customer-support"
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: "http://otel-collector:4317"
        - name: GENOPS_TEAM
          value: "customer-success"
        - name: GENOPS_ENVIRONMENT
          value: "production"
```

### Docker Configuration

```dockerfile
FROM python:3.11-slim

RUN pip install genops[dust]

ENV DUST_API_KEY=""
ENV DUST_WORKSPACE_ID=""
ENV OTEL_SERVICE_NAME="dust-app"
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"

COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
```

### Cost Monitoring and Alerts

```python
from genops.providers.dust_pricing import DustPricingEngine

engine = DustPricingEngine()

# Monitor monthly costs
def monitor_dust_costs(usage_stats: dict):
    cost_estimate = engine.estimate_monthly_cost(
        user_count=usage_stats["active_users"],
        usage_forecast={
            "conversations": usage_stats["monthly_conversations"],
            "agent_runs": usage_stats["monthly_agent_runs"],
            "searches": usage_stats["monthly_searches"]
        },
        plan_type="pro"
    )
    
    if cost_estimate["total_monthly_cost"] > 5000:  # €5000 threshold
        send_cost_alert(cost_estimate)
    
    return cost_estimate

# Get optimization insights
insights = engine.get_cost_optimization_insights({
    "active_users": 45,
    "total_users": 50,
    "total_operations": 10000,
    "conversations": 3000,
    "agent_runs": 5000,
    "searches": 2000
})

for category, recommendation in insights.items():
    print(f"{category}: {recommendation}")
```

## Governance and Compliance

### Audit Trail Configuration

```python
# Enhanced audit logging for compliance
def create_audited_conversation(title: str, customer_id: str, user_id: str):
    return dust.create_conversation(
        title=title,
        visibility="private",
        # Governance attributes for audit trail
        customer_id=customer_id,
        user_id=user_id,
        team="customer-support",
        environment="production",
        cost_center="support-operations",
        # Compliance attributes
        data_classification="customer-pii",
        retention_policy="7-years",
        compliance_tags=["gdpr", "ccpa"]
    )
```

### Budget Enforcement

```python
from genops.core.policy import enforce_policy

# Define budget policy
@enforce_policy("dust_monthly_budget", max_cost=3000)  # €3000/month
def run_dust_agent(agent_id: str, inputs: dict, **kwargs):
    return dust.run_agent(agent_id=agent_id, inputs=inputs, **kwargs)
```

## Monitoring and Observability

### OpenTelemetry Dashboard Queries

Monitor Dust operations in your observability platform:

```sql
-- Conversation volume by team
SELECT team, COUNT(*) as conversations
FROM traces 
WHERE operation_name = 'dust.conversation.create'
  AND time >= now() - interval '24h'
GROUP BY team

-- Average tokens per customer
SELECT customer_id, AVG(tokens_estimated_input + tokens_estimated_output) as avg_tokens
FROM traces
WHERE provider = 'dust'
  AND time >= now() - interval '7d'
GROUP BY customer_id

-- Cost analysis by project
SELECT project, SUM(estimated_cost) as total_cost
FROM traces
WHERE provider = 'dust'
  AND time >= now() - interval '30d'
GROUP BY project
ORDER BY total_cost DESC
```

### Custom Metrics

```python
from opentelemetry import metrics

# Custom metrics for Dust monitoring
meter = metrics.get_meter("dust.custom")

conversation_counter = meter.create_counter(
    "dust.conversations.total",
    description="Total number of Dust conversations created"
)

agent_execution_histogram = meter.create_histogram(
    "dust.agent.execution.duration",
    description="Duration of Dust agent executions"
)

# Use in your application
conversation_counter.add(1, {"team": "support", "customer_type": "enterprise"})
agent_execution_histogram.record(1.5, {"agent_type": "classifier"})
```

## Best Practices

### 1. Cost Optimization

- **Monitor user utilization**: Track active vs. total users to optimize licenses
- **Agent efficiency**: Profile agent execution times and optimize prompts
- **Search optimization**: Cache frequent search results to reduce API calls
- **Batch operations**: Group related operations when possible

### 2. Security and Compliance

- **API key rotation**: Implement regular API key rotation
- **Data classification**: Tag conversations with appropriate data classifications
- **Access controls**: Use workspace-level permissions effectively
- **Audit logging**: Ensure all operations are tracked for compliance

### 3. Performance Optimization

- **Connection pooling**: Reuse HTTP connections for better performance
- **Error handling**: Implement retry logic with exponential backoff
- **Rate limiting**: Respect Dust API rate limits
- **Monitoring**: Set up alerts for API errors and performance degradation

### 4. Governance Implementation

- **Consistent attribution**: Always include team, project, and customer_id
- **Cost centers**: Map operations to appropriate cost centers
- **Environment tagging**: Clearly distinguish dev/staging/prod usage
- **Policy enforcement**: Implement budget and usage policies

## Troubleshooting

### Common Issues

1. **Authentication Errors**
   ```
   Error: 401 Unauthorized
   ```
   - Verify DUST_API_KEY is correct
   - Check API key has workspace access
   - Ensure key hasn't expired

2. **Workspace Access Issues**
   ```
   Error: 403 Forbidden
   ```
   - Verify DUST_WORKSPACE_ID is correct
   - Check user permissions in workspace
   - Confirm API key has required permissions

3. **Network Connectivity**
   ```
   Error: Connection timeout
   ```
   - Check internet connectivity
   - Verify firewall settings allow HTTPS traffic
   - Test with curl: `curl -H "Authorization: Bearer $DUST_API_KEY" https://dust.tt/api/v1/w/$DUST_WORKSPACE_ID/conversations`

### Debug Mode

Enable debug logging:

```python
import logging

# Enable debug logging for Dust operations
logging.getLogger("genops.providers.dust").setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

# Run operations with detailed logging
dust = instrument_dust(
    api_key="your_key",
    workspace_id="your_workspace",
    debug=True  # Enable detailed request/response logging
)
```

## API Reference

### DustAdapter Methods

- `create_conversation(title, visibility, **kwargs)` - Create new conversation
- `send_message(conversation_id, content, **kwargs)` - Send message to conversation  
- `run_agent(agent_id, inputs, **kwargs)` - Execute Dust agent
- `create_datasource(name, description, **kwargs)` - Create new data source
- `search_datasources(query, data_sources, **kwargs)` - Search across data sources

### Governance Attributes

All methods support these governance attributes:

- `team` - Team responsible for the operation
- `project` - Project the operation belongs to
- `customer_id` - Customer identifier for cost attribution
- `environment` - Environment (dev/staging/prod)
- `cost_center` - Cost center for financial reporting
- `user_id` - User performing the operation
- `feature` - Specific feature being used

For complete API documentation and additional examples, see the [GenOps API Reference](../api/).

## Next Steps

Now that you have comprehensive Dust integration set up, here are recommended next steps:

### Production Deployment
- **Enterprise patterns**: Review [production patterns example](../../examples/dust/production_patterns.py) for multi-customer governance
- **Kubernetes deployment**: Configure production telemetry export with OTLP collectors
- **Cost monitoring**: Set up budget alerts and cost optimization dashboards

### Advanced Features
- **Complex workflows**: Explore [advanced features example](../../examples/dust/advanced_features.py) for workflow orchestration
- **Performance optimization**: Implement caching and batch operations for high-volume scenarios
- **Custom telemetry**: Add application-specific metrics and correlation

### Team Adoption
- **Documentation**: Share this integration guide with your team
- **Best practices**: Establish governance attribute standards across projects
- **Cost attribution**: Configure team and project-specific cost centers

### Community & Support
- **Examples repository**: Browse additional [Dust examples](../../examples/dust/) for specific use cases
- **Community discussions**: Join [GitHub Discussions](https://github.com/KoshiHQ/GenOps-AI/discussions) for Q&A
- **Issue reporting**: Report bugs or feature requests via [GitHub Issues](https://github.com/KoshiHQ/GenOps-AI/issues)

**Ready to scale?** Your Dust integration now provides enterprise-grade governance and cost tracking that grows with your organization.