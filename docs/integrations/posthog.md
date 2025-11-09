# PostHog Integration

> 📖 **Navigation:** [Quickstart (5 min)](../posthog-quickstart.md) → **Complete Guide** → [Examples](../../examples/posthog/)

Complete integration guide for PostHog product analytics with GenOps governance, cost intelligence, and policy enforcement.

## 🗺️ Choose Your Learning Path

**👋 New to PostHog + GenOps?** Start here:
1. **[5-minute Quickstart](../posthog-quickstart.md)** - Get running with zero code changes
2. **[Interactive Examples](../../examples/posthog/)** - Copy-paste working code
3. **Come back here** for deep-dive documentation

**📚 Looking for specific info?** Jump to:
- [Cost Intelligence & ROI](../cost-intelligence-guide.md) - Calculate ROI and optimize costs
- [Enterprise Governance](../enterprise-governance-templates.md) - Compliance templates (SOX, GDPR, HIPAA)
- [Production Patterns](#enterprise-deployment-patterns) - HA, scaling, monitoring

## 🗺️ Visual Learning Path

```
🚀 START HERE: 5-minute Quickstart
│   ├── Zero-code setup
│   ├── Basic validation
│   └── Success confirmation
│
├─── 📋 HANDS-ON: Interactive Examples (5-30 min)
│    ├── basic_tracking.py      → See governance in action
│    ├── cost_optimization.py   → Learn cost intelligence  
│    ├── advanced_features.py   → Multi-feature patterns
│    └── production_patterns.py → Enterprise deployment
│
├─── 📖 DEEP-DIVE: Complete Guide (15-60 min)
│    ├── Manual Configuration   → Full control & customization
│    ├── Governance Policies    → Team attribution & budgets
│    ├── Production Monitoring  → Dashboards & alerting
│    └── Troubleshooting       → Problem solving
│
├─── 💰 BUSINESS: Cost Intelligence (15-45 min)
│    ├── ROI Calculator        → Business justification
│    ├── Cost Optimization     → Reduce analytics costs
│    └── Budget Forecasting    → Plan future investments
│
└─── 🏢 ENTERPRISE: Governance Templates (30-120 min)
     ├── SOX Compliance        → Financial regulations
     ├── GDPR Compliance       → EU data protection
     ├── HIPAA Compliance      → Healthcare requirements
     └── Multi-Tenant Setup    → SaaS deployments
```

**🎯 Choose your path based on:**
- **Time available:** 5 min (Quickstart) → 30 min (Examples) → 60+ min (Enterprise)
- **Role:** Developer (Examples) → FinOps (Cost Intelligence) → Architect (Enterprise)
- **Goal:** Quick setup → Production deployment → Compliance requirements

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start) ⏱️ 5 minutes
- [Manual Adapter Usage](#manual-adapter-usage) ⏱️ 15 minutes
- [Cost Intelligence](#cost-intelligence) ⏱️ 10 minutes  
- [Governance Configuration](#governance-configuration) ⏱️ 20 minutes
- [Enterprise Deployment Patterns](#enterprise-deployment-patterns) ⏱️ 30 minutes
- [Production Monitoring](#production-monitoring) ⏱️ 20 minutes
- [Validation and Troubleshooting](#validation-and-troubleshooting) ⏱️ 10 minutes
- [API Reference](#api-reference)

**🚀 Advanced Guides:**
- **[Cost Intelligence & ROI Guide](../cost-intelligence-guide.md)** - ROI templates, cost optimization, and budget forecasting
- **[Production Deployment Patterns](../../examples/posthog/production_patterns.py)** - Enterprise architecture and scaling patterns

## Overview

The GenOps PostHog integration provides comprehensive governance for product analytics operations. PostHog is a leading open-source product analytics platform that provides event tracking, feature flags, session recordings, and A/B testing. This integration adds cost tracking, team attribution, and policy enforcement to your PostHog workflows.

### 🚀 Quick Value Proposition

| ⏱️ Time Investment | 💰 Value Delivered | 🎯 Use Case |
|-------------------|-------------------|-------------|
| **5 minutes** | Zero-code governance for existing PostHog workflows | Quick wins |
| **30 minutes** | Complete cost intelligence and optimization | Production ready |
| **2 hours** | Enterprise governance with compliance | Mission critical |

### Key Features

- **Product Analytics Governance**: Event tracking with team/project attribution and cost intelligence
- **Feature Flag Management**: Cost-aware feature flag evaluation with governance oversight
- **Session Recording Intelligence**: User session monitoring with cost optimization and governance
- **A/B Testing Governance**: Experiment cost tracking with intelligent budget management
- **Budget Enforcement**: Real-time cost tracking with configurable budget limits and alerts
- **Zero-Code Auto-Instrumentation**: Transparent governance for existing PostHog code
- **Multi-Environment Support**: Environment-specific analytics with governance policies

> 💡 **New to PostHog?** Check our [5-minute quickstart guide](../posthog-quickstart.md) for immediate setup.

## Quick Start

### Prerequisites

```bash
# Install GenOps with PostHog support
pip install genops[posthog]

# Set environment variables
export POSTHOG_API_KEY="phc_your_project_api_key"
export GENOPS_TEAM="analytics-team"          # Optional but recommended
export GENOPS_PROJECT="product-analytics"    # Optional but recommended
```

### Zero-Code Integration

```python
# Add ONE line to enable governance for all existing PostHog code
from genops.providers.posthog import auto_instrument
auto_instrument()

# Your existing PostHog code works unchanged
import posthog
posthog.capture("user_signed_up", {"email": "user@example.com"})
# ↑ Now automatically tracked with cost + governance
```

### Validation

```python
# Verify setup is working
from genops.providers.posthog_validation import validate_setup, print_validation_result
result = validate_setup()
print_validation_result(result)
```

## Manual Adapter Usage

For advanced control and customization, use the manual adapter:

### Basic Usage

```python
from genops.providers.posthog import GenOpsPostHogAdapter

# Create adapter with governance configuration
adapter = GenOpsPostHogAdapter(
    posthog_api_key="phc_your_project_api_key",
    team="analytics-team",
    project="product-analytics",
    environment="production",
    daily_budget_limit=100.0,
    enable_governance=True,
    governance_policy="advisory"  # advisory, enforced, or strict
)

# Track analytics session with governance
with adapter.track_analytics_session(
    session_name="user_onboarding_flow",
    customer_id="enterprise_123"
) as session:
    
    # Event tracking with automatic cost attribution
    result = adapter.capture_event_with_governance(
        event_name="signup_completed",
        properties={"plan": "business", "value": 299.00},
        distinct_id="user_12345",
        is_identified=True,
        session_id=session.session_id
    )
    
    # Feature flag evaluation with cost tracking
    flag_value, metadata = adapter.evaluate_feature_flag_with_governance(
        flag_key="new_dashboard_layout",
        distinct_id="user_12345",
        properties={"user_segment": "enterprise"},
        session_id=session.session_id
    )
    
    print(f"Event cost: ${result['cost']:.6f}")
    print(f"Flag cost: ${metadata['cost']:.6f}")
```

### Advanced Configuration

```python
from genops.providers.posthog import GenOpsPostHogAdapter

# Enterprise-grade configuration
adapter = GenOpsPostHogAdapter(
    posthog_api_key=os.getenv('POSTHOG_API_KEY'),
    posthog_host="https://eu.posthog.com",  # EU instance
    team="enterprise-analytics",
    project="saas-platform",
    environment="production",
    customer_id="tenant_123",  # Multi-tenant attribution
    cost_center="product_team",
    daily_budget_limit=500.0,
    monthly_budget_limit=10000.0,
    enable_governance=True,
    enable_cost_alerts=True,
    governance_policy="enforced",  # Strict budget enforcement
    tags={
        'compliance_level': 'sox',
        'data_classification': 'internal',
        'team_tier': 'enterprise',
        'cost_optimization': 'enabled'
    }
)
```

## Cost Intelligence

### Real-Time Cost Tracking

PostHog pricing is based on usage volumes with generous free tiers:

- **Events**: 1M free/month, then tiered pricing starting at $0.00005/event
- **Feature Flags**: 1M free requests/month, then $0.000005/request
- **Session Recordings**: 5K free recordings/month, then $0.000071/recording
- **LLM Analytics**: 100K free events/month, then $0.0001/event

```python
# Get real-time cost summary
cost_summary = adapter.get_cost_summary()
print(f"Daily costs: ${cost_summary['daily_costs']:.4f}")
print(f"Monthly projection: ${cost_summary['daily_costs'] * 30:.2f}")
print(f"Budget utilization: {cost_summary['daily_budget_utilization']:.1f}%")
```

### Volume Discount Analysis

```python
# Analyze volume discount opportunities
analysis = adapter.get_volume_discount_analysis(
    projected_monthly_events=500000
)

print(f"Current monthly cost: ${analysis['projected_monthly_cost']:.2f}")
print(f"Cost per event: ${analysis['cost_per_event']:.6f}")

# Get optimization recommendations
for rec in analysis['optimization_recommendations']:
    print(f"Optimization: {rec['optimization_type']}")
    print(f"Potential savings: ${rec['potential_savings_per_month']:.2f}/month")
    print(f"Priority score: {rec['priority_score']:.1f}/100")
```

### Cost Forecasting

```python
from genops.providers.posthog import PostHogCostCalculator

calculator = PostHogCostCalculator()

# Scenario analysis
scenarios = [
    {"events": 100000, "flags": 50000, "recordings": 2000},  # Current
    {"events": 200000, "flags": 100000, "recordings": 5000}, # 2x growth
    {"events": 500000, "flags": 250000, "recordings": 10000} # 5x growth
]

for i, scenario in enumerate(scenarios, 1):
    cost = calculator.calculate_session_cost(**scenario)
    print(f"Scenario {i}: ${cost.total_cost:.2f}/month")
    print(f"  Events: {scenario['events']:,} → ${cost.cost_breakdown['events']:.2f}")
    print(f"  Flags: {scenario['flags']:,} → ${cost.cost_breakdown['feature_flags']:.2f}")
    print(f"  Recordings: {scenario['recordings']:,} → ${cost.cost_breakdown['session_recordings']:.2f}")
```

## Governance Configuration

### Team and Project Attribution

```python
# Configure team-based cost attribution
adapter = GenOpsPostHogAdapter(
    team="mobile-analytics",           # Cost attribution
    project="ios-app",                # Project tracking
    cost_center="mobile_development",  # Financial reporting
    customer_id="enterprise_client",   # Multi-tenant attribution
    environment="production",          # Environment segregation
    tags={
        'app_version': '2.1.0',
        'platform': 'ios',
        'team_tier': 'premium'
    }
)
```

### Budget Governance

```python
# Configure budget enforcement
adapter = GenOpsPostHogAdapter(
    daily_budget_limit=200.0,
    monthly_budget_limit=5000.0,
    enable_cost_alerts=True,
    governance_policy="enforced",  # Enforce budget limits
    tags={'budget_tier': 'enterprise'}
)

# Budget-aware analytics session
try:
    with adapter.track_analytics_session("high_volume_campaign") as session:
        # Analytics operations with budget enforcement
        for event_data in campaign_events:
            adapter.capture_event_with_governance(**event_data)
            
except GenOpsBudgetExceededError as e:
    print(f"Budget exceeded: {e}")
    # Implement budget overflow handling
```

### Multi-Environment Governance

```python
# Development environment
dev_adapter = GenOpsPostHogAdapter(
    environment="development",
    daily_budget_limit=25.0,
    governance_policy="advisory",  # Flexible for development
    tags={'cost_optimization': 'aggressive'}
)

# Production environment
prod_adapter = GenOpsPostHogAdapter(
    environment="production",
    daily_budget_limit=500.0,
    governance_policy="enforced",  # Strict budget enforcement
    tags={'compliance_required': 'true'}
)
```

### Compliance Integration

```python
# GDPR compliance configuration
gdpr_adapter = GenOpsPostHogAdapter(
    governance_policy="strict",
    tags={
        'compliance_framework': 'gdpr',
        'data_retention_days': '1095',  # 3 years
        'consent_required': 'true',
        'data_classification': 'personal'
    }
)

# SOX compliance configuration  
sox_adapter = GenOpsPostHogAdapter(
    governance_policy="enforced",
    tags={
        'compliance_framework': 'sox',
        'audit_trail_required': 'true',
        'data_retention_days': '2555',  # 7 years
        'financial_reporting': 'true'
    }
)
```

## Enterprise Deployment Patterns

### High Availability Setup

```python
from genops.providers.posthog import GenOpsPostHogAdapter

# Primary region adapter
primary_adapter = GenOpsPostHogAdapter(
    posthog_api_key=os.getenv('POSTHOG_API_KEY'),
    team="ha-analytics",
    project="global-platform",
    environment="production-primary",
    daily_budget_limit=800.0,
    tags={
        'region': 'us-east-1',
        'ha_role': 'primary',
        'failover_enabled': 'true'
    }
)

# Secondary region adapter
secondary_adapter = GenOpsPostHogAdapter(
    posthog_api_key=os.getenv('POSTHOG_API_KEY'),  
    team="ha-analytics",
    project="global-platform",
    environment="production-secondary",
    daily_budget_limit=400.0,
    tags={
        'region': 'us-west-2',
        'ha_role': 'secondary',
        'failover_enabled': 'true'
    }
)

# Failover logic
def track_with_failover(event_name, properties, distinct_id):
    try:
        return primary_adapter.capture_event_with_governance(
            event_name=event_name,
            properties=properties,
            distinct_id=distinct_id
        )
    except Exception as primary_error:
        logger.warning(f"Primary region failed: {primary_error}")
        return secondary_adapter.capture_event_with_governance(
            event_name=event_name,
            properties=properties,
            distinct_id=distinct_id
        )
```

### Multi-Tenant Architecture

```python
# Tenant-specific adapters with isolation
def create_tenant_adapter(tenant_config):
    return GenOpsPostHogAdapter(
        team=f"tenant_{tenant_config['tenant_id']}",
        project="multi_tenant_analytics",
        customer_id=tenant_config['tenant_id'],
        daily_budget_limit=tenant_config['daily_budget'],
        governance_policy=tenant_config['compliance_level'],
        cost_center=f"tenant_{tenant_config['tier']}",
        tags={
            'tenant_tier': tenant_config['tier'],
            'sla_level': tenant_config['sla'],
            'data_residency': tenant_config['region'],
            'compliance_requirements': ','.join(tenant_config['compliance'])
        }
    )

# Tenant configurations
tenants = [
    {
        'tenant_id': 'enterprise_corp',
        'tier': 'enterprise',
        'daily_budget': 500.0,
        'compliance_level': 'strict',
        'sla': 'premium',
        'region': 'us',
        'compliance': ['sox', 'gdpr']
    },
    {
        'tenant_id': 'startup_inc',
        'tier': 'professional',
        'daily_budget': 100.0,
        'compliance_level': 'standard',
        'sla': 'standard',
        'region': 'us',
        'compliance': ['gdpr']
    }
]

# Create tenant adapters
tenant_adapters = {
    tenant['tenant_id']: create_tenant_adapter(tenant)
    for tenant in tenants
}
```

### Auto-Scaling Integration

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ScalablePostHogAnalytics:
    def __init__(self, base_config):
        self.base_adapter = GenOpsPostHogAdapter(**base_config)
        self.executor = ThreadPoolExecutor(max_workers=10)
        
    async def process_high_volume_events(self, events):
        """Process high-volume analytics events with auto-scaling."""
        
        # Determine processing strategy based on volume
        if len(events) > 10000:
            # High volume: use batch processing with sampling
            return await self._process_with_sampling(events, sample_rate=0.1)
        elif len(events) > 1000:
            # Medium volume: parallel processing
            return await self._process_parallel(events)
        else:
            # Low volume: sequential processing
            return await self._process_sequential(events)
    
    async def _process_with_sampling(self, events, sample_rate):
        sampled_events = random.sample(events, int(len(events) * sample_rate))
        
        with self.base_adapter.track_analytics_session(
            "high_volume_sampling",
            sample_rate=sample_rate,
            original_volume=len(events)
        ) as session:
            
            tasks = []
            for event in sampled_events:
                task = asyncio.create_task(self._process_single_event(event, session))
                tasks.append(task)
            
            return await asyncio.gather(*tasks)
```

## Production Monitoring

### OpenTelemetry Integration

```python
from opentelemetry import trace
from genops.providers.posthog import GenOpsPostHogAdapter

# Configure OpenTelemetry export
adapter = GenOpsPostHogAdapter(
    team="observability-team",
    project="production-monitoring",
    tags={
        'otel_export': 'enabled',
        'tracing_enabled': 'true',
        'metrics_export': 'datadog,grafana'
    }
)

# Analytics with distributed tracing
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("analytics_session") as span:
    with adapter.track_analytics_session("user_journey") as session:
        # Analytics operations are automatically traced
        result = adapter.capture_event_with_governance(
            event_name="user_conversion",
            properties={"value": 299.0, "source": "organic"}
        )
        
        # Add trace metadata
        span.set_attributes({
            "analytics.cost": result['cost'],
            "analytics.session_id": session.session_id,
            "analytics.governance": "enabled"
        })
```

### Metrics and Alerting

```python
# Cost-based alerting configuration
adapter = GenOpsPostHogAdapter(
    enable_cost_alerts=True,
    tags={
        'alert_webhook': 'https://your-alerting-system.com/webhook',
        'alert_thresholds': 'daily:80,weekly:90,monthly:95',
        'escalation_policy': 'team_lead,manager,finance'
    }
)

# Custom alerting integration
def setup_cost_monitoring():
    cost_summary = adapter.get_cost_summary()
    
    # Daily budget alert
    if cost_summary['daily_budget_utilization'] > 80:
        send_alert(
            level='warning',
            message=f"PostHog costs approaching daily limit: {cost_summary['daily_budget_utilization']:.1f}%"
        )
    
    # Weekly trend analysis
    weekly_trend = analyze_weekly_cost_trend()
    if weekly_trend['growth_rate'] > 50:
        send_alert(
            level='info',
            message=f"PostHog costs growing rapidly: {weekly_trend['growth_rate']:.1f}% week-over-week"
        )
```

### Dashboard Integration

```python
# Grafana dashboard data export
def export_analytics_metrics():
    adapter = get_current_adapter()
    cost_summary = adapter.get_cost_summary()
    
    # Export metrics in Prometheus format
    metrics = {
        'posthog_daily_cost': cost_summary['daily_costs'],
        'posthog_budget_utilization': cost_summary['daily_budget_utilization'],
        'posthog_governance_active': 1 if cost_summary['governance_enabled'] else 0,
        'posthog_events_today': get_daily_event_count(),
        'posthog_flags_evaluated': get_daily_flag_count()
    }
    
    return metrics

# Datadog integration
def send_to_datadog():
    metrics = export_analytics_metrics()
    
    for metric_name, value in metrics.items():
        datadog.statsd.gauge(
            metric_name,
            value,
            tags=[
                f"team:{adapter.team}",
                f"project:{adapter.project}",
                f"environment:{adapter.environment}"
            ]
        )
```

## Validation and Troubleshooting

### Comprehensive Validation

```python
from genops.providers.posthog_validation import (
    validate_setup, 
    print_validation_result,
    validate_posthog_connection
)

# Full validation with detailed diagnostics
result = validate_setup(verbose=True)
print_validation_result(result, show_successes=True)

# Test PostHog connectivity
connection_issues = validate_posthog_connection(
    api_key=os.getenv('POSTHOG_API_KEY'),
    host="https://app.posthog.com"
)

for issue in connection_issues:
    if issue.level == ValidationLevel.ERROR:
        print(f"Connection error: {issue.issue}")
        print(f"Fix: {issue.recommendation}")
```

### Common Issues and Solutions

#### Issue: Budget Exceeded Errors

```python
# Problem: Analytics operations blocked by budget limits
# Solution: Adjust budget or change governance policy

adapter = GenOpsPostHogAdapter(
    daily_budget_limit=500.0,  # Increase budget
    governance_policy="advisory",  # Or switch to advisory mode
    enable_cost_alerts=True  # Keep monitoring active
)
```

#### Issue: High Volume Cost Spikes

```python
# Problem: Unexpected cost increases during high-traffic events
# Solution: Implement intelligent event sampling

def smart_event_sampling(event_name, properties, traffic_level):
    """Implement cost-aware event sampling."""
    
    # Critical events: always track
    if event_name in ['conversion', 'signup', 'purchase']:
        return True
    
    # High traffic: sample based on importance
    if traffic_level == 'high':
        # Sample rates by event importance
        sample_rates = {
            'page_view': 0.1,      # 10% sampling
            'click': 0.2,          # 20% sampling  
            'feature_use': 0.8,    # 80% sampling
            'error': 1.0           # Always track errors
        }
        
        sample_rate = sample_rates.get(event_name, 0.5)
        return random.random() < sample_rate
    
    return True  # Normal traffic: track everything

# Use sampling in high-volume scenarios
if smart_event_sampling(event_name, properties, current_traffic_level):
    adapter.capture_event_with_governance(
        event_name=event_name,
        properties=properties,
        distinct_id=user_id
    )
```

#### Issue: Feature Flag Cost Optimization

```python
# Problem: High feature flag evaluation costs
# Solution: Implement local caching and batch evaluation

from functools import lru_cache
import time

class CachedFeatureFlagEvaluator:
    def __init__(self, adapter, cache_ttl=300):  # 5-minute cache
        self.adapter = adapter
        self.cache_ttl = cache_ttl
        self._cache = {}
    
    def evaluate_with_cache(self, flag_key, distinct_id, properties=None):
        cache_key = f"{flag_key}:{distinct_id}:{hash(str(properties))}"
        current_time = time.time()
        
        # Check cache
        if cache_key in self._cache:
            cached_result, timestamp = self._cache[cache_key]
            if current_time - timestamp < self.cache_ttl:
                return cached_result['value'], {'cost': 0.0, 'cached': True}
        
        # Evaluate flag with cost tracking
        flag_value, metadata = self.adapter.evaluate_feature_flag_with_governance(
            flag_key=flag_key,
            distinct_id=distinct_id,
            properties=properties
        )
        
        # Cache result
        self._cache[cache_key] = ({'value': flag_value}, current_time)
        
        return flag_value, metadata

# Usage
cached_evaluator = CachedFeatureFlagEvaluator(adapter)
flag_value, metadata = cached_evaluator.evaluate_with_cache(
    "expensive_feature_flag",
    "user_123"
)
```

### Performance Optimization

```python
# Batch event processing for better performance
class BatchEventProcessor:
    def __init__(self, adapter, batch_size=100, flush_interval=60):
        self.adapter = adapter
        self.batch_size = batch_size
        self.flush_interval = flush_interval
        self.event_buffer = []
        self.last_flush = time.time()
        
    def add_event(self, event_name, properties, distinct_id):
        """Add event to batch buffer."""
        self.event_buffer.append({
            'event_name': event_name,
            'properties': properties,
            'distinct_id': distinct_id,
            'timestamp': time.time()
        })
        
        # Flush if batch is full or interval exceeded
        if (len(self.event_buffer) >= self.batch_size or 
            time.time() - self.last_flush > self.flush_interval):
            self.flush_events()
    
    def flush_events(self):
        """Flush buffered events with cost optimization."""
        if not self.event_buffer:
            return
            
        with self.adapter.track_analytics_session("batch_processing") as session:
            total_cost = 0
            
            for event_data in self.event_buffer:
                result = self.adapter.capture_event_with_governance(
                    session_id=session.session_id,
                    **event_data
                )
                total_cost += result['cost']
            
            print(f"Flushed {len(self.event_buffer)} events, cost: ${total_cost:.4f}")
            
        self.event_buffer.clear()
        self.last_flush = time.time()

# Usage
batch_processor = BatchEventProcessor(adapter)

# Add events to batch
batch_processor.add_event("user_action", {"action": "click"}, "user_123")
batch_processor.add_event("page_view", {"page": "/dashboard"}, "user_123")
```

## API Reference

### GenOpsPostHogAdapter

```python
class GenOpsPostHogAdapter:
    """PostHog adapter with GenOps governance."""
    
    def __init__(
        self,
        posthog_api_key: Optional[str] = None,
        posthog_host: str = "https://app.posthog.com",
        team: str = "default",
        project: str = "default",
        environment: str = "production",
        customer_id: Optional[str] = None,
        cost_center: Optional[str] = None,
        daily_budget_limit: float = 1000.0,
        monthly_budget_limit: Optional[float] = None,
        enable_governance: bool = True,
        enable_cost_alerts: bool = True,
        governance_policy: str = "advisory",  # advisory, enforced, strict
        tags: Optional[Dict[str, str]] = None
    )
    
    def track_analytics_session(
        self,
        session_name: str,
        customer_id: Optional[str] = None,
        cost_center: Optional[str] = None,
        environment: Optional[str] = None,
        **governance_attributes
    ) -> PostHogAnalyticsSession
    
    def capture_event_with_governance(
        self,
        event_name: str,
        properties: Optional[Dict[str, Any]] = None,
        distinct_id: Optional[str] = None,
        is_identified: bool = False,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]
    
    def evaluate_feature_flag_with_governance(
        self,
        flag_key: str,
        distinct_id: str,
        properties: Optional[Dict[str, Any]] = None,
        session_id: Optional[str] = None
    ) -> Tuple[Any, Dict[str, Any]]
    
    def get_cost_summary(self) -> Dict[str, Any]
    
    def get_volume_discount_analysis(
        self, 
        projected_monthly_events: int
    ) -> Dict[str, Any]
```

### Auto-Instrumentation Functions

```python
def auto_instrument(
    posthog_api_key: Optional[str] = None,
    team: str = "auto-instrumented",
    project: str = "default",
    **adapter_kwargs
) -> GenOpsPostHogAdapter

def instrument_posthog(
    posthog_api_key: Optional[str] = None,
    team: str = "default", 
    project: str = "default",
    **kwargs
) -> GenOpsPostHogAdapter

def get_current_adapter() -> Optional[GenOpsPostHogAdapter]
```

### Cost Calculator

```python
from genops.providers.posthog import PostHogCostCalculator

calculator = PostHogCostCalculator()

# Calculate event costs
event_cost = calculator.calculate_event_cost(
    event_count=10000,
    is_identified=True
)

# Calculate feature flag costs
flag_cost = calculator.calculate_feature_flag_cost(
    request_count=50000
)

# Calculate session recording costs  
recording_cost = calculator.calculate_session_recording_cost(
    recording_count=2000
)

# Comprehensive session cost
session_cost = calculator.calculate_session_cost(
    event_count=10000,
    identified_events=3000,
    feature_flag_requests=25000,
    session_recordings=1000
)
```

### Validation Utilities

```python
from genops.providers.posthog_validation import (
    validate_setup,
    print_validation_result,
    validate_environment_config,
    validate_posthog_connection,
    ValidationResult
)

# Comprehensive validation
result: ValidationResult = validate_setup()
print_validation_result(result)

# Individual validation components
env_issues = validate_environment_config()
connection_issues = validate_posthog_connection()
```

---

## Advanced Integration Patterns

### Web Framework Integration

```python
# Django middleware
class PostHogGovernanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.adapter = GenOpsPostHogAdapter(
            team="web-team",
            project="django-app"
        )
    
    def __call__(self, request):
        with self.adapter.track_analytics_session("web_request") as session:
            request.analytics_session = session
            response = self.get_response(request)
            return response

# Flask integration
from flask import Flask, request, g
app = Flask(__name__)

@app.before_request
def before_request():
    g.adapter = GenOpsPostHogAdapter(team="api-team", project="flask-api")
    g.session = g.adapter.track_analytics_session("api_request").__enter__()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'session'):
        g.session.__exit__(None, None, None)
```

### Cloud Function Integration

```python
# AWS Lambda
import json
from genops.providers.posthog import GenOpsPostHogAdapter

def lambda_handler(event, context):
    adapter = GenOpsPostHogAdapter(
        team="serverless-team",
        project="lambda-analytics",
        environment="production"
    )
    
    with adapter.track_analytics_session("lambda_execution") as session:
        # Process analytics events
        for record in event.get('Records', []):
            adapter.capture_event_with_governance(
                event_name="lambda_processed",
                properties={"record_type": record.get('eventName')},
                distinct_id=f"lambda_{context.aws_request_id}"
            )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Analytics processed'})
        }
```

### Kubernetes Deployment

```yaml
# k8s-posthog-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: posthog-config
data:
  POSTHOG_API_KEY: "phc_your_project_api_key"
  GENOPS_TEAM: "k8s-analytics"
  GENOPS_PROJECT: "microservices"
  GENOPS_DAILY_BUDGET_LIMIT: "200.0"
  GENOPS_GOVERNANCE_POLICY: "enforced"

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: analytics-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: analytics-service
  template:
    metadata:
      labels:
        app: analytics-service
    spec:
      containers:
      - name: analytics-service
        image: your-analytics-service:latest
        envFrom:
        - configMapRef:
            name: posthog-config
```

---

**🎯 Ready for production?** Check out our [production deployment patterns](../../examples/posthog/production_patterns.py) and [enterprise governance templates](../enterprise-governance-templates.md)!

**Questions?** Join our [community discussions](https://github.com/KoshiHQ/GenOps-AI/discussions) or [open an issue](https://github.com/KoshiHQ/GenOps-AI/issues).