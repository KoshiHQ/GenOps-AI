# CI/CD Integration Guide for GenOps AI

This guide shows how to integrate GenOps AI governance into your CI/CD pipelines for automated cost monitoring, quality gates, and deployment validation.

## Overview

GenOps AI provides CI/CD integration through:
- **Cost Budget Gates** - Prevent deployments that exceed cost thresholds
- **Quality Validation** - Ensure AI model performance meets standards
- **Governance Compliance** - Validate security and compliance requirements
- **Performance Testing** - Automated load testing with cost tracking
- **Multi-Environment Management** - Separate governance for dev/staging/prod

## GitHub Actions Integration

### Basic Cost Monitoring Workflow

```yaml
# .github/workflows/ai-cost-monitoring.yml
name: AI Cost Monitoring

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

env:
  GENOPS_ENVIRONMENT: ${{ github.ref == 'refs/heads/main' && 'production' || 'staging' }}
  GENOPS_TELEMETRY_ENABLED: true
  GENOPS_COST_TRACKING_ENABLED: true

jobs:
  cost-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install genops-ai llama-index
          pip install -r requirements.txt
      
      - name: Run cost validation tests
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          python -m pytest tests/test_cost_validation.py -v
          
      - name: Generate cost impact report
        run: |
          python scripts/generate_cost_report.py \
            --environment ${{ env.GENOPS_ENVIRONMENT }} \
            --output-format github-summary
            
      - name: Upload cost report
        uses: actions/upload-artifact@v3
        with:
          name: cost-impact-report
          path: cost-report.json

  performance-testing:
    runs-on: ubuntu-latest
    needs: cost-validation
    if: github.event_name == 'pull_request'
    steps:
      - uses: actions/checkout@v3
      
      - name: Load testing with cost tracking
        env:
          GENOPS_BUDGET_LIMIT: "5.00"  # $5 limit for PR testing
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python scripts/load_test_with_costs.py \
            --duration 300 \
            --concurrent-users 10 \
            --cost-limit ${{ env.GENOPS_BUDGET_LIMIT }}
            
      - name: Validate performance SLA
        run: |
          python scripts/validate_performance_sla.py \
            --max-p95-latency 3000 \
            --min-success-rate 95.0 \
            --max-cost-per-request 0.01

  deployment-gate:
    runs-on: ubuntu-latest
    needs: [cost-validation, performance-testing]
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Production deployment gate
        env:
          GENOPS_MONTHLY_BUDGET: ${{ vars.PRODUCTION_MONTHLY_BUDGET }}
        run: |
          python scripts/deployment_gate.py \
            --environment production \
            --monthly-budget ${{ env.GENOPS_MONTHLY_BUDGET }} \
            --require-compliance-approval
```

### Advanced Multi-Environment Pipeline

```yaml
# .github/workflows/ai-deployment-pipeline.yml
name: AI Deployment Pipeline

on:
  push:
    branches: [main, develop]
  release:
    types: [published]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [development, staging, production]
        provider: [openai, anthropic, google]
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Configure environment-specific settings
        run: |
          case "${{ matrix.environment }}" in
            development)
              echo "GENOPS_BUDGET_LIMIT=1.00" >> $GITHUB_ENV
              echo "GENOPS_ENABLE_ALERTS=false" >> $GITHUB_ENV
              ;;
            staging)
              echo "GENOPS_BUDGET_LIMIT=10.00" >> $GITHUB_ENV
              echo "GENOPS_ENABLE_ALERTS=true" >> $GITHUB_ENV
              ;;
            production)
              echo "GENOPS_BUDGET_LIMIT=100.00" >> $GITHUB_ENV
              echo "GENOPS_ENABLE_ALERTS=true" >> $GITHUB_ENV
              echo "GENOPS_REQUIRE_APPROVAL=true" >> $GITHUB_ENV
              ;;
          esac
      
      - name: Multi-provider cost comparison
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
        run: |
          python scripts/multi_provider_benchmark.py \
            --providers ${{ matrix.provider }} \
            --environment ${{ matrix.environment }} \
            --benchmark-suite comprehensive
      
      - name: Store benchmark results
        uses: actions/upload-artifact@v3
        with:
          name: benchmark-${{ matrix.environment }}-${{ matrix.provider }}
          path: benchmarks/

  security-compliance:
    runs-on: ubuntu-latest
    steps:
      - name: AI Security Scan
        run: |
          python scripts/ai_security_scan.py \
            --check-api-key-exposure \
            --validate-data-handling \
            --check-compliance SOC2,GDPR,HIPAA
      
      - name: Generate compliance report
        run: |
          python scripts/compliance_report.py \
            --format json \
            --output compliance-report.json
            
      - name: Upload compliance report
        uses: actions/upload-artifact@v3
        with:
          name: compliance-report
          path: compliance-report.json

  deploy:
    runs-on: ubuntu-latest
    needs: [build-and-test, security-compliance]
    if: github.ref == 'refs/heads/main'
    environment: production
    
    steps:
      - name: Deploy to Kubernetes with GenOps monitoring
        env:
          KUBECONFIG: ${{ secrets.KUBECONFIG }}
        run: |
          # Generate Kubernetes manifests with GenOps configuration
          python scripts/generate_k8s_manifests.py \
            --environment production \
            --enable-genops-monitoring \
            --cost-budget-limit ${{ vars.PRODUCTION_MONTHLY_BUDGET }}
          
          # Apply manifests
          kubectl apply -f k8s/production/
          
          # Verify deployment with health checks
          kubectl rollout status deployment/genops-ai-service -n ai-production
          
          # Run post-deployment validation
          python scripts/post_deploy_validation.py \
            --environment production \
            --run-smoke-tests \
            --validate-cost-tracking
```

## GitLab CI Integration

### Basic Pipeline Configuration

```yaml
# .gitlab-ci.yml
stages:
  - validate
  - test
  - security
  - deploy
  - monitor

variables:
  GENOPS_TELEMETRY_ENABLED: "true"
  GENOPS_COST_TRACKING_ENABLED: "true"
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip/

before_script:
  - pip install genops-ai llama-index
  - export GENOPS_ENVIRONMENT=${CI_ENVIRONMENT_NAME:-development}

cost-validation:
  stage: validate
  script:
    - python scripts/validate_cost_budgets.py
    - python scripts/estimate_deployment_costs.py --environment $CI_ENVIRONMENT_NAME
  artifacts:
    reports:
      junit: cost-validation-report.xml
    paths:
      - cost-estimates.json
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == "main"

ai-performance-test:
  stage: test
  parallel:
    matrix:
      - PROVIDER: [openai, anthropic, google]
        WORKLOAD: [light, medium, heavy]
  script:
    - |
      python scripts/performance_test.py \
        --provider $PROVIDER \
        --workload $WORKLOAD \
        --max-cost-per-test 2.00 \
        --output-format junit
  artifacts:
    reports:
      junit: performance-test-$PROVIDER-$WORKLOAD.xml

security-scan:
  stage: security
  script:
    - python scripts/ai_security_audit.py
    - python scripts/check_api_key_security.py
    - python scripts/validate_data_governance.py
  artifacts:
    reports:
      security: security-report.json

deploy-staging:
  stage: deploy
  environment:
    name: staging
    url: https://ai-staging.example.com
  script:
    - helm upgrade --install genops-ai-staging ./helm/genops-ai
      --set environment=staging
      --set genops.budgetLimit=50.00
      --set genops.enableAlerts=true
  rules:
    - if: $CI_COMMIT_BRANCH == "develop"

deploy-production:
  stage: deploy
  environment:
    name: production
    url: https://ai-production.example.com
  script:
    - |
      # Production deployment with approval gates
      python scripts/pre_deploy_validation.py --environment production
      helm upgrade --install genops-ai-prod ./helm/genops-ai
        --set environment=production
        --set genops.budgetLimit=$PRODUCTION_MONTHLY_BUDGET
        --set genops.enableCircuitBreakers=true
        --set genops.enableGracefulDegradation=true
  when: manual
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

post-deploy-monitoring:
  stage: monitor
  script:
    - python scripts/post_deploy_health_check.py
    - python scripts/validate_cost_tracking.py
    - python scripts/send_deployment_notification.py
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

## Jenkins Pipeline Integration

### Declarative Pipeline

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        GENOPS_TELEMETRY_ENABLED = 'true'
        GENOPS_COST_TRACKING_ENABLED = 'true'
        GENOPS_ENVIRONMENT = "${env.BRANCH_NAME == 'main' ? 'production' : 'staging'}"
    }
    
    stages {
        stage('Setup') {
            steps {
                script {
                    sh 'pip install genops-ai llama-index'
                    
                    // Set environment-specific budget limits
                    if (env.BRANCH_NAME == 'main') {
                        env.BUDGET_LIMIT = '100.00'
                        env.ENABLE_ALERTS = 'true'
                    } else {
                        env.BUDGET_LIMIT = '10.00'
                        env.ENABLE_ALERTS = 'false'
                    }
                }
            }
        }
        
        stage('Cost Validation') {
            parallel {
                stage('Budget Check') {
                    steps {
                        script {
                            sh """
                                python scripts/budget_validation.py \
                                    --budget-limit ${env.BUDGET_LIMIT} \
                                    --environment ${env.GENOPS_ENVIRONMENT}
                            """
                        }
                    }
                }
                
                stage('Provider Cost Comparison') {
                    steps {
                        withCredentials([
                            string(credentialsId: 'openai-api-key', variable: 'OPENAI_API_KEY'),
                            string(credentialsId: 'anthropic-api-key', variable: 'ANTHROPIC_API_KEY')
                        ]) {
                            sh '''
                                python scripts/provider_cost_analysis.py \
                                    --providers openai,anthropic \
                                    --sample-queries 50 \
                                    --max-cost-per-provider 5.00
                            '''
                        }
                    }
                }
            }
        }
        
        stage('AI Quality Gate') {
            steps {
                script {
                    def qualityResults = sh(
                        script: '''
                            python scripts/ai_quality_gate.py \
                                --min-accuracy 0.85 \
                                --max-latency 3000 \
                                --min-success-rate 0.95 \
                                --output-format json
                        ''',
                        returnStdout: true
                    ).trim()
                    
                    def quality = readJSON text: qualityResults
                    
                    if (quality.overall_score < 0.8) {
                        error "AI Quality Gate failed: Overall score ${quality.overall_score} < 0.8"
                    }
                }
            }
        }
        
        stage('Load Testing') {
            when {
                anyOf {
                    branch 'main'
                    changeRequest()
                }
            }
            steps {
                sh '''
                    python scripts/load_test_ai_service.py \
                        --duration 300 \
                        --concurrent-users 20 \
                        --cost-limit 10.00 \
                        --generate-report
                '''
                
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'load-test-reports',
                    reportFiles: 'index.html',
                    reportName: 'Load Test Report'
                ])
            }
        }
        
        stage('Deploy') {
            when { branch 'main' }
            steps {
                script {
                    // Production deployment with GenOps monitoring
                    sh '''
                        helm upgrade --install genops-ai-prod ./helm/genops-ai \
                            --set environment=production \
                            --set genops.budgetLimit=${BUDGET_LIMIT} \
                            --set genops.enableMonitoring=true \
                            --set genops.enableAlerts=${ENABLE_ALERTS} \
                            --wait --timeout=600s
                    '''
                    
                    // Post-deployment validation
                    sh 'python scripts/post_deploy_validation.py --environment production'
                }
            }
        }
        
        stage('Post-Deploy Monitoring') {
            when { branch 'main' }
            steps {
                script {
                    // Set up continuous monitoring
                    sh '''
                        python scripts/setup_continuous_monitoring.py \
                            --environment production \
                            --enable-cost-alerts \
                            --enable-performance-alerts \
                            --enable-quality-alerts
                    '''
                }
            }
        }
    }
    
    post {
        always {
            // Archive cost and performance reports
            archiveArtifacts artifacts: '**/cost-reports/*.json, **/performance-reports/*.html'
            
            // Send notifications
            script {
                sh '''
                    python scripts/send_pipeline_notification.py \
                        --status ${currentBuild.result} \
                        --environment ${GENOPS_ENVIRONMENT} \
                        --include-cost-summary
                '''
            }
        }
        
        failure {
            script {
                sh '''
                    python scripts/failure_analysis.py \
                        --build-url ${BUILD_URL} \
                        --generate-debug-report
                '''
            }
        }
    }
}
```

## Cost Budget Gates

### Python Budget Validation Script

```python
#!/usr/bin/env python3
"""
Budget validation script for CI/CD pipelines.
"""

import os
import sys
import argparse
from genops.providers.llamaindex import multi_provider_cost_tracking

def validate_budget_constraints(budget_limit: float, environment: str) -> bool:
    """Validate that estimated costs are within budget constraints."""
    
    # Create cost tracker for validation
    tracker = multi_provider_cost_tracking(
        providers=['openai', 'anthropic', 'google'],
        budget_per_provider={'openai': budget_limit * 0.5, 'anthropic': budget_limit * 0.3, 'google': budget_limit * 0.2},
        enable_cost_optimization=True,
        environment=environment
    )
    
    # Simulate typical workload costs
    estimated_costs = {
        'development': budget_limit * 0.1,   # 10% of budget for dev testing
        'staging': budget_limit * 0.3,       # 30% of budget for staging validation
        'production': budget_limit * 0.8     # 80% of budget for production (with headroom)
    }
    
    estimated_cost = estimated_costs.get(environment, budget_limit * 0.5)
    
    print(f"Environment: {environment}")
    print(f"Budget Limit: ${budget_limit:.2f}")
    print(f"Estimated Cost: ${estimated_cost:.2f}")
    print(f"Budget Utilization: {(estimated_cost / budget_limit) * 100:.1f}%")
    
    # Check budget constraints
    if estimated_cost > budget_limit:
        print(f"❌ BUDGET VALIDATION FAILED: Estimated cost exceeds budget")
        return False
    
    if estimated_cost > budget_limit * 0.9:
        print(f"⚠️  WARNING: Estimated cost is >90% of budget")
        if environment == 'production':
            print(f"❌ BUDGET VALIDATION FAILED: Production deployment too close to budget limit")
            return False
    
    print(f"✅ BUDGET VALIDATION PASSED")
    return True

def main():
    parser = argparse.ArgumentParser(description='Validate AI deployment budget constraints')
    parser.add_argument('--budget-limit', type=float, required=True, help='Maximum budget limit in USD')
    parser.add_argument('--environment', choices=['development', 'staging', 'production'], required=True)
    parser.add_argument('--fail-on-warning', action='store_true', help='Fail validation on warnings')
    
    args = parser.parse_args()
    
    # Get API keys from environment
    api_keys = {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'ANTHROPIC_API_KEY': os.getenv('ANTHROPIC_API_KEY'),
        'GOOGLE_API_KEY': os.getenv('GOOGLE_API_KEY')
    }
    
    if not any(api_keys.values()):
        print("❌ ERROR: No AI provider API keys found in environment")
        sys.exit(1)
    
    # Run budget validation
    if not validate_budget_constraints(args.budget_limit, args.environment):
        sys.exit(1)
    
    print(f"✅ Budget validation completed successfully")

if __name__ == '__main__':
    main()
```

## Quality Gates and Performance SLA Validation

### AI Quality Gate Script

```python
#!/usr/bin/env python3
"""
AI Quality Gate validation for CI/CD pipelines.
"""

import json
import time
import statistics
from typing import Dict, List, Any
from genops.providers.llamaindex import instrument_llamaindex, create_llamaindex_cost_context

def run_quality_validation(
    min_accuracy: float = 0.85,
    max_latency_ms: float = 3000,
    min_success_rate: float = 0.95,
    sample_size: int = 20
) -> Dict[str, Any]:
    """Run comprehensive quality validation tests."""
    
    adapter = instrument_llamaindex()
    
    test_queries = [
        "What is artificial intelligence?",
        "Explain machine learning basics",
        "How do neural networks work?",
        "What are the benefits of cloud computing?",
        "Describe database optimization techniques"
    ] * (sample_size // 5)  # Repeat to reach sample size
    
    results = {
        'total_tests': len(test_queries),
        'successful_tests': 0,
        'failed_tests': 0,
        'latencies': [],
        'costs': [],
        'quality_scores': [],
        'errors': []
    }
    
    with create_llamaindex_cost_context("quality_gate_validation", budget_limit=5.0) as context:
        
        for i, query in enumerate(test_queries):
            try:
                start_time = time.time()
                
                # Simulate query execution
                time.sleep(0.1 + (i % 3) * 0.05)  # Simulate variable latency
                
                end_time = time.time()
                latency_ms = (end_time - start_time) * 1000
                
                # Simulate cost and quality scores
                estimated_cost = 0.001 + (i % 5) * 0.0002
                quality_score = 0.8 + (i % 20) * 0.01  # 0.8 to 0.99
                
                results['latencies'].append(latency_ms)
                results['costs'].append(estimated_cost)
                results['quality_scores'].append(quality_score)
                results['successful_tests'] += 1
                
                # Record operation in cost context
                context.add_llamaindex_operation({
                    'operation_type': 'query',
                    'provider': 'openai',
                    'model': 'gpt-3.5-turbo',
                    'tokens_consumed': 100,
                    'cost_usd': estimated_cost,
                    'duration_ms': latency_ms,
                    'quality_score': quality_score
                })
                
            except Exception as e:
                results['failed_tests'] += 1
                results['errors'].append(str(e))
    
    # Calculate metrics
    success_rate = results['successful_tests'] / results['total_tests']
    avg_latency = statistics.mean(results['latencies']) if results['latencies'] else 0
    p95_latency = statistics.quantiles(results['latencies'], n=20)[18] if len(results['latencies']) >= 20 else avg_latency
    avg_quality = statistics.mean(results['quality_scores']) if results['quality_scores'] else 0
    total_cost = sum(results['costs'])
    
    # Quality gate evaluation
    quality_gate_results = {
        'metrics': {
            'success_rate': success_rate,
            'avg_latency_ms': avg_latency,
            'p95_latency_ms': p95_latency,
            'avg_quality_score': avg_quality,
            'total_cost': total_cost,
            'cost_per_query': total_cost / results['total_tests'] if results['total_tests'] > 0 else 0
        },
        'thresholds': {
            'min_accuracy': min_accuracy,
            'max_latency_ms': max_latency_ms,
            'min_success_rate': min_success_rate
        },
        'results': {
            'accuracy_pass': avg_quality >= min_accuracy,
            'latency_pass': p95_latency <= max_latency_ms,
            'success_rate_pass': success_rate >= min_success_rate
        }
    }
    
    # Calculate overall score
    overall_pass = all(quality_gate_results['results'].values())
    quality_gate_results['overall_pass'] = overall_pass
    quality_gate_results['overall_score'] = (
        (1.0 if quality_gate_results['results']['accuracy_pass'] else 0.0) +
        (1.0 if quality_gate_results['results']['latency_pass'] else 0.0) +
        (1.0 if quality_gate_results['results']['success_rate_pass'] else 0.0)
    ) / 3.0
    
    return quality_gate_results

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='AI Quality Gate validation')
    parser.add_argument('--min-accuracy', type=float, default=0.85)
    parser.add_argument('--max-latency', type=float, default=3000)
    parser.add_argument('--min-success-rate', type=float, default=0.95)
    parser.add_argument('--sample-size', type=int, default=20)
    parser.add_argument('--output-format', choices=['json', 'text'], default='text')
    
    args = parser.parse_args()
    
    # Run quality validation
    results = run_quality_validation(
        min_accuracy=args.min_accuracy,
        max_latency_ms=args.max_latency,
        min_success_rate=args.min_success_rate,
        sample_size=args.sample_size
    )
    
    if args.output_format == 'json':
        print(json.dumps(results, indent=2))
    else:
        print("🎯 AI QUALITY GATE RESULTS")
        print("=" * 40)
        
        metrics = results['metrics']
        thresholds = results['thresholds']
        test_results = results['results']
        
        print(f"Success Rate: {metrics['success_rate']:.1%} ({'✅' if test_results['success_rate_pass'] else '❌'} >= {thresholds['min_success_rate']:.1%})")
        print(f"Avg Latency: {metrics['avg_latency_ms']:.0f}ms")
        print(f"P95 Latency: {metrics['p95_latency_ms']:.0f}ms ({'✅' if test_results['latency_pass'] else '❌'} <= {thresholds['max_latency_ms']:.0f}ms)")
        print(f"Avg Quality: {metrics['avg_quality_score']:.3f} ({'✅' if test_results['accuracy_pass'] else '❌'} >= {thresholds['min_accuracy']:.3f})")
        print(f"Total Cost: ${metrics['total_cost']:.6f}")
        print(f"Cost/Query: ${metrics['cost_per_query']:.6f}")
        
        print(f"\nOverall Result: {'✅ PASSED' if results['overall_pass'] else '❌ FAILED'}")
        print(f"Overall Score: {results['overall_score']:.1%}")
    
    # Exit with appropriate code
    exit_code = 0 if results['overall_pass'] else 1
    exit(exit_code)

if __name__ == '__main__':
    main()
```

## Best Practices

### 1. Environment-Specific Configuration

- **Development**: Low budget limits, minimal monitoring
- **Staging**: Production-like testing with cost controls
- **Production**: Full monitoring, alerts, and approval gates

### 2. Budget Management

- Set appropriate budget limits per environment
- Implement automatic cost alerts and circuit breakers
- Use cost forecasting to predict monthly spending

### 3. Quality Assurance

- Establish minimum quality thresholds
- Test performance across multiple providers
- Validate compliance requirements automatically

### 4. Security

- Store API keys securely using CI/CD secrets management
- Implement proper RBAC for different environments
- Enable audit logging for all AI operations

### 5. Monitoring and Alerting

- Set up real-time cost monitoring
- Configure alerts for budget overruns
- Monitor performance metrics continuously

This guide provides comprehensive CI/CD integration patterns that ensure your AI deployments maintain cost efficiency, quality standards, and governance compliance throughout the development lifecycle.