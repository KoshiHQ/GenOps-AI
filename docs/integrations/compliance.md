# Compliance Integration Guide

This guide provides comprehensive information on integrating compliance frameworks with GenOps provider implementations, including audit trails, data governance, and regulatory reporting.

## 📋 Overview

GenOps supports compliance integration across multiple regulatory frameworks through standardized patterns and templates. This guide covers implementation strategies for common compliance requirements.

## 🏛️ Supported Compliance Frameworks

### Financial Services Compliance
- **SOX (Sarbanes-Oxley Act)**: Financial reporting controls and audit trails
- **PCI DSS**: Payment card industry data security standards  
- **GDPR Article 22**: Automated decision-making in financial contexts

### Data Protection & Privacy
- **GDPR (General Data Protection Regulation)**: EU data protection requirements
- **CCPA (California Consumer Privacy Act)**: California privacy regulations
- **HIPAA**: Healthcare data protection (coming soon)

### Enterprise Security
- **SOC 2**: Service organization controls for security and availability
- **ISO 27001**: Information security management systems
- **FedRAMP**: US government cloud security requirements (coming soon)

## 🔧 Implementation Patterns

### 1. Audit Trail Architecture

All compliance integrations follow consistent audit trail patterns:

```python
from genops.core.compliance import ComplianceAuditTrail

audit_trail = ComplianceAuditTrail(
    framework="sox|gdpr|ccpa",
    retention_period="7_years|3_years|custom",
    immutable_logging=True,
    encryption_required=True
)
```

### 2. Data Classification

Implement data classification for compliance-aware processing:

```python
@dataclass
class DataClassification:
    sensitivity_level: str  # "public", "internal", "confidential", "restricted"
    regulatory_scope: List[str]  # ["gdpr", "sox", "ccpa"]
    retention_requirements: str
    processing_restrictions: List[str]
```

### 3. Governance Controls

Standard governance controls across all compliance frameworks:

```python
compliance_adapter = GenOpsAdapter(
    governance_policy="strict",  # enforced, advisory, strict
    audit_trail_enabled=True,
    data_classification="confidential",
    retention_policy="regulation_required",
    access_controls="role_based"
)
```

## 📊 Compliance Templates

### Available Templates

| Framework | Location | Use Case |
|-----------|----------|----------|
| **SOX** | [`examples/posthog/compliance_templates/SOX_compliance_template.py`](../../examples/posthog/compliance_templates/SOX_compliance_template.py) | Public companies, financial reporting |
| **GDPR** | [`examples/posthog/compliance_templates/GDPR_compliance_template.py`](../../examples/posthog/compliance_templates/GDPR_compliance_template.py) | EU data processing, privacy rights |

### Template Structure

All compliance templates follow this structure:

1. **Regulatory Requirement Mapping**
2. **Data Classification and Controls**  
3. **Audit Trail Implementation**
4. **Data Subject Rights (where applicable)**
5. **Retention and Deletion Policies**
6. **Reporting and Documentation**

## 🔍 Audit Trail Requirements

### Immutable Logging

All compliance frameworks require tamper-evident audit trails:

```python
def create_audit_entry(action, resource, metadata):
    entry = AuditEntry(
        timestamp=datetime.now(timezone.utc),
        action=action,
        resource=resource,
        user_context=get_current_user(),
        data_hash=generate_hash(metadata),
        retention_until=calculate_retention_date()
    )
    return sign_and_store(entry)
```

### Audit Data Requirements

Standard audit data captured across all frameworks:

- **Who**: User identification and authentication details
- **What**: Action performed and data accessed/modified
- **When**: Precise timestamp with timezone
- **Where**: System location and network context
- **Why**: Business justification and authorization
- **How**: Technical method and system used

## 📋 Data Retention Policies

### Framework-Specific Requirements

| Framework | Minimum Retention | Typical Retention |
|-----------|------------------|-------------------|
| **SOX** | 7 years | 7+ years |
| **GDPR** | Purpose-limited | 2-7 years |
| **CCPA** | 12 months | 2-3 years |
| **HIPAA** | 6 years | 6+ years |

### Implementation

```python
retention_policies = {
    "sox": RetentionPolicy(
        minimum_years=7,
        trigger="financial_year_end",
        legal_hold_supported=True
    ),
    "gdpr": RetentionPolicy(
        duration="purpose_limited",
        trigger="consent_withdrawal",
        deletion_required=True
    )
}
```

## 🛡️ Data Subject Rights

### GDPR Rights Implementation

For EU data processing, implement all GDPR data subject rights:

```python
class DataSubjectRights:
    def handle_access_request(self, subject_id):
        # Article 15 - Right of access
        return generate_data_export(subject_id)
    
    def handle_erasure_request(self, subject_id):
        # Article 17 - Right to erasure
        return schedule_data_deletion(subject_id)
    
    def handle_portability_request(self, subject_id):
        # Article 20 - Right to data portability
        return export_portable_data(subject_id)
```

## 🔐 Access Controls

### Role-Based Access Control (RBAC)

Implement segregation of duties for compliance:

```python
compliance_roles = {
    "data_controller": ["read_data", "process_data", "delete_data"],
    "data_processor": ["read_data", "process_data"],
    "compliance_officer": ["audit_access", "generate_reports"],
    "auditor": ["read_audit_logs", "export_compliance_data"]
}
```

### Principle of Least Privilege

Ensure minimal necessary access:

```python
def check_compliance_access(user, action, resource):
    required_permissions = get_required_permissions(action, resource)
    user_permissions = get_user_permissions(user)
    
    if not all(perm in user_permissions for perm in required_permissions):
        audit_access_denied(user, action, resource)
        raise InsufficientPermissionsError()
    
    audit_access_granted(user, action, resource)
    return True
```

## 📈 Compliance Monitoring

### Real-Time Monitoring

Monitor compliance status in real-time:

```python
def monitor_compliance_status():
    metrics = {
        "audit_trail_integrity": check_audit_integrity(),
        "retention_policy_compliance": check_retention_compliance(),
        "access_control_violations": count_access_violations(),
        "data_breach_indicators": scan_for_breaches()
    }
    return ComplianceStatus(metrics)
```

### Automated Reporting

Generate compliance reports automatically:

```python
def generate_compliance_report(framework, period):
    report = ComplianceReport(
        framework=framework,
        reporting_period=period,
        audit_entries=get_audit_entries(period),
        compliance_metrics=calculate_metrics(period),
        violations=get_violations(period),
        remediation_actions=get_remediation_status()
    )
    return report
```

## 🚨 Incident Response

### Compliance Incident Handling

Standardized incident response for compliance events:

```python
def handle_compliance_incident(incident_type, details):
    incident = ComplianceIncident(
        type=incident_type,
        severity=assess_severity(incident_type),
        details=details,
        timestamp=datetime.now(timezone.utc),
        notification_required=determine_notification_requirements()
    )
    
    # Immediate containment
    contain_incident(incident)
    
    # Regulatory notification if required
    if incident.notification_required:
        notify_regulators(incident)
    
    # Audit trail
    audit_incident(incident)
    
    return incident
```

## 📚 Integration Examples

### Provider-Specific Implementation

Each GenOps provider can implement compliance controls:

```python
# Example: PostHog with GDPR compliance
posthog_adapter = GenOpsPostHogAdapter(
    compliance_framework="gdpr",
    data_processing_basis="consent",
    retention_policy="2_years_after_last_activity",
    data_subject_rights_enabled=True,
    audit_trail_required=True
)
```

### Multi-Framework Compliance

Support multiple frameworks simultaneously:

```python
multi_compliance_adapter = GenOpsAdapter(
    compliance_frameworks=["sox", "gdpr"],
    governance_policy="strict",
    audit_retention="longest_required",  # 7 years for SOX
    cross_framework_validation=True
)
```

## 🤝 Professional Services

For enterprise compliance implementations requiring legal review and validation:

- **Compliance Assessment**: Gap analysis and risk assessment
- **Implementation Support**: Custom framework development
- **Legal Review**: Coordination with legal counsel
- **Audit Preparation**: External audit support and preparation

## 📞 Support & Resources

- **Documentation**: [Audit Trail Patterns](../audit-trail-patterns.md)
- **Templates**: [Data Retention Templates](../data-retention-templates.md)  
- **Best Practices**: [Compliance Best Practices](../compliance-best-practices.md)
- **Community**: [GitHub Discussions](https://github.com/KoshiHQ/GenOps-AI/discussions)
- **Professional Services**: Contact for enterprise compliance consulting

---

**⚖️ Legal Disclaimer**: This guide provides technical implementation guidance only. Always consult with qualified legal counsel for compliance requirements specific to your organization and jurisdiction.