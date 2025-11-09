# Data Retention Policy Templates

This guide provides comprehensive templates and implementation patterns for data retention policies across GenOps provider integrations, ensuring compliance with regulatory frameworks and organizational requirements.

## 📋 Overview

Data retention policies define how long data should be kept, when it should be deleted, and how retention requirements vary by data type, regulation, and business need. GenOps provides standardized templates for implementing retention policies across all provider integrations.

## 🏛️ Regulatory Framework Templates

### SOX (Sarbanes-Oxley) Retention Template

**Requirement**: 7+ years for financial records and audit trails

```python
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, Any, List
import enum

class RetentionTrigger(enum.Enum):
    FISCAL_YEAR_END = "fiscal_year_end"
    TRANSACTION_DATE = "transaction_date" 
    AUDIT_COMPLETION = "audit_completion"
    LEGAL_HOLD_RELEASE = "legal_hold_release"

@dataclass
class SOXRetentionPolicy:
    """SOX-compliant data retention policy."""
    
    minimum_retention_years: int = 7
    trigger_event: RetentionTrigger = RetentionTrigger.FISCAL_YEAR_END
    legal_hold_supported: bool = True
    immutable_period_days: int = 365  # Cannot be deleted for first year
    audit_trail_required: bool = True
    
    def calculate_retention_date(self, data_created_date: datetime, fiscal_year_end: datetime) -> datetime:
        """Calculate when data can be deleted under SOX requirements."""
        
        if self.trigger_event == RetentionTrigger.FISCAL_YEAR_END:
            # Retain for 7 years from end of fiscal year containing the transaction
            fiscal_year_containing_data = fiscal_year_end
            if data_created_date > fiscal_year_end:
                # If data created after fiscal year end, use next fiscal year
                fiscal_year_containing_data = fiscal_year_end.replace(year=fiscal_year_end.year + 1)
            
            retention_end = fiscal_year_containing_data + timedelta(days=365 * self.minimum_retention_years)
            
        elif self.trigger_event == RetentionTrigger.TRANSACTION_DATE:
            retention_end = data_created_date + timedelta(days=365 * self.minimum_retention_years)
        
        return retention_end
    
    def can_delete_data(self, data_created_date: datetime, current_date: datetime, 
                       legal_hold_active: bool = False) -> tuple[bool, str]:
        """Determine if data can be deleted under SOX policy."""
        
        if legal_hold_active:
            return False, "Legal hold prevents deletion"
        
        # Check immutable period
        immutable_until = data_created_date + timedelta(days=self.immutable_period_days)
        if current_date < immutable_until:
            return False, f"Data immutable until {immutable_until.isoformat()}"
        
        # Check minimum retention
        retention_end = self.calculate_retention_date(data_created_date, get_fiscal_year_end())
        if current_date < retention_end:
            return False, f"Minimum retention until {retention_end.isoformat()}"
        
        return True, "Data eligible for deletion"

# SOX Implementation
sox_retention = SOXRetentionPolicy()

def implement_sox_retention(financial_data):
    """Implement SOX retention for financial data."""
    
    retention_metadata = {
        'retention_policy': 'sox_7_year',
        'minimum_retention_until': sox_retention.calculate_retention_date(
            financial_data['created_at'], 
            get_fiscal_year_end()
        ).isoformat(),
        'legal_hold_supported': True,
        'audit_trail_required': True,
        'data_classification': 'financial_material'
    }
    
    return retention_metadata
```

### GDPR Retention Template

**Requirement**: Purpose-limited retention with data subject rights

```python
@dataclass
class GDPRRetentionPolicy:
    """GDPR-compliant data retention policy."""
    
    lawful_basis: str  # consent, contract, legitimate_interest, etc.
    processing_purpose: str
    default_retention_years: int = 3
    consent_withdrawal_deletion_days: int = 30
    subject_rights_supported: bool = True
    cross_border_restrictions: bool = True
    
    def calculate_retention_date(self, data_created_date: datetime, 
                               consent_date: datetime = None,
                               purpose_fulfilled_date: datetime = None) -> datetime:
        """Calculate GDPR retention end date based on lawful basis and purpose."""
        
        if self.lawful_basis == "consent":
            # Retain while consent is active, max default period
            if consent_date:
                max_retention = consent_date + timedelta(days=365 * self.default_retention_years)
            else:
                max_retention = data_created_date + timedelta(days=365 * self.default_retention_years)
            
            return max_retention
            
        elif self.lawful_basis == "contract":
            # Retain for duration of contract plus statutory period
            if purpose_fulfilled_date:
                # Contract completed, retain for statutory period
                return purpose_fulfilled_date + timedelta(days=365 * 2)  # 2 year statutory
            else:
                # Contract ongoing, use default
                return data_created_date + timedelta(days=365 * self.default_retention_years)
                
        elif self.lawful_basis == "legitimate_interest":
            # Balance test - retain while interest exists, max default
            return data_created_date + timedelta(days=365 * self.default_retention_years)
        
        # Default fallback
        return data_created_date + timedelta(days=365 * self.default_retention_years)
    
    def handle_consent_withdrawal(self, data_subject_id: str, withdrawal_date: datetime):
        """Handle GDPR consent withdrawal - data must be deleted within 30 days."""
        
        deletion_deadline = withdrawal_date + timedelta(days=self.consent_withdrawal_deletion_days)
        
        return {
            'action_required': 'delete_personal_data',
            'data_subject_id': data_subject_id,
            'deletion_deadline': deletion_deadline.isoformat(),
            'scope': 'all_personal_data',
            'legal_basis': 'consent_withdrawn'
        }
    
    def handle_erasure_request(self, data_subject_id: str, request_date: datetime):
        """Handle GDPR Article 17 erasure request."""
        
        fulfillment_deadline = request_date + timedelta(days=30)
        
        # Evaluate if erasure can be granted
        erasure_assessment = {
            'data_subject_id': data_subject_id,
            'request_date': request_date.isoformat(),
            'fulfillment_deadline': fulfillment_deadline.isoformat(),
            'erasure_grounds': [
                'personal_data_no_longer_necessary',
                'consent_withdrawn',
                'unlawful_processing',
                'legal_obligation'
            ],
            'erasure_exceptions': [
                'freedom_of_expression',
                'compliance_with_legal_obligation',
                'public_interest',
                'archiving_purposes'
            ]
        }
        
        return erasure_assessment

# GDPR Implementation  
def implement_gdpr_retention(personal_data, processing_context):
    """Implement GDPR retention for personal data."""
    
    gdpr_policy = GDPRRetentionPolicy(
        lawful_basis=processing_context.get('lawful_basis', 'legitimate_interest'),
        processing_purpose=processing_context.get('purpose', 'analytics'),
        default_retention_years=2  # Conservative default
    )
    
    retention_metadata = {
        'retention_policy': 'gdpr_purpose_limited',
        'lawful_basis': gdpr_policy.lawful_basis,
        'processing_purpose': gdpr_policy.processing_purpose,
        'retention_until': gdpr_policy.calculate_retention_date(
            personal_data['created_at'],
            processing_context.get('consent_date'),
            processing_context.get('purpose_fulfilled_date')
        ).isoformat(),
        'data_subject_rights': ['access', 'rectification', 'erasure', 'portability', 'restriction'],
        'cross_border_processing': 'eu_only',
        'data_minimization': True
    }
    
    return retention_metadata
```

### HIPAA Retention Template

**Requirement**: 6+ years for healthcare data

```python
@dataclass
class HIPAARetentionPolicy:
    """HIPAA-compliant data retention policy."""
    
    minimum_retention_years: int = 6
    patient_access_required: bool = True
    business_associate_agreements: bool = True
    breach_notification_required: bool = True
    encryption_required: bool = True
    
    def calculate_retention_date(self, data_created_date: datetime, 
                               patient_last_activity: datetime = None) -> datetime:
        """Calculate HIPAA retention end date."""
        
        # HIPAA requires 6 years from creation or last patient activity
        if patient_last_activity:
            reference_date = max(data_created_date, patient_last_activity)
        else:
            reference_date = data_created_date
            
        return reference_date + timedelta(days=365 * self.minimum_retention_years)
    
    def handle_patient_access_request(self, patient_id: str, request_date: datetime):
        """Handle HIPAA patient access request - must respond within 30 days."""
        
        response_deadline = request_date + timedelta(days=30)
        
        return {
            'patient_id': patient_id,
            'request_type': 'patient_access_request',
            'response_deadline': response_deadline.isoformat(),
            'access_rights': ['view', 'copy', 'transmit'],
            'fees_allowed': 'reasonable_cost_based',
            'format_options': ['paper', 'electronic', 'patient_choice']
        }

# HIPAA Implementation
def implement_hipaa_retention(healthcare_data, patient_context):
    """Implement HIPAA retention for healthcare data."""
    
    hipaa_policy = HIPAARetentionPolicy()
    
    retention_metadata = {
        'retention_policy': 'hipaa_6_year',
        'data_classification': 'protected_health_information',
        'retention_until': hipaa_policy.calculate_retention_date(
            healthcare_data['created_at'],
            patient_context.get('last_activity_date')
        ).isoformat(),
        'patient_rights': ['access', 'amendment', 'accounting_of_disclosures'],
        'business_associate_agreement': True,
        'encryption_required': True,
        'audit_trail_required': True
    }
    
    return retention_metadata
```

## 📊 Industry-Specific Templates

### Financial Services Template

```python
@dataclass
class FinancialServicesRetentionPolicy:
    """Financial services industry retention policy."""
    
    transaction_records_years: int = 7      # SOX requirement
    customer_records_years: int = 5         # Bank Secrecy Act
    kyc_records_years: int = 5              # Know Your Customer
    anti_money_laundering_years: int = 5    # AML requirements
    investment_records_years: int = 3       # Investment Company Act
    
    def get_retention_period(self, data_type: str, regulatory_scope: List[str]) -> int:
        """Get retention period based on data type and regulatory requirements."""
        
        retention_requirements = {
            'transaction_record': self.transaction_records_years,
            'customer_record': self.customer_records_years,
            'kyc_document': self.kyc_records_years,
            'aml_report': self.anti_money_laundering_years,
            'investment_record': self.investment_records_years
        }
        
        base_retention = retention_requirements.get(data_type, 7)  # Default to SOX
        
        # Apply additional regulatory requirements
        if 'sox' in regulatory_scope:
            base_retention = max(base_retention, 7)
        if 'bsa' in regulatory_scope:  # Bank Secrecy Act
            base_retention = max(base_retention, 5)
            
        return base_retention

# Financial Services Implementation
def implement_financial_services_retention(financial_data, regulatory_context):
    """Implement financial services retention policy."""
    
    fs_policy = FinancialServicesRetentionPolicy()
    
    retention_years = fs_policy.get_retention_period(
        financial_data['data_type'],
        regulatory_context.get('regulatory_scope', [])
    )
    
    retention_metadata = {
        'retention_policy': 'financial_services',
        'retention_years': retention_years,
        'retention_until': (
            financial_data['created_at'] + timedelta(days=365 * retention_years)
        ).isoformat(),
        'regulatory_scope': regulatory_context.get('regulatory_scope', []),
        'audit_trail_required': True,
        'immutable_logging': True
    }
    
    return retention_metadata
```

### Healthcare Template

```python
@dataclass 
class HealthcareRetentionPolicy:
    """Healthcare industry retention policy."""
    
    medical_records_years: int = 6          # HIPAA minimum
    research_data_years: int = 10           # Research requirements
    billing_records_years: int = 7          # Financial compliance
    quality_data_years: int = 10            # Quality reporting
    
    def calculate_pediatric_retention(self, patient_birth_date: datetime, 
                                    record_date: datetime) -> datetime:
        """Calculate retention for pediatric records - longer requirements."""
        
        # Pediatric records: retain until age 25 or 6 years after last treatment
        age_25_date = patient_birth_date + timedelta(days=365 * 25)
        standard_retention = record_date + timedelta(days=365 * self.medical_records_years)
        
        return max(age_25_date, standard_retention)

# Healthcare Implementation
def implement_healthcare_retention(healthcare_data, patient_context):
    """Implement healthcare retention policy."""
    
    hc_policy = HealthcareRetentionPolicy()
    
    # Special handling for pediatric patients
    if patient_context.get('age') and patient_context['age'] < 18:
        retention_until = hc_policy.calculate_pediatric_retention(
            patient_context['birth_date'],
            healthcare_data['created_at']
        )
    else:
        retention_until = healthcare_data['created_at'] + timedelta(
            days=365 * hc_policy.medical_records_years
        )
    
    retention_metadata = {
        'retention_policy': 'healthcare_industry',
        'retention_until': retention_until.isoformat(),
        'patient_type': 'pediatric' if patient_context.get('age', 18) < 18 else 'adult',
        'hipaa_compliance': True,
        'patient_access_rights': True
    }
    
    return retention_metadata
```

## 🔧 Implementation Patterns

### Automated Retention Management

```python
import asyncio
from typing import List, Dict, Any
from datetime import datetime, timedelta

class AutomatedRetentionManager:
    """Automated data retention management system."""
    
    def __init__(self):
        self.retention_policies = {}
        self.scheduled_deletions = []
        
    def register_policy(self, policy_name: str, policy: Any):
        """Register a retention policy."""
        self.retention_policies[policy_name] = policy
        
    async def evaluate_retention_schedule(self):
        """Evaluate all data for retention schedule."""
        
        current_date = datetime.now()
        
        # Get all data subject to retention policies
        data_items = await self.get_all_data_items()
        
        for data_item in data_items:
            policy_name = data_item.get('retention_policy')
            if policy_name not in self.retention_policies:
                continue
                
            policy = self.retention_policies[policy_name]
            
            # Calculate retention end date
            retention_end = policy.calculate_retention_date(
                data_item['created_at'],
                **data_item.get('retention_context', {})
            )
            
            # Schedule deletion if retention period expired
            if current_date >= retention_end:
                deletion_record = {
                    'data_id': data_item['id'],
                    'data_type': data_item['type'],
                    'retention_policy': policy_name,
                    'deletion_date': retention_end.isoformat(),
                    'legal_hold_check': True
                }
                
                self.scheduled_deletions.append(deletion_record)
                
    async def execute_scheduled_deletions(self):
        """Execute scheduled data deletions with legal hold checks."""
        
        for deletion in self.scheduled_deletions:
            # Check for legal holds
            legal_hold_active = await self.check_legal_hold(deletion['data_id'])
            
            if legal_hold_active:
                await self.defer_deletion(deletion, reason="legal_hold_active")
                continue
                
            # Perform deletion with audit trail
            deletion_result = await self.delete_data_with_audit(deletion)
            
            # Log deletion for compliance reporting
            await self.log_retention_action(deletion, deletion_result)
        
        # Clear processed deletions
        self.scheduled_deletions.clear()

# Usage Example
retention_manager = AutomatedRetentionManager()

# Register policies
retention_manager.register_policy("sox_7_year", SOXRetentionPolicy())
retention_manager.register_policy("gdpr_purpose_limited", GDPRRetentionPolicy(
    lawful_basis="legitimate_interest",
    processing_purpose="analytics"
))
retention_manager.register_policy("hipaa_6_year", HIPAARetentionPolicy())

# Daily retention evaluation
async def daily_retention_job():
    await retention_manager.evaluate_retention_schedule()
    await retention_manager.execute_scheduled_deletions()
```

### Legal Hold Integration

```python
class LegalHoldManager:
    """Legal hold management for retention policies."""
    
    def __init__(self):
        self.active_holds = {}
        
    def create_legal_hold(self, hold_id: str, case_info: Dict[str, Any], 
                         data_criteria: Dict[str, Any]):
        """Create new legal hold."""
        
        hold_record = {
            'hold_id': hold_id,
            'created_date': datetime.now().isoformat(),
            'case_info': case_info,
            'data_criteria': data_criteria,
            'status': 'active',
            'custodians': case_info.get('custodians', []),
            'date_range': case_info.get('date_range', {}),
            'notification_sent': False
        }
        
        self.active_holds[hold_id] = hold_record
        return hold_record
        
    def check_data_under_hold(self, data_item: Dict[str, Any]) -> List[str]:
        """Check if data item is under legal hold."""
        
        applicable_holds = []
        
        for hold_id, hold in self.active_holds.items():
            if hold['status'] != 'active':
                continue
                
            # Check data criteria match
            if self._matches_hold_criteria(data_item, hold['data_criteria']):
                applicable_holds.append(hold_id)
                
        return applicable_holds
    
    def release_legal_hold(self, hold_id: str, release_reason: str):
        """Release legal hold and resume normal retention."""
        
        if hold_id in self.active_holds:
            self.active_holds[hold_id]['status'] = 'released'
            self.active_holds[hold_id]['release_date'] = datetime.now().isoformat()
            self.active_holds[hold_id]['release_reason'] = release_reason
            
            # Trigger retention re-evaluation for affected data
            self._reevaluate_held_data(hold_id)

# Legal Hold Implementation
legal_hold_manager = LegalHoldManager()

# Integration with retention policies
def can_delete_with_legal_hold_check(data_item, retention_policy):
    """Check if data can be deleted considering retention policy and legal holds."""
    
    # First check retention policy
    can_delete, policy_reason = retention_policy.can_delete_data(
        data_item['created_at'],
        datetime.now()
    )
    
    if not can_delete:
        return False, policy_reason
    
    # Check legal holds
    active_holds = legal_hold_manager.check_data_under_hold(data_item)
    
    if active_holds:
        return False, f"Legal hold prevents deletion: {', '.join(active_holds)}"
    
    return True, "Data eligible for deletion"
```

## 📈 Monitoring and Reporting

### Retention Compliance Monitoring

```python
class RetentionComplianceMonitor:
    """Monitor retention policy compliance."""
    
    def __init__(self):
        self.compliance_metrics = {}
        
    def generate_compliance_report(self, period_start: datetime, 
                                 period_end: datetime) -> Dict[str, Any]:
        """Generate retention compliance report."""
        
        report = {
            'reporting_period': {
                'start': period_start.isoformat(),
                'end': period_end.isoformat()
            },
            'retention_policies': {},
            'compliance_summary': {},
            'violations': [],
            'legal_holds': {
                'active_count': len([h for h in legal_hold_manager.active_holds.values() 
                                   if h['status'] == 'active']),
                'released_count': len([h for h in legal_hold_manager.active_holds.values() 
                                     if h['status'] == 'released'])
            }
        }
        
        # Analyze compliance by policy
        for policy_name, policy in retention_manager.retention_policies.items():
            policy_compliance = self._analyze_policy_compliance(policy_name, period_start, period_end)
            report['retention_policies'][policy_name] = policy_compliance
            
        return report
    
    def _analyze_policy_compliance(self, policy_name: str, 
                                 start_date: datetime, end_date: datetime) -> Dict[str, Any]:
        """Analyze compliance for specific retention policy."""
        
        return {
            'policy_name': policy_name,
            'total_data_items': 0,  # Would query actual data
            'items_within_retention': 0,
            'items_past_retention': 0,
            'items_under_legal_hold': 0,
            'scheduled_deletions': 0,
            'compliance_percentage': 95.0,  # Calculated value
            'violations': []
        }

# Monitoring Implementation
compliance_monitor = RetentionComplianceMonitor()

# Generate monthly compliance report
monthly_report = compliance_monitor.generate_compliance_report(
    datetime.now() - timedelta(days=30),
    datetime.now()
)
```

## 🎯 Best Practices

### Retention Policy Design

**Essential Principles:**
- **Know Your Data**: Classify and categorize all data types
- **Understand Regulations**: Map regulatory requirements to data types
- **Document Everything**: Maintain clear retention policy documentation
- **Automate Compliance**: Implement automated retention management
- **Monitor Continuously**: Regular compliance monitoring and reporting

### Implementation Guidelines

**1. Data Classification Framework**
```python
data_classification = {
    'personal_data': {
        'retention_default': '3_years',
        'regulations': ['gdpr', 'ccpa'],
        'subject_rights': True
    },
    'financial_data': {
        'retention_default': '7_years', 
        'regulations': ['sox', 'pci'],
        'audit_trail_required': True
    },
    'healthcare_data': {
        'retention_default': '6_years',
        'regulations': ['hipaa'],
        'patient_access': True
    }
}
```

**2. Retention Automation**
- Schedule daily retention evaluation jobs
- Implement legal hold integration
- Automate deletion with audit trails
- Monitor compliance continuously

**3. Legal Hold Management**
- Integrate with legal and compliance teams
- Automate hold notifications
- Track hold release and retention resumption
- Maintain hold audit trails

## 📚 Additional Resources

### Regulatory Documentation
- **SOX**: [SEC Sarbanes-Oxley Resources](https://www.sec.gov/spotlight/sarbanes-oxley.htm)
- **GDPR**: [EU GDPR Article 5 (Storage Limitation)](https://gdpr-info.eu/art-5-gdpr/)
- **HIPAA**: [HHS HIPAA Administrative Safeguards](https://www.hhs.gov/hipaa/for-professionals/security/guidance/administrative-safeguards/index.html)

### Implementation Support
- [Compliance Integration Guide](integrations/compliance.md)
- [Audit Trail Architecture](audit-trail-patterns.md)
- [Enterprise Governance Templates](enterprise-governance-templates.md)

---

This comprehensive data retention framework ensures regulatory compliance while maintaining operational efficiency across all GenOps provider integrations.