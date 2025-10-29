---
name: 🐛 Bug Fix Pull Request
about: Fixing issues or problems in GenOps AI
title: "fix: "
labels: ["bug"]
---

## 🐛 **Bug Description**

<!--
Clearly describe the bug this PR fixes.
Link to the related issue.
-->

**Related Issue**: Fixes #(issue number)

**Bug Summary**:
<!-- Brief description of the problem being fixed -->

---

## 🔧 **Root Cause Analysis**

### **What Was Wrong**
<!-- Explain what was causing the bug -->

### **Why It Happened**
<!-- Describe the underlying cause -->

### **Impact Assessment**
<!--
Who was affected and how severe was the issue?
-->
- **Severity**: Critical / High / Medium / Low
- **Affected Users**: All users / Specific scenarios / Edge cases
- **Data Impact**: None / Potential data loss / Performance degradation

---

## ✅ **Solution**

### **Fix Description**
<!-- Describe how you fixed the issue -->

### **Code Changes**
<!--
Summarize the key changes made:
-->
- Changed: Description of change
- Added: Description of addition
- Removed: Description of removal

### **Alternative Solutions Considered**
<!-- Why did you choose this approach over others? -->

---

## 🧪 **Testing**

### **Bug Reproduction**
- [ ] Bug reproduced before fix
- [ ] Steps to reproduce documented
- [ ] Fix verified to resolve the issue

### **Regression Testing**
- [ ] Unit tests added for the bug scenario
- [ ] Integration tests updated (if needed)
- [ ] Manual testing completed
- [ ] No regressions introduced

### **Test Results**
```bash
# Paste test results showing the fix works
make test
```

---

## 🛡️ **Validation**

### **Before Fix**
<!--
Describe the behavior before the fix (error messages, screenshots, etc.)
-->

### **After Fix**
<!--
Describe the correct behavior after the fix
-->

### **Edge Cases Tested**
- [ ] Boundary conditions
- [ ] Error conditions
- [ ] Race conditions (if applicable)
- [ ] Resource constraints

---

## 📚 **Documentation Impact**

- [ ] No documentation changes needed
- [ ] Documentation updated to reflect fix
- [ ] Known issues removed from docs
- [ ] Troubleshooting guide updated

---

## 🎯 **Governance & Telemetry Impact**

<!--
For GenOps AI bugs, consider:
-->

- [ ] Does this fix affect cost calculations?
- [ ] Does this impact policy enforcement accuracy?
- [ ] Does this change telemetry data structure?
- [ ] Does this affect OpenTelemetry exports?

**Telemetry Changes**:
<!-- Describe any changes to governance data -->

---

## 🚀 **Deployment Considerations**

### **Urgency**
- [ ] Can wait for next regular release
- [ ] Should be included in next patch
- [ ] Needs hotfix deployment

### **Rollback Plan**
<!-- How can this change be rolled back if needed? -->

### **Monitoring**
<!-- What should we monitor after deployment? -->

---

## 🔍 **Security Impact**

- [ ] No security implications
- [ ] Security vulnerability fixed
- [ ] Security review completed

**Security Details** (if applicable):
<!-- Describe security implications -->

---

## ✅ **Checklist**

### **Code Quality**
- [ ] Code follows project style guidelines
- [ ] Error handling improved/maintained
- [ ] Logging added for debugging (if needed)
- [ ] Performance not degraded

### **Testing**
- [ ] Bug scenario covered by tests
- [ ] All existing tests still pass
- [ ] Manual verification completed

### **Review Readiness**
- [ ] Branch up to date with main
- [ ] Self-review completed
- [ ] Ready for peer review

---

## 👥 **Reviewer Focus**

### **Key Areas to Review**
1. **Fix Correctness**: Does this actually resolve the reported issue?
2. **Side Effects**: Could this change introduce new problems?
3. **Test Coverage**: Are there sufficient tests to prevent regression?

### **Reproduction Steps**
<!--
Provide clear steps for reviewers to reproduce the original bug and verify the fix:
-->

1. Step 1
2. Step 2
3. Expected: Bug should be resolved

---

**Additional Context**: 
<!-- Any other relevant information for reviewers -->

/cc @maintainers