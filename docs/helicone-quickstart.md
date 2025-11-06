# Helicone AI Gateway Integration - 5-Minute Quickstart

**🎯 Get GenOps tracking for 100+ AI models through unified gateway in 5 minutes**

This guide gets you from zero to tracking multi-provider AI costs and performance with GenOps through Helicone AI gateway in under 5 minutes, featuring unified access to OpenAI, Anthropic, Vertex, Groq, and more.

---

## 🚀 Prerequisites (30 seconds)

**Before you start, make sure you have:**

1. **Helicone API key**
   ```bash
   # Get your API key from https://app.helicone.ai/
   export HELICONE_API_KEY="your-helicone-api-key-here"
   ```

2. **At least one provider API key**
   ```bash
   # OpenAI (recommended for quickstart)
   export OPENAI_API_KEY="your-openai-api-key"
   
   # Or Anthropic
   export ANTHROPIC_API_KEY="your-anthropic-api-key"
   
   # Or Groq (free tier available)
   export GROQ_API_KEY="your-groq-api-key"
   ```

3. **Install requests library** (if not already installed)
   ```bash
   pip install requests
   ```

4. **Verify gateway access**
   ```bash
   curl -H "Helicone-Auth: Bearer $HELICONE_API_KEY" https://ai-gateway.helicone.ai/v1/health
   ```

---

## ⚡ Quick Setup (2 minutes)

### Step 1: Install GenOps (30 seconds)
```bash
pip install genops[helicone]
```

### Step 2: Verify Setup (30 seconds)
Run this validation script to check everything is working:

```python
from genops.providers.helicone_validation import validate_setup, print_validation_result

# Check your Helicone + providers setup
result = validate_setup()
print_validation_result(result)
```

You should see: ✅ **Overall Status: PASSED**

### Step 3: Test Gateway Tracking (60 seconds)
Create this minimal test file:

```python
# test_helicone_genops.py
from genops.providers.helicone import instrument_helicone

# Enable GenOps tracking for AI gateway (zero code changes needed!)
adapter = instrument_helicone(
    helicone_api_key="your-helicone-key",  # Or use env var
    provider_keys={
        "openai": "your-openai-key"  # Or use env vars
    },
    team="ai-team", 
    project="quickstart-test"
)

print("🚀 Testing AI gateway with GenOps tracking...")

# Access any provider through unified interface
response = adapter.chat(
    message="What are the benefits of AI gateways?",
    provider="openai",
    model="gpt-3.5-turbo"
)

print(f"📝 Response: {response.content[:100]}...")
print(f"💰 Provider cost: ${response.usage.provider_cost:.6f}")
print(f"🌐 Gateway cost: ${response.usage.helicone_cost:.6f}")
print(f"📊 Total cost: ${response.usage.total_cost:.6f}")
print("✅ SUCCESS! GenOps is now tracking your AI gateway usage")
```

**Run it:**
```bash
python test_helicone_genops.py
```

**Expected output:**
```
🚀 Testing AI gateway with GenOps tracking...
📝 Response: AI gateways provide unified access to multiple AI providers, enabling cost optimization...
💰 Provider cost: $0.000075
🌐 Gateway cost: $0.000001
📊 Total cost: $0.000076
✅ SUCCESS! GenOps is now tracking your AI gateway usage
```

---

## 🎯 What Just Happened?

**GenOps automatically tracked:**
- ✅ **Multi-provider costs** (provider costs + gateway fees with precise pricing)
- ✅ **Unified operations** (access 100+ models through single interface)
- ✅ **Gateway intelligence** (routing, failover, and optimization insights)
- ✅ **Team attribution** (costs attributed to "ai-team" and "quickstart-test")
- ✅ **Provider comparison** (cost and performance across providers)

**All with zero changes to your AI workflow - just route through the gateway!**

---

## 📊 See Your Data (1 minute)

### Option 1: Multi-Provider Access
```python
from genops.providers.helicone import instrument_helicone

adapter = instrument_helicone(
    team="analytics-team",
    provider_keys={
        "openai": "your-openai-key",
        "anthropic": "your-anthropic-key"
    }
)

# Same interface, different providers
openai_response = adapter.chat(message="Hello from OpenAI", provider="openai", model="gpt-3.5-turbo")
anthropic_response = adapter.chat(message="Hello from Anthropic", provider="anthropic", model="claude-3-haiku-20240307")

print(f"🤖 OpenAI cost: ${openai_response.usage.total_cost:.6f}")
print(f"🧠 Anthropic cost: ${anthropic_response.usage.total_cost:.6f}")
```

### Option 2: Intelligent Multi-Provider Routing
```python
from genops.providers.helicone import instrument_helicone

adapter = instrument_helicone(team="routing-team")

# Let the gateway choose the best provider automatically
response = adapter.multi_provider_chat(
    message="Explain machine learning briefly",
    providers=["openai", "anthropic", "groq"],
    model_preferences={
        "openai": "gpt-3.5-turbo",
        "anthropic": "claude-3-haiku-20240307", 
        "groq": "llama3-8b-8192"
    },
    routing_strategy="cost_optimized"  # or "performance_optimized"
)

print(f"🎯 Selected provider: {response.primary_response.provider}")
print(f"💡 Routing decision: {response.routing_decision}")
print(f"💰 Cost comparison: {response.cost_comparison}")
print(f"⚡ Performance metrics: {response.performance_metrics}")
```

### Option 3: Gateway Usage Summary
```python
# Get comprehensive gateway usage summary
summary = adapter.get_usage_summary()
print(f"🌐 Gateway operations: {summary['total_operations']}")
print(f"💰 Total cost: ${summary['total_cost']:.6f}")
print(f"🔀 Providers used: {', '.join(summary['providers_used'])}")
print(f"📊 Routing decisions: {summary.get('routing_decisions', 0)}")
```

---

## 🏗️ Next Steps (Your Choice!)

**✅ You now have GenOps tracking all your AI gateway operations!**

**Choose your next adventure:**

### 🎯 **30-Second Next Step: Try More Providers**
```python
# Add more providers to your gateway
from genops.providers.helicone import instrument_helicone

adapter = instrument_helicone(
    team="research",
    provider_keys={
        "openai": "your-openai-key",
        "anthropic": "your-anthropic-key",
        "groq": "your-groq-key",      # Often free tier available
        "together": "your-together-key"  # Open source models
    }
)

providers = ["openai", "anthropic", "groq", "together"]
prompt = "Compare yourself to other AI models in one sentence"

for provider in providers:
    model = {"openai": "gpt-3.5-turbo", "anthropic": "claude-3-haiku-20240307", 
             "groq": "llama3-8b-8192", "together": "meta-llama/Llama-2-7b-chat-hf"}[provider]
    
    response = adapter.chat(message=prompt, provider=provider, model=model)
    print(f"🤖 {provider}: ${response.usage.total_cost:.6f} - {response.content[:80]}...")
```

### 🚀 **5-Minute Next Step: Cost Optimization**
```python
# Automatic cost optimization with routing
from genops.providers.helicone import instrument_helicone, RoutingStrategy

adapter = instrument_helicone(team="optimization")

# Test different routing strategies
strategies = [
    RoutingStrategy.COST_OPTIMIZED,
    RoutingStrategy.PERFORMANCE_OPTIMIZED,
    RoutingStrategy.QUALITY_OPTIMIZED
]

for strategy in strategies:
    response = adapter.multi_provider_chat(
        message="Write a professional email subject line",
        providers=["openai", "anthropic", "groq"],
        model_preferences={
            "openai": "gpt-3.5-turbo",
            "anthropic": "claude-3-haiku-20240307",
            "groq": "llama3-8b-8192"
        },
        routing_strategy=strategy
    )
    
    print(f"📋 Strategy {strategy.value}:")
    print(f"   Selected: {response.primary_response.provider}")
    print(f"   Cost: ${response.primary_response.usage.total_cost:.6f}")
    print(f"   Performance: {response.primary_response.usage.request_time:.2f}s")
```

### 📚 **15-Minute Next Step: Complete Integration**
- **[Complete Helicone Integration Guide](./integrations/helicone.md)** - Full reference documentation
- **[All Helicone Examples](../examples/helicone/)** - Progressive complexity tutorials
- **[Multi-Provider Cost Analysis](../examples/helicone/multi_provider_costs.py)** - Advanced routing and optimization

---

## 🆘 Troubleshooting

**Getting errors? Here are quick fixes:**

### ❌ "Invalid Helicone API key" or "Unauthorized"
```bash
# Make sure your Helicone API key is set correctly
echo $HELICONE_API_KEY
# Should show your key (not empty)

# Or set it in Python
import os
os.environ["HELICONE_API_KEY"] = "your-helicone-api-key"

# Get your key from: https://app.helicone.ai/
```

### ❌ "No provider API keys configured"
```bash
# Configure at least one provider
export OPENAI_API_KEY="your-openai-key"
# OR
export ANTHROPIC_API_KEY="your-anthropic-key" 
# OR
export GROQ_API_KEY="your-groq-key"  # Often has free tier

# Verify providers are configured
python -c "
import os
providers = ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'GROQ_API_KEY']
configured = [p for p in providers if os.getenv(p)]
print(f'Configured providers: {configured}')
"
```

### ❌ "Gateway connectivity failed"
```bash
# Test gateway connectivity directly
curl -H "Helicone-Auth: Bearer $HELICONE_API_KEY" \
     https://ai-gateway.helicone.ai/v1/health

# Should return 200 OK
```

### ❌ "Requests library not found"
```bash
# Install requests library
pip install requests

# Verify installation
python -c "import requests; print('✅ Requests available')"
```

**Still stuck?** Run the diagnostic:
```python
from genops.providers.helicone_validation import validate_setup, print_validation_result
result = validate_setup(include_performance_tests=True)
print_validation_result(result, detailed=True)
```

---

## 💡 Key Advantages of AI Gateways

**Helicone gateway tracking is optimized for multi-provider intelligence:**

| Aspect | Direct Provider Integration | AI Gateway (Helicone) |
|--------|---------------------------|----------------------|
| **Provider Access** | Single provider per integration | 100+ models through unified API |
| **Cost Optimization** | Manual provider comparison | Automatic routing and optimization |
| **Failover** | Manual failover logic | Built-in provider failover |
| **Observability** | Separate tracking per provider | Unified analytics across providers |
| **Vendor Lock-in** | Tied to specific provider APIs | Provider-agnostic with easy switching |

**That's why GenOps Helicone integration focuses on:**
- 🌐 **Unified Multi-Provider Access** (OpenAI, Anthropic, Vertex, Groq, Together, Cohere)
- 🎯 **Intelligent Routing** (cost, performance, and quality optimization)
- 📊 **Comprehensive Analytics** (cross-provider comparison and insights)
- 🔄 **Zero Vendor Lock-in** (switch providers without code changes)

---

## 🎉 Success!

**🎯 In 5 minutes, you've accomplished:**
- ✅ Set up GenOps tracking for Helicone AI gateway operations
- ✅ Automatically tracked costs across multiple AI providers
- ✅ Attributed costs to teams and projects with gateway intelligence
- ✅ Accessed 100+ models through unified interface
- ✅ Got insights into cross-provider performance and cost optimization

**Your AI operations now have enterprise-grade governance with multi-provider intelligence!**

**🚀 Ready for more advanced features?** Check out:
- **[Multi-Provider Examples](../examples/helicone/)**
- **[Cost Optimization Strategies](../examples/helicone/multi_provider_optimization.py)**
- **[Complete Integration Guide](../docs/integrations/helicone.md)**

---

**Questions? Issues?** 
- 📝 [Create an issue](https://github.com/KoshiHQ/GenOps-AI/issues)
- 💬 [Join discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)
- 🌐 [AI Gateway Community](https://github.com/KoshiHQ/GenOps-AI/discussions/categories/ai-gateways)