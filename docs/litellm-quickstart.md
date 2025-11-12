# LiteLLM + GenOps: 5-Minute Quickstart

**Get governance across 100+ LLM providers in under 5 minutes.**

The highest-leverage GenOps integration - single instrumentation layer providing comprehensive cost tracking, team attribution, and compliance monitoring across the entire LLM ecosystem.

## ⚡ Prerequisites (30 seconds)

```bash
pip install litellm genops[litellm]
export OPENAI_API_KEY="your_openai_key_here"
```

**Don't have an OpenAI key?** Use any of 100+ providers: Anthropic, Google, Azure, Cohere, etc. [See all providers →](https://docs.litellm.ai/docs/providers)

## 🚀 Zero-Code Integration (2 minutes)

Copy and paste this complete working example:

```python
#!/usr/bin/env python3
"""
LiteLLM + GenOps: Zero-Code Quickstart
Run this file directly to see governance in action across 100+ providers.
"""

# Step 1: Import and enable governance (2 lines)
import litellm
from genops.providers.litellm import auto_instrument

# Step 2: Enable GenOps governance across ALL providers (3 lines)
auto_instrument(
    team="quickstart-team",
    project="litellm-demo"
)

# Step 3: Use LiteLLM normally - governance added automatically!
print("🚀 Testing LiteLLM + GenOps integration...")

# Your existing LiteLLM code works unchanged
response = litellm.completion(
    model="gpt-3.5-turbo",  # Or claude-3, gemini-pro, any of 100+ models
    messages=[{"role": "user", "content": "What is LiteLLM in one sentence?"}],
    max_tokens=50
)

print(f"✅ Response: {response.choices[0].message.content}")

# Step 4: See your governance data
from genops.providers.litellm import get_usage_stats
stats = get_usage_stats()

print(f"\n📊 Governance Results:")
print(f"   💰 Cost: ${stats['total_cost']:.6f}")
print(f"   🎫 Tokens: {stats['total_tokens']}")
print(f"   👥 Team: quickstart-team")
print(f"   📁 Project: litellm-demo")
print(f"   ✅ Governance active across 100+ providers!")
```

**Save as `quickstart.py` and run:**

```bash
python quickstart.py
```

**Expected output:**
```
🚀 Testing LiteLLM + GenOps integration...
✅ Response: LiteLLM is a unified interface that standardizes API calls across 100+ language model providers.

📊 Governance Results:
   💰 Cost: $0.000123
   🎫 Tokens: 73
   👥 Team: quickstart-team
   📁 Project: litellm-demo
   ✅ Governance active across 100+ providers!
```

## 🎯 What Just Happened? (1 minute)

**With just 2 lines of code**, you added enterprise-grade governance to LiteLLM:

✅ **Cost Tracking**: Real-time cost calculation across all 100+ providers  
✅ **Team Attribution**: Every request tagged with team/project/customer  
✅ **Multi-Provider Support**: Switch providers seamlessly with governance maintained  
✅ **OpenTelemetry Export**: Standard telemetry for your observability stack  
✅ **Budget Controls**: Built-in spending limits and governance policies

**This is different from other solutions because:**
- **Zero Code Changes**: Your existing LiteLLM code keeps working exactly as before
- **Provider-Agnostic**: Governance works the same whether you use OpenAI, Anthropic, Google, or any of 100+ providers
- **OpenTelemetry Native**: Standard telemetry that works with your existing monitoring stack  

## 🔧 Quick Customization (1 minute)

**Need more providers?** Add API keys and they work automatically:

```bash
export ANTHROPIC_API_KEY="your_anthropic_key"
export GOOGLE_API_KEY="your_google_key"
# Any of 100+ providers...
```

**Need team/customer attribution?**

```python
auto_instrument(
    team="production-ai",
    project="customer-service",
    customer_id="enterprise-123",
    daily_budget_limit=500.0
)
```

**Need different models?** Change one line:

```python
# OpenAI
response = litellm.completion(model="gpt-4", messages=[...])

# Anthropic  
response = litellm.completion(model="claude-3-sonnet", messages=[...])

# Google
response = litellm.completion(model="gemini-pro", messages=[...])

# Any of 100+ models - governance tracks them all!
```

## 📊 Instant Validation

Verify everything works:

```bash
cd examples/litellm
python setup_validation.py
```

This validates your environment and provides specific fixes for any issues.

## 🚨 Troubleshooting (30 seconds)

**Most issues are quick fixes. Here's how to solve the common ones:**

**❌ Error: "LiteLLM not found"**
```bash
pip install litellm
```

**❌ Error: "GenOps LiteLLM provider not available"** 
```bash
pip install genops[litellm]
```

**❌ Error: "API key not configured"**
```bash
export OPENAI_API_KEY="sk-your-key"
# OR use any other provider - see https://docs.litellm.ai/docs/providers
```

**❌ Still having issues?** Run our diagnostic tool:
```bash
python examples/litellm/setup_validation.py --quick
```
This will identify exactly what's wrong and provide specific fixes.

## 🎉 Success! What's Next?

🎊 **Congratulations!** You now have enterprise-grade governance across 100+ LLM providers with just 2 lines of code.

**Your AI operations are now:**
- 👀 **Visible**: See exactly what each team/project is spending across all providers
- 💰 **Controlled**: Built-in budget limits and governance policies
- 📊 **Trackable**: Standard OpenTelemetry data flowing to your observability stack
- 🔄 **Flexible**: Switch providers anytime while keeping the same governance

**Ready to explore more?** Here are your next steps:

### **🟢 Next 15 minutes: Explore Examples**
```bash
cd examples/litellm

# Zero-code instrumentation demo
python auto_instrumentation.py

# Manual tracking patterns  
python basic_tracking.py
```

### **🔵 Next 30 minutes: Cost Intelligence**
```bash
# Multi-provider cost comparison  
python multi_provider_costs.py

# Advanced cost optimization and model selection
python cost_optimization.py

# Budget controls and management
python budget_management.py
```

### **🟡 Next 60 minutes: Production Ready**
```bash
# Enterprise deployment patterns
python production_patterns.py

# Performance optimization and intelligent routing
python performance_optimization.py

# Compliance monitoring and audit trails
python compliance_monitoring.py
```

## 📖 Complete Documentation

- **[Full Integration Guide →](../integrations/litellm.md)** - Complete API reference and advanced patterns
- **[All Examples →](../../examples/litellm/)** - 7 progressive examples from basic to enterprise
- **[LiteLLM Providers →](https://docs.litellm.ai/docs/providers)** - Complete list of 100+ supported providers

---

**🌟 The Highest-Leverage GenOps Integration**

Single instrumentation → Governance across 100+ providers → Unified AI operations intelligence.

**Questions?** Check our [troubleshooting guide](../integrations/litellm.md#troubleshooting) or [integration examples](../../examples/litellm/).