#!/bin/bash
"""
GenOps + Helicone: Complete Example Suite Runner

This script runs all Helicone examples in order, providing comprehensive
validation and demonstration of GenOps + Helicone AI Gateway integration.

Usage:
    ./run_all_examples.sh

Prerequisites:
    - Helicone API key: export HELICONE_API_KEY="your_key"
    - At least one provider API key (OpenAI, Anthropic, Groq)
    - GenOps installed: pip install genops[helicone]
"""

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[$(date +'%H:%M:%S')] $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check if we're in the right directory
if [ ! -f "setup_validation.py" ]; then
    print_error "Must run from examples/helicone/ directory"
    exit 1
fi

print_status "🚀 GenOps + Helicone: Complete Example Suite"
echo "============================================================"

# Track results
declare -a results=()
total_examples=0
passed_examples=0
failed_examples=0

# Function to run an example
run_example() {
    local example_file="$1"
    local example_name="$2"
    local time_estimate="$3"
    
    total_examples=$((total_examples + 1))
    
    if [ ! -f "$example_file" ]; then
        print_error "Example file not found: $example_file"
        results+=("❌ $example_name: File not found")
        failed_examples=$((failed_examples + 1))
        return 1
    fi
    
    print_status "Running: $example_name ($time_estimate)"
    echo "------------------------------------------------------------"
    
    if python3 "$example_file"; then
        print_success "$example_name completed successfully"
        results+=("✅ $example_name: Success")
        passed_examples=$((passed_examples + 1))
        return 0
    else
        print_error "$example_name failed"
        results+=("❌ $example_name: Failed")
        failed_examples=$((failed_examples + 1))
        return 1
    fi
}

# Pre-flight checks
print_status "🔍 Pre-flight Checks"
echo "------------------------------------------------------------"

# Check Python
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is required but not found"
    exit 1
fi
print_success "Python 3 found"

# Check environment variables
if [ -z "$HELICONE_API_KEY" ]; then
    print_error "HELICONE_API_KEY environment variable not set"
    echo "  Get your key at: https://app.helicone.ai/"
    echo "  Set it with: export HELICONE_API_KEY='your_key'"
    exit 1
fi
print_success "Helicone API key found"

# Check for at least one provider key
provider_count=0
if [ -n "$OPENAI_API_KEY" ]; then
    print_success "OpenAI API key found"
    provider_count=$((provider_count + 1))
fi

if [ -n "$ANTHROPIC_API_KEY" ]; then
    print_success "Anthropic API key found"
    provider_count=$((provider_count + 1))
fi

if [ -n "$GROQ_API_KEY" ]; then
    print_success "Groq API key found"
    provider_count=$((provider_count + 1))
fi

if [ $provider_count -eq 0 ]; then
    print_error "No provider API keys found"
    echo "  Configure at least one:"
    echo "  • export OPENAI_API_KEY='your_openai_key'"
    echo "  • export ANTHROPIC_API_KEY='your_anthropic_key'"
    echo "  • export GROQ_API_KEY='your_groq_key' (free tier available)"
    exit 1
fi

print_success "$provider_count provider API key(s) configured"

echo ""
print_status "🏃 Running All Examples (Estimated time: ~15 minutes)"
echo "============================================================"

# Level 1: Getting Started (5 minutes each)
echo ""
print_status "📚 Level 1: Getting Started Examples"
echo "============================================================"

run_example "setup_validation.py" "Setup Validation" "2 minutes"
echo ""

run_example "basic_tracking.py" "Basic Multi-Provider Tracking" "3 minutes" 
echo ""

run_example "auto_instrumentation.py" "Auto-Instrumentation" "2 minutes"
echo ""

# Level 2: Multi-Provider Intelligence (30 minutes each - but we'll run shorter versions)
print_status "📚 Level 2: Multi-Provider Intelligence Examples"
echo "============================================================"

run_example "multi_provider_costs.py" "Multi-Provider Cost Analysis" "5 minutes"
echo ""

run_example "cost_optimization.py" "Cost Optimization Strategies" "4 minutes"
echo ""

# Level 3: Advanced Features (2 hours each - but we'll run shorter versions)
print_status "📚 Level 3: Advanced Gateway Features"
echo "============================================================"

run_example "advanced_features.py" "Advanced Features & Routing" "3 minutes"
echo ""

run_example "production_patterns.py" "Production Deployment Patterns" "3 minutes"
echo ""

# Final Results
echo ""
echo "============================================================"
print_status "📊 FINAL RESULTS"
echo "============================================================"

echo ""
echo "📈 Summary:"
echo "  • Total examples: $total_examples"
echo "  • Passed: $passed_examples"
echo "  • Failed: $failed_examples"
echo ""

echo "📋 Detailed Results:"
for result in "${results[@]}"; do
    echo "  $result"
done

echo ""

if [ $failed_examples -eq 0 ]; then
    print_success "🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!"
    echo ""
    echo "🌟 You're now ready to:"
    echo "  • Integrate GenOps + Helicone into your applications"
    echo "  • Implement multi-provider cost optimization"
    echo "  • Deploy enterprise-ready AI gateway solutions"
    echo ""
    echo "📚 Next Steps:"
    echo "  • Review docs/integrations/helicone.md for detailed guidance"
    echo "  • Implement patterns from the examples in your code"
    echo "  • Set up monitoring and governance for production use"
    echo ""
    exit 0
else
    print_warning "Some examples failed. Check the detailed results above."
    echo ""
    echo "🔧 Troubleshooting:"
    echo "  • Ensure all API keys are valid and have sufficient credits"
    echo "  • Check network connectivity to AI providers"
    echo "  • Verify GenOps installation: pip install genops[helicone]"
    echo "  • Run setup_validation.py for detailed diagnostics"
    echo ""
    exit 1
fi