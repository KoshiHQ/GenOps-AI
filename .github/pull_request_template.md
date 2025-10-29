<!-- 
This is the default pull request template for GenOps AI.
For specific types of changes, please use the specialized templates:
- Feature: .github/PULL_REQUEST_TEMPLATE/feature.md
- Bug Fix: .github/PULL_REQUEST_TEMPLATE/bugfix.md  
- Documentation: .github/PULL_REQUEST_TEMPLATE/documentation.md
-->

## 📋 **Summary**

<!--
Provide a clear, concise description of your changes.
Link to related issues if applicable.
-->

**Type of Change**: 
- [ ] 🚀 New feature
- [ ] 🐛 Bug fix
- [ ] 📚 Documentation update
- [ ] 🔧 Refactoring
- [ ] ⚡ Performance improvement
- [ ] 🧪 Tests
- [ ] 🔨 Build/CI changes

**Related Issue**: Fixes #(issue number)

---

## 🧪 **Testing**

### **Test Coverage**
- [ ] Tests added/updated for changes
- [ ] All tests pass (`make test`)
- [ ] Manual testing completed

### **Test Results**
```bash
# Paste key test results here
```

---

## 📚 **Documentation**

- [ ] Code is self-documenting with docstrings
- [ ] Documentation updated (if needed)
- [ ] Examples updated (if needed)

---

## ✅ **Checklist**

### **Code Quality**
- [ ] Code follows style guidelines (`make lint` passes)
- [ ] Self-review completed  
- [ ] No breaking changes (or breaking changes documented)

### **GenOps AI Specific**
- [ ] OpenTelemetry integration maintained
- [ ] Governance telemetry not affected
- [ ] Cost attribution accuracy preserved
- [ ] Policy enforcement not broken

---

**Additional Notes**: 
<!-- Any context helpful for reviewers -->

/cc @maintainers