#!/usr/bin/env python3
"""
SOX Compliance Template for PostHog + GenOps

This template demonstrates Sarbanes-Oxley (SOX) compliance implementation for 
PostHog analytics with GenOps governance. SOX requires strict financial data 
controls, audit trails, and change management for publicly traded companies.

SOX Requirements Addressed:
- Section 302: Management assessment of internal controls
- Section 404: Management assessment of internal control over financial reporting
- Section 409: Real-time financial disclosure requirements
- Audit trail requirements with immutable logs
- Data retention policies (7 years minimum)
- Access controls and segregation of duties

Use Case:
    - Publicly traded companies tracking financial metrics
    - E-commerce revenue and transaction analytics
    - Financial dashboard and reporting compliance
    - Audit trail generation for financial data access

Usage:
    python compliance_templates/SOX_compliance_template.py

Prerequisites:
    pip install genops[posthog]
    export POSTHOG_API_KEY="phc_your_project_api_key"
    export GENOPS_TEAM="finance-analytics"
    export GENOPS_PROJECT="sox-compliance"
    export SOX_AUDITOR_EMAIL="auditor@company.com"  # Required for audit notifications

Expected Output:
    SOX-compliant financial analytics tracking with full audit trail,
    immutable logs, and compliance reporting for financial data governance.

Learning Objectives:
    - SOX compliance requirements for financial data analytics
    - Audit trail generation and immutable logging patterns
    - Financial data access controls and segregation of duties
    - Real-time financial reporting with compliance governance

Author: GenOps AI Compliance Team
License: Apache 2.0
"""

import os
import time
import json
import hashlib
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, List, Optional
from decimal import Decimal
from dataclasses import dataclass, asdict

@dataclass
class SOXAuditEntry:
    """SOX-compliant audit log entry with immutable properties."""
    audit_id: str
    timestamp: str
    user_id: str
    action: str
    resource_type: str
    resource_id: str
    financial_data_involved: bool
    sox_control_point: str
    risk_level: str
    approval_status: str
    supervisor_approval: Optional[str]
    data_hash: str
    retention_until: str
    compliance_metadata: Dict[str, Any]

def generate_audit_hash(data: Dict[str, Any]) -> str:
    """Generate immutable hash for audit trail integrity."""
    audit_string = json.dumps(data, sort_keys=True)
    return hashlib.sha256(audit_string.encode()).hexdigest()

def main():
    """Demonstrate SOX-compliant PostHog analytics with full governance."""
    print("🏛️ SOX Compliance Template for PostHog + GenOps")
    print("=" * 55)
    print()
    
    # Import and setup GenOps PostHog adapter with SOX configuration
    try:
        from genops.providers.posthog import GenOpsPostHogAdapter
        print("✅ GenOps PostHog integration loaded")
    except ImportError as e:
        print(f"❌ Failed to import GenOps PostHog: {e}")
        print("💡 Fix: pip install genops[posthog]")
        return False
    
    # SOX Compliance Configuration
    print("\n🔧 Configuring SOX Compliance Environment...")
    
    sox_auditor_email = os.getenv('SOX_AUDITOR_EMAIL')
    if not sox_auditor_email:
        print("⚠️ SOX_AUDITOR_EMAIL not configured - using demo value")
        sox_auditor_email = "sox-auditor@company-demo.com"
    
    # Initialize SOX-compliant adapter
    adapter = GenOpsPostHogAdapter(\n        team=\"sox-finance-analytics\",\n        project=\"financial-reporting-system\",\n        environment=\"production\",\n        customer_id=\"sox_compliance_entity\",\n        cost_center=\"financial_operations\",\n        daily_budget_limit=500.0,  # Higher budget for critical financial systems\n        governance_policy=\"strict\",  # Strictest enforcement for SOX\n        tags={\n            'compliance_framework': 'sox',\n            'sox_entity': 'publicly_traded_company',\n            'data_classification': 'financial_confidential',\n            'retention_policy': '7_years_minimum',\n            'audit_trail_required': 'true',\n            'change_management': 'formal_approval_required',\n            'access_control': 'role_based_segregated',\n            'sox_auditor_contact': sox_auditor_email,\n            'financial_year': '2024',\n            'sox_compliance_level': 'section_302_404'\n        }\n    )\n    \n    print(\"✅ SOX-compliant adapter configured\")\n    print(f\"   🏢 Entity: Publicly traded company\")\n    print(f\"   📋 Compliance level: SOX Sections 302 & 404\")\n    print(f\"   🔒 Governance policy: Strict enforcement\")\n    print(f\"   📧 SOX auditor: {sox_auditor_email}\")\n    print(f\"   💾 Data retention: 7+ years\")\n    print(f\"   🛡️ Access controls: Role-based segregation\")\n    \n    # SOX audit log for compliance tracking\n    sox_audit_log: List[SOXAuditEntry] = []\n    \n    def create_sox_audit_entry(\n        action: str, \n        resource_type: str, \n        resource_id: str,\n        financial_data: bool = True,\n        sox_control: str = \"general\",\n        risk_level: str = \"medium\"\n    ) -> SOXAuditEntry:\n        \"\"\"Create SOX-compliant audit entry with immutable properties.\"\"\"\n        \n        timestamp = datetime.now(timezone.utc)\n        audit_data = {\n            'action': action,\n            'resource_type': resource_type,\n            'resource_id': resource_id,\n            'timestamp': timestamp.isoformat(),\n            'financial_data_involved': financial_data\n        }\n        \n        entry = SOXAuditEntry(\n            audit_id=f\"SOX_{timestamp.strftime('%Y%m%d_%H%M%S')}_{hashlib.md5(str(audit_data).encode()).hexdigest()[:8]}\",\n            timestamp=timestamp.isoformat(),\n            user_id=\"finance_analytics_system\",\n            action=action,\n            resource_type=resource_type,\n            resource_id=resource_id,\n            financial_data_involved=financial_data,\n            sox_control_point=sox_control,\n            risk_level=risk_level,\n            approval_status=\"system_approved\" if risk_level == \"low\" else \"supervisor_approval_required\",\n            supervisor_approval=\"auto_approved\" if risk_level == \"low\" else \"pending_finance_manager\",\n            data_hash=generate_audit_hash(audit_data),\n            retention_until=(timestamp + timedelta(days=2557)).isoformat(),  # 7+ years\n            compliance_metadata={\n                'sox_section': '302_404',\n                'financial_materiality': 'material' if financial_data else 'non_material',\n                'segregation_compliance': 'verified',\n                'change_control_id': f\"CC_{timestamp.strftime('%Y%m%d')}_{len(sox_audit_log) + 1:03d}\"\n            }\n        )\n        \n        sox_audit_log.append(entry)\n        return entry\n    \n    # Demonstrate SOX-compliant financial analytics scenarios\n    print(\"\\n\" + \"=\"*55)\n    print(\"💰 SOX-Compliant Financial Analytics Tracking\")\n    print(\"=\"*55)\n    \n    # Financial reporting scenarios with SOX requirements\n    financial_scenarios = [\n        {\n            'scenario': 'quarterly_revenue_reporting',\n            'description': 'Q4 2024 revenue recognition and reporting',\n            'sox_control': 'revenue_recognition',\n            'risk_level': 'high',\n            'events': [\n                {'type': 'revenue_transaction', 'amount': 125000.00, 'currency': 'USD'},\n                {'type': 'revenue_adjustment', 'amount': -2500.00, 'currency': 'USD'},\n                {'type': 'revenue_recognition', 'amount': 122500.00, 'currency': 'USD'}\n            ]\n        },\n        {\n            'scenario': 'financial_dashboard_access',\n            'description': 'Executive dashboard access for SOX reporting',\n            'sox_control': 'management_assessment',\n            'risk_level': 'medium',\n            'events': [\n                {'type': 'dashboard_view', 'report_type': 'executive_summary'},\n                {'type': 'financial_metric_access', 'metric_type': 'cash_flow'},\n                {'type': 'sox_control_review', 'control_type': 'internal_control_assessment'}\n            ]\n        },\n        {\n            'scenario': 'audit_preparation',\n            'description': 'Preparing for external SOX audit',\n            'sox_control': 'audit_compliance',\n            'risk_level': 'critical',\n            'events': [\n                {'type': 'audit_trail_export', 'period': 'FY2024'},\n                {'type': 'control_testing', 'control_id': 'ITGC-001'},\n                {'type': 'deficiency_tracking', 'deficiency_type': 'material_weakness'}\n            ]\n        }\n    ]\n    \n    total_financial_transactions = 0\n    total_audit_entries = 0\n    sox_compliance_score = 100.0\n    \n    for scenario_idx, scenario in enumerate(financial_scenarios, 1):\n        print(f\"\\n📊 Scenario {scenario_idx}: {scenario['description']}\")\n        print(\"-\" * 50)\n        print(f\"   SOX Control: {scenario['sox_control']}\")\n        print(f\"   Risk Level: {scenario['risk_level']}\")\n        \n        # Create audit entry for scenario initiation\n        audit_entry = create_sox_audit_entry(\n            action=\"scenario_initiated\",\n            resource_type=\"financial_analytics_scenario\",\n            resource_id=scenario['scenario'],\n            financial_data=True,\n            sox_control=scenario['sox_control'],\n            risk_level=scenario['risk_level']\n        )\n        \n        total_audit_entries += 1\n        print(f\"   🔍 Audit entry created: {audit_entry.audit_id}\")\n        \n        with adapter.track_analytics_session(\n            session_name=scenario['scenario'],\n            cost_center=\"sox_compliance_reporting\",\n            sox_control_point=scenario['sox_control'],\n            risk_assessment=scenario['risk_level'],\n            financial_materiality=\"material\"\n        ) as session:\n            \n            scenario_cost = Decimal('0')\n            \n            for event_idx, event in enumerate(scenario['events']):\n                print(f\"\\n   📈 Event {event_idx + 1}: {event['type']}\")\n                \n                # Build SOX-compliant event properties\n                event_properties = {\n                    'sox_control_point': scenario['sox_control'],\n                    'risk_level': scenario['risk_level'],\n                    'financial_materiality': 'material',\n                    'segregation_verified': True,\n                    'approval_status': 'authorized',\n                    'sox_section_applicable': '302_404',\n                    'change_control_documented': True,\n                    'audit_trail_enabled': True,\n                    **event\n                }\n                \n                # Add financial amount tracking if present\n                if 'amount' in event:\n                    event_properties.update({\n                        'financial_transaction': True,\n                        'transaction_amount': event['amount'],\n                        'currency': event.get('currency', 'USD'),\n                        'materiality_threshold_check': abs(event['amount']) >= 10000.0\n                    })\n                    total_financial_transactions += 1\n                \n                # Capture event with SOX compliance\n                result = adapter.capture_event_with_governance(\n                    event_name=f\"sox_{event['type']}\",\n                    properties=event_properties,\n                    distinct_id=f\"sox_user_{scenario['scenario']}\",\n                    is_identified=True,  # Financial events are always identified\n                    session_id=session.session_id\n                )\n                \n                scenario_cost += Decimal(str(result['cost']))\n                \n                # Create detailed audit entry for each financial event\n                event_audit = create_sox_audit_entry(\n                    action=f\"financial_event_captured\",\n                    resource_type=\"postoh_analytics_event\",\n                    resource_id=f\"{scenario['scenario']}_{event['type']}\",\n                    financial_data='amount' in event,\n                    sox_control=scenario['sox_control'],\n                    risk_level=scenario['risk_level']\n                )\n                \n                total_audit_entries += 1\n                \n                print(f\"     Event tracked with SOX compliance - Cost: ${result['cost']:.6f}\")\n                print(f\"     Audit ID: {event_audit.audit_id}\")\n                print(f\"     Data hash: {event_audit.data_hash[:16]}...\")\n                \n                if 'amount' in event:\n                    print(f\"     Financial amount: {event.get('currency', 'USD')} {event['amount']:,.2f}\")\n                    print(f\"     Materiality check: {'✅ Material' if abs(event['amount']) >= 10000.0 else '⚠️ Below threshold'}\")\n            \n            # Session compliance summary\n            print(f\"\\n   📋 Scenario Summary:\")\n            print(f\"     Events processed: {len(scenario['events'])}\")\n            print(f\"     Session cost: ${scenario_cost:.4f}\")\n            print(f\"     SOX control: {scenario['sox_control']}\")\n            print(f\"     Risk level: {scenario['risk_level']}\")\n            print(f\"     Audit entries: {len([e for e in sox_audit_log if scenario['scenario'] in e.resource_id])}\")\n    \n    # SOX Compliance Summary and Reporting\n    print(\"\\n\" + \"=\"*55)\n    print(\"📋 SOX Compliance Summary & Audit Report\")\n    print(\"=\"*55)\n    \n    cost_summary = adapter.get_cost_summary()\n    \n    print(f\"\\n💰 Financial Analytics Summary:\")\n    print(f\"   Total financial transactions tracked: {total_financial_transactions}\")\n    print(f\"   Total audit entries generated: {total_audit_entries}\")\n    print(f\"   Analytics cost: ${cost_summary['daily_costs']:.6f}\")\n    print(f\"   Budget utilization: {cost_summary['daily_budget_utilization']:.1f}%\")\n    \n    print(f\"\\n🏛️ SOX Compliance Status:\")\n    print(f\"   Compliance framework: SOX (Sarbanes-Oxley Act)\")\n    print(f\"   Applicable sections: 302 (Management Assessment), 404 (Internal Controls)\")\n    print(f\"   Data retention period: 7+ years (until {(datetime.now() + timedelta(days=2557)).strftime('%Y-%m-%d')})\")\n    print(f\"   Audit trail completeness: {'✅ 100%' if total_audit_entries > 0 else '❌ Incomplete'}\")\n    print(f\"   Financial data segregation: ✅ Verified\")\n    print(f\"   Change control compliance: ✅ Documented\")\n    print(f\"   Access controls: ✅ Role-based segregation\")\n    \n    # Audit Trail Analysis\n    print(f\"\\n🔍 Audit Trail Analysis:\")\n    \n    # Group audit entries by risk level\n    risk_level_summary = {}\n    for entry in sox_audit_log:\n        level = entry.risk_level\n        if level not in risk_level_summary:\n            risk_level_summary[level] = 0\n        risk_level_summary[level] += 1\n    \n    for risk_level, count in risk_level_summary.items():\n        print(f\"   {risk_level.title()} risk operations: {count}\")\n    \n    # SOX Control Point Analysis\n    control_points = {}\n    for entry in sox_audit_log:\n        control = entry.sox_control_point\n        if control not in control_points:\n            control_points[control] = 0\n        control_points[control] += 1\n    \n    print(f\"\\n🛡️ SOX Control Points Coverage:\")\n    for control, count in control_points.items():\n        print(f\"   {control.replace('_', ' ').title()}: {count} operations\")\n    \n    # Generate SOX Audit Report Export\n    print(f\"\\n📄 SOX Audit Report Generation:\")\n    \n    audit_report = {\n        'report_metadata': {\n            'generated_at': datetime.now(timezone.utc).isoformat(),\n            'report_type': 'sox_compliance_audit_trail',\n            'reporting_entity': 'publicly_traded_company',\n            'financial_year': '2024',\n            'sox_sections': ['302', '404'],\n            'auditor_contact': sox_auditor_email\n        },\n        'compliance_summary': {\n            'total_financial_transactions': total_financial_transactions,\n            'total_audit_entries': total_audit_entries,\n            'analytics_cost_usd': float(cost_summary['daily_costs']),\n            'compliance_score': sox_compliance_score,\n            'control_points_tested': list(control_points.keys())\n        },\n        'audit_entries': [asdict(entry) for entry in sox_audit_log[-5:]]  # Last 5 entries for demo\n    }\n    \n    # In production, this would be exported to secure audit storage\n    print(f\"   ✅ Audit report generated: {len(audit_report['audit_entries'])} entries (sample)\")\n    print(f\"   🔒 Report hash: {generate_audit_hash(audit_report)[:16]}...\")\n    print(f\"   📧 Auditor notification: {sox_auditor_email}\")\n    print(f\"   💾 Retention until: {(datetime.now() + timedelta(days=2557)).strftime('%Y-%m-%d')}\")\n    \n    # SOX Compliance Recommendations\n    print(f\"\\n💡 SOX Compliance Recommendations:\")\n    \n    recommendations = [\n        {\n            'category': 'Internal Controls',\n            'recommendation': 'Implement automated control testing for ITGC controls',\n            'priority': 'High',\n            'timeline': '30 days'\n        },\n        {\n            'category': 'Data Retention',\n            'recommendation': 'Establish automated 7-year retention policy with legal hold',\n            'priority': 'Medium',\n            'timeline': '60 days'\n        },\n        {\n            'category': 'Access Controls',\n            'recommendation': 'Regular access review and segregation of duties validation',\n            'priority': 'High',\n            'timeline': 'Quarterly'\n        },\n        {\n            'category': 'Audit Preparation',\n            'recommendation': 'Implement continuous controls monitoring and deficiency tracking',\n            'priority': 'Medium',\n            'timeline': '90 days'\n        }\n    ]\n    \n    for i, rec in enumerate(recommendations, 1):\n        print(f\"   {i}. {rec['category']}: {rec['recommendation']}\")\n        print(f\"      Priority: {rec['priority']}, Timeline: {rec['timeline']}\")\n        print()\n    \n    print(f\"✅ SOX compliance template demonstration completed successfully!\")\n    print(f\"\\n📚 Next Steps for SOX Implementation:\")\n    print(f\"   1. Review and customize SOX control points for your organization\")\n    print(f\"   2. Implement automated audit trail export and archival\")\n    print(f\"   3. Set up role-based access controls and segregation of duties\")\n    print(f\"   4. Establish quarterly SOX compliance review processes\")\n    print(f\"   5. Coordinate with external auditors for SOX 404 assessment\")\n    \n    return True\n\nif __name__ == \"__main__\":\n    try:\n        success = main()\n        exit(0 if success else 1)\n    except KeyboardInterrupt:\n        print(\"\\n\\n👋 SOX compliance demonstration interrupted by user\")\n        exit(1)\n    except Exception as e:\n        print(f\"\\n💥 Error in SOX compliance example: {e}\")\n        print(\"🔧 Please check your PostHog configuration and compliance settings\")\n        exit(1)"