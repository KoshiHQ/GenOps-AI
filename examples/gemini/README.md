# Google Gemini GenOps Examples

**🎯 New here? [Skip to: Where do I start?](#where-do-i-start) | 📚 Need definitions? [Skip to: What do these terms mean?](#what-do-these-terms-mean)**

---

## 🌟 **Where do I start?**

**👋 First time with GenOps + Gemini? Answer one question:**

❓ **Do you have existing Gemini code that you want to add cost tracking to?**
- **✅ YES** → Jump to Phase 2: [`auto_instrumentation.py`](#auto_instrumentationpy---phase-2) (15 min)
- **❌ NO** → Start with Phase 1: [`hello_genops_minimal.py`](#hello_genops_minimalpy---start-here---phase-1) (30 sec)

❓ **Are you a manager/non-technical person?**
- Read ["What GenOps does"](#what-genops-does) then watch your team run the examples

❓ **Are you deploying to production?**
- Start with [Phase 1](#phase-1-immediate-value--5-minutes-) for concepts, then jump to [Production Deployment](#production-deployment-scenarios-claude-md-section-6)

❓ **Having errors or issues?**
- Jump straight to [Perfect Error Resolution Guide](#perfect-error-resolution-guide-claude-md-standard)

---

## 📖 **What do these terms mean?**

**New to AI/GenOps? Here are the key terms you'll see:**

**🧠 Essential AI Terms:**
- **Gemini**: Google's AI models (like ChatGPT but from Google)
- **Prompt**: The text you send to ask the AI something  
- **Token**: Unit of AI processing (roughly 4 characters of text)
- **Model**: Different AI "brains" - Flash (fast/cheap), Pro (smart/expensive), Flash-Lite (cheapest)

**📊 GenOps Terms (the main concept):**
- **GenOps**: Cost tracking + team budgets for AI (like monitoring for websites, but for AI)
- **Instrumentation**: Adding tracking to your AI code (GenOps does this automatically)
- **Cost Attribution**: Knowing which team/project spent what on AI
- **Governance**: Rules and budgets to control AI spending

**That's it! You know enough to get started.**

---

## 🧭 **Your Learning Journey**

**This directory implements a 30 seconds → 30 minutes → 2 hours learning path:**

### 🎯 **Phase 1: Prove It Works (30 seconds)** ⚡
**Goal**: See GenOps tracking your Gemini calls - build confidence first

**What you'll learn**: GenOps automatically tracks AI costs  
**What you need**: API key from Google AI Studio  
**Success**: See "✅ SUCCESS! GenOps is now tracking" message

**Next**: Once you see it work → Phase 2 for team tracking

---

### 🏗️ **Phase 2: Add Team Tracking (15-30 minutes)** 🚀  
**Goal**: Track which teams/projects spend what on AI

**What you'll learn**: Cost attribution, governance attributes, retrofitting existing apps  
**What you need**: Basic Python knowledge  
**Success**: See cost breakdowns by team/project

**Next**: Once you understand team tracking → Phase 3 for production

---

### 🎓 **Phase 3: Production Ready (1-2 hours)** 🏛️
**Goal**: Deploy with monitoring, optimization, and enterprise features

**What you'll learn**: Multi-model optimization, Docker/Kubernetes deployment, monitoring  
**What you need**: Production deployment experience  
**Success**: Running in production with cost optimization

**Next**: You're now a GenOps expert! 🎉

---

**Having Issues?** → [Troubleshooting](#troubleshooting) | **Skip Ahead?** → [Phase Navigation](#phase-navigation)

## 📋 Examples by Progressive Phase

### 🎯 **Phase 1: Prove It Works (30 seconds)**

#### [`hello_genops_minimal.py`](hello_genops_minimal.py) ⭐ **START HERE**
✅ **30-second confidence builder** - Just run it and see GenOps tracking your calls

### 🏗️ **Phase 2: Add Team Tracking (15-30 minutes)**

#### [`auto_instrumentation.py`](auto_instrumentation.py) ⭐ **For existing Gemini code**
✅ **Add GenOps to existing apps** - Zero code changes to your current Gemini calls (15 min)

#### [`basic_tracking.py`](basic_tracking.py) ⭐ **For new team projects**
✅ **Team cost attribution** - Track which teams spend what on AI (10 min)

### 🎓 **Phase 3: Production Ready (1-2 hours)**

#### [`cost_optimization.py`](cost_optimization.py) ⭐ **For production deployment**
✅ **Advanced cost optimization** - Multi-model selection, budgets, and monitoring (30 min)

---

**🚀 That's it!** Three examples, three phases, complete GenOps mastery.

## 💡 What You Get

**After completing all phases:**
- ✅ **Cost Tracking**: See exactly how much each AI call costs
- ✅ **Team Attribution**: Know which teams spend what on AI  
- ✅ **Budget Control**: Set limits and get alerts
- ✅ **Zero Code Changes**: Works with your existing Gemini apps

## 🚀 Ready to Start?

**Just pick your situation:**
- **New to GenOps?** → [`hello_genops_minimal.py`](hello_genops_minimal.py)
- **Have existing Gemini code?** → [`auto_instrumentation.py`](auto_instrumentation.py) 
- **Setting up team tracking?** → [`basic_tracking.py`](basic_tracking.py)
- **Going to production?** → [`cost_optimization.py`](cost_optimization.py)

---

## 🛠️ Quick Setup

```bash
# 1. Install
pip install genops-ai[gemini]

# 2. Get API key from https://ai.google.dev/
export GEMINI_API_KEY="your_key_here"

# 3. Run first example
python hello_genops_minimal.py
```

**✅ That's all you need to get started!**

---

## 🆘 Having Issues?

**🔧 Quick fixes for common problems:**
- **`ImportError: genai`** → `pip install google-generativeai`  
- **API key error** → Get free key at https://ai.google.dev/
- **Still stuck?** → Check [`hello_genops_minimal.py`](hello_genops_minimal.py) - it has detailed error messages

---

**🎉 Ready to become a GenOps expert? Start with the 30-second example!**

👉 [`python hello_genops_minimal.py`](hello_genops_minimal.py)

