---
name: Bug report
about: Create a report to help us improve GenOps AI
title: '[BUG] '
labels: bug
assignees: ''
---

## 🐛 **Bug Description**

A clear and concise description of what the bug is.

## 🔄 **Steps to Reproduce**

Steps to reproduce the behavior:

1. Install GenOps AI with `pip install genops[...]`
2. Configure with `genops.init(...)`
3. Run code: '....'
4. See error

## ✅ **Expected Behavior**

A clear and concise description of what you expected to happen.

## ❌ **Actual Behavior**

A clear and concise description of what actually happened.

## 📋 **Code Example**

Please provide a minimal code example that reproduces the issue:

```python
import genops

# Your minimal reproduction code here
genops.init(...)

# Expected to work but fails
```

## 🖥️ **Environment**

- **GenOps AI Version**: [e.g. 0.1.0]
- **Python Version**: [e.g. 3.9.6]
- **Operating System**: [e.g. macOS 13.0, Ubuntu 20.04, Windows 11]
- **AI Provider**: [e.g. OpenAI, Anthropic]
- **Provider Package Version**: [e.g. openai==1.3.0]
- **Observability Platform**: [e.g. Honeycomb, Datadog, Console]

## 📊 **Logs/Output**

If applicable, add logs or error output to help explain your problem:

```
Paste error logs here
```

## 🔍 **Additional Context**

Add any other context about the problem here:

- Is this related to a specific AI provider?
- Does this happen with auto-instrumentation or manual instrumentation?
- Are you using any specific governance policies?
- Any other relevant configuration or environment details?

## ✔️ **Checklist**

- [ ] I have searched existing issues to make sure this is not a duplicate
- [ ] I have provided a minimal code example that reproduces the issue
- [ ] I have included my environment information
- [ ] I have included relevant logs/error output

## 🤝 **Additional Information**

- Would you be willing to submit a PR to fix this issue?
- Is this blocking your use of GenOps AI?
- Any workarounds you've discovered?