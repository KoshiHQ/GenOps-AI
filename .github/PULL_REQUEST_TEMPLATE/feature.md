---
name: 🚀 Feature Pull Request
about: Adding new functionality to GenOps AI
title: "feat: "
labels: ["enhancement"]
---

## 📋 **Summary**

<!--
Provide a clear, concise summary of the new feature.
Link to the related issue if applicable.
-->

**Related Issue**: Fixes #(issue number)

**Feature Description**:
<!-- Brief description of what this feature adds -->

---

## ✨ **What's New**

<!--
Describe the new functionality in detail.
Include screenshots, code examples, or demos if applicable.
-->

### **Key Features**
- [ ] Feature 1: Description
- [ ] Feature 2: Description  
- [ ] Feature 3: Description

### **API Changes**
<!-- List any new APIs, breaking changes, or deprecations -->

---

## 🧪 **Testing**

### **Test Coverage**
- [ ] Unit tests added for new functionality
- [ ] Integration tests updated
- [ ] Manual testing completed
- [ ] Performance impact assessed

### **Test Results**
```bash
# Paste test results here
make test
```

### **Manual Testing Checklist**
- [ ] Feature works as expected
- [ ] Error handling is appropriate
- [ ] Documentation examples work
- [ ] No regression in existing functionality

---

## 📚 **Documentation**

- [ ] Code is self-documenting with clear docstrings
- [ ] README updated (if needed)
- [ ] Documentation updated (if needed)  
- [ ] Examples added/updated (if needed)
- [ ] Migration guide provided (for breaking changes)

---

## 🔍 **Code Quality**

### **Self Review Checklist**
- [ ] Code follows project style guidelines (`make lint` passes)
- [ ] Type hints added where appropriate
- [ ] Error handling is comprehensive
- [ ] Code is performant and doesn't introduce bottlenecks
- [ ] Security considerations addressed

### **Breaking Changes**
<!-- Describe any breaking changes and migration path -->
- [ ] No breaking changes
- [ ] Breaking changes documented with migration guide

---

## 🎯 **Governance Impact**

<!--
For GenOps AI, consider how this feature affects AI governance:
-->

- [ ] Does this affect cost attribution tracking?
- [ ] Does this impact policy enforcement?
- [ ] Does this change compliance telemetry?
- [ ] Does this affect OpenTelemetry integration?

**Governance Considerations**:
<!-- Describe any governance implications -->

---

## 📸 **Screenshots/Demos**

<!--
For UI changes, governance dashboards, or visual features, include:
- Before/after screenshots
- Demo videos or GIFs
- Dashboard examples
-->

---

## 🚀 **Deployment**

### **Release Notes Preview**
<!--
Write the release notes entry for this feature:
-->

```markdown
### 🚀 New Features
- **Feature Name**: Brief description of what users get
```

### **Rollout Plan**
- [ ] Feature can be deployed incrementally
- [ ] No special deployment steps required
- [ ] Database migrations handled (if applicable)

---

## 👥 **Reviewer Guide**

### **Focus Areas**
<!--
Guide reviewers on what to pay special attention to:
-->

1. **Functionality**: Does the feature work as described?
2. **Integration**: How does this integrate with existing GenOps functionality?
3. **Performance**: Any performance implications?
4. **Security**: Are there security considerations?

### **Testing Instructions**
<!--
Provide step-by-step instructions for reviewers to test:
-->

1. Step 1
2. Step 2
3. Step 3

---

## ✅ **Final Checklist**

- [ ] Branch is up to date with main
- [ ] All tests pass (`make check`)
- [ ] Documentation is complete
- [ ] Ready for review
- [ ] Deployment plan confirmed

---

**Additional Notes**: 
<!-- Any other information for reviewers -->

/cc @maintainers