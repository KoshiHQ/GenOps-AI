# LlamaIndex Quickstart Guide

**⚡ 5-Minute Time-to-Value Guarantee**

Get GenOps cost tracking and governance working with LlamaIndex RAG pipelines in exactly 5 minutes or less. **This follows the GenOps Progressive Complexity Architecture**: immediate value first, then progressive mastery.

## 🔧 Prerequisites (2 minutes)

**Before starting, you need:**

1. **LLM API Key**: Get your API key from [OpenAI](https://platform.openai.com/api-keys), [Anthropic](https://console.anthropic.com/), or [Google AI](https://makersuite.google.com/app/apikey)
2. **Python Environment**: Python 3.8+ with pip installed

**⚠️ Cost Notice**: RAG operations vary by model and complexity - text models start at ~$0.001/1K tokens, embeddings ~$0.0001/1K tokens. Most examples cost under $0.01.

## ⚡ Zero-Code Setup (30 seconds)

```bash
# Install GenOps with LlamaIndex support
pip install genops-ai[llamaindex]

# Set your API key (choose one)
export OPENAI_API_KEY="sk-your-openai-key-here"
# OR
export ANTHROPIC_API_KEY="sk-ant-your-anthropic-key-here"
# OR  
export GOOGLE_API_KEY="your-google-api-key-here"
```

## 🎯 Immediate Value Demo (2 minutes)

**Copy-paste this working RAG example:**

```python
from genops.providers.llamaindex import auto_instrument
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Enable automatic instrumentation (zero code changes needed!)
auto_instrument()

# Configure LlamaIndex (your existing setup)
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding()

# Create some sample data
import tempfile
import os
with tempfile.TemporaryDirectory() as temp_dir:
    # Create a sample document
    doc_path = os.path.join(temp_dir, "sample.txt")
    with open(doc_path, "w") as f:
        f.write("""
        GenOps is an open-source framework for AI governance and cost tracking.
        It provides comprehensive observability for RAG pipelines, including
        embedding costs, retrieval performance, and synthesis quality metrics.
        GenOps integrates seamlessly with LlamaIndex for production-ready AI applications.
        """)
    
    # Your existing RAG code works unchanged and is now tracked
    documents = SimpleDirectoryReader(temp_dir).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    
    response = query_engine.query("What is GenOps and how does it help with AI governance?")
    
    print("✅ Success! Your LlamaIndex RAG pipeline now includes GenOps cost tracking!")
    print(f"🤖 Response: {response}")
    print("📊 Cost and performance data automatically exported to your observability platform")
```

## 🚀 Add Team Attribution (1 minute)

**Track costs by team, project, and customer with comprehensive RAG monitoring:**

```python
from genops.providers.llamaindex import instrument_llamaindex, create_llamaindex_cost_context
from llama_index.core import VectorStoreIndex, Document, Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Create adapter with governance defaults
adapter = instrument_llamaindex(
    team="ai-research",
    project="rag-system", 
    customer_id="internal-demo"
)

# Configure LlamaIndex
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding()

# Sample documents
documents = [
    Document(text="LlamaIndex is a framework for building RAG applications with LLMs."),
    Document(text="GenOps provides cost tracking and governance for AI workloads."),
    Document(text="Vector databases enable semantic search for document retrieval.")
]

# Create index and query engine with automatic governance
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Track complete RAG workflow with cost context
with create_llamaindex_cost_context("rag_demo", budget_limit=1.0) as cost_context:
    
    # Query 1: Simple question
    response1 = adapter.track_query(
        query_engine, 
        "What is LlamaIndex?",
        team="ai-research",
        project="rag-system"
    )
    
    # Query 2: Complex question  
    response2 = adapter.track_query(
        query_engine,
        "How does GenOps help with cost tracking in RAG applications?",
        team="ai-research", 
        project="cost-optimization"
    )
    
    print(f"💬 Response 1: {response1.response}")
    print(f"💬 Response 2: {response2.response}")
    
    # Get comprehensive cost summary
    summary = cost_context.get_current_summary()
    print(f"\n💰 Total RAG Cost: ${summary.total_cost:.6f}")
    print(f"📊 Operations: {summary.operation_count}")
    print(f"🔍 Retrieval Operations: {summary.cost_breakdown.retrieval_operations}")
    print(f"🧠 Embedding Tokens: {summary.cost_breakdown.embedding_tokens}")
    print(f"⚡ Synthesis Tokens: {summary.cost_breakdown.synthesis_tokens}")
    print(f"🏷️ Team: ai-research | Project: rag-system")
```

## ✅ Validation (1 minute)

**Verify everything is working:**

```python
from genops.providers.llamaindex.validation import validate_setup, print_validation_result

# Comprehensive setup check with actionable fixes
result = validate_setup()

if result.success:
    print("🎉 GenOps LlamaIndex setup is ready!")
    print("➡️ Your RAG pipelines will now include comprehensive cost tracking and governance")
else:
    print("❌ Setup issues found:")
    print_validation_result(result, detailed=True)
```

## 🎯 What Just Happened?

- **✅ Zero-code auto-instrumentation** - Your existing LlamaIndex code is now automatically tracked
- **💰 Real-time cost tracking** - Every RAG operation shows accurate costs (embeddings + retrieval + synthesis)
- **🏷️ Team attribution** - Costs automatically attributed to teams, projects, and customers
- **📊 OpenTelemetry export** - Data flows to your existing observability platform
- **🎯 RAG optimization** - Built-in recommendations for embedding, retrieval, and synthesis efficiency

## 🚨 Quick Troubleshooting

**Most issues are solved by checking these common problems:**

| Problem | Quick Fix | Why This Happens |
|---------|-----------|-------------------|
| `ImportError: llama_index` | `pip install llama-index>=0.10.0` | LlamaIndex package not installed |
| `API key not found` | `export OPENAI_API_KEY="sk-your-key"` | Environment variable not set correctly |
| `No module named 'openai'` | `pip install openai anthropic` | Provider packages missing |
| `Settings not configured` | Set `Settings.llm` and `Settings.embed_model` | LlamaIndex needs both LLM and embedding models |
| No cost data appearing | This is normal for local development | Costs are calculated locally, telemetry is optional |
| "Invalid API key" | Check your key at provider's website | API key may be incorrect or expired |

**🔧 Advanced Diagnostics**: Run this for detailed setup validation:
```python
from genops.providers.llamaindex.validation import validate_setup, print_validation_result
result = validate_setup()
print_validation_result(result, detailed=True)
```

## 🚀 Progressive Learning Path (GenOps Developer Experience Standard)

**🎯 Phase 1: Immediate Value (≤ 5 minutes) - COMPLETE! ✅**
You've just completed the 5-minute quickstart. You now have working GenOps RAG tracking.

**🎯 Phase 2: RAG Pipeline Optimization (≤ 30 minutes)**
Ready to add advanced RAG monitoring and multi-provider optimization? Continue here:
```bash
python examples/llamaindex/rag_pipeline_tracking.py      # Comprehensive RAG monitoring
python examples/llamaindex/auto_instrumentation.py      # Zero-code setup patterns
```
*Time estimate: 15-30 minutes*

**🎯 Phase 3: Production Mastery (≤ 2 hours)**
Ready for advanced agent workflows and production deployment?
```bash
python examples/llamaindex/advanced_agent_governance.py  # Agent cost tracking
python examples/llamaindex/multi_modal_rag.py           # Complex RAG workflows
```
*Time estimate: 1-2 hours*

**📚 Documentation by Experience Level:**
- **Phase 2 (30-min)**: [`examples/llamaindex/README.md`](../examples/llamaindex/) - Complete practical guide
- **Phase 3 (2-hr)**: [`docs/integrations/llamaindex.md`](integrations/llamaindex.md) - Full reference and advanced patterns

---

## 🎉 Success! You're Now Tracking RAG Costs

**Your GenOps LlamaIndex integration is complete.** Every RAG operation is now:
- ✅ Automatically tracked with accurate costs across all components (embeddings, retrieval, synthesis)
- ✅ Attributed to teams and projects for governance
- ✅ Exported to your observability platform
- ✅ Optimized with intelligent recommendations for embedding, retrieval, and model selection

**Questions?** Join our [community discussions](https://github.com/KoshiHQ/GenOps-AI/discussions) or check the [examples directory](../examples/llamaindex/).

## 📚 Related Documentation

- **[Examples Directory](../examples/llamaindex/)** - Step-by-step practical examples with clear progression
- **[Complete Integration Guide](integrations/llamaindex.md)** - Full API reference and advanced patterns  
- **[Security Best Practices](security-best-practices.md)** - Production security guidance
- **[CI/CD Integration Guide](ci-cd-integration.md)** - Automated testing and deployment patterns

---

## 🔍 Advanced Features Preview

### Multi-Modal RAG Monitoring
```python
from genops.providers.llamaindex import create_rag_monitor

# Advanced RAG pipeline monitoring
rag_monitor = create_rag_monitor(
    enable_quality_metrics=True,
    enable_performance_profiling=True
)

with rag_monitor.monitor_rag_operation("complex_query", team="research") as monitor:
    # Automatic tracking of all RAG components
    response = query_engine.query("Complex multi-step question")
    
    # Get detailed analytics
    analytics = rag_monitor.get_analytics()
    print(f"Retrieval Relevance: {analytics.avg_retrieval_relevance}")
    print(f"Response Time: {analytics.avg_response_time_ms}ms")
```

### Agent Workflow Governance
```python
from llama_index.core.agent import ReActAgent

# Track agent workflows with cost attribution
agent = ReActAgent.from_tools(tools, llm=Settings.llm)
instrumented_agent = adapter.instrument_agent(
    agent,
    team="ai-agents",
    project="customer-support"
)

response = adapter.track_chat(
    instrumented_agent,
    "Help me analyze this document and create a summary",
    customer_id="enterprise-123"
)
```

### Budget-Constrained Operations
```python
# Set budget limits for RAG operations
with create_llamaindex_cost_context("production_rag", budget_limit=10.0, enable_alerts=True) as context:
    for query in user_queries:
        if context.total_cost < context.budget_limit * 0.9:  # 90% threshold
            response = adapter.track_query(query_engine, query)
        else:
            print("⚠️ Approaching budget limit - switching to cheaper model")
            # Switch to cost-optimized configuration
```

Ready to explore these advanced features? Continue with the **Phase 2** examples!