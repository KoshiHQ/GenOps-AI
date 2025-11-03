<p align="center">
  <img width="500" src="./assets/brand/genops-logo-optimized.jpg" alt="GenOps: Open Runtime Governance for AI Systems" style="max-width: 100%;">
</p>

# 🧭 GenOps: Open Runtime Governance for AI Systems

GenOps is an open-source runtime governance framework for AI and LLM workloads — built on [OpenTelemetry](https://opentelemetry.io) and FinOps standards.

<div align="center">
  
  [![GitHub stars](https://img.shields.io/github/stars/KoshiHQ/GenOps-AI?style=social)](https://github.com/KoshiHQ/GenOps-AI/stargazers)
  [![CI Status](https://img.shields.io/github/actions/workflow/status/KoshiHQ/GenOps-AI/ci.yml?branch=main)](https://github.com/KoshiHQ/GenOps-AI/actions)  
  [![PyPI version](https://badge.fury.io/py/genops.svg)](https://badge.fury.io/py/genops)
  [![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
  [![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
  [![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
  [![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-native-purple.svg)](https://opentelemetry.io/)

</div>

---

## 🚨 The Problem: AI Is Powerful, Opaque, and Ungoverned

AI is now core to production systems — yet most organizations are flying blind.  
Costs are rising, but that's just one symptom of a deeper governance gap.

- 💸 **Unpredictable costs** — Token usage explodes without accountability
- ⚖️ **Policy drift** — Teams deploy new models with no enforcement or oversight  
- 🔍 **Observability silos** — Logs, metrics, and traces don't connect to governance
- 🔒 **Compliance blind spots** — No runtime record of who did what, where, or why
- 🤖 **Shadow AI** — Models and prompts operate outside organizational control

The result: AI systems that are functional but unaccountable — and teams that can't answer:

**"What ran, under whose authority, and at what cost — financial, ethical, or operational?"**

Without runtime governance, AI becomes a black box: costly, risky, and impossible to trust at scale.

## 👥 Who This Is For

GenOps sits where DevOps, FinOps, and RiskOps converge — aligning engineering, finance, and compliance around a single source of operational truth.

| **Stakeholder** | **Core Need** | **What GenOps Provides** |
|------------------|---------------|---------------------------|
| **CTOs / Heads of Platform** | Visibility into AI usage, cost, and risk across the enterprise | A unified control plane for runtime governance and observability |
| **DevOps / Platform Engineers** | Integration with existing telemetry and infra tooling | OpenTelemetry-native instrumentation and tracing |
| **FinOps Teams** | Transparent attribution by team, customer, and feature | Per-request cost tracking and budget enforcement |
| **Compliance & Risk Teams** | Runtime audit trails and data residency assurance | Policy telemetry and enforcement hooks with OPA compatibility |
| **Product & AI Teams** | Safe experimentation with production accountability | Governance-aware SDKs and cost-aware routing intelligence |

GenOps gives each of these roles shared visibility into AI behavior in production —  
**turning runtime data into governance, and governance into trust.**

---

## 💡 The GenOps Solution

GenOps provides cost, policy, and compliance telemetry across your AI stack, enabling teams to:

- **Track spend and efficiency** across models, teams, and customers
- **Enforce usage policies** and model governance in real time  
- **Integrate with existing** observability, billing, and compliance systems

Because GenOps emits standard OpenTelemetry traces, logs, and metrics, it plugs directly into your existing monitoring, FinOps, and policy infrastructure. GenOps standardizes and enforces runtime governance across your AI systems, turning observability data into actionable accountability.

---

## ⚙️ Key Capabilities

GenOps standardizes and enforces runtime governance across your AI systems.

| **Dimension** | **Example Metrics / Policies** | **Purpose** |
|---------------|----------------------------------|-------------|
| **Cost Telemetry** | Cost per request, team, feature, or customer | Enables FinOps visibility and chargeback |
| **Policy Compliance** | Allowed models, region routing, rate limits | Prevents policy drift and shadow usage |
| **Data Residency** | Model invocation region, storage compliance | Ensures GDPR / SOC2 / FedRAMP adherence |
| **Performance Metrics** | Latency, cache hits, throughput | Optimizes efficiency and reliability |
| **Safety & Guardrails** | Toxicity filters, jailbreak detection | Enforces responsible deployment |
| **Usage Attribution** | Project, user, and customer-level metering | Enables cross-org accountability |

---

## 📦 Quick Start

### 1. Install the SDK
```bash
pip install genops
```

### 2. Initialize in your app
```python
from genops import GenOps
GenOps.init()
```

### 3. Run your app
GenOps automatically collects runtime telemetry and governance signals.  
View data in your existing observability stack or policy engine.

---

## 🔌 Integrations & Destinations

### Supported Integrations

GenOps integrates natively with your AI and infrastructure layer to collect and normalize runtime signals.

#### LLM & Model Providers

- ✅ [OpenAI](https://github.com/KoshiHQ/GenOps-AI/tree/main/examples/openai) (<a href="https://openai.com/" target="_blank">↗</a>)
- ☐ Azure OpenAI (<a href="https://azure.microsoft.com/en-us/products/ai-services/openai-service" target="_blank">↗</a>)
- ✅ [Anthropic](https://github.com/KoshiHQ/GenOps-AI/tree/main/examples/anthropic) (<a href="https://www.anthropic.com/" target="_blank">↗</a>)
- ✅ [OpenRouter](https://github.com/KoshiHQ/GenOps-AI/tree/main/examples/openrouter) (<a href="https://openrouter.ai/" target="_blank">↗</a>)
- ☐ Mistral (<a href="https://mistral.ai/" target="_blank">↗</a>)
- ☐ Lepton (<a href="https://www.lepton.ai/" target="_blank">↗</a>)
- ☐ Gemini (<a href="https://deepmind.google/technologies/gemini/" target="_blank">↗</a>)
- ☐ Ollama (<a href="https://ollama.com/" target="_blank">↗</a>)
- ☐ Bedrock (<a href="https://aws.amazon.com/bedrock/" target="_blank">↗</a>)
- ☐ SageMaker (<a href="https://aws.amazon.com/sagemaker/" target="_blank">↗</a>)
- ☐ Replicate (<a href="https://replicate.com/" target="_blank">↗</a>)
- ☐ Together (<a href="https://www.together.ai/" target="_blank">↗</a>)
- ☐ Groq (<a href="https://groq.com/" target="_blank">↗</a>)

#### Frameworks & Tooling

- ✅ [LangChain](https://github.com/KoshiHQ/GenOps-AI/tree/main/examples/langchain) (<a href="https://python.langchain.com/" target="_blank">↗</a>)
- ☐ LlamaIndex (<a href="https://www.llamaindex.ai/" target="_blank">↗</a>)
- ☐ LiteLLM (<a href="https://litellm.vercel.app/" target="_blank">↗</a>)
- ☐ DSPy (<a href="https://dspy-docs.vercel.app/" target="_blank">↗</a>)
- ☐ Guidance (<a href="https://github.com/guidance-ai/guidance" target="_blank">↗</a>)
- ☐ CrewAI (<a href="https://www.crewai.com/" target="_blank">↗</a>)
- ☐ OpenAI Agents (<a href="https://platform.openai.com/docs/assistants/overview" target="_blank">↗</a>)
- ☐ Haystack (<a href="https://haystack.deepset.ai/" target="_blank">↗</a>)
- ☐ LangGraph (<a href="https://langchain-ai.github.io/langgraph/" target="_blank">↗</a>)
- ☐ Langflow (<a href="https://www.langflow.org/" target="_blank">↗</a>)

#### Infrastructure & Runtime

- ☐ Kubernetes (<a href="https://kubernetes.io/" target="_blank">↗</a>)
- ☐ Cloudflare Workers (<a href="https://workers.cloudflare.com/" target="_blank">↗</a>)
- ☐ Vercel AI SDK (<a href="https://sdk.vercel.ai/" target="_blank">↗</a>)
- ☐ Ray (<a href="https://www.ray.io/" target="_blank">↗</a>)
- ☐ Modal (<a href="https://modal.com/" target="_blank">↗</a>)
- ☐ Fly.io (<a href="https://fly.io/" target="_blank">↗</a>)
- ☐ AWS Lambda (<a href="https://aws.amazon.com/lambda/" target="_blank">↗</a>)
- ☐ Google Cloud Run (<a href="https://cloud.google.com/run" target="_blank">↗</a>)
- ☐ Azure Functions (<a href="https://azure.microsoft.com/en-us/products/functions/" target="_blank">↗</a>)

### Supported Destinations

GenOps exports standardized telemetry and governance events to your existing stack.

#### Observability & Monitoring

- ✅ [OpenTelemetry Collector](https://github.com/KoshiHQ/GenOps-AI/tree/main/observability) (<a href="https://opentelemetry.io/docs/collector/" target="_blank">↗</a>)
- ✅ [Datadog](https://github.com/KoshiHQ/GenOps-AI/tree/main/examples/observability/datadog_integration.py) (<a href="https://www.datadoghq.com/" target="_blank">↗</a>)
- ✅ [Grafana](https://github.com/KoshiHQ/GenOps-AI/tree/main/observability/grafana) (<a href="https://grafana.com/" target="_blank">↗</a>)
- ✅ [Loki](https://github.com/KoshiHQ/GenOps-AI/tree/main/observability/loki-config.yaml) (<a href="https://grafana.com/oss/loki/" target="_blank">↗</a>)
- ✅ [Honeycomb](https://github.com/KoshiHQ/GenOps-AI/tree/main/examples/observability/honeycomb_integration.py) (<a href="https://www.honeycomb.io/" target="_blank">↗</a>)
- ✅ [Prometheus](https://github.com/KoshiHQ/GenOps-AI/tree/main/observability/prometheus.yml) (<a href="https://prometheus.io/" target="_blank">↗</a>)
- ✅ [Tempo](https://github.com/KoshiHQ/GenOps-AI/tree/main/observability/tempo-config.yaml) (<a href="https://grafana.com/oss/tempo/" target="_blank">↗</a>)
- ☐ New Relic (<a href="https://newrelic.com/" target="_blank">↗</a>)
- ☐ Jaeger (<a href="https://www.jaegertracing.io/" target="_blank">↗</a>)
- ☐ SigNoz (<a href="https://signoz.io/" target="_blank">↗</a>)

#### Cost & FinOps Platforms

- ☐ OpenCost (<a href="https://www.opencost.io/" target="_blank">↗</a>)
- ☐ Finout (<a href="https://www.finout.io/" target="_blank">↗</a>)
- ☐ CloudZero (<a href="https://www.cloudzero.com/" target="_blank">↗</a>)
- ☐ AWS Cost Explorer (<a href="https://aws.amazon.com/aws-cost-management/" target="_blank">↗</a>)
- ☐ GCP Billing (<a href="https://cloud.google.com/billing/docs" target="_blank">↗</a>)
- ☐ Azure Cost Management (<a href="https://azure.microsoft.com/en-us/products/cost-management/" target="_blank">↗</a>)
- ☐ Cloudflare Workers AI Analytics (<a href="https://developers.cloudflare.com/workers-ai/" target="_blank">↗</a>)
- ☐ Traceloop (<a href="https://traceloop.com/" target="_blank">↗</a>)
- ☐ OpenLLMetry (<a href="https://github.com/traceloop/openllmetry" target="_blank">↗</a>)

### Policy & Compliance

- ☐ OPA (Open Policy Agent) (<a href="https://www.openpolicyagent.org/" target="_blank">↗</a>)
- ☐ Kyverno (<a href="https://kyverno.io/" target="_blank">↗</a>)
- ☐ Cloud Custodian (<a href="https://cloudcustodian.io/" target="_blank">↗</a>)
- ☐ HashiCorp Sentinel (<a href="https://www.hashicorp.com/sentinel" target="_blank">↗</a>)
- ☐ Rego-compatible policies

### Data & Security Pipelines

- ☐ BigQuery (<a href="https://cloud.google.com/bigquery" target="_blank">↗</a>)
- ☐ Snowflake (<a href="https://www.snowflake.com/" target="_blank">↗</a>)
- ☐ S3 (<a href="https://aws.amazon.com/s3/" target="_blank">↗</a>)
- ☐ GCS (<a href="https://cloud.google.com/storage" target="_blank">↗</a>)
- ☐ Azure Blob (<a href="https://azure.microsoft.com/en-us/products/storage/blobs/" target="_blank">↗</a>)
- ☐ Splunk (<a href="https://www.splunk.com/" target="_blank">↗</a>)
- ☐ Elastic (<a href="https://www.elastic.co/" target="_blank">↗</a>)

---

## 🏢 Production Features

### **Compliance & Audit Trails**
GenOps automatically creates detailed audit logs for:
- **Cost attribution** with exact token counts and pricing models
- **Policy decisions** with enforcement context and reasoning
- **Data flow tracking** for privacy and compliance requirements  
- **Model usage patterns** for governance and risk management

### **Observability Integration**
Works with your existing tools and workflows:
- **Per-customer cost allocation** for accurate billing
- **Team and department spend tracking** for budget management
- **Feature-level cost analysis** for product decisions
- **Model efficiency metrics** for optimization opportunities
- **Real-time dashboards** using your current observability platform

---

## 🏢 **Production Ready**

### **Compliance & Audit Trails**
GenOps AI automatically creates detailed audit logs for:
- **Cost attribution** with exact token counts and pricing models
- **Policy decisions** with enforcement context and reasoning
- **Data flow tracking** for privacy and compliance requirements  
- **Model usage patterns** for governance and risk management

### **Observability Integration**
Works with your existing tools and workflows:
- **Per-customer cost allocation** for accurate billing
- **Team and department spend tracking** for budget management
- **Feature-level cost analysis** for product decisions
- **Model efficiency metrics** for optimization opportunities
- **Real-time dashboards** using your current observability platform

---

## 🤝 **Community & Support**

### **Contributing**
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup and testing guidelines
- Code standards and review process
- Community guidelines and code of conduct

### **Getting Help**
- 📖 **Documentation**: [GitHub Docs](https://github.com/KoshiHQ/GenOps-AI/tree/main/docs)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/KoshiHQ/GenOps-AI/issues)

### **Roadmap**
See our [public roadmap](https://github.com/KoshiHQ/GenOps-AI/projects) for upcoming features:
- 🚧 AWS Bedrock and Google Gemini adapters
- 🚧 LangChain and LlamaIndex integrations  
- 🚧 OpenTelemetry Collector processors for real-time governance
- 🚧 Pre-built dashboards for major observability platforms

---

## 📄 **License**

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

---

## 🌟 **Why GenOps AI?**

**Traditional AI monitoring tells you what happened. GenOps AI tells you what it cost, who did it, whether it should have been allowed, and how well it worked.**

- **For DevOps Teams**: Integrate AI governance into existing observability workflows
- **For FinOps Teams**: Get precise cost attribution and budget controls
- **For Compliance Teams**: Automated policy enforcement with audit trails
- **For Product Teams**: Feature-level AI cost analysis and optimization insights

**Open source, OpenTelemetry-native, and designed to work with your existing stack.**

---

## 🤝 **Community & Quick Wins**

**New to open source?** Start here:
- 🐛 [Good first issues](https://github.com/KoshiHQ/GenOps-AI/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) - Perfect for newcomers
- 📚 [Documentation improvements](https://github.com/KoshiHQ/GenOps-AI/issues?q=is%3Aissue+is%3Aopen+label%3Adocumentation) - Help others learn
- 🔧 [Help fix our CI tests!](https://github.com/KoshiHQ/GenOps-AI/issues?q=is%3Aissue+is%3Aopen+label%3Aci-fix) - Great for contributors who love debugging

**5-minute contributions welcome!** Every small improvement helps the community grow.

**Looking for bigger challenges?**
- 🏗️ [Provider integrations](https://github.com/KoshiHQ/GenOps-AI/issues?q=is%3Aissue+is%3Aopen+label%3Aprovider) - Add AWS Bedrock, Google Gemini support
- 📊 [Dashboard templates](https://github.com/KoshiHQ/GenOps-AI/issues?q=is%3Aissue+is%3Aopen+label%3Adashboard) - Pre-built observability dashboards
- 🤖 [AI governance patterns](https://github.com/KoshiHQ/GenOps-AI/issues?q=is%3Aissue+is%3Aopen+label%3Agovernance) - Real-world scenarios

---

## ⚠️ **Known Issues & Contributing**

This is a **preview release** with comprehensive features but some ongoing CI test issues:

### 🚧 Current Status
- ✅ **Core functionality working**: Security scans pass, package installation works
- ✅ **Comprehensive examples**: All governance scenarios and integrations functional
- ⚠️ **Some CI tests failing**: Integration tests and Python 3.11 compatibility
- 🤝 **Community help wanted**: [See open issues](https://github.com/KoshiHQ/GenOps-AI/issues) for contribution opportunities

### 🆘 Need Help?
- 💬 **Questions**: [GitHub Discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/KoshiHQ/GenOps-AI/issues)
- 🤝 **Contributing**: [Contributing Guide](CONTRIBUTING.md)

---

## ✨ Contributors

Thanks goes to these wonderful people who have contributed to GenOps AI:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

---

## 🏷️ **Trademark & Brand Guidelines**

### **GenOps AI Trademark Usage**

The "GenOps AI" name and associated branding are trademarks used to identify this project and its official implementations.

**✅ Acceptable Use:**
- Referring to this project in documentation, blog posts, or presentations
- Building integrations or extensions that work with GenOps AI
- Using "Built with GenOps AI" or "Powered by GenOps AI" attributions
- Community projects that extend or integrate with GenOps AI functionality

**❌ Prohibited Use:**
- Using "GenOps" in the name of competing commercial AI governance products
- Creating confusion about official vs. community implementations  
- Using GenOps branding for unrelated products or services
- Implying official endorsement without permission

**📄 License Note:** The GenOps AI code is licensed under Apache 2.0, but trademark rights are separate from code rights. You're free to use, modify, and distribute the code under Apache 2.0, but please respect our trademark guidelines when naming your projects or products.

For questions about trademark usage, please open an issue or contact the maintainers.

---

## 📄 **Legal & Licensing**

- **Code License**: [Apache License 2.0](LICENSE) - Permissive open source license
- **Contributor Agreement**: All contributions require [DCO sign-off](CONTRIBUTING.md#developer-certificate-of-origin-dco)
- **Copyright**: Copyright © 2024 GenOps AI Contributors
- **Trademark**: "GenOps AI" and associated marks are trademarks of the project maintainers

---

<div align="center">
  <p><strong>Ready to bring governance to your AI systems?</strong></p>
  
  ```bash
  pip install genops
  ```
  
  <p>⭐ <strong>Star us on GitHub</strong> if you find GenOps AI useful!</p>
  
  [![GitHub stars](https://img.shields.io/github/stars/KoshiHQ/GenOps-AI?style=social)](https://github.com/KoshiHQ/GenOps-AI/stargazers)
</div>