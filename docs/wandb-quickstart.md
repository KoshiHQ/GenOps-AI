# Weights & Biases Integration - 5-Minute Quickstart

**🎯 Get GenOps governance for ML experiment tracking in 5 minutes**

This guide gets you from zero to tracking ML experiments with cost intelligence and team attribution using GenOps + Weights & Biases in under 5 minutes.

### 🧭 **Navigation Guide**
- **New to W&B?** You're in the right place - follow this guide
- **Want hands-on examples?** Go to [W&B Examples Directory](../examples/wandb/) after completing this
- **Need comprehensive docs?** See [Complete Integration Guide](./integrations/wandb.md)
- **Enterprise deployment?** Check [Enterprise Guide](./enterprise/wandb-enterprise-deployment.md)

---

## 🚀 Prerequisites (30 seconds)

**Before you start, make sure you have:**

1. **W&B account and API key**
   ```bash
   # Sign up at https://wandb.ai (free tier available)
   # Get your API key from https://wandb.ai/settings
   export WANDB_API_KEY="your-wandb-api-key-here"
   ```

2. **Python environment**
   ```bash
   # Ensure you have Python 3.9+
   python --version
   ```

3. **Install GenOps with W&B support**
   ```bash
   pip install genops[wandb]
   ```

4. **Verify setup**
   ```bash
   python -c "import wandb, genops; print('✅ Ready to go!')"
   ```

---

## ⚡ Quick Setup (2 minutes)

### Step 1: Install and Configure (30 seconds)
```bash
pip install genops[wandb]
export WANDB_API_KEY="your-wandb-api-key"
export GENOPS_TEAM="ml-team"      # Optional but recommended
export GENOPS_PROJECT="quickstart" # Optional but recommended
```

### Step 2: Verify Setup (30 seconds)
Run this validation script to check everything is working:

```python
# Save as validate.py and run: python validate.py
from genops.providers.wandb_validation import validate_setup, print_validation_result

result = validate_setup()
print_validation_result(result)
```

You should see: ✅ **Overall Status: PASSED**

### Step 3: Test Basic Tracking (60 seconds)
Create this minimal test file:

```python
# test_wandb_genops.py
import os
import wandb
from genops.providers.wandb import auto_instrument

# Enable GenOps governance for W&B (ONE LINE!)
auto_instrument(
    team="ml-team",
    project="quickstart-test",
    daily_budget_limit=10.0  # $10 daily budget
)

print("🚀 Testing W&B with GenOps governance...")

# Your normal W&B code works unchanged!
run = wandb.init(
    project="genops-quickstart", 
    name="test-run",
    config={
        'learning_rate': 0.001,
        'batch_size': 32,
        'model': 'simple_nn'
    }
)

# Log some metrics (your existing code)
for epoch in range(5):
    accuracy = 0.5 + (epoch * 0.1)
    loss = 2.0 - (epoch * 0.3)
    
    wandb.log({
        'epoch': epoch,
        'accuracy': accuracy,
        'loss': loss
    })

# Create and log an artifact
artifact = wandb.Artifact('test-model', type='model')
import tempfile
with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
    f.write(f"Model with final accuracy: {accuracy:.3f}")
    artifact.add_file(f.name)

run.log_artifact(artifact)
run.finish()

print(f"✅ SUCCESS! ML experiment tracked with governance")
print(f"📊 View your run at: {run.url}")
```

**Run it:**
```bash
python test_wandb_genops.py
```

**Expected output:**
```
🚀 Testing W&B with GenOps governance...
✅ SUCCESS! ML experiment tracked with governance
📊 View your run at: https://wandb.ai/your-team/genops-quickstart/runs/abc123
```

---

## 🎯 What Just Happened?

**GenOps automatically added:**
- ✅ **Cost intelligence** (tracked compute and storage costs for the experiment)
- ✅ **Team attribution** (costs attributed to "ml-team" and "quickstart-test")
- ✅ **Budget monitoring** (enforced $10 daily spending limit)
- ✅ **Governance metadata** (enhanced W&B runs with governance attributes)
- ✅ **Policy compliance** (automatic policy checking and violation tracking)

**All with zero changes to your existing W&B workflow!**

---

## 📊 See Your Governance Data (1 minute)

### Option 1: View Enhanced W&B Run
Your W&B run now includes governance data:
- Navigate to your W&B dashboard
- Check the run config for governance attributes
- View enhanced tags with team/project information

### Option 2: Query Governance Metrics
```python
from genops.providers.wandb import instrument_wandb

adapter = instrument_wandb(team="ml-team", project="quickstart")
metrics = adapter.get_metrics()

print(f"📊 Governance Metrics:")
print(f"   • Daily Usage: ${metrics['daily_usage']:.3f}")
print(f"   • Budget Remaining: ${metrics['budget_remaining']:.2f}")
print(f"   • Team: {metrics['team']}")
print(f"   • Experiments Tracked: {metrics['operation_count']}")
```

### Option 3: Cost Breakdown Analysis
```python
from genops.providers.wandb_cost_aggregator import calculate_simple_experiment_cost

# Estimate cost for different experiment configurations
cost = calculate_simple_experiment_cost(
    compute_hours=2.0,
    gpu_type="v100", 
    storage_gb=5.0
)

print(f"💰 Estimated experiment cost: ${cost:.3f}")
```

---

## 🏗️ Next Steps (Your Choice!)

**✅ You now have GenOps governance for all your W&B experiments!**

**Choose your next adventure:**

### 🎯 **30-Second Next Step: Try Different Experiment Types**
```python
# Test different ML workflows
from genops.providers.wandb import auto_instrument

auto_instrument(
    team="research", 
    project="model-comparison",
    daily_budget_limit=25.0
)

# Your existing hyperparameter sweep code
sweep_config = {
    'method': 'grid',
    'parameters': {
        'learning_rate': {'values': [0.001, 0.01, 0.1]},
        'batch_size': {'values': [16, 32, 64]}
    }
}

# W&B sweep with automatic governance
sweep_id = wandb.sweep(sweep_config, project="genops-sweep")
wandb.agent(sweep_id, function=your_train_function, count=5)
```

### 🚀 **5-Minute Next Step: Advanced Cost Intelligence**
```python
# Advanced experiment lifecycle management
from genops.providers.wandb import instrument_wandb

adapter = instrument_wandb(
    team="ml-engineering", 
    project="production-models",
    max_experiment_cost=20.0,
    enable_cost_alerts=True
)

# Track complete experiment lifecycle with cost breakdown
with adapter.track_experiment_lifecycle("model-training-v2") as experiment:
    run = wandb.init(project="production", name="resnet50-training")
    
    # Your training code here...
    for epoch in range(50):
        train_loss, val_accuracy = train_epoch()
        wandb.log({'loss': train_loss, 'accuracy': val_accuracy})
        
        # Update experiment cost (optional - auto-calculated if not provided)
        experiment.estimated_cost += calculate_epoch_cost()
    
    # Log governed artifacts
    model_artifact = wandb.Artifact("trained-resnet50", type="model")
    model_artifact.add_file("model.pth")
    adapter.log_governed_artifact(model_artifact, cost_estimate=0.05)
    
    run.finish()

# Get detailed cost breakdown
cost_summary = adapter.get_experiment_cost_summary(experiment.run_id)
print(f"Total cost: ${cost_summary.total_cost:.2f}")
print(f"Compute: ${cost_summary.compute_cost:.2f}")
print(f"Storage: ${cost_summary.storage_cost:.2f}")
```

### 📚 **15-Minute Next Step: Complete Integration**
- **[Complete W&B Integration Guide](./integrations/wandb.md)** - Full reference documentation
- **[All W&B Examples](../examples/wandb/)** - Progressive complexity tutorials
- **[Cost Optimization Guide](../examples/wandb/cost_optimization.py)** - Advanced cost intelligence

---

## 🆘 Troubleshooting

**Getting errors? Here are quick fixes:**

### ❌ "WANDB_API_KEY not found" or authentication errors
```bash
# Make sure your W&B API key is set correctly
echo $WANDB_API_KEY
# Should show your key (not empty)

# Or set it in Python
import os
os.environ["WANDB_API_KEY"] = "your-wandb-api-key"

# Get your key from: https://wandb.ai/settings
```

### ❌ "wandb module not found"
```bash
# Install W&B and GenOps integration
pip install genops[wandb]

# Verify installation
python -c "import wandb; print(f'W&B version: {wandb.__version__}')"
```

### ❌ "GenOps validation failed"
```bash
# Run comprehensive validation
python -c "
from genops.providers.wandb_validation import validate_setup, print_validation_result
result = validate_setup(include_connectivity_tests=True)
print_validation_result(result, detailed=True)
"
```

### ❌ "W&B login required"
```bash
# Login to W&B (alternative to API key)
wandb login
```

**Still stuck?** Run the diagnostic:
```python
from genops.providers.wandb_validation import validate_setup, print_validation_result
result = validate_setup(include_performance_tests=True, include_governance_tests=True)
print_validation_result(result, detailed=True)
```

---

## 💡 Key Advantages of W&B + GenOps

**W&B + GenOps integration is optimized for ML operations governance:**

| Aspect | Standard W&B | W&B + GenOps |
|--------|--------------|---------------|
| **Experiment Tracking** | Metrics, configs, artifacts | + Cost attribution + Budget limits |
| **Team Collaboration** | Shared workspace | + Cost visibility + Governance boundaries |
| **Cost Management** | Manual tracking | + Automatic cost intelligence + Forecasting |
| **Compliance** | Basic metadata | + Policy enforcement + Audit trails |
| **Enterprise Ready** | Team features | + Multi-tenant governance + Budget controls |

**That's why GenOps W&B integration focuses on:**
- 🧪 **Enhanced Experiment Tracking** (all standard W&B features + governance)
- 💰 **Automatic Cost Intelligence** (compute, storage, and platform costs)
- 🏛️ **Enterprise Governance** (team attribution, policy enforcement, compliance)
- 📊 **Advanced Analytics** (cost efficiency, resource optimization, forecasting)

---

## 🎉 Success!

**🎯 In 5 minutes, you've accomplished:**
- ✅ Set up GenOps governance for W&B experiments
- ✅ Automatically tracked ML experiment costs and resource usage
- ✅ Attributed costs to teams and projects with budget limits
- ✅ Enhanced W&B runs with governance metadata and policy compliance
- ✅ Gained cost intelligence and optimization insights for ML workflows

**Your ML experiments now have enterprise-grade governance with cost intelligence!**

**🚀 Ready for more advanced features?** Choose your next step:

### 📚 **Continue Learning (Recommended)**
- **[W&B Examples Directory](../examples/wandb/)** - Step-by-step progressive examples
- **[Complete Integration Guide](./integrations/wandb.md)** - Comprehensive documentation
- **[Enterprise Deployment Guide](./enterprise/wandb-enterprise-deployment.md)** - Production patterns

### 🎯 **Jump to Specific Topics**  
- **Cost Intelligence:** [Cost Optimization Example](../examples/wandb/cost_optimization.py)
- **Zero-Code Setup:** [Auto-Instrumentation Example](../examples/wandb/auto_instrumentation.py)
- **Production Ready:** [Production Patterns Example](../examples/wandb/production_patterns.py)

### 🔄 **Migration from Other Platforms**
- **From MLflow/TensorBoard/Comet:** [Migration Guide](./migration-guides/wandb-from-competitors.md)

---

**Questions? Issues?** 
- 📝 [Create an issue](https://github.com/anthropics/GenOps-AI/issues)
- 💬 [Join discussions](https://github.com/anthropics/GenOps-AI/discussions)
- 🧪 [ML Community](https://github.com/anthropics/GenOps-AI/discussions/categories/ml-ops)