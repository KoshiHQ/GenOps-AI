# ADR-0003: Governance Telemetry Semantics Specification  

## Status
Accepted

*Date: 2024-01-25*

## Context

GenOps AI extends OpenTelemetry with governance-specific semantic conventions to capture cost, policy, compliance, and evaluation telemetry. These conventions must:

- **Integrate seamlessly** with existing OpenTelemetry semantic conventions
- **Provide sufficient granularity** for accurate cost attribution and policy enforcement
- **Remain vendor-neutral** while supporting provider-specific optimizations
- **Enable rich querying** and analysis in observability platforms
- **Support both simple and complex** governance scenarios

The challenge is balancing **expressiveness** (capturing all necessary governance context) with **simplicity** (easy to adopt and understand). Too many attributes create complexity; too few limit functionality.

Existing standards considered:
- **OpenTelemetry Semantic Conventions** - Foundation but lacks governance concepts
- **OpenLLMetry Conventions** - Covers LLM observability but not governance  
- **FinOps Framework** - Financial operations but not AI-specific
- **Custom conventions** - Maximum flexibility but poor interoperability

## Decision

We will define **GenOps Governance Semantic Conventions** as an extension to OpenTelemetry, organized into four main namespaces:

### 1. Cost Attribution (`genops.cost.*`)
```yaml
genops.cost.amount: 0.00234          # Total cost in base currency
genops.cost.currency: "USD"          # ISO 4217 currency code  
genops.cost.provider: "openai"       # AI provider name
genops.cost.model: "gpt-4"          # Model/service used
genops.cost.breakdown.input: 0.0012 # Cost breakdown by component
genops.cost.breakdown.output: 0.0011
```

### 2. Policy Governance (`genops.policy.*`)
```yaml
genops.policy.name: "cost_limit"     # Policy identifier
genops.policy.result: "allowed"      # allowed|warning|blocked
genops.policy.reason: "within_budget" # Human-readable explanation
genops.policy.enforcement_level: "warning" # Policy configuration
```

### 3. Evaluation Metrics (`genops.eval.*`)
```yaml
genops.eval.metric_name: "quality"   # Evaluation metric identifier
genops.eval.score: 0.87             # Numeric score/rating
genops.eval.threshold: 0.80          # Pass/fail threshold
genops.eval.passed: true             # Boolean result
genops.eval.evaluator: "human"       # Who/what performed evaluation
```

### 4. Budget Tracking (`genops.budget.*`)
```yaml
genops.budget.name: "team_monthly"   # Budget identifier
genops.budget.allocated: 1000.00     # Total budget amount
genops.budget.consumed: 234.50       # Amount used so far
genops.budget.remaining: 765.50      # Amount remaining
genops.budget.period: "2024-01"      # Budget period identifier
```

### Core Attribution Attributes
```yaml
# Team and organizational context
genops.team: "engineering"           # Team responsible
genops.project: "ai-assistant"       # Project/product name
genops.environment: "production"     # Deployment environment

# Customer and business context  
genops.customer_id: "enterprise_123" # Customer identifier
genops.feature: "chat_completion"    # Feature/capability used
genops.session_id: "session_abc123"  # User session identifier

# Technical context
genops.operation_name: "ai_chat"     # High-level operation
genops.model_version: "gpt-4-0314"   # Specific model version
genops.provider_region: "us-east-1"  # Provider region/zone
```

## Alternatives Considered

### Flat Attribute Namespace
```yaml
genops_cost_amount: 0.00234
genops_cost_currency: "USD"  
genops_policy_result: "allowed"
```

**Pros:** Simple, no nesting complexity  
**Cons:** Verbose, poor organization, difficult to query by category

### Deep Hierarchical Structure  
```yaml
genops.governance.cost.attribution.amount: 0.00234
genops.governance.policy.enforcement.result: "allowed"
```

**Pros:** Very organized and explicit  
**Cons:** Extremely verbose, difficult to type and remember

### Provider-Specific Extensions
```yaml
genops.openai.cost: 0.00234
genops.anthropic.tokens: 150
```

**Pros:** Allows provider-specific optimizations  
**Cons:** Breaks vendor neutrality, fragmented querying

## Consequences

### Positive
- **Standardized governance telemetry** across all GenOps implementations
- **Rich attribution context** for accurate cost allocation and analysis  
- **Policy traceability** with clear enforcement results and reasoning
- **Evaluation framework** for quality, safety, and performance metrics
- **Budget visibility** with spend tracking and utilization monitoring
- **Query-friendly structure** for dashboards and analytics

### Negative
- **Attribute proliferation** may overwhelm spans with metadata
- **Learning curve** for developers adopting governance conventions
- **Cardinality concerns** in high-volume environments
- **Version management** as conventions evolve over time

### Neutral
- **OpenTelemetry alignment** ensures compatibility with existing tooling
- **Namespace organization** balances discoverability with verbosity  
- **Extensibility** allows provider-specific additions when needed

## Implementation Notes

### Convention Evolution
- **Version tagging**: Conventions versioned separately from SDK
- **Backward compatibility**: New attributes added, existing ones deprecated gradually  
- **Community input**: RFC process for convention changes
- **Provider feedback**: Regular review with AI provider partners

### Cardinality Management
```python
# High-cardinality attributes on spans only
span.set_attribute("genops.customer_id", "customer_123")
span.set_attribute("genops.session_id", "session_abc")

# Low-cardinality attributes on metrics  
cost_metric.add(amount, {
    "genops.team": "engineering",
    "genops.provider": "openai",
    "genops.model": "gpt-4"
})
```

### Documentation Structure
- **Semantic convention registry** with all attribute definitions
- **Usage examples** for common governance scenarios  
- **Migration guide** from custom attributes to standard conventions
- **Query cookbook** for common analysis patterns

## References

- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/)
- [OpenLLMetry Conventions](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-semantic-conventions-ai)
- [FinOps Framework](https://www.finops.org/framework/)
- [ISO 4217 Currency Codes](https://www.iso.org/iso-4217-currency-codes.html)
- [OpenTelemetry Attribute Guidelines](https://opentelemetry.io/docs/specs/otel/common/attribute-naming/)

---

*Author: GenOps AI Team*  
*Reviewers: Semantic Conventions Working Group, OpenTelemetry Community*