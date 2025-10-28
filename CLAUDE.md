# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Strategic Context

### Mission: "Governance for AI, Built on OpenTelemetry"

GenOps AI builds **alongside OpenLLMetry**, on the **OpenTelemetry foundation** — interoperable by design, independent by governance.
It standardizes **cost, policy, compliance, and evaluation telemetry** for AI workloads across internal teams, departments, and per-customer usage.

Where **OpenLLMetry** defines *what* to trace (LLM prompts, completions, tokens),
**GenOps** defines *why and how* — the governance layer that turns telemetry into actionable accountability.

---

## Project Overview

This Python SDK is the reference implementation of **GenOps-OTel** — the open-source governance telemetry layer for AI systems.

It provides a **vendor-neutral, OTel-native SDK** that enables teams to:

* Capture and export governance signals: cost, budget, policy, compliance, and evaluation metrics
* Integrate with existing observability stacks (Datadog, Honeycomb, Grafana Tempo, etc.)
* Feed data into governance dashboards and enterprise control planes

---

### Core Purpose

* Extend the OpenTelemetry signal model to cover **governance semantics** (`genops.cost.*`, `genops.policy.*`, `genops.eval.*`, `genops.budget.*`)
* Provide **interoperable adapters** for LLM providers and frameworks (OpenAI, Anthropic, Gemini, Bedrock, Mistral, LangChain, etc.)
* Enable **transparent per-team, per-feature, per-customer cost governance** across AI systems
* Serve as the **foundation for enterprise governance automation**

---

## Open Source Strategy

### Licensing & Governance

* **License:** Apache 2.0 (permissive and OSS-friendly)
* **Governance:** Open community development with maintainer stewardship
* **Community:** Public RFC process for spec evolution; open contribution model
* **Vendor Neutrality:** Aligns with OpenTelemetry and OpenLLMetry specs; avoids lock-in with any observability or model vendor

### Philosophy: Developer-first, Governance-aware

* Minimal setup and frictionless integration
* Multipattern instrumentation (decorators, context managers, auto-detect)
* Zero-dashboards-by-default → reuse existing observability stack
* Extensible adapter architecture to empower community contributions

---

## Architectural Principles

### Design Layering

```
OpenTelemetry (foundation)
   ├── OpenLLMetry (LLM observability: prompts, completions, latency)
   └── GenOps-OTel (AI governance: cost, policy, compliance, evaluation)
```

GenOps operates *next to* OpenLLMetry, not on top of it — interoperable by design, but independent by governance.
Both layers export standard OTLP signals, enabling any organization to maintain full autonomy and transparency.

---

### Core Components

1. **Governance Semantics Spec:** Defines official telemetry keys for cost, policy, and evaluation
2. **Provider Adapters:** Thin wrappers for major AI providers and frameworks
3. **Collector Processors:** OpenTelemetry Collector extensions (Go-based) for cost, redaction, policy, and budget processing
4. **CLI / Local Dashboard:** Minimal local tools for developers
5. **Exporter Configs:** OTLP examples for all major observability backends

---

### Integration Patterns

* `@track_usage`: Function-level instrumentation decorator
* `with genops.track():`: Context manager for block-level tracking
* `enforce_policy`: Declarative runtime guardrail enforcement
* Auto-instrumentation for OpenAI, Anthropic, Bedrock, Gemini, LangChain, LlamaIndex, Chroma, and others

---

## Technical Standards

### Package Structure

```
genops-ai/
├── src/genops/
│   ├── core/              # Core telemetry engine
│   ├── providers/         # Provider adapters (OpenAI, Anthropic, etc.)
│   ├── exporters/         # OTLP exporters
│   ├── processors/        # OTel Collector processors
│   ├── config/            # Config & environment handling
│   └── cli/               # Local CLI tools
├── tests/
├── examples/
├── docs/
├── pyproject.toml
└── CONTRIBUTING.md
```

### Development Tools

* **Build**: `python -m build`
* **Test**: `pytest`
* **Format**: `ruff format`
* **Lint**: `ruff check`
* **Type Check**: `mypy src/`

---

## Ecosystem Vision

### Interoperability Focus

GenOps doesn't replace observability — it **enriches it with governance semantics**.

Compatible with:

* **OpenTelemetry** (base standard)
* **OpenLLMetry** (LLM observability layer)
* **All major observability platforms:** Datadog, Honeycomb, New Relic, Grafana Tempo, Dynatrace, Splunk, Instana, Highlight, Traceloop
* **All major model providers:** OpenAI, Anthropic, Bedrock, Gemini, Mistral, Together, Ollama, WatsonX

### Community Growth

* Encourage third-party adapters via `genops-adapters` template repo
* Recognize contributors who add new frameworks and exporters
* Co-marketing for high-quality integrations and case studies
* Public governance RFCs (like OTel SIGs)

---

## Success Metrics

### Community Goals

* 1K+ GitHub stars
* 10+ provider adapters  
* 5+ supported observability platforms
* Community RFC adoption and schema contributions
* Active FinOps Foundation and enterprise adoption

---

## Key References

* **OpenTelemetry:** [https://opentelemetry.io](https://opentelemetry.io)
* **OpenLLMetry:** [https://github.com/traceloop/openllmetry](https://github.com/traceloop/openllmetry)
* **Next.js → Vercel Playbook**
* **Sentry → Sentry Cloud Playbook**
* **Open-core Model:** "Open Source standard, Closed Source experience"

---

### TL;DR (for Claude Code)

> GenOps AI builds *alongside* OpenLLMetry on the OpenTelemetry foundation —
> **interoperable by design, independent by governance.**
> It defines open-source semantics for AI cost, policy, and compliance telemetry.
> Built and maintained as an open-source project under the Apache 2.0 license.