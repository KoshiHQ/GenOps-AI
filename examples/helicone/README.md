# Helicone AI Gateway Examples

This directory contains comprehensive examples demonstrating GenOps governance telemetry integration with Helicone AI Gateway applications for multi-provider AI operations.

## 🌐 What is Helicone?

**Helicone is an AI gateway** that provides unified access to 100+ AI models across multiple providers through a single API. Think of it as a smart router and cost optimizer for your AI operations.

### Why Use Helicone + GenOps?

- **🔄 One API, 100+ Models**: Access OpenAI, Anthropic, Vertex AI, Groq, and more through single interface
- **💰 Cost Optimization**: Intelligent routing strategies to minimize AI spend across providers
- **🛡️  Built-in Reliability**: Automatic failover, load balancing, and provider switching
- **📊 Unified Analytics**: Comprehensive usage and performance monitoring across all providers
- **🏛️  Enterprise Governance**: Team cost attribution, budget controls, and compliance tracking

**Perfect for**: Teams using multiple AI providers, cost-conscious applications, enterprise AI deployments.

## 🚀 Quick Start

### Prerequisites

Before running these examples, you need:

**1. Install GenOps with Helicone support:**
```bash
pip install genops[helicone]
```

**2. Get your Helicone API key:**
- Sign up at [helicone.ai](https://app.helicone.ai/) (free tier available)
- Get your API key from the dashboard

**3. Configure at least one AI provider:**
```bash
# Required: Helicone gateway key
export HELICONE_API_KEY="your_helicone_api_key"

# At least one provider required (choose any):
export OPENAI_API_KEY="your_openai_api_key"          # Get from platform.openai.com
export ANTHROPIC_API_KEY="your_anthropic_api_key"    # Get from console.anthropic.com  
export GROQ_API_KEY="your_groq_api_key"              # Get from console.groq.com (free tier!)
```

### Validate Your Setup (30 seconds)

Run this first to ensure everything is configured correctly:

```bash
python setup_validation.py
```

You should see: ✅ **Overall Status: PASSED**

## 📚 Examples by Complexity

### Level 1: Getting Started (5 minutes each)

Perfect for first-time users to understand the basics:

**[setup_validation.py](setup_validation.py)** ⭐ *Start here*
- Verify your Helicone + GenOps setup across multiple providers
- Validate API keys, gateway connectivity, and basic functionality
- Get immediate feedback on configuration issues with actionable fixes
- Test provider availability and performance

**[basic_tracking.py](basic_tracking.py)**
- Simple multi-provider chat completions through Helicone gateway
- Introduction to unified cost tracking across providers
- Governance attributes for cross-provider cost attribution
- Minimal code changes for maximum multi-provider capability

**[auto_instrumentation.py](auto_instrumentation.py)**
- Zero-code setup using GenOps auto-instrumentation with Helicone
- Automatic routing and cost tracking for existing AI applications
- Drop-in gateway integration with no code changes required

### Level 2: Multi-Provider Intelligence (30 minutes each)

Build expertise in cost optimization and provider management:

**[multi_provider_costs.py](multi_provider_costs.py)**
- Cross-provider cost comparison (OpenAI vs. Anthropic vs. Groq vs. Vertex)
- Real-time cost aggregation and provider cost analytics
- Gateway fee analysis and total cost optimization
- Provider migration cost analysis and recommendations

**[cost_optimization.py](cost_optimization.py)**
- Intelligent routing strategies for cost optimization
- Dynamic provider and model selection based on cost constraints
- Budget management and cost alerts across multiple providers
- Performance vs cost trade-off analysis

### Level 3: Advanced Gateway Features (2 hours each)

Master enterprise-grade features and deployment patterns:

**[advanced_features.py](advanced_features.py)**
- Intelligent routing strategies: cost-optimized, performance-optimized, failover
- Multi-provider streaming responses with unified telemetry
- Custom routing logic and provider selection algorithms
- Advanced cost intelligence and optimization recommendations

**[production_patterns.py](production_patterns.py)**
- Enterprise-ready Helicone gateway deployment patterns
- High-availability multi-provider configurations
- Context managers for complex multi-provider workflows
- Policy enforcement and governance automation across providers
- Self-hosted gateway integration patterns

## 🎯 Use Case Examples

Each example includes:
- ✅ **Complete working code** you can run immediately
- ✅ **Multi-provider demonstrations** with unified governance
- ✅ **Cost optimization strategies** across different providers
- ✅ **Gateway intelligence** showcasing routing and failover
- ✅ **Error handling** and graceful degradation
- ✅ **Performance considerations** for production deployments
- ✅ **Comments explaining** GenOps + Helicone integration points

## 🏃 Running Examples

### Option 1: Run Individual Examples

```bash
# Level 1: Getting Started (5 minutes each)
python setup_validation.py      # ⭐ Start here - validate your setup
python basic_tracking.py        # Simple multi-provider tracking
python auto_instrumentation.py  # Zero-code gateway integration

# Level 2: Multi-Provider Intelligence (30 minutes each)
python multi_provider_costs.py  # Cross-provider cost comparison
python cost_optimization.py     # Intelligent routing and optimization

# Level 3: Advanced Gateway Features (2 hours each)
python advanced_features.py     # Advanced routing and streaming
python production_patterns.py   # Enterprise deployment patterns
```

### Option 2: Run Complete Suite

```bash
# Run all examples with comprehensive validation (~15 minutes)
./run_all_examples.sh
```

## 📊 What You'll Learn

### Multi-Provider AI Gateway Mastery
- How to access 100+ AI models through a unified interface
- Cost optimization strategies across different providers
- Intelligent routing for performance and reliability
- Real-time cost tracking and budget management

### GenOps Governance Excellence  
- Cross-provider cost attribution and team tracking
- Unified telemetry across your entire AI stack
- Policy enforcement and compliance automation
- Enterprise-ready governance patterns

### Production Deployment Patterns
- High-availability multi-provider configurations
- Self-hosted gateway deployment strategies
- Performance optimization and scaling considerations
- Integration with existing observability platforms

## 🔍 Troubleshooting

### Common Issues

**❌ "Helicone API key not found"**
```bash
# Get your key from https://app.helicone.ai/
export HELICONE_API_KEY="your_helicone_api_key"
```

**❌ "No provider API keys found"**
```bash
# Configure at least one provider:
export OPENAI_API_KEY="your_openai_key"     # Or
export ANTHROPIC_API_KEY="your_anthropic_key" # Or  
export GROQ_API_KEY="your_groq_key"         # Free tier available!
```

**❌ Gateway connection issues:**
```bash
# Test gateway connectivity
curl -H "Helicone-Auth: Bearer $HELICONE_API_KEY" https://ai-gateway.helicone.ai/v1/health
```

**❌ Import errors:**
```bash
# Ensure correct installation
pip install genops[helicone]
```

**❌ Cost tracking issues:**
```bash
# Enable detailed logging
export GENOPS_LOG_LEVEL=DEBUG
python basic_tracking.py
```

### Need Help?

- 📚 **Comprehensive Guide**: [GenOps Helicone Integration Guide](../../docs/integrations/helicone.md)
- 🚀 **Quick Start**: [5-Minute Helicone Quickstart](../../docs/helicone-quickstart.md)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/KoshiHQ/GenOps-AI/issues)
- 💬 **Community Support**: Join our developer community

## 🌟 Next Steps

After running these examples:

1. **Start Simple**: Use patterns from `basic_tracking.py` in your applications
2. **Optimize Costs**: Implement strategies from `cost_optimization.py`
3. **Add Governance**: Apply patterns from `production_patterns.py`
4. **Scale Up**: Follow guidance in our [comprehensive integration guide](../../docs/integrations/helicone.md)

## 🎯 Decision Guide: When to Use Helicone

**✅ Use Helicone + GenOps when you:**
- Want to access multiple AI providers through single API
- Need cost optimization across different providers
- Require enterprise governance and cost attribution
- Want built-in failover and reliability
- Need comprehensive analytics across all AI operations

**🤔 Consider alternatives when you:**
- Only use one AI provider (direct integration may be simpler)
- Have very simple use cases with no cost optimization needs
- Require specialized features only available in direct provider APIs

---

**Ready to get started?** Run `python setup_validation.py` to validate your setup and begin your GenOps + Helicone journey!