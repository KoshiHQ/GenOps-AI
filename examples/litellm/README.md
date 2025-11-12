# LiteLLM + GenOps: Unified Governance for 100+ LLM Providers

The **highest-leverage GenOps integration** - single instrumentation layer providing comprehensive governance telemetry across the entire LLM ecosystem through LiteLLM's unified interface.

## 🎯 Strategic Value

**Why LiteLLM + GenOps is game-changing:**
- **Single Integration → Massive Coverage**: One GenOps integration covers 100+ LLM providers
- **Provider-Agnostic Governance**: Unified cost tracking, budgets, and compliance across all providers
- **Zero Vendor Lock-in**: Switch providers seamlessly while maintaining governance
- **Ecosystem Multiplier**: GenOps scales with every new LiteLLM provider addition

**Supported Providers** (100+):
OpenAI, Anthropic, Azure, VertexAI, AWS Bedrock, Google Gemini, Cohere, HuggingFace, Ollama, Together, Replicate, Mistral, Fireworks, Perplexity, Anyscale, DeepInfra, and many more.

## 🚀 Quick Start (2 Minutes)

### Prerequisites
```bash
pip install litellm genops[litellm]
export OPENAI_API_KEY="your_key_here"  # Or any other provider
```

### Zero-Code Integration
```python
import litellm
from genops.providers.litellm import auto_instrument

# Enable GenOps governance across ALL providers
auto_instrument(
    team="your-team",
    project="your-project"
)

# Use LiteLLM normally - governance added automatically!
response = litellm.completion(
    model="gpt-4",  # Or claude-3, gemini-pro, any of 100+ models
    messages=[{"role": "user", "content": "Hello!"}]
)
# ✅ Cost tracking, team attribution, and compliance monitoring added!
```

## 📚 Examples Overview

### **🟢 Foundation (5-10 minutes)**
- **`setup_validation.py`** - Comprehensive environment validation with actionable fixes
- **`auto_instrumentation.py`** - Zero-code instrumentation demo across multiple providers
- **`basic_tracking.py`** - Manual tracking patterns and context managers

### **🔵 Cost Optimization (15-30 minutes)**  
- **`multi_provider_costs.py`** - Multi-provider cost comparison and optimization engine
- **`cost_optimization.py`** - Advanced cost reduction strategies and intelligent model selection
- **`budget_management.py`** - Budget controls, spending limits, and financial governance

### **🟡 Production & Enterprise (30-60 minutes)**
- **`production_patterns.py`** - Enterprise deployment patterns and scaling strategies  
- **`performance_optimization.py`** - Latency optimization and intelligent provider routing
- **`compliance_monitoring.py`** - Audit trails and governance automation

## 🎮 Running Examples

### **Always Start Here**
```bash
python setup_validation.py
```
This validates your entire setup and provides specific fixes for any issues.

### **Progressive Learning Path**

#### **🟢 Foundation (15 minutes total)**
```bash
# Zero-code instrumentation across providers
python auto_instrumentation.py

# Manual tracking for fine control
python basic_tracking.py
```

#### **🔵 Cost Intelligence (45 minutes total)**
```bash
# Multi-provider cost comparison and optimization
python multi_provider_costs.py

# Advanced cost reduction strategies
python cost_optimization.py

# Budget controls and financial governance
python budget_management.py
```

#### **🟡 Production Ready (90 minutes total)**
```bash
# Enterprise deployment patterns and scaling
python production_patterns.py

# Performance optimization and intelligent routing
python performance_optimization.py

# Compliance monitoring and governance automation
python compliance_monitoring.py
```

## 🔧 Key Integration Patterns

### Zero-Code Auto-Instrumentation
```python
from genops.providers.litellm import auto_instrument

# Enable governance across ALL 100+ providers
auto_instrument(
    team="ai-team",
    project="multi-provider-app",
    daily_budget_limit=500.0,
    governance_policy="enforced"  # or "advisory"
)

# All LiteLLM requests now tracked!
```

### Manual Context Management
```python
from genops.providers.litellm import track_completion

with track_completion("gpt-4", team="research") as context:
    response = litellm.completion(
        model="gpt-4",
        messages=[{"role": "user", "content": "Research query"}]
    )
    print(f"Cost: ${context.cost}, Tokens: {context.tokens}")
```

### Multi-Provider Cost Optimization
```python
from genops.providers.litellm import get_cost_summary

# Get cost breakdown by provider
summary = get_cost_summary(group_by="provider")
print(f"OpenAI: ${summary['cost_by_provider']['openai']:.4f}")
print(f"Anthropic: ${summary['cost_by_provider']['anthropic']:.4f}")

# Optimize based on cost per token
cheapest_provider = min(summary['cost_by_provider'], 
                       key=summary['cost_by_provider'].get)
```

### Enterprise Governance
```python
# Production configuration with advanced governance  
auto_instrument(
    team="production-ai",
    project="customer-service",
    environment="production",
    customer_id="enterprise-123",
    daily_budget_limit=1000.0,
    governance_policy="enforced",
    
    # Custom attributes for compliance
    cost_center="engineering",
    feature="chat-support",
    compliance_level="sox"
)
```

## 🌟 GenOps Value-Add to LiteLLM

LiteLLM provides the unified interface, GenOps adds enterprise governance:

| Feature | LiteLLM | LiteLLM + GenOps |
|---------|---------|------------------|
| **Provider Coverage** | 100+ providers | ✅ Same + governance |
| **Cost Tracking** | Basic built-in | ✅ Enhanced with attribution |
| **Team Attribution** | None | ✅ Team/project/customer tracking |
| **Budget Controls** | None | ✅ Limits and alerts |
| **Compliance** | None | ✅ Audit trails and policies |
| **OpenTelemetry** | None | ✅ Standard telemetry export |
| **Observability** | Basic | ✅ Rich dashboards integration |

## 🏗️ Architecture Benefits

### Single Point of Control
```
Your Application
       ↓
   GenOps LiteLLM Integration (1 integration)
       ↓  
   LiteLLM Unified Interface
       ↓
100+ LLM Providers (OpenAI, Anthropic, Google, etc.)
```

**vs. Traditional Approach:**
```
Your Application
  ↓   ↓   ↓   ↓
OpenAI Anthropic Google Azure (N integrations)
```

### Governance Layer
- **Cost Attribution**: Every request tagged with team/project/customer
- **Budget Enforcement**: Spending limits with configurable policies
- **Compliance Monitoring**: Audit trails and governance automation
- **Performance Tracking**: Latency and error rate monitoring
- **Provider Intelligence**: Cost optimization recommendations

## 📊 Real-World Impact

### Cost Optimization Example
```python
# Before: Manual provider management
if budget_remaining > expensive_threshold:
    model = "gpt-4"  # Expensive but powerful
else:
    model = "gpt-3.5-turbo"  # Cheaper alternative

# After: Automated with GenOps
auto_instrument(
    daily_budget_limit=100.0,
    governance_policy="enforced"  # Automatic fallback
)
# GenOps automatically manages cost optimization across ALL providers
```

### Multi-Tenant Usage  
```python
# Track costs per customer across all providers
for customer in customers:
    auto_instrument(
        team="customer-service",
        customer_id=customer.id,
        daily_budget_limit=customer.budget_limit
    )
    
    # LiteLLM calls now attributed to specific customer
    response = litellm.completion(...)
```

## 🔍 Troubleshooting

### Quick Diagnostics
```bash
python setup_validation.py --quick
```

### Common Issues

**No API Keys Configured**
```bash
# Solution: Set at least one provider key
export OPENAI_API_KEY="sk-..."
# OR
export ANTHROPIC_API_KEY="sk-ant-..."
# OR any of 100+ other providers
```

**LiteLLM Not Found**
```bash
pip install litellm
```

**GenOps Integration Missing**
```bash
pip install genops[litellm]
```

**Callback System Issues**
- Update LiteLLM: `pip install --upgrade litellm`
- Check callback support in your LiteLLM version

### Performance Tuning
```python
# For high-volume applications
auto_instrument(
    sampling_rate=0.1,  # Track 10% of requests
    enable_cost_tracking=True,  # Keep cost tracking
    governance_policy="advisory"  # Reduce overhead
)
```

## 🚀 Next Steps

1. **Start Simple**: Run `auto_instrumentation.py` to see immediate value
2. **Optimize Costs**: Explore `multi_provider_costs.py` for savings opportunities  
3. **Scale Production**: Implement patterns from `production_patterns.py`
4. **Integrate**: Add GenOps to your existing LiteLLM applications

## 📖 Additional Resources

- **LiteLLM Documentation**: [docs.litellm.ai](https://docs.litellm.ai/)
- **Provider Setup Guides**: [Provider-specific configuration](https://docs.litellm.ai/docs/providers)
- **GenOps Architecture**: [OpenTelemetry integration patterns](../../README.md)

---

**The highest-leverage AI governance integration available.** 🚀

Single instrumentation → Ecosystem-wide governance → Massive operational intelligence.