# Weights & Biases Integration with GenOps Governance

**Complete integration guide for ML experiment tracking with enterprise governance**

This comprehensive guide covers the complete integration of Weights & Biases (W&B) with GenOps governance for ML experiment tracking, cost intelligence, and enterprise-grade compliance.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Installation & Setup](#installation--setup)
- [Integration Patterns](#integration-patterns)
- [Cost Intelligence](#cost-intelligence)
- [Governance Features](#governance-features)
- [Production Deployment](#production-deployment)
- [Advanced Features](#advanced-features)
- [API Reference](#api-reference)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

---

## Overview

### What is Weights & Biases?

**Weights & Biases (W&B)** is a comprehensive MLOps platform for experiment tracking, model versioning, and ML pipeline orchestration. It provides:

- **Experiment Tracking**: Log metrics, hyperparameters, and artifacts
- **Model Registry**: Version and manage trained models
- **Hyperparameter Tuning**: Automated parameter optimization 
- **Data & Model Lineage**: Track data and model dependencies
- **Collaboration**: Share experiments and insights across teams

### GenOps + W&B Integration Benefits

GenOps enhances W&B with enterprise governance intelligence:

| Feature | Standard W&B | W&B + GenOps |
|---------|--------------|---------------|
| **Experiment Tracking** | Metrics, configs, artifacts | + Cost attribution + Budget limits |
| **Team Collaboration** | Shared workspace | + Cost visibility + Governance boundaries |
| **Cost Management** | Manual tracking | + Automatic cost intelligence + Forecasting |
| **Compliance** | Basic metadata | + Policy enforcement + Audit trails |
| **Enterprise Ready** | Team features | + Multi-tenant governance + Budget controls |

### Perfect For

- **ML Research Teams** needing cost visibility and budget controls
- **Production ML Operations** requiring governance and compliance
- **Enterprise Organizations** with multi-team cost attribution needs
- **Regulated Industries** needing comprehensive audit trails
- **Cost-Conscious Teams** wanting ML experiment cost optimization

---

## Quick Start

**⏱️ Get value in 5 minutes**

### Prerequisites
```bash
# 1. Install GenOps with W&B support
pip install genops[wandb]

# 2. Set up environment variables
export WANDB_API_KEY="your-wandb-api-key"     # Get from https://wandb.ai/settings
export GENOPS_TEAM="your-team"               # Optional but recommended
export GENOPS_PROJECT="your-project"         # Optional but recommended
```

### Zero-Code Integration
```python
# Add ONE line to your existing W&B code
from genops.providers.wandb import auto_instrument
auto_instrument(
    team="ml-team",
    project="experiment-tracking",
    daily_budget_limit=25.0
)

# Your existing W&B code works unchanged!
import wandb

run = wandb.init(project="my-project", name="experiment-1")
wandb.log({"accuracy": 0.95, "loss": 0.05})
run.finish()

# ✅ Now includes automatic cost tracking and governance!
```

**🎯 What Just Happened:**
- ✅ **Cost Intelligence**: Every experiment includes estimated cost ($0.001-$0.05 typical)
- ✅ **Team Attribution**: Costs attributed to your team/project for billing
- ✅ **Budget Monitoring**: Automatic alerts when approaching daily limit
- ✅ **Governance Metadata**: Enhanced W&B runs with governance attributes
- ✅ **OpenTelemetry Export**: Data flows to your observability stack

---

## Installation & Setup

### System Requirements

- **Python**: 3.8+ (3.9+ recommended)
- **W&B Account**: Free tier or paid plan
- **Operating System**: Linux, macOS, Windows
- **Memory**: 512MB+ for basic usage
- **Storage**: 100MB+ for package and cache

### Installation Options

#### Option 1: Standard Installation
```bash
pip install genops[wandb]
```

#### Option 2: Development Installation
```bash
git clone https://github.com/KoshiHQ/GenOps-AI.git
cd GenOps-AI
pip install -e ".[wandb]"
```

#### Option 3: Docker Installation
```bash
docker run -e WANDB_API_KEY=$WANDB_API_KEY \
           -e GENOPS_TEAM=$GENOPS_TEAM \
           genops/wandb:latest
```

### Configuration

#### Environment Variables

**Required:**
```bash
export WANDB_API_KEY="your-wandb-api-key"
```

**Recommended:**
```bash
export GENOPS_TEAM="your-team"
export GENOPS_PROJECT="your-project"
export GENOPS_CUSTOMER_ID="your-customer"    # For multi-tenant scenarios
export GENOPS_ENVIRONMENT="development"       # development/staging/production
```

**Advanced:**
```bash
export GENOPS_DAILY_BUDGET_LIMIT="100.0"     # Default daily budget ($)
export GENOPS_MAX_EXPERIMENT_COST="50.0"     # Default max experiment cost ($)
export GENOPS_COST_CENTER="ml_research"      # Cost center for billing
export GENOPS_GOVERNANCE_POLICY="advisory"    # advisory/enforced
```

#### Configuration File (Optional)

Create `~/.genops/config.yaml`:
```yaml
wandb:
  api_key: "your-wandb-api-key"
  default_team: "ml-team"
  default_project: "experiments"
  
governance:
  daily_budget_limit: 100.0
  max_experiment_cost: 50.0
  policy_enforcement: "advisory"
  enable_cost_alerts: true
  
observability:
  export_to_otel: true
  export_interval_seconds: 30
  enable_detailed_metrics: true
```

### Setup Validation

Always validate your setup before starting:

```python
from genops.providers.wandb_validation import validate_setup, print_validation_result

result = validate_setup(
    include_connectivity_tests=True,
    include_governance_tests=True
)
print_validation_result(result, detailed=True)
```

**Expected Output:**
```
✅ GenOps W&B Setup Validation
Overall Status: PASSED
📊 Summary: ✅ Passed: 12, ⚠️ Warnings: 0, ❌ Failed: 0

✅ Environment Configuration
✅ W&B API Connectivity  
✅ GenOps Governance Setup
✅ Cost Tracking Capabilities
✅ OpenTelemetry Integration
```

---

## Integration Patterns

### Pattern 1: Auto-Instrumentation (Zero Code Changes)

**Best for:** Existing W&B applications, legacy code, quick adoption

```python
from genops.providers.wandb import auto_instrument

# Enable governance for ALL W&B usage in your application
auto_instrument(
    team="research-team",
    project="model-optimization", 
    daily_budget_limit=50.0,
    enable_cost_alerts=True
)

# All existing W&B code automatically includes governance
import wandb

# This run now includes cost tracking and governance
run = wandb.init(project="research", name="baseline-model")
wandb.log({"accuracy": 0.87, "loss": 0.23})
run.finish()
```

### Pattern 2: Manual Adapter (Full Control)

**Best for:** New applications, custom governance requirements, production use

```python
from genops.providers.wandb import instrument_wandb

# Create adapter with specific configuration
adapter = instrument_wandb(
    wandb_api_key="your-api-key",
    team="production-ml",
    project="customer-models",
    customer_id="client-abc123",
    environment="production",
    max_experiment_cost=200.0,
    governance_policy="enforced",  # Strict enforcement
    enable_cost_alerts=True
)

# Enhanced experiment with governance context
with adapter.track_experiment_lifecycle(
    "customer-model-training",
    experiment_type="supervised_learning",
    max_cost=150.0
) as experiment:
    
    run = wandb.init(project="production", name="customer-model-v2")
    
    # Your training code here
    for epoch in range(10):
        metrics = train_epoch()
        wandb.log(metrics)
        
        # Update experiment cost (optional - auto-calculated if not provided)
        experiment.estimated_cost += calculate_epoch_cost()
    
    run.finish()

# Get governance metrics
metrics = adapter.get_metrics()
print(f"Daily usage: ${metrics['daily_usage']:.2f}")
print(f"Budget remaining: ${metrics['budget_remaining']:.2f}")
```

### Pattern 3: Context Manager (Granular Control)

**Best for:** Complex workflows, multi-stage experiments, fine-grained cost tracking

```python
from genops.providers.wandb import instrument_wandb

adapter = instrument_wandb(
    team="advanced-research",
    project="multi-stage-training"
)

# Track complete experiment lifecycle with multiple stages
with adapter.track_experiment_lifecycle(
    "multi-stage-experiment",
    max_cost=100.0
) as experiment:
    
    # Stage 1: Data preparation
    with wandb.init(project="prep", name="data-preprocessing") as prep_run:
        prep_cost = prepare_data()
        experiment.estimated_cost += prep_cost
        wandb.log({"prep_cost": prep_cost})
    
    # Stage 2: Model training  
    with wandb.init(project="train", name="model-training") as train_run:
        model, train_cost = train_model()
        experiment.estimated_cost += train_cost
        wandb.log({"train_cost": train_cost, "accuracy": model.score})
    
    # Stage 3: Model evaluation
    with wandb.init(project="eval", name="model-evaluation") as eval_run:
        eval_metrics, eval_cost = evaluate_model(model)
        experiment.estimated_cost += eval_cost
        wandb.log({**eval_metrics, "eval_cost": eval_cost})

print(f"Total experiment cost: ${experiment.estimated_cost:.2f}")
```

### Pattern 4: Artifact Governance

**Best for:** Model management, compliance requirements, production deployments

```python
from genops.providers.wandb import instrument_wandb
import wandb

adapter = instrument_wandb(team="model-ops", project="production-models")

run = wandb.init(project="models", name="production-classifier")

# Create model artifact with governance
model_artifact = wandb.Artifact("customer-classifier-v2", type="model")
model_artifact.add_file("model.pkl")

# Log with governance metadata and cost tracking
adapter.log_governed_artifact(
    model_artifact,
    cost_estimate=5.0,  # Storage and processing cost
    governance_metadata={
        "model_approval_status": "approved",
        "compliance_review": "completed",
        "data_classification": "internal",
        "retention_policy": "3_years"
    }
)

run.finish()
```

---

## Cost Intelligence

### Automatic Cost Tracking

GenOps automatically tracks costs for all W&B operations:

```python
from genops.providers.wandb import instrument_wandb

adapter = instrument_wandb(team="cost-aware-team", project="optimization")

# Costs are automatically tracked for:
run = wandb.init(project="cost-tracking", name="experiment")

# 1. Logging operations
wandb.log({"accuracy": 0.95})  # ~$0.001

# 2. Artifact uploads  
artifact = wandb.Artifact("model", type="model")
artifact.add_file("model.pkl")  # Cost based on file size
run.log_artifact(artifact)

# 3. Compute time
# Cost calculated based on experiment duration and resource usage

run.finish()

# View accumulated costs
metrics = adapter.get_metrics()
print(f"Experiment cost: ${metrics['daily_usage']:.3f}")
```

### Cost Breakdown Analysis

```python
from genops.providers.wandb_cost_aggregator import WandbCostAggregator

aggregator = WandbCostAggregator(
    team="research-team",
    project="cost-analysis"
)

# Get detailed cost breakdown
cost_summary = aggregator.get_comprehensive_cost_summary(
    time_period_days=30,
    include_forecasting=True
)

print("📊 Cost Breakdown (30 days):")
print(f"  • Total: ${cost_summary.total_cost:.2f}")
print(f"  • Compute: ${cost_summary.compute_cost:.2f}")
print(f"  • Storage: ${cost_summary.storage_cost:.2f}")
print(f"  • Data Transfer: ${cost_summary.data_transfer_cost:.2f}")

# Cost by experiment type
for exp_type, cost in cost_summary.cost_by_experiment_type.items():
    print(f"  • {exp_type}: ${cost:.2f}")

# Forecasting
print(f"\n📈 Cost Forecast (next 30 days): ${cost_summary.forecasted_cost:.2f}")
```

### Budget Management

```python
from genops.providers.wandb import instrument_wandb

# Set up budget controls
adapter = instrument_wandb(
    team="budget-conscious-team",
    project="controlled-experiments",
    daily_budget_limit=100.0,        # $100 daily limit
    max_experiment_cost=25.0,        # $25 per experiment limit
    enable_cost_alerts=True,         # Email alerts
    governance_policy="enforced"     # Block over-budget experiments
)

# Budget is automatically enforced
try:
    with adapter.track_experiment_lifecycle(
        "expensive-experiment",
        max_cost=30.0  # Exceeds $25 limit
    ) as experiment:
        # This will raise an exception due to budget limits
        pass
        
except ValueError as e:
    print(f"Budget enforcement: {e}")
    # Experiment blocked - over budget

# Check budget status
metrics = adapter.get_metrics()
print(f"Budget remaining: ${metrics['budget_remaining']:.2f}")
print(f"Daily usage: ${metrics['daily_usage']:.2f} / ${metrics['daily_budget_limit']:.2f}")
```

### Cost Optimization Recommendations

```python
from genops.providers.wandb_cost_aggregator import generate_cost_optimization_recommendations

# Analyze historical experiments for optimization opportunities
recommendations = generate_cost_optimization_recommendations(
    team="research-team",
    lookback_days=30,
    target_savings_percentage=20.0
)

print("💡 Cost Optimization Recommendations:")
for rec in recommendations:
    print(f"  • {rec['category']}: {rec['recommendation']}")
    print(f"    Potential savings: ${rec['estimated_savings']:.2f} ({rec['confidence']:.1f}% confidence)")
```

---

## Governance Features

### Policy Enforcement

```python
from genops.providers.wandb import instrument_wandb, GovernancePolicy

# Configure governance policies
adapter = instrument_wandb(
    team="governed-team",
    project="compliant-experiments",
    governance_policy=GovernancePolicy.ENFORCED,
    daily_budget_limit=200.0,
    enable_governance=True
)

# Policies are automatically enforced:
# 1. Cost limits - experiments blocked if over budget
# 2. Data residency - data must stay in approved regions  
# 3. Retention policies - automatic cleanup of old experiments
# 4. Access controls - team-based permissions
# 5. Approval workflows - production deployments require approval

# Check policy compliance
compliance_status = adapter.get_compliance_status()
print(f"Policy compliance: {compliance_status['overall_score']:.1f}%")

for violation in compliance_status['violations']:
    print(f"⚠️ Violation: {violation['policy']} - {violation['description']}")
```

### Audit Trail Generation

```python
from genops.providers.wandb import instrument_wandb

adapter = instrument_wandb(
    team="audited-team", 
    project="regulated-ml",
    enable_governance=True
)

# All operations automatically generate audit entries
run = wandb.init(project="audit-demo", name="tracked-experiment")

# This generates audit trail:
# - Who: user identity and team
# - What: experiment started, metrics logged, artifacts created
# - When: precise timestamps
# - Where: IP address, region, environment
# - Why: business context and approval chain

wandb.log({"accuracy": 0.91})
run.finish()

# Export audit trail
audit_trail = adapter.export_audit_trail(
    start_date="2024-01-01",
    end_date="2024-12-31",
    format="json"  # or "csv", "parquet"
)

print(f"Audit events exported: {len(audit_trail['events'])}")
```

### Team and Customer Attribution

```python
from genops.providers.wandb import instrument_wandb

# Multi-tenant configuration
adapter = instrument_wandb(
    team="platform-team",
    project="customer-experiments", 
    customer_id="customer-abc123",      # Customer attribution
    environment="production",
    cost_center="customer_success",     # Financial attribution
    enable_governance=True
)

# Experiments are automatically attributed to:
# - Team: for internal cost allocation
# - Customer: for billing and usage reporting  
# - Cost Center: for financial reporting
# - Environment: for stage-specific tracking

run = wandb.init(project="customer-models", name="customer-abc-model-v2")
wandb.log({"customer_satisfaction": 0.94})
run.finish()

# Generate customer usage report
usage_report = adapter.generate_customer_usage_report(
    customer_id="customer-abc123",
    billing_period="2024-01"
)

print(f"Customer usage: {usage_report['total_experiments']} experiments")
print(f"Customer cost: ${usage_report['total_cost']:.2f}")
```

### Data Lineage and Compliance

```python
from genops.providers.wandb import instrument_wandb
from genops.providers.wandb_governance import create_data_lineage

adapter = instrument_wandb(
    team="compliance-team",
    project="regulated-models",
    enable_governance=True
)

# Track data lineage for compliance
lineage = create_data_lineage(
    data_sources=["customer_data.csv", "public_dataset.json"],
    transformations=["cleaning", "feature_engineering", "normalization"],
    validation_results={"quality_score": 0.95, "bias_check": "passed"},
    compliance_approvals=["data_governance", "legal_review"]
)

run = wandb.init(project="compliance", name="gdpr-compliant-model")

# Log model with full lineage
model_artifact = wandb.Artifact("compliant-model", type="model")
model_artifact.add_file("model.pkl")

adapter.log_governed_artifact(
    model_artifact,
    governance_metadata={
        "data_lineage": lineage,
        "gdpr_compliant": True,
        "retention_period_days": 365,
        "data_classification": "personal_data"
    }
)

run.finish()
```

---

## Production Deployment

### Production Configuration

```python
from genops.providers.wandb import instrument_wandb
from genops.providers.wandb_production import ProductionConfiguration

# Production-grade configuration
prod_config = ProductionConfiguration(
    environment="production",
    security_level="enterprise",
    max_concurrent_experiments=100,
    max_daily_cost=10000.0,
    enable_encryption_at_rest=True,
    enable_encryption_in_transit=True,
    require_mfa=True,
    audit_log_retention_years=7,
    backup_frequency_hours=6,
    disaster_recovery_rpo_hours=2
)

adapter = instrument_wandb(
    team="production-ml",
    project="customer-facing-models",
    production_config=prod_config,
    governance_policy="enforced"
)
```

### CI/CD Integration

```yaml
# .github/workflows/ml-pipeline.yml
name: ML Model Training Pipeline

on: [push, pull_request]

jobs:
  train-model:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          
      - name: Install dependencies
        run: |
          pip install genops[wandb]
          
      - name: Validate GenOps setup
        env:
          WANDB_API_KEY: ${{ secrets.WANDB_API_KEY }}
          GENOPS_TEAM: ${{ vars.GENOPS_TEAM }}
        run: |
          python -c "
          from genops.providers.wandb_validation import validate_setup, print_validation_result
          result = validate_setup(include_governance_tests=True)
          print_validation_result(result)
          assert result['overall_status'] == 'PASSED'
          "
          
      - name: Train model with governance
        env:
          WANDB_API_KEY: ${{ secrets.WANDB_API_KEY }}
          GENOPS_TEAM: ${{ vars.GENOPS_TEAM }}
          GENOPS_PROJECT: "cicd-pipeline"
        run: |
          python train_model.py --governance-enabled --max-cost=100.0
          
      - name: Generate governance report
        run: |
          python -c "
          from genops.providers.wandb import get_current_adapter
          adapter = get_current_adapter()
          if adapter:
              report = adapter.generate_compliance_report()
              print(f'Governance compliance: {report[\"compliance_score\"]}%')
          "
```

### Kubernetes Deployment

```yaml
# k8s/ml-training-job.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: ml-training-with-governance
spec:
  template:
    spec:
      containers:
      - name: ml-trainer
        image: your-registry/ml-trainer:latest
        env:
        - name: WANDB_API_KEY
          valueFrom:
            secretKeyRef:
              name: wandb-secret
              key: api-key
        - name: GENOPS_TEAM
          value: "production-ml"
        - name: GENOPS_PROJECT  
          value: "k8s-training"
        - name: GENOPS_ENVIRONMENT
          value: "production"
        - name: GENOPS_DAILY_BUDGET_LIMIT
          value: "500.0"
        resources:
          limits:
            memory: "8Gi"
            cpu: "4"
            nvidia.com/gpu: "1"
          requests:
            memory: "4Gi" 
            cpu: "2"
        command:
        - python
        - train_with_governance.py
      restartPolicy: Never
```

### Production Monitoring

```python
from genops.providers.wandb import instrument_wandb
from genops.monitoring import ProductionMonitor

# Set up production monitoring
adapter = instrument_wandb(
    team="production-ops",
    project="production-monitoring",
    enable_detailed_monitoring=True
)

monitor = ProductionMonitor(adapter)

# Monitor key metrics
monitor.add_metric_alert(
    metric="daily_cost",
    threshold=1000.0,
    alert_channel="slack://ml-ops-alerts"
)

monitor.add_metric_alert(
    metric="experiment_failure_rate", 
    threshold=5.0,  # 5% failure rate
    alert_channel="email://oncall@company.com"
)

# Generate daily reports
@monitor.schedule(interval="daily")
def generate_daily_report():
    report = adapter.generate_production_report()
    monitor.send_report(report, channels=["slack://daily-reports"])
```

---

## Advanced Features

### Multi-Region Deployment

```python
from genops.providers.wandb import instrument_wandb

# Configure multi-region deployment
adapters = {
    "us-east-1": instrument_wandb(
        team="global-ml",
        project="us-experiments",
        region="us-east-1",
        data_residency_policy="us_only"
    ),
    "eu-west-1": instrument_wandb(
        team="global-ml", 
        project="eu-experiments",
        region="eu-west-1",
        data_residency_policy="eu_gdpr_compliant"
    )
}

# Route experiments based on data location
def route_experiment(data_location: str):
    if data_location.startswith("eu"):
        return adapters["eu-west-1"]
    else:
        return adapters["us-east-1"]

# Experiment with proper data residency
adapter = route_experiment("eu-customer-data")
run = wandb.init(project="gdpr-experiment", name="eu-customer-model")
# Automatically routed to EU region for GDPR compliance
```

### Custom Cost Models

```python
from genops.providers.wandb_pricing import CustomPricingModel

# Define custom pricing for your infrastructure
custom_pricing = CustomPricingModel(
    compute_rates={
        "gpu_v100": 3.06,      # $/hour
        "gpu_a100": 4.56,      # $/hour  
        "cpu_standard": 0.045   # $/hour
    },
    storage_rates={
        "ssd": 0.10,           # $/GB/month
        "archive": 0.004       # $/GB/month
    },
    data_transfer_rates={
        "internal": 0.0,       # Free
        "external": 0.09       # $/GB
    }
)

adapter = instrument_wandb(
    team="custom-pricing-team",
    project="accurate-costing",
    pricing_model=custom_pricing
)

# Costs calculated using your custom rates
with adapter.track_experiment_lifecycle("custom-cost-experiment") as experiment:
    # Specify actual resource usage
    experiment.add_compute_cost("gpu_a100", hours=2.5)
    experiment.add_storage_cost("ssd", gb=50, duration_days=30)
    experiment.add_data_transfer_cost("external", gb=10)

print(f"Accurate cost: ${experiment.total_cost:.2f}")
```

### Advanced Analytics Integration

```python
from genops.providers.wandb import instrument_wandb
from genops.analytics import MLAnalytics

adapter = instrument_wandb(team="analytics-team", project="ml-insights")

# Set up advanced analytics
analytics = MLAnalytics(adapter)

# Performance vs Cost Analysis
analysis = analytics.analyze_performance_vs_cost(
    time_period_days=90,
    group_by=["model_type", "team", "experiment_type"]
)

print("📊 Performance vs Cost Analysis:")
for group, metrics in analysis.items():
    print(f"  {group}:")
    print(f"    Avg Accuracy: {metrics['avg_accuracy']:.3f}")
    print(f"    Avg Cost: ${metrics['avg_cost']:.2f}")
    print(f"    Cost Efficiency: {metrics['accuracy_per_dollar']:.1f}")

# Anomaly Detection
anomalies = analytics.detect_cost_anomalies(
    sensitivity=0.95,
    lookback_days=30
)

print(f"\n🚨 Cost Anomalies Detected: {len(anomalies)}")
for anomaly in anomalies[:3]:  # Top 3
    print(f"  • {anomaly['experiment']}: ${anomaly['cost']:.2f} "
          f"(expected: ${anomaly['expected_cost']:.2f})")
```

### Workflow Integration

```python
# Apache Airflow Integration
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from genops.providers.wandb import instrument_wandb

def train_with_governance(**context):
    adapter = instrument_wandb(
        team="airflow-ml",
        project="scheduled-training",
        workflow_context=context  # Airflow context
    )
    
    with adapter.track_experiment_lifecycle(
        f"scheduled-training-{context['ds']}"
    ) as experiment:
        # Your training code here
        result = train_model()
        return result

dag = DAG('ml_training_with_governance', schedule_interval='@daily')

train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_with_governance,
    dag=dag
)
```

```python
# Kubeflow Integration  
from kfp import dsl
from genops.providers.wandb import instrument_wandb

@dsl.component
def train_component(
    team: str,
    project: str,
    max_cost: float
) -> str:
    adapter = instrument_wandb(
        team=team,
        project=project,
        max_experiment_cost=max_cost
    )
    
    with adapter.track_experiment_lifecycle("kubeflow-experiment") as experiment:
        # Training logic
        model_path = train_model()
        return model_path

@dsl.pipeline(name='ML Training with Governance')
def ml_pipeline():
    train_op = train_component(
        team="kubeflow-ml",
        project="pipeline-experiments", 
        max_cost=100.0
    )
```

---

## API Reference

### Core Classes

#### `GenOpsWandbAdapter`

Main adapter class for W&B integration with governance.

```python
class GenOpsWandbAdapter:
    def __init__(
        self,
        wandb_api_key: Optional[str] = None,
        team: Optional[str] = None,
        project: Optional[str] = None,
        customer_id: Optional[str] = None,
        environment: str = "development",
        daily_budget_limit: float = 100.0,
        max_experiment_cost: float = 50.0,
        governance_policy: Union[GovernancePolicy, str] = GovernancePolicy.ADVISORY,
        enable_cost_alerts: bool = True,
        enable_governance: bool = True,
        cost_center: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None
    )
```

**Methods:**

- `track_experiment_lifecycle(experiment_name, experiment_type, max_cost, **kwargs)` → Context manager for experiment tracking
- `log_governed_artifact(artifact, cost_estimate, governance_metadata)` → Log artifact with governance
- `get_metrics()` → Get current governance metrics and status
- `get_experiment_cost_summary(experiment_id)` → Get detailed cost breakdown
- `generate_compliance_report()` → Generate governance compliance report

#### `WandbCostAggregator`

Advanced cost tracking and analysis.

```python
class WandbCostAggregator:
    def __init__(
        self,
        team: str,
        project: Optional[str] = None,
        customer_id: Optional[str] = None
    )
```

**Methods:**

- `get_comprehensive_cost_summary(time_period_days, include_forecasting)` → Detailed cost analysis
- `calculate_team_attribution()` → Multi-team cost breakdown
- `generate_cost_optimization_recommendations()` → AI-powered cost optimization suggestions
- `forecast_monthly_costs(confidence_interval)` → Predictive cost modeling

### Utility Functions

#### Auto-Instrumentation

```python
def auto_instrument(
    wandb_api_key: Optional[str] = None,
    team: Optional[str] = None,
    project: Optional[str] = None,
    **kwargs
) -> GenOpsWandbAdapter
```

Enable zero-code auto-instrumentation for existing W&B applications.

#### Manual Instrumentation

```python
def instrument_wandb(
    wandb_api_key: Optional[str] = None,
    team: Optional[str] = None,
    project: Optional[str] = None,
    **kwargs
) -> GenOpsWandbAdapter
```

Create configured adapter for manual integration.

#### Validation

```python
def validate_setup(
    include_connectivity_tests: bool = True,
    include_governance_tests: bool = False,
    include_performance_tests: bool = False
) -> ValidationResult

def print_validation_result(
    result: ValidationResult,
    detailed: bool = False
) -> None
```

Comprehensive setup validation with detailed reporting.

### Configuration Classes

#### `GovernancePolicy`

```python
class GovernancePolicy(Enum):
    AUDIT_ONLY = "audit_only"     # Log violations only
    ADVISORY = "advisory"         # Log and warn
    ENFORCED = "enforced"         # Block violations
```

#### `ExperimentCostSummary`

```python
@dataclass
class ExperimentCostSummary:
    total_cost: float
    compute_cost: float
    storage_cost: float
    data_transfer_cost: float
    cost_by_run: Dict[str, float]
    experiment_duration: float
    resource_efficiency: float
```

---

## Troubleshooting

### Common Issues

#### ❌ "WANDB_API_KEY not found"
```bash
# Check if API key is set
echo $WANDB_API_KEY

# Set API key
export WANDB_API_KEY="your-wandb-api-key"

# Or in Python
import os
os.environ["WANDB_API_KEY"] = "your-wandb-api-key"

# Get API key from: https://wandb.ai/settings
```

#### ❌ "wandb module not found"
```bash
# Install W&B and GenOps
pip install genops[wandb]

# Verify installation
python -c "import wandb, genops; print('✅ Installation successful')"
```

#### ❌ "Authentication failed"
```python
# Test W&B authentication
import wandb
wandb.login()  # Opens browser for authentication

# Or set API key directly
wandb.login(key="your-wandb-api-key")
```

#### ❌ "GenOps validation failed"
```python
# Run detailed validation
from genops.providers.wandb_validation import validate_setup, print_validation_result

result = validate_setup(
    include_connectivity_tests=True,
    include_governance_tests=True
)
print_validation_result(result, detailed=True)

# Fix issues based on validation output
```

#### ❌ "Cost tracking not working"
```python
# Verify auto-instrumentation is enabled
from genops.providers.wandb import get_current_adapter

adapter = get_current_adapter()
if adapter is None:
    print("❌ Auto-instrumentation not enabled")
    # Enable it:
    from genops.providers.wandb import auto_instrument
    auto_instrument(team="your-team", project="your-project")
else:
    print("✅ Auto-instrumentation active")
    metrics = adapter.get_metrics()
    print(f"Daily usage: ${metrics['daily_usage']:.3f}")
```

#### ❌ "Permission denied errors"
```bash
# Check W&B permissions
wandb whoami

# Check file permissions
ls -la ~/.netrc
ls -la ~/.config/wandb/

# Fix permissions
chmod 600 ~/.netrc
```

### Performance Issues

#### Slow experiment initialization
```python
# Enable caching
from genops.providers.wandb import instrument_wandb

adapter = instrument_wandb(
    team="your-team",
    project="your-project",
    enable_caching=True,
    cache_ttl_minutes=30
)
```

#### High memory usage
```python
# Configure sampling for high-volume scenarios
adapter = instrument_wandb(
    team="your-team",
    project="your-project",
    sampling_rate=0.1,  # Sample 10% of operations
    enable_compression=True
)
```

#### Network timeouts
```python
# Configure timeouts and retries
adapter = instrument_wandb(
    team="your-team",
    project="your-project",
    connection_timeout_seconds=30,
    retry_attempts=3,
    retry_backoff_factor=2.0
)
```

### Debug Mode

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Enable detailed logging
from genops.providers.wandb import instrument_wandb

adapter = instrument_wandb(
    team="debug-team",
    project="debug-session",
    debug_mode=True,
    verbose_logging=True
)

# Check internal state
print(f"Active runs: {len(adapter.active_runs)}")
print(f"Daily usage: ${adapter.daily_usage:.3f}")
```

---

## Best Practices

### Development Best Practices

#### 1. Environment-Specific Configuration

```python
# Use different configurations for each environment
import os

environment = os.getenv("GENOPS_ENVIRONMENT", "development")

config = {
    "development": {
        "daily_budget_limit": 10.0,
        "governance_policy": "advisory",
        "enable_detailed_monitoring": False
    },
    "staging": {
        "daily_budget_limit": 50.0,
        "governance_policy": "advisory", 
        "enable_detailed_monitoring": True
    },
    "production": {
        "daily_budget_limit": 1000.0,
        "governance_policy": "enforced",
        "enable_detailed_monitoring": True,
        "require_approval": True
    }
}

adapter = instrument_wandb(
    team="ml-team",
    project="adaptive-config",
    environment=environment,
    **config[environment]
)
```

#### 2. Cost-Conscious Development

```python
# Always set reasonable budget limits
adapter = instrument_wandb(
    team="cost-conscious-team",
    project="budget-aware-ml",
    daily_budget_limit=25.0,        # Conservative daily limit
    max_experiment_cost=10.0,       # Reasonable experiment limit
    enable_cost_alerts=True,        # Get notified early
    governance_policy="advisory"    # Warn but don't block in dev
)

# Use cost tracking for optimization
with adapter.track_experiment_lifecycle(
    "cost-optimized-experiment",
    max_cost=5.0  # Tight budget for experimentation
) as experiment:
    
    # Monitor cost during experiment
    checkpoint_cost = experiment.estimated_cost
    if checkpoint_cost > 2.5:  # 50% of budget
        print(f"⚠️ Checkpoint: ${checkpoint_cost:.2f} spent")
    
    # Your training code here
    train_model()
```

#### 3. Team Collaboration Patterns

```python
# Clear team and project attribution
adapter = instrument_wandb(
    team="data-science-team",        # Clear team ownership
    project="customer-churn-model",   # Descriptive project name
    customer_id="internal-research",  # Customer attribution
    cost_center="r_and_d",           # Budget attribution
    tags={
        "experiment_type": "research",
        "priority": "high",
        "reviewer": "senior_ds_lead"
    }
)

# Use descriptive experiment names
run = wandb.init(
    project="churn-prediction",
    name=f"gradient_boost_v2_{datetime.now().strftime('%Y%m%d')}",
    tags=["gradient_boosting", "feature_v2", "hyperopt"]
)
```

### Production Best Practices

#### 1. Robust Error Handling

```python
import logging
from genops.providers.wandb import instrument_wandb

logger = logging.getLogger(__name__)

def train_with_error_handling():
    adapter = None
    try:
        adapter = instrument_wandb(
            team="production-ml",
            project="robust-training",
            governance_policy="enforced",
            enable_cost_alerts=True
        )
        
        with adapter.track_experiment_lifecycle(
            "production-training",
            max_cost=100.0
        ) as experiment:
            
            run = wandb.init(
                project="production",
                name="model-training-v2"
            )
            
            try:
                # Training code with checkpoints
                for epoch in range(100):
                    try:
                        metrics = train_epoch()
                        wandb.log(metrics)
                        
                        # Validate governance constraints
                        if experiment.estimated_cost > 80.0:
                            logger.warning("Approaching cost limit")
                            
                    except Exception as epoch_error:
                        logger.error(f"Epoch {epoch} failed: {epoch_error}")
                        # Decide whether to continue or abort
                        if epoch < 10:  # Early failure - abort
                            raise
                        else:  # Late failure - try to save progress
                            save_checkpoint(epoch)
                            break
                            
            finally:
                run.finish()
                
    except Exception as e:
        logger.error(f"Experiment failed: {e}")
        
        # Generate failure report
        if adapter:
            failure_report = adapter.generate_failure_report()
            logger.info(f"Failure report: {failure_report}")
            
        raise
    
    finally:
        # Cleanup resources
        if adapter:
            adapter.cleanup()
```

#### 2. Monitoring and Alerting

```python
from genops.providers.wandb import instrument_wandb
from genops.monitoring import AlertManager

# Set up comprehensive monitoring
adapter = instrument_wandb(
    team="production-ops",
    project="monitored-ml",
    enable_detailed_monitoring=True
)

alert_manager = AlertManager(adapter)

# Cost-based alerts
alert_manager.add_cost_alert(
    threshold_percentage=80,
    notification_channels=["email://ml-ops@company.com", "slack://alerts"]
)

# Performance-based alerts  
alert_manager.add_performance_alert(
    metric="experiment_failure_rate",
    threshold=5.0,  # 5% failure rate
    time_window_minutes=60
)

# Governance alerts
alert_manager.add_governance_alert(
    violation_types=["budget_exceeded", "policy_violation"],
    severity="HIGH",
    escalation_chain=["team_lead", "ml_director"]
)

# Custom health checks
@alert_manager.health_check(interval_minutes=15)
def check_system_health():
    metrics = adapter.get_metrics()
    
    # Check various health indicators
    health_score = 100
    
    if metrics['error_rate_percentage'] > 2.0:
        health_score -= 20
        
    if metrics['daily_usage'] > metrics['daily_budget_limit'] * 0.9:
        health_score -= 15
        
    if len(adapter.active_runs) > 50:  # High load
        health_score -= 10
        
    return {
        "health_score": health_score,
        "status": "healthy" if health_score >= 80 else "degraded" if health_score >= 60 else "unhealthy"
    }
```

#### 3. Security and Compliance

```python
from genops.providers.wandb import instrument_wandb
from genops.security import SecurityManager

# Production security configuration
adapter = instrument_wandb(
    team="secure-ml",
    project="compliant-training",
    environment="production",
    security_level="enterprise",
    enable_encryption_at_rest=True,
    enable_encryption_in_transit=True,
    require_mfa=True,
    audit_log_retention_years=7
)

security_manager = SecurityManager(adapter)

# Data classification and handling
@security_manager.classify_data("PII")
def handle_sensitive_data(data):
    # Automatic encryption and access logging
    return process_data(data)

# Compliance validation
@security_manager.compliance_checkpoint("SOX")  
def financial_model_training():
    # Automatic compliance validation
    with adapter.track_experiment_lifecycle(
        "sox-compliant-model",
        compliance_requirements=["sox", "internal_audit"]
    ) as experiment:
        
        # Training with compliance tracking
        result = train_financial_model()
        return result

# Regular compliance reporting
@security_manager.schedule_compliance_report(frequency="monthly")
def generate_compliance_report():
    report = adapter.generate_comprehensive_compliance_report()
    security_manager.submit_compliance_report(report)
```

### Performance Optimization

#### 1. Efficient Resource Usage

```python
# Configure for high-throughput scenarios
adapter = instrument_wandb(
    team="high-performance-ml",
    project="batch-processing",
    
    # Performance optimizations
    batch_size=1000,              # Batch telemetry operations
    async_export=True,            # Non-blocking telemetry export
    sampling_rate=0.1,            # Sample 10% for very high volume
    enable_compression=True,      # Compress telemetry data
    
    # Resource limits
    max_concurrent_experiments=10,
    memory_limit_mb=2048,
    
    # Caching
    enable_caching=True,
    cache_ttl_minutes=60
)

# Efficient batch processing
experiment_batch = []
for experiment_config in large_experiment_list:
    
    # Batch experiments for efficiency
    if len(experiment_batch) < 10:
        experiment_batch.append(experiment_config)
        continue
    
    # Process batch
    results = adapter.process_experiment_batch(experiment_batch)
    experiment_batch.clear()
    
    # Yield control periodically  
    if len(results) % 100 == 0:
        time.sleep(0.1)  # Prevent resource exhaustion
```

#### 2. Scaling Patterns

```python
from concurrent.futures import ThreadPoolExecutor
from genops.providers.wandb import instrument_wandb

# Concurrent experiment processing
def run_experiment_concurrently(experiment_configs, max_workers=5):
    
    adapters = [
        instrument_wandb(
            team=f"worker-team-{i}",
            project="concurrent-experiments",
            max_experiment_cost=20.0
        )
        for i in range(max_workers)
    ]
    
    def run_single_experiment(config_and_adapter):
        config, adapter = config_and_adapter
        
        with adapter.track_experiment_lifecycle(
            config['name'],
            max_cost=config['budget']
        ) as experiment:
            
            # Run experiment
            result = train_model(config)
            return result
    
    # Distribute experiments across workers
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        experiment_pairs = list(zip(experiment_configs, adapters * len(experiment_configs)))
        results = list(executor.map(run_single_experiment, experiment_pairs))
    
    return results

# Auto-scaling based on load
class AutoScalingMLRunner:
    def __init__(self):
        self.base_adapter = instrument_wandb(
            team="autoscale-team",
            project="dynamic-scaling"
        )
        self.worker_adapters = []
        
    def scale_up(self, target_capacity):
        while len(self.worker_adapters) < target_capacity:
            worker = instrument_wandb(
                team=f"worker-{len(self.worker_adapters)}",
                project="autoscaled-worker",
                max_concurrent_experiments=5
            )
            self.worker_adapters.append(worker)
            
    def scale_down(self, target_capacity):
        while len(self.worker_adapters) > target_capacity:
            worker = self.worker_adapters.pop()
            worker.cleanup()  # Graceful shutdown
            
    def adaptive_scaling(self, experiment_queue):
        queue_size = len(experiment_queue)
        
        # Scale up for high load
        if queue_size > 50:
            self.scale_up(10)
        elif queue_size > 20:
            self.scale_up(5)  
        # Scale down for low load
        elif queue_size < 5:
            self.scale_down(1)
        elif queue_size < 10:
            self.scale_down(3)
```

---

This comprehensive documentation provides everything needed to successfully integrate W&B with GenOps governance, from basic setup through advanced production deployment patterns. The progressive complexity approach ensures developers can start simple and grow into more sophisticated use cases as their needs evolve.