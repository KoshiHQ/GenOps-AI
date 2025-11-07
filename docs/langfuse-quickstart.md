# Langfuse LLM Observability Integration - 5-Minute Quickstart

**🎯 Add GenOps governance to Langfuse observability in 5 minutes**

This guide gets you from zero to comprehensive LLM governance + observability with GenOps and Langfuse in under 5 minutes, featuring advanced tracing, evaluation tracking, and cost intelligence.

---

## 🚀 Prerequisites (30 seconds)

**Before you start, make sure you have:**

1. **Langfuse account and API keys**
   ```bash
   # Get your API keys from https://cloud.langfuse.com/
   export LANGFUSE_PUBLIC_KEY="pk-lf-your-public-key-here"
   export LANGFUSE_SECRET_KEY="sk-lf-your-secret-key-here"
   export LANGFUSE_BASE_URL="https://cloud.langfuse.com"  # Optional: for self-hosted
   ```

2. **At least one AI provider API key**
   ```bash
   # OpenAI (recommended for quickstart)
   export OPENAI_API_KEY="your-openai-api-key"
   
   # Or Anthropic
   export ANTHROPIC_API_KEY="your-anthropic-api-key"
   ```

3. **Verify Langfuse connectivity** (optional)
   ```bash
   curl -H "Authorization: Bearer $LANGFUSE_PUBLIC_KEY" \
        "$LANGFUSE_BASE_URL/api/public/health"
   ```

---

## ⚡ Quick Setup (2 minutes)

### Step 1: Install GenOps with Langfuse (30 seconds)
```bash
pip install genops[langfuse]
```

### Step 2: Verify Setup (30 seconds)
Run this validation script to check everything is working:

```python
from genops.providers.langfuse_validation import validate_setup, print_validation_result

# Check your Langfuse + GenOps setup
result = validate_setup()
print_validation_result(result)
```

You should see: ✅ **Overall Status: PASSED**

### Step 3: Test Enhanced Observability (60 seconds)
Create this minimal test file:

```python
# test_langfuse_genops.py
from genops.providers.langfuse import instrument_langfuse

# Enable GenOps governance for Langfuse observability
adapter = instrument_langfuse(
    langfuse_public_key="your-langfuse-public-key",  # Or use env var
    langfuse_secret_key="your-langfuse-secret-key",  # Or use env var
    team="ai-team", 
    project="quickstart-test",
    environment="development"
)

print("🚀 Testing Langfuse with GenOps governance...")

# Enhanced tracing with cost attribution
with adapter.trace_with_governance(
    name="quickstart_demo",
    customer_id="demo-customer",
    cost_center="engineering"
) as trace:
    
    # LLM generation with cost tracking and governance
    response = adapter.generation_with_cost_tracking(
        prompt="What are the benefits of LLM observability?",
        model="gpt-3.5-turbo",
        max_cost=0.05  # Budget enforcement
    )
    
    print(f"📝 Response: {response.content[:100]}...")
    print(f"💰 Cost: ${response.usage.cost:.6f}")
    print(f"📊 Team: {response.usage.team}")
    print(f"🎯 Project: {response.usage.project}")
    print(f"⏱️  Latency: {response.usage.latency_ms:.1f}ms")

print("✅ SUCCESS! GenOps governance is now tracking your Langfuse operations")
```

**Run it:**
```bash
python test_langfuse_genops.py
```

**Expected output:**
```
🚀 Testing Langfuse with GenOps governance...
📝 Response: LLM observability provides comprehensive insights into model performance, cost optimization...
💰 Cost: $0.000024
📊 Team: ai-team
🎯 Project: quickstart-test
⏱️  Latency: 847.3ms
✅ SUCCESS! GenOps governance is now tracking your Langfuse operations
```

---

## 🎯 What Just Happened?

**GenOps automatically enhanced Langfuse with:**
- ✅ **Cost Intelligence** (precise cost tracking with team/project attribution)
- ✅ **Budget Enforcement** (max_cost limits with automatic policy compliance)
- ✅ **Governance Attribution** (team, project, customer_id propagation to all traces)
- ✅ **Enhanced Observability** (latency tracking and performance monitoring)
- ✅ **Policy Compliance** (automatic governance validation and violation tracking)

**All while preserving Langfuse's powerful observability and evaluation capabilities!**

---

## 📊 See Your Data in Langfuse Dashboard (1 minute)

Your Langfuse dashboard now shows:

### Enhanced Traces with Governance
```python
# View in Langfuse dashboard - your traces now include:
# - GenOps governance metadata (team, project, cost_center)
# - Cost attribution per operation
# - Budget compliance status
# - Performance metrics with GenOps context
```

### Cost Intelligence Integration
```python
# Get comprehensive cost summary
cost_summary = adapter.get_cost_summary("daily")
print(f"📈 Daily cost summary:")
print(f"   💰 Total cost: ${cost_summary['total_cost']:.6f}")
print(f"   📊 Operations: {cost_summary['operation_count']}")
print(f"   🎯 Team: {cost_summary['governance']['team']}")
print(f"   💡 Budget remaining: ${cost_summary['budget_remaining']:.6f}")
print(f"   ⚠️  Policy violations: {cost_summary['policy_violations']}")
```

### Zero-Code Auto-Instrumentation
```python
from genops.providers.langfuse import instrument_langfuse
from langfuse.decorators import observe
import openai

# Enable governance for ALL Langfuse operations
instrument_langfuse(
    team="auto-instrumented-team",
    project="zero-code-demo"
)

# Your existing Langfuse code now has governance automatically
@observe()
def my_existing_function():
    client = openai.OpenAI()
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello Langfuse + GenOps!"}]
    )

# This function now automatically includes:
# - Cost tracking and attribution
# - Team/project governance metadata
# - Budget compliance checking
# - Enhanced performance monitoring
result = my_existing_function()
```

---

## 🏗️ Next Steps (Your Choice!)

**✅ You now have enhanced Langfuse observability with GenOps governance!**

**Choose your next adventure:**

### 🎯 **30-Second Next Step: Enhanced Evaluations**
```python
# LLM evaluations with cost tracking and governance
from genops.providers.langfuse import instrument_langfuse

adapter = instrument_langfuse(
    team="evaluation-team",
    budget_limits={"daily": 10.0}  # $10 daily evaluation budget
)

def quality_evaluator():
    return {"score": 0.85, "comment": "High quality response"}

# Run evaluation with cost and governance tracking
evaluation_result = adapter.evaluate_with_governance(
    trace_id="your-trace-id",
    evaluation_name="response_quality",
    evaluator_function=quality_evaluator,
    customer_id="enterprise_123"
)

print(f"📊 Evaluation score: {evaluation_result['score']}")
print(f"💰 Evaluation cost tracked for team: {evaluation_result['governance']['team']}")
```

### 🚀 **5-Minute Next Step: Advanced Governance**
```python
# Advanced governance patterns with policy enforcement
from genops.providers.langfuse import GenOpsLangfuseAdapter, GovernancePolicy

adapter = GenOpsLangfuseAdapter(
    team="production-team",
    budget_limits={
        "daily": 100.0,    # $100 daily limit
        "monthly": 2000.0  # $2000 monthly limit
    },
    policy_mode=GovernancePolicy.ENFORCED  # Block policy violations
)

# Production workflow with comprehensive governance
with adapter.trace_with_governance(
    name="production_analysis",
    customer_id="enterprise_456",
    cost_center="ai-research",
    feature="market-analysis"
) as trace:
    
    # This will be blocked if budget limits are exceeded
    response = adapter.generation_with_cost_tracking(
        prompt="Analyze quarterly market trends...",
        model="gpt-4",
        max_cost=5.0  # Per-operation limit
    )
```

### 📚 **15-Minute Next Step: Complete Integration**
- **[Complete Langfuse Integration Guide](./integrations/langfuse.md)** - Full reference documentation
- **[All Langfuse Examples](../examples/langfuse/)** - Progressive complexity tutorials
- **[LLM Evaluation Governance](../examples/langfuse/evaluation_integration.py)** - Advanced evaluation patterns

---

## 🆘 Troubleshooting

**Getting errors? Here are quick fixes:**

### ❌ "Langfuse API key not found" or "Unauthorized"
```bash
# Make sure your Langfuse API keys are set correctly
echo $LANGFUSE_PUBLIC_KEY
echo $LANGFUSE_SECRET_KEY
# Should show your keys (not empty)

# Or set them in Python
import os
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-your-key"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-your-key"

# Get your keys from: https://cloud.langfuse.com/
```

### ❌ "No LLM provider API keys configured"
```bash
# Configure at least one AI provider
export OPENAI_API_KEY="your-openai-key"
# OR
export ANTHROPIC_API_KEY="your-anthropic-key" 

# Verify providers are configured
python -c "
import os
providers = ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY']
configured = [p for p in providers if os.getenv(p)]
print(f'Configured providers: {configured}')
"
```

### ❌ "Langfuse connectivity failed"
```bash
# Test Langfuse connectivity directly
curl -H "Authorization: Bearer $LANGFUSE_PUBLIC_KEY" \
     "$LANGFUSE_BASE_URL/api/public/health"

# Should return 200 OK with health status
```

### ❌ "Import error: langfuse not found"
```bash
# Install Langfuse with GenOps
pip install genops[langfuse]

# Or install Langfuse separately
pip install langfuse

# Verify installation
python -c "import langfuse; print('✅ Langfuse available')"
```

**Still stuck?** Run the comprehensive diagnostic:
```python
from genops.providers.langfuse_validation import validate_setup, print_validation_result
result = validate_setup(include_performance_tests=True)
print_validation_result(result, detailed=True)
```

---

## 💡 Key Advantages of GenOps + Langfuse

**GenOps enhances Langfuse observability with enterprise governance:**

| Aspect | Langfuse Alone | GenOps + Langfuse |
|--------|-----------------|------------------|
| **Observability** | Comprehensive LLM tracing and evaluation | Enhanced traces with cost attribution and governance |
| **Cost Tracking** | Basic usage monitoring | Precise cost calculation with team/project attribution |
| **Budget Control** | Manual cost monitoring | Automated budget enforcement with policy compliance |
| **Governance** | Trace metadata and tags | Full governance attributes (team, customer, cost_center) |
| **Policy Enforcement** | Manual review and analysis | Automated compliance checking and violation blocking |

**That's why GenOps + Langfuse focuses on:**
- 🔍 **Enhanced Observability** (governance context in all traces and evaluations)
- 💰 **Cost Intelligence** (precise cost tracking with attribution and forecasting)
- 🛡️ **Policy Compliance** (automated governance enforcement and violation detection)
- 📊 **Business Intelligence** (cost optimization insights and team attribution)

---

## 🎉 Success!

**🎯 In 5 minutes, you've accomplished:**
- ✅ Enhanced Langfuse observability with GenOps governance attributes
- ✅ Automatic cost tracking and team attribution for all LLM operations
- ✅ Budget enforcement and policy compliance integrated with Langfuse traces
- ✅ Advanced evaluation tracking with governance oversight
- ✅ Zero-code auto-instrumentation for existing Langfuse applications

**Your LLM observability now has enterprise-grade governance with comprehensive intelligence!**

**🚀 Ready for more advanced features?** Check out:
- **[LLM Evaluation Examples](../examples/langfuse/)**
- **[Cost Optimization Strategies](../examples/langfuse/evaluation_integration.py)**
- **[Complete Integration Guide](./integrations/langfuse.md)**

---

**Questions? Issues?** 
- 📝 [Create an issue](https://github.com/KoshiHQ/GenOps-AI/issues)
- 💬 [Join discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)
- 🔍 [LLM Observability Community](https://github.com/KoshiHQ/GenOps-AI/discussions/categories/observability)