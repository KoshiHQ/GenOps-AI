---
name: Provider integration request
about: Request support for a new AI provider
title: '[PROVIDER] Add support for '
labels: provider, enhancement
assignees: ''
---

## 🔌 **Provider Integration Request**

Request for GenOps AI to support a new AI provider.

## 📋 **Provider Information**

### **Basic Details**
- **Provider Name**: [e.g., AWS Bedrock, Google Gemini, Hugging Face]
- **Provider Website**: [URL]
- **Python SDK**: [Package name and PyPI link]
- **SDK Version**: [Current stable version]
- **API Documentation**: [Link to API docs]

### **Provider Capabilities**
- [ ] **Text Generation** (Chat/completion APIs)
- [ ] **Text Embeddings** (Vector generation)
- [ ] **Image Generation** (DALL-E style APIs)
- [ ] **Fine-tuning** (Custom model training)
- [ ] **Function Calling** (Tool use/agents)
- [ ] **Streaming** (Real-time response streaming)
- [ ] **Other**: [Specify other capabilities]

## 🤖 **Available Models**

List the key models this provider offers:

### **Text Generation Models**
| Model Name | Context Length | Cost per 1K Input Tokens | Cost per 1K Output Tokens |
|------------|----------------|---------------------------|----------------------------|
| [model-1]  | [8k/32k/etc]   | $[0.001]                 | $[0.002]                  |
| [model-2]  | [8k/32k/etc]   | $[0.005]                 | $[0.010]                  |

### **Other Models** (if applicable)
- **Embedding Models**: [List with dimensions and pricing]
- **Image Models**: [List with pricing per image]

## 🏢 **Business Context**

### **Why is this provider important?**
- [ ] **Market Share** - Widely used in industry
- [ ] **Enterprise Adoption** - Popular with enterprise customers
- [ ] **Unique Capabilities** - Offers features not available elsewhere
- [ ] **Cost Effectiveness** - More cost-effective option
- [ ] **Regional Requirements** - Needed for specific geographic regions
- [ ] **Compliance** - Required for regulatory compliance

### **Use Cases**
What are the primary use cases for this provider?

1. **[Use Case 1]**: [Description of how this provider is used]
2. **[Use Case 2]**: [Description of specific scenarios]
3. **[Use Case 3]**: [Enterprise or compliance requirements]

## 📊 **Usage & Demand**

### **Community Interest**
- [ ] **High demand** in community discussions/issues
- [ ] **Multiple requests** for this provider
- [ ] **Enterprise customers** have requested this
- [ ] **Personal/team need** for this integration

### **Your Use Case**
- **Team Size**: [How many developers would use this?]
- **Volume**: [Approximate monthly API calls]
- **Models**: [Which specific models would you use?]
- **Governance Needs**: [Cost tracking, policies, compliance requirements]

## 🛠️ **Technical Information**

### **SDK Installation**
```bash
# How to install the provider's Python SDK
pip install [provider-package]
```

### **Basic Usage Example**
```python
# Provide a simple example of how this provider is typically used
import provider_sdk

client = provider_sdk.Client(api_key="...")
response = client.generate(
    model="model-name",
    prompt="Hello world",
    max_tokens=100
)

print(response.text)
print(f"Tokens used: {response.usage.total_tokens}")
```

### **Authentication**
How does this provider handle authentication?
- [ ] **API Key** (Header/query param)
- [ ] **OAuth** (Token-based authentication)
- [ ] **IAM/Role-based** (Cloud provider authentication)
- [ ] **Custom** (Describe method)

### **Rate Limiting**
- **Rate Limits**: [Requests per minute/hour limits]
- **Pricing Model**: [Per-token, per-request, subscription, etc.]
- **Free Tier**: [Any free usage allowances]

## 🎯 **GenOps Integration Requirements**

### **Essential Features**
- [ ] **Cost Tracking** - Track costs per request with accurate pricing
- [ ] **Token Counting** - Input/output token usage tracking
- [ ] **Error Handling** - Graceful handling of API failures
- [ ] **Auto-instrumentation** - Support for `genops.init()`
- [ ] **Manual Instrumentation** - Support for explicit adapter usage

### **Advanced Features** (Nice to have)
- [ ] **Streaming Support** - Handle real-time streaming responses
- [ ] **Async Support** - Support for asyncio-based usage
- [ ] **Batch Operations** - Handle batch API calls
- [ ] **Function Calling** - Support for tool use/agent patterns
- [ ] **Fine-tuning Costs** - Track training and inference costs separately

### **Governance Requirements**
- [ ] **Policy Enforcement** - Support for cost limits and content filtering
- [ ] **Budget Tracking** - Integration with budget management
- [ ] **Audit Trails** - Comprehensive request/response logging
- [ ] **Multi-tenant** - Support for customer/team attribution

## 🔬 **Implementation Notes**

### **Unique Characteristics**
Are there any unique aspects of this provider that affect implementation?

- **Pricing Model**: [Any unusual pricing structures?]
- **Token Calculation**: [How are tokens counted?]
- **Response Format**: [Any unique response structures?]
- **API Patterns**: [Any non-standard API patterns?]

### **Potential Challenges**
- **Rate Limiting**: [Any unusual rate limiting behavior?]
- **Authentication**: [Complex authentication requirements?]
- **Cost Calculation**: [Challenges in accurate cost tracking?]
- **Model Variations**: [Many models with different pricing?]

## 📚 **Reference Materials**

### **Documentation Links**
- **API Documentation**: [Link]
- **Python SDK Documentation**: [Link]
- **Pricing Information**: [Link]
- **Rate Limit Documentation**: [Link]

### **Example Projects**
- **Official Examples**: [Links to provider's example code]
- **Community Projects**: [Links to popular projects using this provider]
- **Integration Examples**: [Similar integrations in other tools]

## 🤝 **Contribution Interest**

### **Your Involvement**
- [ ] **I can help implement** this provider adapter
- [ ] **I can help test** the implementation
- [ ] **I can provide** domain expertise and requirements
- [ ] **I can help document** the integration
- [ ] **I have access** to this provider's APIs for testing

### **Timeline**
- **Urgency**: [When would you need this integration?]
- **Availability**: [When could you help with implementation?]

## ✅ **Acceptance Criteria**

For this provider integration to be considered complete:

- [ ] **Provider adapter** implemented following GenOps patterns
- [ ] **Accurate cost calculation** for all supported models
- [ ] **Comprehensive tests** with mock provider responses
- [ ] **Auto-instrumentation support** integrated
- [ ] **Documentation** with examples and pricing information
- [ ] **Error handling** for common failure scenarios

## 🔗 **Related**

- Link to any existing issues or discussions
- Reference similar provider implementations
- Mention any blocking dependencies