# Weights & Biases (W&B) Examples

This directory contains comprehensive examples demonstrating GenOps governance telemetry integration with Weights & Biases experiment tracking applications for ML operations and cost intelligence.

## 🧪 What is Weights & Biases?

**Weights & Biases (W&B) is an MLOps platform** that provides experiment tracking, model versioning, and collaboration tools for machine learning teams. Think of it as a comprehensive toolkit for managing the entire ML experiment lifecycle from development to production.

### Why Use W&B + GenOps?

- **🔬 Comprehensive Experiment Tracking**: Track metrics, hyperparameters, and artifacts with governance
- **💰 Cost Intelligence**: Understand compute and resource costs for ML experiments
- **👥 Team Collaboration**: Share experiments with cost attribution and budget controls
- **📊 Advanced Analytics**: Visualize experiment results with governance insights
- **🚀 Production ML**: Deploy models with cost awareness and policy compliance
- **🏛️ Enterprise Governance**: Team cost attribution, budget controls, and compliance tracking

**Perfect for**: ML teams, data scientists, MLOps engineers, and organizations managing machine learning workflows.

## 🚀 Quick Start

### Step 1: Prerequisites & Setup (2 minutes)

**New to GenOps + W&B?** Start here for a complete setup:

1. **Install GenOps with W&B support:**
   ```bash
   pip install genops[wandb]
   ```

2. **Get your W&B API key:**
   - Sign up at [wandb.ai](https://wandb.ai/) (free tier available)
   - Get your API key from [https://wandb.ai/settings](https://wandb.ai/settings)

3. **Configure environment variables:**
   ```bash
   # Required: W&B API key
   export WANDB_API_KEY="your_wandb_api_key"
   
   # Recommended for full governance
   export GENOPS_TEAM="your-team"
   export GENOPS_PROJECT="your-project"
   ```

### Step 2: Validate Your Setup (30 seconds) ⭐ **START HERE**

**Run this FIRST** to ensure everything is working:

```bash
python setup_validation.py
```

✅ **Expected result:** `Overall Status: PASSED`  
❌ **If you see errors:** Check the [Troubleshooting section](#-troubleshooting) below

### Step 3: Choose Your Learning Path

**✨ New to ML governance?** → [5-Minute Quickstart Guide](../../docs/wandb-quickstart.md)  
**🏃 Want to try examples?** → Continue with [Level 1 examples](#level-1-getting-started-5-minutes-each) below  
**📚 Need complete documentation?** → [Comprehensive Integration Guide](../../docs/integrations/wandb.md)

## 📚 Examples by Complexity

### Level 1: Getting Started (5 minutes each)

**🎯 Goal:** Understand basics of W&B + GenOps integration  
**👤 Perfect for:** First-time users, developers new to ML governance

**1. [setup_validation.py](setup_validation.py)** ⭐ **Run this first**
- ✅ Verify your W&B + GenOps setup across dependencies and configuration
- ✅ Validate API keys, connectivity, and basic functionality  
- ✅ Get immediate feedback on configuration issues with actionable fixes
- ✅ Test governance features and cost tracking accuracy
- **Next:** Try `basic_tracking.py` to see governance in action

**2. [basic_tracking.py](basic_tracking.py)** 
- 🔬 Simple experiment tracking with W&B and GenOps governance
- 💰 Introduction to cost attribution and team tracking
- 📊 Basic metrics logging with governance attributes
- 🚀 Minimal code changes for maximum governance capability
- **Next:** Try `auto_instrumentation.py` for zero-code setup

**3. [auto_instrumentation.py](auto_instrumentation.py)**
- 🤖 Zero-code setup using GenOps auto-instrumentation with W&B
- 📈 Automatic cost tracking for existing W&B applications
- 🔄 Drop-in governance integration with no code changes required
- **Next:** Ready for Level 2 - Experiment Management

### Level 2: Experiment Management (30 minutes each)

**🎯 Goal:** Build expertise in ML experiment governance and cost optimization  
**👤 Perfect for:** ML engineers, data scientists ready for advanced workflows  
**📋 Prerequisites:** Complete Level 1 examples

**4. [experiment_management.py](experiment_management.py)**
- 🔄 Complete experiment lifecycle management with governance
- 📊 Multi-run campaign tracking with unified cost intelligence
- 🎛️ Hyperparameter sweep governance and budget enforcement
- 📈 Experiment comparison with cost-aware analysis
- **Next:** Try `cost_optimization.py` to optimize spending

**5. [cost_optimization.py](cost_optimization.py)**
- 💰 Cost-aware experiment planning and resource optimization
- 🚨 Budget monitoring and alerts for ML experiments
- 📊 Resource efficiency analysis and optimization recommendations
- 🔮 Cost forecasting based on historical experiment patterns
- **Next:** Ready for Level 3 - Advanced Features

### Level 3: Advanced Features (2 hours each)

**🎯 Goal:** Master enterprise-grade features and deployment patterns  
**👤 Perfect for:** MLOps engineers, platform teams, enterprise deployments  
**📋 Prerequisites:** Complete Level 2 examples

**6. [advanced_features.py](advanced_features.py)**
- 🚀 Advanced W&B features with governance integration
- 📊 Custom metrics and artifact tracking with cost attribution
- 👥 Multi-team collaboration patterns with governance boundaries
- 📈 Advanced cost aggregation and reporting across experiments
- **Next:** Try `production_patterns.py` for enterprise deployment

**7. [production_patterns.py](production_patterns.py)**
- 🏭 Enterprise-ready W&B deployment patterns with governance
- ⚡ High-availability experiment tracking configurations
- 🔧 Context managers for complex ML workflows with cost tracking
- 🛡️ Policy enforcement and governance automation for ML operations
- 🚀 CI/CD integration patterns for ML experiments
- **Next:** Deploy in production with [Enterprise Deployment Guide](../../docs/enterprise/wandb-enterprise-deployment.md)

## 🎯 Use Case Examples

Each example includes:
- ✅ **Complete working code** you can run immediately
- ✅ **ML experiment demonstrations** with real governance scenarios
- ✅ **Cost optimization strategies** for compute and storage resources
- ✅ **Team collaboration patterns** showcasing multi-user governance
- ✅ **Error handling** and graceful degradation for production use
- ✅ **Performance considerations** for large-scale ML operations
- ✅ **Comments explaining** GenOps + W&B integration points

## 🏃 Running Examples

### 🎯 Recommended Path for First-Time Users

**Follow this exact sequence for the best learning experience:**

```bash
# Step 1: Validate setup (REQUIRED)
python setup_validation.py      # ⭐ Always run this first!

# Step 2: Choose your path
# For beginners → Start with basic tracking
python basic_tracking.py        # Learn the fundamentals

# For existing W&B users → Try auto-instrumentation  
python auto_instrumentation.py  # Zero-code governance integration

# Step 3: Build expertise (after completing Level 1)
python experiment_management.py # Complete experiment lifecycle
python cost_optimization.py     # Cost-aware planning

# Step 4: Advanced usage (after completing Level 2)
python advanced_features.py     # Advanced governance features
python production_patterns.py   # Enterprise deployment patterns
```

### ⚡ Quick Options

**New to everything?**
```bash
# Complete beginner path (30 minutes total)
python setup_validation.py && python basic_tracking.py && python auto_instrumentation.py
```

**Already know W&B?**
```bash  
# Advanced user path (2 hours total)
python setup_validation.py && python auto_instrumentation.py && python production_patterns.py
```

**Want to try everything?**
```bash
# Run all examples with comprehensive validation
./run_all_examples.sh
```

## 📊 What You'll Learn & Success Checkpoints

### ✅ **Level 1 Success Criteria (Getting Started)**
After completing Level 1, you should be able to:
- [ ] Run `python setup_validation.py` and see `Overall Status: PASSED` 
- [ ] Track a basic ML experiment with cost attribution
- [ ] See governance metadata in your W&B dashboard
- [ ] Understand automatic cost tracking for your experiments

**🎯 Success Validation:**
```bash
# You should see cost and governance data in output
python basic_tracking.py | grep -E "(Cost|Team|Governance)"
```

### ✅ **Level 2 Success Criteria (Experiment Management)**  
After completing Level 2, you should be able to:
- [ ] Manage complete experiment lifecycles with governance
- [ ] Set up budget monitoring and cost alerts
- [ ] Run hyperparameter sweeps with cost intelligence
- [ ] Generate cost optimization recommendations

**🎯 Success Validation:**
```bash
# Should show experiment management and cost optimization completed
python experiment_management.py && python cost_optimization.py
```

### ✅ **Level 3 Success Criteria (Advanced Features)**
After completing Level 3, you should be able to:
- [ ] Deploy production patterns with enterprise governance
- [ ] Configure high-availability tracking with auto-scaling
- [ ] Implement custom governance policies
- [ ] Integrate with CI/CD pipelines and enterprise systems

**🎯 Success Validation:**  
```bash
# Should complete without errors and show production metrics
python production_patterns.py | tail -20
```

### 📚 **Knowledge Areas Covered**

**ML Experiment Governance Excellence:**
- How to track ML experiments with comprehensive cost intelligence
- Cost optimization strategies for compute-intensive ML workloads  
- Team collaboration patterns with governance boundaries
- Budget enforcement and policy compliance for ML operations

**GenOps Governance Excellence:**
- Cross-experiment cost attribution and team tracking
- Unified telemetry across your entire ML stack
- Policy enforcement and compliance automation
- Enterprise-ready governance patterns for ML workflows

**Production ML Deployment Patterns:**
- High-availability experiment tracking configurations
- Auto-scaling ML workloads with cost awareness
- Performance optimization and resource efficiency analysis
- Integration with existing MLOps and observability platforms

## 🔍 Troubleshooting

### Common Issues

### 🆘 **Most Common Issues (90% of problems)**

**❌ "W&B API key not found" or authentication errors**
```bash
# Step 1: Get your key from https://wandb.ai/settings
export WANDB_API_KEY="your_wandb_api_key"

# Step 2: Verify it's set correctly  
echo $WANDB_API_KEY  # Should show your key (not empty)

# Step 3: Test W&B login
wandb login
```

**❌ "wandb module not found" or import errors**
```bash
# Step 1: Install with correct extras
pip install genops[wandb]

# Step 2: Verify installation
python -c "import wandb, genops; print('✅ Ready to go!')"

# Step 3: If still failing, try upgrading
pip install --upgrade genops[wandb]
```

**❌ "GenOps validation failed" - setup issues**
```bash
# Step 1: Run detailed validation to see specific errors
python setup_validation.py --detailed --connectivity --governance

# Step 2: Enable debug logging for more info
export GENOPS_LOG_LEVEL=DEBUG
python setup_validation.py

# Step 3: Check prerequisites one by one
python -c "import os; print('API Key:', '✅ Set' if os.getenv('WANDB_API_KEY') else '❌ Missing')"
```

### 🔧 **Less Common Issues**

**❌ Cost tracking not working:**
```bash
# Enable detailed logging and retry
export GENOPS_LOG_LEVEL=DEBUG
python basic_tracking.py
```

**❌ Examples running but no governance data:**
```bash
# Check your team/project settings
echo "Team: $GENOPS_TEAM, Project: $GENOPS_PROJECT"
# If empty, set them:
export GENOPS_TEAM="your-team"
export GENOPS_PROJECT="your-project"
```

**❌ Permission or network issues:**
```bash
# Test basic connectivity
curl -I https://wandb.ai
curl -I https://api.wandb.ai

# Check firewall/proxy settings if needed
```

### 🆘 **Still Having Issues?**

**📧 Get Help:**
- 📚 **First:** Check [Complete Integration Guide](../../docs/integrations/wandb.md) for detailed solutions
- 🚀 **Alternative:** Try [5-Minute W&B Quickstart](../../docs/wandb-quickstart.md) for simpler approach
- 🐛 **Bug Reports:** [GitHub Issues](https://github.com/anthropics/GenOps-AI/issues) with full error details
- 💬 **Community:** [GitHub Discussions](https://github.com/anthropics/GenOps-AI/discussions) for questions

**📋 When Asking for Help, Include:**
1. Output from `python setup_validation.py --detailed`
2. Your Python version: `python --version`  
3. Your operating system and version
4. Complete error messages (copy-paste, don't screenshot)
5. What you were trying to do when the error occurred

## 🌟 Next Steps

### ✅ After Completing Level 1 (Beginner)
- **Integrate patterns** from `basic_tracking.py` into your existing ML experiments
- **Add auto-instrumentation** to existing W&B applications for instant governance
- **Read:** [5-Minute W&B Quickstart Guide](../../docs/wandb-quickstart.md) for additional examples

### ✅ After Completing Level 2 (Intermediate)  
- **Implement cost optimization** strategies from `cost_optimization.py` in your team
- **Set up experiment lifecycle management** for better ML operations
- **Configure budget controls** and team cost attribution

### ✅ After Completing Level 3 (Advanced)
- **Deploy production patterns** using `production_patterns.py` as a template
- **Read:** [Enterprise Deployment Guide](../../docs/enterprise/wandb-enterprise-deployment.md)
- **Consider:** [Migration from other MLOps platforms](../../docs/migration-guides/wandb-from-competitors.md)

### 📚 Continue Learning
- **Comprehensive Guide**: [Complete W&B Integration Documentation](../../docs/integrations/wandb.md)
- **Other Integrations**: Explore [OpenAI](../openai/), [Anthropic](../anthropic/), and [LangChain](../langchain/) examples
- **Community**: Join discussions at [GitHub Discussions](https://github.com/anthropics/GenOps-AI/discussions)

## 🎯 Decision Guide: Is W&B + GenOps Right for You?

### ✅ **Perfect for W&B + GenOps:**
- **ML Teams** wanting comprehensive experiment tracking with cost intelligence
- **Data Scientists** who need to optimize compute costs for ML workloads
- **MLOps Engineers** requiring team collaboration with governance boundaries
- **Enterprises** needing policy enforcement and compliance for ML operations
- **Organizations** wanting cost attribution and budget controls for ML experiments

### 🤔 **Consider alternatives:**
- **Simple ML workflows** with minimal tracking needs → Try [OpenAI](../openai/) or [Anthropic](../anthropic/) examples
- **Basic experiment logging** without governance → Standard W&B might be sufficient
- **Non-ML use cases** → Explore other [GenOps integrations](../../docs/integrations/)

### 💡 **Still unsure?**
- **Start with:** [5-Minute W&B Quickstart](../../docs/wandb-quickstart.md) to see if it fits your needs
- **Compare:** Check our [migration guide](../../docs/migration-guides/wandb-from-competitors.md) if you're using MLflow, TensorBoard, or Comet
- **Ask questions:** Join our [community discussions](https://github.com/anthropics/GenOps-AI/discussions)

---

**Ready to get started?** Run `python setup_validation.py` to validate your setup and begin your GenOps + W&B journey!