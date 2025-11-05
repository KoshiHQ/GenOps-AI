# LlamaIndex GenOps Examples

**🎯 New here? [Skip to: Where do I start?](#where-do-i-start) | 📚 Need definitions? [Skip to: What do these terms mean?](#what-do-these-terms-mean)**

---

## 🌟 **Where do I start?**

**👋 First time with GenOps + LlamaIndex? Answer one question:**

❓ **Do you have existing LlamaIndex RAG pipelines that you want to add cost tracking to?**
- **✅ YES** → Jump to Phase 2: [`auto_instrumentation.py`](#auto_instrumentationpy---phase-2) (15 min)
- **❌ NO** → Start with Phase 1: [`hello_genops_minimal.py`](#hello_genops_minimalpy---start-here---phase-1) (30 sec)

❓ **Are you a manager/non-technical person?**
- Read ["What GenOps does"](#what-genops-does) then watch your team run the examples

❓ **Are you deploying to production?**
- Start with [Phase 1](#phase-1-prove-it-works-30-seconds-) for concepts, then jump to [Phase 3](#phase-3-production-ready-1-2-hours-)

❓ **Having errors or issues?**
- Jump straight to [Quick fixes](#having-issues)

---

## 📖 **What do these terms mean?**

**New to RAG/GenOps? Here are the key terms you'll see:**

**🧠 Essential RAG Terms:**
- **RAG**: Retrieval-Augmented Generation - AI that searches documents to answer questions
- **LlamaIndex**: Framework for building RAG applications with document indexing
- **Embedding**: Converting text to numbers for semantic search (costs ~$0.0001/1K tokens)
- **Vector Store**: Database that stores embeddings for fast similarity search
- **Query Engine**: LlamaIndex component that handles question-answering workflows
- **Synthesis**: LLM generating final answers from retrieved context (costs vary by model)

**📊 GenOps Terms (the main concept):**
- **GenOps**: Cost tracking + team budgets for AI (like monitoring for websites, but for RAG)
- **Instrumentation**: Adding tracking to your RAG code (GenOps does this automatically)
- **Cost Attribution**: Knowing which team/project spent what on embeddings, retrieval, synthesis
- **Governance**: Rules and budgets to control RAG pipeline spending

**That's it! You know enough to get started.**

---

## 🧭 **Your Learning Journey**

**This directory implements a 30 seconds → 30 minutes → 2 hours learning path:**

### 🎯 **Phase 1: Prove It Works (30 seconds)** ⚡
**Goal**: See GenOps tracking your RAG pipeline - build confidence first

**What you'll learn**: GenOps automatically tracks RAG costs (embeddings + retrieval + synthesis)  
**What you need**: API token from OpenAI, Anthropic, or Google  
**Success**: See "✅ SUCCESS! GenOps is now tracking" message

**Next**: Once you see it work → Phase 2 for team tracking

---

### 🏗️ **Phase 2: Add RAG Optimization (15-30 minutes)** 🚀  
**Goal**: Track which teams spend what on RAG components with quality monitoring

**What you'll learn**: RAG cost attribution, retrieval optimization, embedding efficiency  
**What you need**: Basic Python knowledge  
**Success**: See cost breakdowns by RAG component and team attribution

**Next**: Once you understand RAG governance → Phase 3 for production

---

### 🎓 **Phase 3: Production Ready (1-2 hours)** 🏛️
**Goal**: Deploy with advanced agent workflows, multi-modal RAG, enterprise features

**What you'll learn**: Agent cost tracking, complex RAG workflows, budget controls  
**What you need**: Production deployment experience  
**Success**: Running production RAG with comprehensive governance and optimization

**Next**: You're now a GenOps + LlamaIndex RAG expert! 🎉

---

**Having Issues?** → [Quick fixes](#having-issues) | **Skip Ahead?** → [Examples](#examples-by-progressive-phase) | **Want Full Reference?** → [Complete Integration Guide](../../docs/integrations/llamaindex.md)

## 📋 Examples by Progressive Phase

### 🎯 **Phase 1: Prove It Works (30 seconds)**

#### [`hello_genops_minimal.py`](hello_genops_minimal.py) ⭐ **START HERE**
✅ **30-second confidence builder** - Just run it and see GenOps tracking your RAG pipeline  
🎯 **What you'll accomplish**: Verify GenOps works with your AI provider and see cost tracking in action  
▶️ **Next step after success**: Move to [`auto_instrumentation.py`](auto_instrumentation.py) to add tracking to existing code

### 🏗️ **Phase 2: Add RAG Optimization (15-30 minutes)**

#### [`auto_instrumentation.py`](auto_instrumentation.py) ⭐ **For existing RAG code**
✅ **Add GenOps to existing apps** - Zero code changes to your current LlamaIndex pipelines (15 min)  
🎯 **What you'll learn**: How `auto_instrument()` works and team cost attribution  
▶️ **Next step**: Try [`rag_pipeline_tracking.py`](rag_pipeline_tracking.py) for detailed monitoring

#### [`rag_pipeline_tracking.py`](rag_pipeline_tracking.py) ⭐ **For new RAG projects**
✅ **Complete RAG monitoring** - Track embeddings, retrieval, synthesis with team attribution (20 min)  
🎯 **What you'll learn**: Cost breakdowns by RAG component and quality metrics  
▶️ **Next step**: Explore [`embedding_cost_optimization.py`](embedding_cost_optimization.py) for efficiency

#### [`embedding_cost_optimization.py`](embedding_cost_optimization.py) ⭐ **For cost optimization**
✅ **Embedding efficiency** - Optimize embedding models and caching strategies (15 min)  
🎯 **What you'll learn**: Reduce embedding costs by 50-80% with smart optimization  
▶️ **Ready for production?**: Move to Phase 3 advanced examples

### 🎓 **Phase 3: Production Ready (1-2 hours)**

#### [`advanced_agent_governance.py`](advanced_agent_governance.py) ⭐ **For agent workflows**
✅ **Agent cost tracking** - Monitor multi-step agent operations with tool usage (45 min)  
🎯 **What you'll learn**: Track complex agent workflows, tool costs, and conversation analytics  
▶️ **Next step**: Try [`multi_modal_rag.py`](multi_modal_rag.py) for document processing

#### [`multi_modal_rag.py`](multi_modal_rag.py) ⭐ **For complex RAG**
✅ **Advanced RAG patterns** - Multi-modal document processing with governance (30 min)  
🎯 **What you'll learn**: Handle PDFs, images, structured data with comprehensive cost tracking  
▶️ **Next step**: Deploy with [`production_rag_deployment.py`](production_rag_deployment.py)

#### [`production_rag_deployment.py`](production_rag_deployment.py) ⭐ **For production**
✅ **Enterprise deployment** - Budget controls, alerts, multi-provider optimization (45 min)  
🎯 **What you'll learn**: Production patterns, Kubernetes deployment, budget enforcement, compliance  
▶️ **You're now ready**: Deploy GenOps RAG governance to production! 🎉

---

**🚀 That's it!** Six examples, three phases, complete GenOps + LlamaIndex RAG mastery.

## 💡 What You Get

**After completing all phases:**
- ✅ **RAG Cost Tracking**: See exactly how much each component costs (embeddings, retrieval, synthesis)
- ✅ **Quality Monitoring**: Track retrieval relevance and synthesis quality across pipelines
- ✅ **Team Attribution**: Know which teams spend what on different RAG operations
- ✅ **Budget Control**: Set limits and get alerts for RAG pipeline costs
- ✅ **Zero Code Changes**: Works with your existing LlamaIndex applications
- ✅ **Multi-Provider Intelligence**: Optimize across OpenAI, Anthropic, Google, local models

---

## 🚀 Ready to Start?

**🎯 Choose Your Path (recommended order):**
1. **New to GenOps?** → [`hello_genops_minimal.py`](hello_genops_minimal.py) *(Start here - 30 seconds)*
2. **Have existing RAG code?** → [`auto_instrumentation.py`](auto_instrumentation.py) *(Add tracking - 15 minutes)*
3. **Want detailed monitoring?** → [`rag_pipeline_tracking.py`](rag_pipeline_tracking.py) *(Full RAG analytics - 20 minutes)*
4. **Need cost optimization?** → [`embedding_cost_optimization.py`](embedding_cost_optimization.py) *(Save 50-80% on embeddings - 15 minutes)*
5. **Ready for production?** → [`production_rag_deployment.py`](production_rag_deployment.py) *(Enterprise patterns - 45 minutes)*

**🔀 Or Jump to Specific Needs:**
- **Agent workflows** → [`advanced_agent_governance.py`](advanced_agent_governance.py)
- **Complex documents** → [`multi_modal_rag.py`](multi_modal_rag.py)
- **Full documentation** → [Complete Integration Guide](../../docs/integrations/llamaindex.md)

---

## 🛠️ Quick Setup

```bash
# 1. Install
pip install genops-ai[llamaindex]

# 2. Get API token (choose one)
export OPENAI_API_KEY="sk-your-openai-key-here"
# OR
export ANTHROPIC_API_KEY="sk-ant-your-anthropic-key-here"  
# OR
export GOOGLE_API_KEY="your-google-api-key-here"

# 3. Run first example
python hello_genops_minimal.py
```

**✅ That's all you need to get started!**

---

## 🆘 Having Issues?

**🔧 Quick fixes for common problems:**

**Installation Issues:**
- **`ImportError: llama_index`** → `pip install llama-index>=0.10.0`
- **`No module named 'openai'`** → `pip install openai anthropic google-generativeai`
- **Version conflicts** → `pip install --upgrade genops-ai[llamaindex]`

**API Configuration:**
- **API token error** → Set API key: `export OPENAI_API_KEY="sk-your-key"`
- **"No API key found"** → Make sure you export the key in your terminal before running Python
- **"Invalid API key"** → Check your key at [OpenAI Platform](https://platform.openai.com/api-keys)

**LlamaIndex Configuration:**
- **Settings not configured** → Check examples - they configure `Settings.llm` and `Settings.embed_model`
- **"LLM not set"** → Run `Settings.llm = OpenAI(model="gpt-3.5-turbo")` before creating indexes
- **"Embedding model not set"** → Run `Settings.embed_model = OpenAIEmbedding()` before creating indexes

**GenOps Specific:**
- **No cost data appearing** → Check if telemetry endpoint is configured (optional for local development)
- **"Team attribution not working"** → Ensure you pass governance attributes like `team="your-team"`
- **Still stuck?** → Check [`hello_genops_minimal.py`](hello_genops_minimal.py) - it has detailed error messages and diagnostics

**💡 Pro Tip**: Run the validation script to check your setup:
```python
from genops.providers.llamaindex.validation import validate_setup, print_validation_result
result = validate_setup()
print_validation_result(result, detailed=True)
```

---

## 🎯 What GenOps Does

**For managers and non-technical folks:**

GenOps is like having a **cost meter** and **performance monitor** for your AI systems:

**💰 Cost Tracking**
- See exactly how much your RAG pipelines cost to run
- Break down costs by team, project, and customer
- Get alerts when spending approaches budget limits
- Compare costs across different AI models and providers

**📊 Quality Monitoring**
- Monitor how well your RAG system retrieves relevant documents
- Track the quality of AI-generated responses
- Identify performance bottlenecks in your pipelines
- Get recommendations for optimization

**🏛️ Governance & Control**
- Set budget limits for different teams and projects
- Ensure compliance with cost and usage policies
- Track which teams are using which AI models
- Generate reports for finance and management

**🔧 Zero Disruption**
- Works with existing LlamaIndex applications
- No need to rewrite code or change workflows
- Integrates with your current monitoring systems
- Provides immediate value without migration

**Think of it as "Google Analytics for AI" - you get comprehensive insights into how your AI systems are performing and what they cost to run.**

---

**🎉 Ready to become a GenOps + LlamaIndex RAG expert?**

**📚 Complete Learning Path:**
1. **30 seconds**: [`python hello_genops_minimal.py`](hello_genops_minimal.py) - Prove it works
2. **15 minutes**: [`python auto_instrumentation.py`](auto_instrumentation.py) - Add to existing code  
3. **30 minutes**: [`python rag_pipeline_tracking.py`](rag_pipeline_tracking.py) - Comprehensive monitoring
4. **1-2 hours**: Choose from Phase 3 examples based on your needs

**🚀 Quick Start**: `python hello_genops_minimal.py`

## 📚 Documentation & Resources

**📖 Complete Guides:**
- **[5-Minute Quickstart](../../docs/llamaindex-quickstart.md)** - Get running in 5 minutes with copy-paste examples
- **[Complete Integration Guide](../../docs/integrations/llamaindex.md)** - Full API reference, advanced patterns, and production deployment
- **[Security Best Practices](../../docs/security-best-practices.md)** - Enterprise security and compliance guidance
- **[CI/CD Integration](../../docs/ci-cd-integration.md)** - Automated testing, deployment, and cost monitoring

**🤝 Community & Support:**
- **[GitHub Discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)** - Questions, ideas, and community help
- **[GitHub Issues](https://github.com/KoshiHQ/GenOps-AI/issues)** - Bug reports and feature requests