#!/bin/bash

# W&B + GenOps Examples Runner
# This script runs all W&B examples in progressive complexity order
# with proper error handling and detailed output.

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_header() {
    echo -e "${BLUE}$1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Function to check prerequisites
check_prerequisites() {
    print_header "🔍 Checking Prerequisites..."
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed or not in PATH"
        exit 1
    fi
    
    # Check if we're in the right directory
    if [[ ! -f "setup_validation.py" ]]; then
        print_error "Please run this script from the examples/wandb directory"
        exit 1
    fi
    
    # Check environment variables
    if [[ -z "$WANDB_API_KEY" ]]; then
        print_warning "WANDB_API_KEY not set - some examples may fail"
        echo "  Get your API key from: https://wandb.ai/settings"
        echo "  Then run: export WANDB_API_KEY='your-api-key'"
        echo ""
    fi
    
    if [[ -z "$GENOPS_TEAM" ]]; then
        print_warning "GENOPS_TEAM not set - using default"
        export GENOPS_TEAM="demo-team"
    fi
    
    if [[ -z "$GENOPS_PROJECT" ]]; then
        print_warning "GENOPS_PROJECT not set - using default"
        export GENOPS_PROJECT="examples-demo"
    fi
    
    print_success "Prerequisites check completed"
    echo ""
}

# Function to run an example with proper error handling
run_example() {
    local script=$1
    local name=$2
    local expected_time=$3
    local complexity=$4
    
    print_header "🚀 Running: $name"
    echo "   📁 Script: $script"
    echo "   ⏱️ Expected time: $expected_time"
    echo "   📊 Complexity: $complexity"
    echo "   ⏰ Started: $(date '+%H:%M:%S')"
    echo ""
    
    local start_time=$(date +%s)
    
    if python3 "$script"; then
        local end_time=$(date +%s)
        local duration=$((end_time - start_time))
        print_success "$name completed successfully in ${duration}s"
    else
        local end_time=$(date +%s)
        local duration=$((end_time - start_time))
        print_error "$name failed after ${duration}s"
        echo ""
        print_error "Example '$name' failed. Check the output above for details."
        echo ""
        echo "Common solutions:"
        echo "  1. Run 'python3 setup_validation.py' first"
        echo "  2. Check your WANDB_API_KEY is set correctly"
        echo "  3. Ensure you have internet connectivity"
        echo "  4. Try running the example individually: python3 $script"
        echo ""
        read -p "Continue with remaining examples? (y/N) " -n 1 -r
        echo ""
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
    echo ""
}

# Main execution
main() {
    echo "🤖 W&B + GenOps Examples Suite Runner"
    echo "🕒 Started at: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "==============================================="
    echo ""
    
    check_prerequisites
    
    print_header "📚 Running Examples in Progressive Complexity Order"
    echo ""
    
    # Level 1: Getting Started (5 minutes each)
    print_header "📖 Level 1: Getting Started (5 minutes each)"
    echo ""
    
    run_example "setup_validation.py" "Setup Validation" "30 seconds" "⭐ Beginner"
    run_example "basic_tracking.py" "Basic Tracking" "5 minutes" "⭐ Beginner"
    run_example "auto_instrumentation.py" "Auto-Instrumentation" "5 minutes" "⭐ Beginner"
    
    # Check if we have more advanced examples
    if [[ -f "experiment_management.py" ]]; then
        # Level 2: Experiment Management (30 minutes each)
        print_header "📖 Level 2: Experiment Management (30 minutes each)"
        echo ""
        
        run_example "experiment_management.py" "Experiment Management" "30 minutes" "⭐⭐ Intermediate"
        
        if [[ -f "cost_optimization.py" ]]; then
            run_example "cost_optimization.py" "Cost Optimization" "30 minutes" "⭐⭐ Intermediate"
        fi
    fi
    
    if [[ -f "advanced_features.py" ]]; then
        # Level 3: Advanced Features (2 hours each)
        print_header "📖 Level 3: Advanced Features (2 hours each)"
        echo ""
        
        run_example "advanced_features.py" "Advanced Features" "2 hours" "⭐⭐⭐ Advanced"
        
        if [[ -f "production_patterns.py" ]]; then
            run_example "production_patterns.py" "Production Patterns" "2 hours" "⭐⭐⭐ Advanced"
        fi
    fi
    
    # Summary
    print_header "🎉 All Examples Completed!"
    echo ""
    print_success "Congratulations! You've successfully run all W&B + GenOps examples."
    echo ""
    echo "📚 What you learned:"
    echo "   ✅ How to set up and validate W&B + GenOps integration"
    echo "   ✅ Basic experiment tracking with governance"
    echo "   ✅ Zero-code auto-instrumentation for existing applications"
    if [[ -f "experiment_management.py" ]]; then
        echo "   ✅ Complete experiment lifecycle management"
    fi
    if [[ -f "cost_optimization.py" ]]; then
        echo "   ✅ Cost optimization and budget management"
    fi
    if [[ -f "advanced_features.py" ]]; then
        echo "   ✅ Advanced features and enterprise patterns"
    fi
    if [[ -f "production_patterns.py" ]]; then
        echo "   ✅ Production deployment and scaling patterns"
    fi
    echo ""
    
    echo "🚀 Next Steps:"
    echo "   • Integrate these patterns into your ML workflows"
    echo "   • Read the comprehensive guide: ../../docs/integrations/wandb.md"
    echo "   • Join the community: https://github.com/anthropics/GenOps-AI/discussions"
    echo ""
    
    echo "💡 Quick Reference:"
    echo "   • Basic tracking: python3 basic_tracking.py"
    echo "   • Auto-instrumentation: python3 auto_instrumentation.py"
    echo "   • Setup validation: python3 setup_validation.py"
    echo ""
    
    print_success "W&B + GenOps examples suite completed at $(date '+%H:%M:%S')"
}

# Run main function
main "$@"