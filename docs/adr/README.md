# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records (ADRs) for GenOps AI, documenting important architectural decisions made during the development of the project.

## What are ADRs?

Architecture Decision Records (ADRs) are short text documents that capture important architectural decisions made along with their context and consequences. They help teams:

- **Document the reasoning** behind architectural choices
- **Preserve context** for future team members
- **Track the evolution** of architectural decisions over time
- **Avoid revisiting** already-decided questions
- **Learn from past decisions** both good and bad

## ADR Format

We use a lightweight format based on Michael Nygard's template:

```markdown
# ADR-XXXX: Title

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-YYYY]

## Context
What is the issue that we're seeing that is motivating this decision or change?

## Decision
What is the change that we're proposing and/or doing?

## Consequences
What becomes easier or more difficult to do because of this change?
```

## Current ADRs

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [0001](0001-opentelemetry-foundation.md) | Use OpenTelemetry as Telemetry Foundation | Accepted | 2024-01-15 |
| [0002](0002-provider-adapter-pattern.md) | Provider Adapter Pattern for AI Integrations | Accepted | 2024-01-20 |
| [0003](0003-governance-semantics-spec.md) | Governance Telemetry Semantics Specification | Accepted | 2024-01-25 |
| [0004](0004-policy-engine-architecture.md) | Declarative Policy Engine Architecture | Accepted | 2024-02-01 |
| [0005](0005-observability-stack-integration.md) | Multi-Backend Observability Integration Strategy | Accepted | 2024-02-10 |

## Creating New ADRs

When making a significant architectural decision:

1. **Copy the template** from `template.md`
2. **Number it sequentially** (next available ADR-XXXX)
3. **Fill in all sections** with context and reasoning
4. **Propose it** via pull request for team review
5. **Update the table above** once accepted

## ADR Lifecycle

ADRs go through several states:

- **Proposed**: Under discussion, not yet decided
- **Accepted**: Decision made and implemented
- **Deprecated**: No longer current but kept for historical context  
- **Superseded**: Replaced by a newer ADR (reference the new one)

## Guidelines

- **Be concise** but provide sufficient context
- **Focus on the "why"** not just the "what"
- **Consider alternatives** and explain why they were rejected
- **Think about consequences** both positive and negative
- **Use simple language** that newcomers can understand
- **Link to relevant resources** like RFCs, documentation, or discussions

## Tools

Use these commands to help manage ADRs:

```bash
# Create a new ADR (requires adr-tools)
adr new "Title of Decision"

# List all ADRs
adr list

# Generate ADR graph
adr generate graph
```

For more information about ADRs, see:
- [Architecture Decision Records](https://adr.github.io/) - ADR community site
- [ADR Tools](https://github.com/npryce/adr-tools) - Command line tools
- [When Should I Write an ADR?](https://engineering-management.space/post/when-should-i-write-an-architecture-decision-record/)