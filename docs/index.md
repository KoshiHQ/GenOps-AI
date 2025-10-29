# GenOps AI

<div align="center">
  <h2>OpenTelemetry-native governance for AI systems</h2>
  <p><em>Turn AI telemetry into actionable accountability</em></p>
  
  <a href="https://github.com/KoshiHQ/GenOps-AI/stargazers">
    <img src="https://img.shields.io/github/stars/KoshiHQ/GenOps-AI?style=social" alt="GitHub stars">
  </a>
  <a href="https://github.com/KoshiHQ/GenOps-AI/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/KoshiHQ/GenOps-AI/ci.yml?branch=main" alt="CI Status">
  </a>  
  <a href="https://badge.fury.io/py/genops">
    <img src="https://badge.fury.io/py/genops.svg" alt="PyPI version">
  </a>
  <a href="https://opensource.org/licenses/Apache-2.0">
    <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License">
  </a>
</div>

---

## What is GenOps AI?

GenOps AI is an **open-source governance framework** that brings cost attribution, policy enforcement, and compliance automation to AI systems using **OpenTelemetry standards**.

While [OpenLLMetry](https://github.com/traceloop/openllmetry) tells you *what* your AI is doing (prompts, completions, tokens), **GenOps AI tells you *why and how* — with governance telemetry** that enables:

- 💰 **Cost Attribution** across teams, projects, features, and customers
- 🛡️ **Policy Enforcement** with configurable limits and content filtering  
- 📊 **Budget Tracking** with automated alerts and spend controls
- 🔍 **Compliance Automation** with evaluation metrics and audit trails
- 📈 **Observability Integration** with your existing monitoring stack

**Built on OpenTelemetry standards, works alongside OpenLLMetry and other observability tools.**

## Quick Start

### Installation

=== "Basic"
    ```bash
    pip install genops
    ```

=== "With AI Providers"
    ```bash
    pip install "genops[openai,anthropic]"  # For OpenAI + Anthropic
    pip install "genops[all]"               # All providers
    ```

=== "Development"
    ```bash
    git clone https://github.com/KoshiHQ/GenOps-AI.git
    cd GenOps-AI
    make dev-install  # Sets up everything including pre-commit hooks
    ```

### 30-Second Test

Verify your installation works:

```bash
# Test the CLI
genops --version

# Quick Python test
python -c "import genops; print('✅ GenOps AI installed successfully!')"
```

### 5-Minute Governance Setup

```python
from genops.providers.openai import instrument_openai
import genops

# 1. Set default attribution (once at app startup)
genops.set_default_attributes(
    team="platform-engineering",
    project="ai-services", 
    environment="production"
)

# 2. Instrument your AI providers  
client = instrument_openai(api_key="your-openai-key")

# 3. Use normally - defaults inherited automatically
response = client.chat_completions_create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}],
    # Only specify what's unique to this operation
    customer_id="enterprise-123",
    feature="chat-assistant"
    # team, project, environment automatically included!
)

# 4. OpenTelemetry exports complete attribution data
# ✅ Cost, tokens, team, customer, feature → Your observability platform
```

## Key Features

### 🚀 **Provider Instrumentation**

Automatic governance tracking for major AI providers:

```python
from genops.providers.openai import instrument_openai

# Instrument OpenAI with automatic governance tracking
client = instrument_openai(api_key="your-openai-key")

# All calls now include cost, token, and governance telemetry
response = client.chat_completions_create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}],
    # Governance attributes
    team="support-team",
    project="ai-assistant", 
    customer_id="enterprise-123"
)
# ✅ Cost, tokens, policies automatically tracked and exported via OpenTelemetry
```

### 🛡️ **Policy Enforcement**

Configurable governance policies with real-time enforcement:

```python
from genops.core.policy import register_policy, PolicyResult, _policy_engine

# Register governance policies  
register_policy(
    name="cost_limit",
    enforcement_level=PolicyResult.BLOCKED,
    conditions={"max_cost": 5.00}
)

# Evaluate policies before operations
def safe_ai_operation(prompt: str, estimated_cost: float):
    # Check policy before operation
    result = _policy_engine.evaluate_policy("cost_limit", {"cost": estimated_cost})
    
    if result.result == PolicyResult.BLOCKED:
        raise Exception(f"Policy violation: {result.reason}")
    
    return call_ai_model(prompt)  # Proceeds if policy allows
```

### 📊 **Rich Governance Telemetry**

Comprehensive tracking with OpenTelemetry integration:

```python
from genops.core.telemetry import GenOpsTelemetry

telemetry = GenOpsTelemetry()

with telemetry.trace_operation(operation_name="document_analysis") as span:
    # AI processing...
    ai_result = process_document()
    
    # Record comprehensive governance signals
    telemetry.record_cost(span, cost=2.50, currency="USD", provider="openai")
    telemetry.record_policy(span, policy_name="content_safety", result="allowed") 
    telemetry.record_evaluation(span, metric_name="quality_score", score=0.92)
    telemetry.record_budget(span, budget_name="monthly_ai_spend", allocated=1000, consumed=150)
```

## Why GenOps AI?

**Traditional AI monitoring tells you what happened. GenOps AI tells you what it cost, who did it, whether it should have been allowed, and how well it worked.**

- **For DevOps Teams**: Integrate AI governance into existing observability workflows
- **For FinOps Teams**: Get precise cost attribution and budget controls
- **For Compliance Teams**: Automated policy enforcement with audit trails
- **For Product Teams**: Feature-level AI cost analysis and optimization insights

**Open source, OpenTelemetry-native, and designed to work with your existing stack.**

## Next Steps

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **Quick Start**

    ---

    Get up and running in 5 minutes with our comprehensive quick start guide.

    [:octicons-arrow-right-24: Quick Start](quickstart.md)

-   :material-book-open-page-variant:{ .lg .middle } **User Guide**

    ---

    Learn core concepts and best practices for AI governance.

    [:octicons-arrow-right-24: User Guide](user-guide/concepts.md)

-   :material-puzzle:{ .lg .middle } **Integrations**

    ---

    Connect GenOps AI with your AI providers and observability stack.

    [:octicons-arrow-right-24: Integrations](integrations/index.md)

-   :material-api:{ .lg .middle } **API Reference**

    ---

    Detailed API documentation for all GenOps AI components.

    [:octicons-arrow-right-24: API Reference](api/index.md)

</div>

## Community

We welcome contributions! GenOps AI is built by the community, for the community.

- **GitHub**: [KoshiHQ/GenOps-AI](https://github.com/KoshiHQ/GenOps-AI)
- **Discussions**: [GitHub Discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)  
- **Issues**: [Report bugs or request features](https://github.com/KoshiHQ/GenOps-AI/issues)

---

*Ready to bring governance to your AI systems?*

```bash
pip install genops
```