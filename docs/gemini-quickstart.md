# Google Gemini Quickstart Guide

**⚡ 5-Minute Time-to-Value Guarantee**

Get GenOps cost tracking and governance working with Google Gemini in exactly 5 minutes or less. **This follows the GenOps Progressive Complexity Architecture**: immediate value first, then progressive mastery.

## 🔧 Prerequisites (2 minutes)

**Before starting, you need:**

1. **Google AI API Key**: Get your free API key from [Google AI Studio](https://ai.google.dev/)
2. **Python Environment**: Python 3.9+ with pip installed

**⚠️ Cost Notice**: Gemini API has free tier with usage limits. Paid tier starts at $0.30 per 1M input tokens for Flash model.

## ⚡ Zero-Code Setup (30 seconds)

```bash
# Install GenOps with Gemini support
pip install genops-ai[gemini]

# Set your API key
export GEMINI_API_KEY="your_api_key_here"
```

## 🎯 Immediate Value Demo (2 minutes)

**Copy-paste this working example:**

```python
from genops.providers.gemini import auto_instrument
from google import genai
import os

# Enable automatic instrumentation (zero code changes needed!)
auto_instrument()

# Your existing Gemini code works unchanged and is now tracked
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello from GenOps! Explain AI in one sentence."
)

print("✅ Success! Your Gemini calls now include GenOps cost tracking!")
print(f"🤖 Response: {response.text}")
```

## 🚀 Add Team Attribution (1 minute)

**Track costs by team, project, and customer:**

```python
from genops.providers.gemini import GenOpsGeminiAdapter

adapter = GenOpsGeminiAdapter()

result = adapter.text_generation(
    prompt="Analyze this quarterly report and provide key insights...",
    model="gemini-2.5-flash",
    # Governance attributes - automatic cost attribution!
    team="analytics-team",
    project="quarterly-analysis", 
    customer_id="enterprise-client-123"
)

print(f"💰 Cost: ${result.cost_usd:.6f}")
print(f"⚡ Latency: {result.latency_ms:.0f}ms")
print(f"🏷️ Team: analytics-team, Project: quarterly-analysis")
```

## ✅ Validation (1 minute)

**Verify everything is working:**

```python
from genops.providers.gemini import validate_setup, print_validation_result

# Comprehensive setup check with actionable fixes
result = validate_setup()

if result.success:
    print("🎉 GenOps Gemini setup is ready!")
    print("➡️ Your Gemini calls will now include cost tracking and governance")
else:
    print("❌ Setup issues found:")
    for error in result.errors:
        print(f"   - {error}")
    print("\n💡 For detailed diagnostics, run:")
    print("   python -c \"from genops.providers.gemini import validate_setup, print_validation_result; print_validation_result(validate_setup(), detailed=True)\"")
```

## 🎯 What Just Happened?

- **✅ Zero-code auto-instrumentation** - Your existing Gemini calls are now automatically tracked
- **💰 Real-time cost tracking** - Every operation shows accurate cost with token-level precision
- **🏷️ Team attribution** - Costs automatically attributed to teams, projects, and customers
- **📊 OpenTelemetry export** - Data flows to your existing observability platform
- **🎯 Model optimization** - Built-in cost optimization recommendations

## 🚨 Quick Troubleshooting

| Problem | Quick Fix |
|---------|-----------|
| `ImportError: genai` | Run `pip install google-generativeai` |
| `API key` error | Set `export GEMINI_API_KEY="your_key_here"` and get key from https://ai.google.dev/ |
| `quota exceeded` | Wait a few minutes (free tier has rate limits) or upgrade to paid tier |
| No telemetry data | **Optional**: Set `export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"` to send to local collector |

## 🚀 Progressive Learning Path (GenOps Developer Experience Standard)

**🎯 Phase 1: Immediate Value (≤ 5 minutes) - COMPLETE! ✅**
You've just completed the 5-minute quickstart. You now have working GenOps tracking.

**🎯 Phase 2: Team Control & Attribution (≤ 30 minutes)**
Ready to add team cost tracking and governance? Continue here:
```bash
python examples/gemini/basic_tracking.py        # Team attribution patterns
python examples/gemini/auto_instrumentation.py  # Zero-code setup patterns
```
*Time estimate: 15-30 minutes*

**🎯 Phase 3: Production Mastery (≤ 2 hours)**
Ready for advanced cost optimization and production deployment?
```bash
python examples/gemini/cost_optimization.py     # Advanced cost intelligence
# More production examples in examples/gemini/README.md
```
*Time estimate: 1-2 hours*

**📚 Documentation by Experience Level:**
- **Phase 2 (30-min)**: [`examples/gemini/README.md`](../../examples/gemini/) - Complete practical guide
- **Phase 3 (2-hr)**: [`docs/integrations/gemini.md`](../integrations/gemini.md) *(Coming Soon)* - Full reference

---

## 🎉 Success! You're Now Tracking AI Costs

**Your GenOps Gemini integration is complete.** Every AI operation is now:
- ✅ Automatically tracked with accurate costs
- ✅ Attributed to teams and projects
- ✅ Exported to your observability platform
- ✅ Optimized with intelligent model recommendations

**Questions?** Join our [community discussions](https://github.com/KoshiHQ/GenOps-AI/discussions) or check the [examples directory](../../examples/gemini/).