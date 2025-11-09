# PostHog + GenOps 5-Minute Quickstart

> 📖 **Navigation:** **Quickstart (5 min)** → [Complete Guide](integrations/posthog.md) → [Examples](../examples/posthog/)

Get PostHog product analytics with GenOps governance running in 5 minutes with zero code changes to your existing PostHog workflows.

## 🎯 What You'll Achieve

⏱️ **5 minutes** → PostHog analytics with automatic cost tracking, team attribution, and budget governance

✅ **Zero code changes** to your existing PostHog implementation  
✅ **Automatic cost tracking** for all analytics events and feature flags  
✅ **Team attribution** for cost allocation and governance  
✅ **Budget enforcement** with configurable limits and alerts  
✅ **OpenTelemetry export** for your observability stack

## Prerequisites

- Python 3.9+
- PostHog account with API key ([get one here](https://app.posthog.com/project/settings))

## Step 1: Install GenOps with PostHog Support
⏱️ **30 seconds**

```bash
pip install genops[posthog]
```

<details>
<summary>🔧 Installation Issues?</summary>

**If you get permission errors:**
```bash
pip install --user genops[posthog]
```

**If you're using conda:**
```bash
pip install genops[posthog]  # PostHog isn't available via conda
```

**If you're in a virtual environment:**
```bash
source your-venv/bin/activate
pip install genops[posthog]
```

</details>

## Step 2: Configure Environment
⏱️ **60 seconds**

```bash
# Required: Your PostHog project API key
export POSTHOG_API_KEY="phc_your_project_api_key_here"

# Recommended: Team and project for cost attribution
export GENOPS_TEAM="analytics-team"
export GENOPS_PROJECT="product-analytics"

# Optional: Budget limits and governance
export GENOPS_DAILY_BUDGET_LIMIT="100.0"  # USD per day
export GENOPS_GOVERNANCE_POLICY="advisory"  # advisory, enforced, or strict
```

<details>
<summary>🔍 Where to find your PostHog API key</summary>

1. Go to [PostHog Project Settings](https://app.posthog.com/project/settings)
2. Copy your "Project API Key" (starts with `phc_`)
3. **Important:** Don't use your Personal API Key - use the Project API Key

**EU customers:** Your key will work automatically with `https://eu.posthog.com`

</details>

## Step 3: Validate Setup  
⏱️ **30 seconds**

```python
# Quick validation - copy and run this
from genops.providers.posthog_validation import validate_setup, print_validation_result

result = validate_setup()
print_validation_result(result)
```

**Expected output:**
```
🔍 PostHog + GenOps Integration Validation Report
============================================================

✅ Overall Status: SUCCESS

💡 Recommendations:
  1. All validation checks passed successfully!

🚀 Next Steps:
  1. You can now use GenOps PostHog integration with confidence
```

<details>
<summary>❌ Seeing validation errors?</summary>

**Common fixes:**

1. **API Key issues:**
   ```bash
   export POSTHOG_API_KEY="phc_your_correct_api_key"
   ```

2. **Installation issues:**
   ```bash
   pip install --upgrade genops[posthog]
   ```

3. **Permission issues:**
   ```bash
   pip install --user genops[posthog]
   ```

</details>

## Step 4: Add Governance to Existing PostHog Code
⏱️ **90 seconds**

**Option A: Zero-Code Auto-Instrumentation (Recommended)**

Add this ONE LINE at the start of your application:

```python
# Add this single line to enable governance for ALL your PostHog code
from genops.providers.posthog import auto_instrument
auto_instrument()  # 🎉 That's it! Your existing PostHog code now has governance
```

**Your existing PostHog code works unchanged:**
```python
import posthog

# Your existing code - no changes needed!
posthog.capture("user_signed_up", {"email": "user@example.com"})
posthog.feature_enabled("new_dashboard", "user_123")
# ↑ Now automatically tracked with cost + governance
```

**Option B: Manual Adapter (Advanced Control)**

```python
from genops.providers.posthog import GenOpsPostHogAdapter

# Create adapter with governance
adapter = GenOpsPostHogAdapter(
    team="your-team",
    project="your-project",
    daily_budget_limit=50.0
)

# Track analytics with governance
with adapter.track_analytics_session("user_onboarding") as session:
    # Analytics events with automatic cost tracking
    adapter.capture_event_with_governance(
        event_name="user_signed_up",
        properties={"email": "user@example.com", "source": "organic"}
    )
```

## Step 5: Verify It's Working
⏱️ **60 seconds**

Run this test to confirm governance is active:

```python
# Test script - save as test_posthog.py and run it
from genops.providers.posthog import auto_instrument

# Enable governance
adapter = auto_instrument()

# Simulate some analytics events
print("🔄 Testing PostHog + GenOps integration...")

# Test event capture
result = adapter.capture_event_with_governance(
    event_name="test_event",
    properties={"test": True, "source": "quickstart"},
    distinct_id="quickstart_user"
)

print(f"✅ Event tracked! Cost: ${result['cost']:.6f}")

# Get cost summary
cost_summary = adapter.get_cost_summary()
print(f"📊 Daily costs: ${cost_summary['daily_costs']:.6f}")
print(f"🏛️ Team: {cost_summary['team']}")
print(f"🎯 Project: {cost_summary['project']}")

print("\n🎉 PostHog + GenOps integration is working!")
```

**Expected output:**
```
🔄 Testing PostHog + GenOps integration...
✅ Event tracked! Cost: $0.000050
📊 Daily costs: $0.000050
🏛️ Team: analytics-team
🎯 Project: product-analytics

🎉 PostHog + GenOps integration is working!
```

## 🎉 Success! You Now Have:

✅ **Cost Tracking** - Every PostHog event, feature flag, and recording is tracked with precise costs  
✅ **Team Attribution** - All costs are attributed to your team and project  
✅ **Budget Governance** - Automatic budget monitoring with configurable limits  
✅ **OpenTelemetry Export** - Governance data flows to your observability stack  
✅ **Zero Code Changes** - Your existing PostHog code works exactly as before

## Quick Cost Intelligence

**View your PostHog costs in real-time:**
```python
from genops.providers.posthog import get_current_adapter

adapter = get_current_adapter()
if adapter:
    summary = adapter.get_cost_summary()
    print(f"💰 Today's PostHog costs: ${summary['daily_costs']:.4f}")
    print(f"📈 Budget utilization: {summary['daily_budget_utilization']:.1f}%")
```

**Get volume discount analysis:**
```python
analysis = adapter.get_volume_discount_analysis(projected_monthly_events=100000)
print(f"📊 Projected monthly cost: ${analysis['projected_monthly_cost']:.2f}")
print(f"💡 Cost per event: ${analysis['cost_per_event']:.6f}")
```

## What's Next?

### 🚀 **5-Minute Wins** (Try these now!)
- [**See it in action:**](../examples/posthog/basic_tracking.py) Run the basic tracking example
- [**Cost optimization:**](../examples/posthog/cost_optimization.py) Learn how to optimize your PostHog costs
- [**Auto-instrumentation:**](../examples/posthog/auto_instrumentation.py) See zero-code governance in detail

### 📚 **30-Minute Deep Dive**
- [**Complete integration guide:**](integrations/posthog.md) Advanced features and configuration
- [**Interactive examples:**](../examples/posthog/) All examples with expected outputs
- [**Cost intelligence guide:**](cost-intelligence-guide.md) ROI analysis and optimization

### 🏢 **2-Hour Enterprise Setup**
- [**Production deployment patterns:**](../examples/posthog/production_patterns.py) HA, disaster recovery, compliance
- [**Enterprise governance templates:**](enterprise-governance-templates.md) SOX, GDPR, HIPAA compliance
- [**Multi-tenant architecture:**](../examples/posthog/production_patterns.py) SaaS deployment patterns

## Troubleshooting

<details>
<summary>🚨 Common Issues & Fixes</summary>

### Issue: "Module 'posthog' not found"
```bash
pip install posthog
```

### Issue: "Invalid PostHog API key"
1. Check your key starts with `phc_`
2. Get the correct key from [PostHog Project Settings](https://app.posthog.com/project/settings)
3. Use Project API Key, not Personal API Key

### Issue: "Budget exceeded" errors
```python
# Increase budget or switch to advisory mode
adapter = GenOpsPostHogAdapter(
    daily_budget_limit=200.0,  # Increase budget
    governance_policy="advisory"  # Or disable enforcement
)
```

### Issue: Events not appearing in PostHog
- Auto-instrumentation adds governance but doesn't change PostHog behavior
- Check your PostHog dashboard for events
- Verify your PostHog API key and project settings

</details>

## PostHog-Specific Tips

### **Feature Flags with Cost Tracking**
```python
# Your existing feature flag code
flag_value = posthog.feature_enabled("new_feature", "user_123")

# With manual adapter - includes cost tracking
flag_value, metadata = adapter.evaluate_feature_flag_with_governance(
    flag_key="new_feature",
    distinct_id="user_123"
)
print(f"Flag value: {flag_value}, Cost: ${metadata['cost']:.6f}")
```

### **Session Recording Governance**
```python
# Session recordings are automatically tracked for cost
# Configure recording governance
adapter = GenOpsPostHogAdapter(
    daily_budget_limit=100.0,  # Control recording costs
    governance_policy="enforced"  # Enforce limits
)
```

### **A/B Testing with Cost Intelligence**
```python
# A/B tests are tracked with detailed cost attribution
with adapter.track_analytics_session("ab_test_checkout_flow") as session:
    # Test assignment and conversion events tracked with costs
    adapter.capture_event_with_governance("ab_test_assigned", {
        "test": "checkout_flow_v2", 
        "variant": "treatment"
    })
```

## Integration Examples

### **Web Application (Flask/FastAPI)**
```python
from flask import Flask
from genops.providers.posthog import auto_instrument

app = Flask(__name__)
auto_instrument(team="web-team", project="user-analytics")

# Your existing routes work unchanged with governance
@app.route('/api/track')
def track_event():
    return jsonify({'status': 'tracked'})
```

### **Mobile/React Integration**
```python
# Backend API endpoint for frontend analytics
@app.route('/api/analytics', methods=['POST'])
def track_frontend():
    data = request.json
    result = adapter.capture_event_with_governance(
        event_name=data['event'],
        properties=data['properties'],
        distinct_id=data['user_id']
    )
    return jsonify(result)
```

---

## 💡 **Key Insight**

> GenOps adds governance to PostHog **without changing how PostHog works**. Your dashboards, feature flags, and recordings work exactly the same - you just get additional cost intelligence and governance on top.

**🎯 Ready for more?** Check out our [complete integration guide](integrations/posthog.md) or try the [interactive examples](../examples/posthog/)!

---

**Questions?** Join our [community discussions](https://github.com/KoshiHQ/GenOps-AI/discussions) or [open an issue](https://github.com/KoshiHQ/GenOps-AI/issues).

**Found this helpful?** ⭐ [Star us on GitHub](https://github.com/KoshiHQ/GenOps-AI) to help others discover GenOps!