# GenOps AI

<div align="center">
  <h3>OpenTelemetry-native governance for AI systems</h3>
  <p><em>Turn AI telemetry into actionable accountability</em></p>
  
  [![GitHub stars](https://img.shields.io/github/stars/KoshiHQ/GenOps-AI?style=social)](https://github.com/KoshiHQ/GenOps-AI/stargazers)
  [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
  [![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
  [![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-native-purple.svg)](https://opentelemetry.io/)
</div>

---

## 🎯 **What is GenOps AI?**

GenOps AI is an **open-source governance framework** that brings cost attribution, policy enforcement, and compliance automation to AI systems using **OpenTelemetry standards**.

While [OpenLLMetry](https://github.com/traceloop/openllmetry) tells you *what* your AI is doing (prompts, completions, tokens), **GenOps AI tells you *why and how* — with governance telemetry** that enables:

- 💰 **Cost Attribution** across teams, projects, features, and customers
- 🛡️ **Policy Enforcement** with configurable limits and content filtering  
- 📊 **Budget Tracking** with automated alerts and spend controls
- 🔍 **Compliance Automation** with evaluation metrics and audit trails
- 🏢 **Enterprise Governance** feeding dashboards, FinOps, and control planes

**Built alongside OpenLLMetry, interoperable by design, independent by governance.**

---

## ✨ **Key Features**

### 🚀 **One-Line Setup** (OpenLLMetry-inspired)
```python
import genops

# Auto-instrument all AI providers with governance
genops.init()

# Your existing AI code now has automatic governance! 
import openai
response = openai.chat.completions.create(...)  # Tracked automatically
```

### 🎛️ **Manual Instrumentation** 
```python
import genops

@genops.track_usage(
    operation_name="customer_support",
    team="support",
    project="chatbot", 
    feature="conversation",
    customer_id="customer_123"
)
def handle_support_query(message: str):
    # Your AI logic here
    return ai_response

# Governance data flows to your observability stack
```

### 🛡️ **Policy Enforcement**
```python
from genops import enforce_policy, register_policy, PolicyResult

# Register governance policies
register_policy(
    name="cost_control",
    enforcement_level=PolicyResult.BLOCKED,
    max_cost=5.00
)

@enforce_policy(["cost_control"])
def expensive_ai_operation(prompt: str):
    # Blocked if cost exceeds $5.00
    return call_ai_model(prompt)
```

### 📊 **Rich Governance Telemetry**
```python
with genops.track(operation_name="document_analysis") as span:
    # AI processing...
    
    # Record governance signals
    span.record_cost(cost=2.50, currency="USD")
    span.record_policy("content_safety", "allowed")
    span.record_evaluation("quality_score", 0.92)
    span.record_budget("monthly_ai_spend", allocated=1000, used=150)
```

---

## 🚀 **Quick Start**

### Installation

```bash
pip install genops

# With AI provider support
pip install "genops[openai,anthropic]"  # For OpenAI + Anthropic
pip install "genops[all]"               # All providers
```

### 30-Second Governance Setup

```python
import genops

# 1. Initialize with your observability stack
genops.init(
    service_name="my-ai-service",
    environment="production",
    exporter_type="otlp",                    # or "console" for testing
    otlp_endpoint="https://api.honeycomb.io", # Your OTLP endpoint
    otlp_headers={"x-honeycomb-team": "your-api-key"},
    
    # Default governance attributes
    default_team="ai-platform",
    default_project="customer-chat"
)

# 2. Your existing AI code gets automatic governance
import openai
client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
# ✅ Cost, tokens, model, team, project automatically tracked!

# 3. Check what's being tracked
status = genops.status()
print(f"Instrumented providers: {status['instrumented_providers']}")
print(f"Default attributes: {status['default_attributes']}")
```

**That's it!** Your AI operations now emit governance telemetry to your existing observability infrastructure.

---

## 📖 **Core Concepts**

### **Governance Semantics**
GenOps extends OpenTelemetry with standardized governance attributes:

- **`genops.cost.*`** - Cost attribution and financial tracking
- **`genops.policy.*`** - Policy enforcement results and violations  
- **`genops.eval.*`** - Quality, safety, and performance evaluations
- **`genops.budget.*`** - Spend tracking and limit management

### **Provider Adapters** 
Pre-built integrations with accurate cost models:

- ✅ **OpenAI** (GPT-3.5, GPT-4, GPT-4-turbo) with per-token pricing
- ✅ **Anthropic** (Claude-3 Sonnet, Opus, Haiku) with accurate costs
- 🚧 **AWS Bedrock** (coming soon)
- 🚧 **Google Gemini** (coming soon)
- 🚧 **LangChain** (coming soon) 
- 🚧 **LlamaIndex** (coming soon)

### **Observability Stack Integration**
Works with your existing tools:

- 📊 **Datadog, Honeycomb, New Relic** - OTLP export
- 📈 **Grafana Tempo, Jaeger** - Distributed tracing
- 🔍 **Elasticsearch, Splunk** - Log aggregation
- ☁️ **AWS X-Ray, Google Cloud Trace** - Cloud-native tracing

---

## 🏗️ **Architecture**

```mermaid
graph TB
    A[Your AI Application] --> B[GenOps AI SDK]
    B --> C[OpenTelemetry]
    C --> D[Your Observability Stack]
    
    B --> E[Provider Adapters]
    E --> F[OpenAI/Anthropic/Bedrock...]
    
    D --> G[Dashboards & Alerts]
    D --> H[Cost Attribution]  
    D --> I[Policy Automation]
    D --> J[Koshi Control Plane]
    
    style B fill:#e1f5fe
    style D fill:#f3e5f5
    style J fill:#fff3e0
```

**GenOps AI sits alongside OpenLLMetry** in your telemetry stack, adding the governance layer that turns observability data into business accountability.

---

## 🎭 **Usage Examples**

### **Multi-Provider Cost Attribution**
```python
import genops

# Initialize with default governance context
genops.init(default_team="ai-research", default_project="multimodal")

# Use different providers - all automatically tracked
import openai
import anthropic

# OpenAI for quick tasks
openai_response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Summarize this"}],
    # Inherits team/project, adds specific context
    customer_id="enterprise_123", 
    feature="document_summary"
)

# Anthropic for complex reasoning
anthropic_client = anthropic.Anthropic()
claude_response = anthropic_client.messages.create(
    model="claude-3-opus-20240229", 
    max_tokens=2048,
    messages=[{"role": "user", "content": "Analyze this data"}],
    # Different feature, same customer
    customer_id="enterprise_123",
    feature="data_analysis"  
)

# All operations tagged with cost, provider, customer, feature
# Perfect for FinOps dashboards and customer billing
```

### **Policy-Driven Governance**
```python
import genops
from genops import register_policy, PolicyResult

# Set up governance policies
register_policy("cost_limit", max_cost=10.0, enforcement_level=PolicyResult.BLOCKED)
register_policy("content_safety", blocked_patterns=["violence"], enforcement_level=PolicyResult.WARNING)
register_policy("team_budget", max_monthly_spend=5000, enforcement_level=PolicyResult.RATE_LIMITED)

# Apply policies to operations
@genops.enforce_policy(["cost_limit", "content_safety"])
def generate_content(prompt: str, customer_tier: str):
    if customer_tier == "enterprise":
        model = "gpt-4"  # Higher cost, policy will check
    else:
        model = "gpt-3.5-turbo"
        
    return call_ai_model(model, prompt)

# Automatic policy evaluation + telemetry
try:
    result = generate_content("Write a story", "enterprise") 
    # ✅ Allowed: cost under $10, content safe
except genops.PolicyViolationError as e:
    # ❌ Blocked: policy violation with detailed context
    logger.warning(f"Policy {e.policy_name}: {e.reason}")
```

### **Custom Evaluations & Compliance**
```python
import genops

@genops.track_usage(operation_name="content_moderation")
def moderate_content(text: str):
    with genops.track("ai_safety_check") as span:
        # Your content moderation logic
        safety_score = run_safety_model(text)
        toxicity_score = check_toxicity(text)
        
        # Record compliance metrics
        span.record_evaluation("safety", safety_score, threshold=0.8)
        span.record_evaluation("toxicity", toxicity_score, threshold=0.2) 
        
        # Policy decision
        if safety_score > 0.8 and toxicity_score < 0.2:
            span.record_policy("content_policy", "approved")
            return {"approved": True, "reason": "Content meets safety standards"}
        else:
            span.record_policy("content_policy", "rejected", reason="Safety threshold not met")
            return {"approved": False, "reason": "Content violates policy"}

# Rich governance telemetry for audit trails
```

### **Budget Tracking & Alerts**  
```python
import genops

def process_customer_requests(customer_id: str, requests: list):
    # Track budget utilization per customer
    with genops.track(f"customer_{customer_id}_processing") as span:
        total_cost = 0
        
        for request in requests:
            response = process_with_ai(request)
            request_cost = calculate_cost(response)
            total_cost += request_cost
            
        # Update customer budget tracking
        customer_budget = get_customer_budget(customer_id)
        remaining = customer_budget.limit - customer_budget.used - total_cost
        
        span.record_budget(
            budget_name=f"customer_{customer_id}_monthly",
            allocated=customer_budget.limit,
            consumed=customer_budget.used + total_cost, 
            remaining=remaining
        )
        
        # Automatic alerts when budget utilization > 80%
        if remaining / customer_budget.limit < 0.2:
            span.record_policy("budget_warning", "triggered", 
                             reason=f"Customer {customer_id} at 80% budget utilization")
```

---

## 🏢 **Enterprise & Production**

### **Compliance & Audit Trails**
GenOps AI automatically creates detailed audit logs for:
- **Cost attribution** with exact token counts and pricing models
- **Policy decisions** with enforcement context and reasoning
- **Data flow tracking** for privacy and compliance requirements  
- **Model usage patterns** for governance and risk management

### **FinOps Integration**
Perfect for financial operations teams:
- **Per-customer cost allocation** for accurate billing
- **Department/team spend tracking** for budget management
- **Feature-level cost analysis** for product decisions
- **Model efficiency metrics** for optimization opportunities

### **Integration with Koshi**
GenOps AI telemetry feeds into **[Koshi](https://getkoshi.ai)** - the commercial control plane for enterprise AI governance:
- **Real-time dashboards** for executives and compliance teams
- **Automated policy management** across multiple teams and projects  
- **Advanced analytics** for cost optimization and risk management
- **Enterprise SSO and RBAC** for governance at scale

---

## 🤝 **Community & Support**

### **Contributing**
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup and testing guidelines
- Code standards and review process
- Community guidelines and code of conduct

### **Getting Help**
- 📖 **Documentation**: [docs.genopsai.org](https://docs.genopsai.org)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/KoshiHQ/GenOps-AI/issues)
- 📧 **Email**: [hello@genopsai.org](mailto:hello@genopsai.org)

### **Roadmap**
See our [public roadmap](https://github.com/KoshiHQ/GenOps-AI/projects) for upcoming features:
- 🚧 AWS Bedrock and Google Gemini adapters
- 🚧 LangChain and LlamaIndex integrations  
- 🚧 OpenTelemetry Collector processors for real-time governance
- 🚧 Pre-built dashboards for major observability platforms

---

## 📄 **License**

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

---

## 🌟 **Why GenOps AI?**

**Traditional AI monitoring tells you what happened. GenOps AI tells you what it cost, who did it, whether it should have been allowed, and how well it worked.**

- **For DevOps Teams**: Integrate AI governance into existing observability workflows
- **For FinOps Teams**: Get precise cost attribution and budget controls
- **For Compliance Teams**: Automated policy enforcement with audit trails
- **For Product Teams**: Feature-level AI cost analysis and optimization insights
- **For Executives**: Enterprise-wide AI governance visibility and control

**Start with the open-source GenOps AI SDK. Scale with the Koshi commercial control plane.**

---

<div align="center">
  <p><strong>Ready to bring governance to your AI systems?</strong></p>
  
  ```bash
  pip install genops
  ```
  
  <p>⭐ <strong>Star us on GitHub</strong> if you find GenOps AI useful!</p>
  
  [![GitHub stars](https://img.shields.io/github/stars/KoshiHQ/GenOps-AI?style=social)](https://github.com/KoshiHQ/GenOps-AI/stargazers)
</div>