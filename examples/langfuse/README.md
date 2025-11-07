# Langfuse LLM Observability + GenOps Governance Examples

**🎯 Add enterprise governance to your Langfuse LLM observability in 5 minutes**

This directory contains comprehensive examples demonstrating how GenOps enhances Langfuse with enterprise-grade governance, cost intelligence, and policy enforcement for production AI applications.

---

## 🤔 Why Do I Need This?

If you're building production LLM applications, you're likely facing these challenges:

❌ **Without GenOps Governance:**
- No visibility into LLM costs across teams and projects
- Manual budget tracking and cost attribution
- No policy enforcement or compliance validation
- Limited observability context for business decisions
- Difficult to optimize costs or prevent budget overruns

✅ **With GenOps + Langfuse:**
- **Automatic cost attribution** to teams, projects, and customers
- **Real-time budget enforcement** with policy compliance
- **Enhanced observability** with business context in every trace
- **Cost optimization insights** and recommendations
- **Enterprise governance** for compliance and audit requirements

---

## 🧠 What is GenOps?

**GenOps (Generative Operations)** is the practice of applying governance, observability, and cost intelligence to AI/LLM operations. Think "FinOps for AI" - it brings financial accountability and operational excellence to your AI infrastructure.

### 🔍 What is Langfuse?

**Langfuse is an open-source LLM engineering platform** that provides comprehensive observability, evaluation, and prompt management for AI applications. It captures detailed traces of LLM operations and provides powerful analytics for optimization.

### 💡 The Perfect Combination

**GenOps + Langfuse** = Enhanced LLM observability with enterprise governance intelligence

- **🔍 Enhanced Observability**: Every Langfuse trace includes governance context (team, project, customer)
- **💰 Cost Intelligence**: Precise cost tracking and attribution integrated with observability
- **🛡️ Governance Integration**: Policy compliance and budget enforcement within observability workflows
- **📊 Business Intelligence**: Cost optimization insights with team-based attribution
- **🎯 Evaluation Governance**: LLM evaluation tracking with cost and compliance oversight
- **🚀 Enterprise Readiness**: Production-grade governance for LLM observability at scale

---

## ⚡ Quick Value Assessment (2 minutes)

**Before diving in, let's see if this is right for your team:**

### ✅ Perfect For:
- **Engineering Teams** using Langfuse who need cost visibility and governance
- **FinOps Teams** requiring detailed LLM cost attribution and budget controls
- **Enterprise Organizations** needing compliance tracking and audit trails for AI operations
- **Multi-team Companies** where different teams use LLMs with shared budgets
- **Production AI Applications** requiring cost optimization and governance automation

### 🤔 Consider Alternatives If:
- You have simple, single-developer LLM projects with no cost concerns
- You only need basic cost tracking without detailed observability
- You don't use Langfuse and aren't planning to adopt observability practices

**📊 Team Size Guidelines:**
- **1-2 developers**: Start with Level 1 examples (basic governance)
- **3-10 developers**: Focus on Level 2 (advanced observability and evaluation)
- **10+ developers**: Implement Level 3 (enterprise governance and production patterns)

---

## 🚀 Getting Started

### Phase 1: Before You Start (5 minutes)

**First, ensure you have the prerequisites:**

1. **Python Environment**
   ```bash
   python3 --version  # Ensure Python 3.8+
   ```

2. **Langfuse Account** (free tier available)
   - Sign up at [cloud.langfuse.com](https://cloud.langfuse.com/)
   - Create a new project in the Langfuse dashboard
   - Note your API keys (you'll need them in Phase 3)

3. **AI Provider Account** (choose one)
   - [OpenAI Platform](https://platform.openai.com/api-keys) (recommended for getting started)
   - [Anthropic Console](https://console.anthropic.com/) (alternative option)
   - Any provider you're already using

### Phase 2: Installation (1 minute)

```bash
# Install GenOps with Langfuse integration
pip install genops[langfuse]

# Verify installation
python -c "import genops, langfuse; print('✅ Installation successful')"
```

**Quick Troubleshooting:**
- ❌ `ModuleNotFoundError: No module named 'genops'` → Run `pip install genops[langfuse]` again
- ❌ `ModuleNotFoundError: No module named 'langfuse'` → Run `pip install langfuse` directly

### Phase 3: Configuration (2 minutes)

Set up your environment variables:

```bash
# Required: Langfuse observability platform keys
export LANGFUSE_PUBLIC_KEY="pk-lf-your-public-key"      # From Langfuse dashboard
export LANGFUSE_SECRET_KEY="sk-lf-your-secret-key"      # From Langfuse dashboard
export LANGFUSE_BASE_URL="https://cloud.langfuse.com"   # Default (change if self-hosted)

# Required: At least one AI provider (choose what you have)
export OPENAI_API_KEY="your-openai-api-key"             # If using OpenAI
export ANTHROPIC_API_KEY="your-anthropic-api-key"       # If using Anthropic
```

**Quick Test:** Verify your setup works:
```bash
# Test Langfuse connectivity
curl -H "Authorization: Bearer $LANGFUSE_PUBLIC_KEY" "$LANGFUSE_BASE_URL/api/public/health"
# Should return: {"status":"ok"}
```

### Phase 4: Validation (30 seconds)

**🎯 Run this first** to ensure everything is configured correctly:

```bash
python setup_validation.py
```

**Expected output:** ✅ **Overall Status: PASSED**

**If validation fails:** Check the error messages - they include specific fixes for common issues.

---

## 📚 Learning Path Guide

### 🎯 Your Learning Journey

**Total Time Investment:** 4-6 hours (spread across days/weeks)  
**Immediate Value:** Visible in first 5 minutes  
**Production Ready:** After Level 2 completion  

### Level 1: Getting Started (15 minutes total)
**Goal:** Understand the value and get immediate results  
**When to Use:** Perfect for initial evaluation and proof-of-concept

**Learning Outcomes:**
- ✅ See enhanced Langfuse traces with governance attributes
- ✅ Understand automatic cost attribution and team tracking  
- ✅ Experience zero-code governance integration
- ✅ Get immediate cost visibility for your LLM operations

**Examples:**

**[setup_validation.py](setup_validation.py)** ⭐ *Start here* (30 seconds)
- Comprehensive setup validation with actionable diagnostics
- Verify API keys, connectivity, and basic functionality
- Get immediate feedback on configuration issues
- Test governance integration and performance baseline

**[basic_tracking.py](basic_tracking.py)** (5 minutes)
- Simple LLM operations with enhanced Langfuse tracing
- See governance attributes integrated with observability
- Experience cost attribution and team tracking
- Minimal code changes for maximum governance enhancement

**[auto_instrumentation.py](auto_instrumentation.py)** (5 minutes)  
- Zero-code setup for existing Langfuse applications
- Automatic governance enhancement with no code changes
- Perfect for teams already using Langfuse decorators
- Drop-in governance integration that "just works"

**💡 Level 1 Success Criteria:**
- [ ] Validation script shows ✅ **Overall Status: PASSED**
- [ ] You can see cost attribution in Langfuse dashboard
- [ ] Your existing Langfuse code works with governance
- [ ] You understand the immediate value proposition

---

### Level 2: Advanced Observability (1 hour total)
**Goal:** Build production-ready evaluation and optimization workflows  
**When to Use:** When you need advanced LLM evaluation and prompt optimization

**Learning Outcomes:**
- ✅ Implement governance-aware LLM evaluation workflows
- ✅ Build cost-optimized prompt management systems
- ✅ Create A/B testing frameworks with governance attribution
- ✅ Establish evaluation pipelines with compliance tracking

**Examples:**

**[evaluation_integration.py](evaluation_integration.py)** (30 minutes)
- LLM evaluations with governance tracking and cost attribution
- Automated evaluation workflows with budget enforcement
- Policy compliance for evaluation processes
- Advanced evaluation patterns with business intelligence

**[prompt_management.py](prompt_management.py)** (30 minutes)
- Advanced prompt management with cost optimization insights
- A/B testing with governance attribution and cost tracking
- Prompt version control with detailed cost analysis
- Optimization recommendations based on usage patterns

**💡 Level 2 Success Criteria:**
- [ ] You can run cost-attributed LLM evaluations
- [ ] Your team can optimize prompts based on cost/performance data
- [ ] You have A/B testing with governance tracking
- [ ] You understand prompt management with cost intelligence

---

### Level 3: Enterprise Governance (4+ hours total)
**Goal:** Master production-grade governance for enterprise deployment  
**When to Use:** For production systems requiring enterprise governance and compliance

**Learning Outcomes:**
- ✅ Deploy advanced observability with hierarchical tracing
- ✅ Implement multi-provider governance with unified tracking
- ✅ Build high-availability systems with governance automation
- ✅ Create compliance monitoring and audit systems

**Examples:**

**[advanced_observability.py](advanced_observability.py)** (2 hours)
- Advanced tracing patterns with comprehensive governance
- Multi-provider observability with unified governance
- Complex workflow tracing with cost optimization
- Production observability with policy enforcement

**[production_patterns.py](production_patterns.py)** (2 hours)
- Enterprise-ready deployment patterns and high-availability
- Governance automation with compliance monitoring
- Production monitoring with cost intelligence and alerts
- Disaster recovery and business continuity patterns

**💡 Level 3 Success Criteria:**
- [ ] You can deploy multi-region governance systems
- [ ] Your organization has automated compliance monitoring
- [ ] You have production-grade cost intelligence dashboards
- [ ] You understand enterprise governance patterns

---

## 🏃 Running Examples

### Option 1: Individual Examples (Recommended for Learning)

```bash
# 🎯 Level 1: Getting Started (15 minutes total)
python setup_validation.py      # ⭐ Always start here
python basic_tracking.py        # See governance in action  
python auto_instrumentation.py  # Zero-code integration

# 📊 Level 2: Advanced Observability (1 hour total)
python evaluation_integration.py # Advanced evaluations
python prompt_management.py     # Cost-optimized prompts

# 🏭 Level 3: Enterprise Governance (4+ hours total)
python advanced_observability.py # Production observability
python production_patterns.py   # Enterprise deployment
```

### Option 2: Complete Suite (For Comprehensive Evaluation)

```bash
# Run all examples with validation (~20 minutes active time)
./run_all_examples.sh
```

This script includes progress tracking, error handling, and comprehensive reporting.

---

## 🎯 Industry-Specific Use Cases

### 🏦 Financial Services
- **Compliance:** SOC2, PCI DSS audit trails for all LLM operations
- **Cost Control:** Department-level budget attribution and enforcement
- **Risk Management:** Policy compliance for customer data processing
- **Examples:** Start with `evaluation_integration.py` for compliance tracking

### 🏥 Healthcare
- **HIPAA Compliance:** Encrypted governance attributes and audit logs
- **Cost Attribution:** Patient care vs. research cost separation
- **Quality Assurance:** Evaluation workflows with governance oversight
- **Examples:** Focus on `production_patterns.py` for compliance automation

### 🏢 Enterprise SaaS
- **Customer Attribution:** Per-customer cost tracking and billing
- **Team Governance:** Department-level budget controls and reporting
- **Feature Development:** A/B testing with cost attribution
- **Examples:** `prompt_management.py` for cost-optimized customer experiences

### 🎓 Research & Education
- **Grant Tracking:** Research project cost attribution and reporting
- **Collaboration:** Multi-team governance with shared resources
- **Evaluation:** Research quality metrics with cost tracking
- **Examples:** `basic_tracking.py` for simple project attribution

---

## 💰 ROI & Business Value

### Small Teams (1-5 developers)
**Investment:** ~2 hours setup  
**Savings:** 20-40% LLM cost reduction through optimization  
**Value:** Clear cost visibility and basic governance

### Growing Teams (5-20 developers)  
**Investment:** ~1 day implementation  
**Savings:** 30-50% cost reduction + 50% faster debugging  
**Value:** Team attribution, budget controls, evaluation workflows

### Enterprise (20+ developers)
**Investment:** ~1 week enterprise deployment  
**Savings:** 40-60% cost reduction + compliance automation  
**Value:** Full governance automation, audit trails, enterprise observability

---

## 🔧 Quick Troubleshooting

### Setup Issues
**❌ "Command not found: python"**
```bash
# On macOS/Linux, try python3
python3 setup_validation.py
```

**❌ "Langfuse API keys not found"**
```bash
# Double-check your environment variables
echo $LANGFUSE_PUBLIC_KEY  # Should start with pk-lf-
echo $LANGFUSE_SECRET_KEY  # Should start with sk-lf-
```

**❌ "No LLM provider API keys found"**
```bash
# Verify at least one provider is configured
echo $OPENAI_API_KEY       # Should be set if using OpenAI
echo $ANTHROPIC_API_KEY    # Should be set if using Anthropic
```

### Advanced Troubleshooting
**❌ Governance integration issues:**
```bash
# Enable detailed logging for diagnosis
export GENOPS_LOG_LEVEL=DEBUG
python basic_tracking.py
```

**❌ Langfuse connectivity problems:**
```bash
# Test direct connectivity
curl -v -H "Authorization: Bearer $LANGFUSE_PUBLIC_KEY" \
     "$LANGFUSE_BASE_URL/api/public/health"
```

---

## 🆘 Need Help?

### 📚 Documentation
- **[5-Minute Quickstart Guide](../../docs/langfuse-quickstart.md)** - Fastest way to get started
- **[Complete Integration Guide](../../docs/integrations/langfuse.md)** - Comprehensive reference
- **[CLAUDE.md](../../CLAUDE.md)** - Development standards and patterns

### 💬 Community Support  
- **[GitHub Issues](https://github.com/KoshiHQ/GenOps-AI/issues)** - Bug reports and feature requests
- **[GitHub Discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)** - Community questions and sharing

### 🚀 Professional Services
For enterprise deployments, custom integrations, or professional services, contact our team for dedicated support.

---

## 🌟 What's Next?

### After Level 1 (Basic Understanding):
1. **Integrate with your application:** Use patterns from `basic_tracking.py`
2. **Set up team attribution:** Configure governance attributes for your teams
3. **Monitor cost trends:** Watch your Langfuse dashboard for governance insights

### After Level 2 (Advanced Features):
1. **Deploy evaluation workflows:** Implement patterns from `evaluation_integration.py`
2. **Optimize prompts:** Use cost intelligence from `prompt_management.py`
3. **Set up A/B testing:** Create governance-aware prompt experiments

### After Level 3 (Enterprise Ready):
1. **Production deployment:** Follow `production_patterns.py` guidance
2. **Enterprise integration:** Connect to your existing observability stack
3. **Team training:** Share governance patterns across your organization

---

**🎉 Ready to enhance your Langfuse observability with GenOps governance?**

**Start your journey:** `python setup_validation.py`