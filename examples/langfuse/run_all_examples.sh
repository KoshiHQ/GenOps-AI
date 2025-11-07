#!/bin/bash

# Langfuse + GenOps Complete Example Suite Runner
# 
# This script runs all Langfuse integration examples in progressive complexity order,
# demonstrating the full range of GenOps governance capabilities with Langfuse.
#
# Usage: ./run_all_examples.sh
#
# Prerequisites:
#   - pip install genops[langfuse]
#   - Environment variables set (see README.md)
#   - All example files present in current directory

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Script configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOTAL_EXAMPLES=6
CURRENT_EXAMPLE=0
START_TIME=$(date +%s)

# Example files in progressive complexity order
EXAMPLES=(
    "setup_validation.py|Setup Validation|Level 1 (30 seconds)|Validate your Langfuse + GenOps setup"
    "basic_tracking.py|Basic Tracking|Level 1 (5 minutes)|Simple LLM operations with governance"
    "auto_instrumentation.py|Auto-Instrumentation|Level 1 (5 minutes)|Zero-code governance integration"
    "evaluation_integration.py|Evaluation Integration|Level 2 (30 minutes)|LLM evaluation with governance"
    "prompt_management.py|Prompt Management|Level 2 (30 minutes)|Advanced prompt optimization"
    "advanced_observability.py|Advanced Observability|Level 3 (2 hours)|Enterprise observability patterns"
    "production_patterns.py|Production Patterns|Level 3 (2 hours)|Production deployment patterns"
)

# Functions
print_header() {
    echo -e "${BLUE}"
    echo "================================================================================================"
    echo " 🔍 Langfuse LLM Observability + GenOps Governance - Complete Example Suite"
    echo "================================================================================================"
    echo -e "${NC}"
    echo "This script runs all Langfuse integration examples demonstrating progressive complexity:"
    echo ""
    echo -e "${GREEN}Level 1 (Getting Started):${NC} 5-minute examples for immediate value"
    echo -e "${YELLOW}Level 2 (Advanced Features):${NC} 30-minute examples for comprehensive governance"
    echo -e "${RED}Level 3 (Enterprise Grade):${NC} 2-hour examples for production deployment"
    echo ""
    echo "Total examples: $TOTAL_EXAMPLES"
    echo "Estimated total time: ~4-6 hours (depending on your exploration depth)"
    echo ""
}

check_prerequisites() {
    echo -e "${CYAN}🔧 Checking Prerequisites...${NC}"
    
    # Check if we're in the right directory
    if [ ! -f "setup_validation.py" ]; then
        echo -e "${RED}❌ Error: Not in the langfuse examples directory${NC}"
        echo "Please run this script from: examples/langfuse/"
        exit 1
    fi
    
    # Check Python installation
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Error: Python 3 is required${NC}"
        exit 1
    fi
    
    # Check if GenOps is installed
    if ! python3 -c "import genops" &> /dev/null; then
        echo -e "${RED}❌ Error: GenOps not installed${NC}"
        echo "Please install: pip install genops[langfuse]"
        exit 1
    fi
    
    # Check if Langfuse is available
    if ! python3 -c "import langfuse" &> /dev/null; then
        echo -e "${RED}❌ Error: Langfuse not installed${NC}"
        echo "Please install: pip install langfuse"
        exit 1
    fi
    
    # Check required environment variables
    local missing_vars=()
    
    if [ -z "$LANGFUSE_PUBLIC_KEY" ]; then
        missing_vars+=("LANGFUSE_PUBLIC_KEY")
    fi
    
    if [ -z "$LANGFUSE_SECRET_KEY" ]; then
        missing_vars+=("LANGFUSE_SECRET_KEY")
    fi
    
    if [ -z "$OPENAI_API_KEY" ] && [ -z "$ANTHROPIC_API_KEY" ]; then
        missing_vars+=("OPENAI_API_KEY or ANTHROPIC_API_KEY")
    fi
    
    if [ ${#missing_vars[@]} -ne 0 ]; then
        echo -e "${RED}❌ Error: Missing required environment variables:${NC}"
        for var in "${missing_vars[@]}"; do
            echo "   - $var"
        done
        echo ""
        echo "Please set these variables and try again."
        echo "See README.md for setup instructions."
        exit 1
    fi
    
    # Check that all example files exist
    local missing_files=()
    for example_info in "${EXAMPLES[@]}"; do
        local filename=$(echo "$example_info" | cut -d'|' -f1)
        if [ ! -f "$filename" ]; then
            missing_files+=("$filename")
        fi
    done
    
    if [ ${#missing_files[@]} -ne 0 ]; then
        echo -e "${RED}❌ Error: Missing example files:${NC}"
        for file in "${missing_files[@]}"; do
            echo "   - $file"
        done
        exit 1
    fi
    
    echo -e "${GREEN}✅ All prerequisites satisfied${NC}"
    echo ""
}

run_example() {
    local example_info="$1"
    local filename=$(echo "$example_info" | cut -d'|' -f1)
    local name=$(echo "$example_info" | cut -d'|' -f2)
    local level=$(echo "$example_info" | cut -d'|' -f3)
    local description=$(echo "$example_info" | cut -d'|' -f4)
    
    CURRENT_EXAMPLE=$((CURRENT_EXAMPLE + 1))
    
    echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${PURPLE}📊 Example $CURRENT_EXAMPLE/$TOTAL_EXAMPLES: $name${NC}"
    echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}🎯 Complexity: $level${NC}"
    echo -e "${CYAN}📝 Description: $description${NC}"
    echo -e "${CYAN}📁 File: $filename${NC}"
    echo ""
    
    local example_start_time=$(date +%s)
    
    # Run the example
    if python3 "$filename"; then
        local example_end_time=$(date +%s)
        local example_duration=$((example_end_time - example_start_time))
        echo ""
        echo -e "${GREEN}✅ Example completed successfully in ${example_duration}s${NC}"
        
        # Brief pause between examples
        echo ""
        echo -e "${YELLOW}⏸️  Pausing 3 seconds before next example...${NC}"
        sleep 3
    else
        echo ""
        echo -e "${RED}❌ Example failed${NC}"
        echo ""
        read -p "Continue with remaining examples? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${YELLOW}🛑 Example suite stopped by user${NC}"
            exit 1
        fi
    fi
    
    echo ""
}

print_summary() {
    local end_time=$(date +%s)
    local total_duration=$((end_time - START_TIME))
    local hours=$((total_duration / 3600))
    local minutes=$(((total_duration % 3600) / 60))
    local seconds=$((total_duration % 60))
    
    echo -e "${GREEN}"
    echo "================================================================================================"
    echo " 🎉 Langfuse + GenOps Complete Example Suite - FINISHED!"
    echo "================================================================================================"
    echo -e "${NC}"
    echo -e "${GREEN}✅ All $TOTAL_EXAMPLES examples completed successfully!${NC}"
    echo ""
    echo -e "${CYAN}⏱️  Total Execution Time: ${hours}h ${minutes}m ${seconds}s${NC}"
    echo ""
    echo -e "${YELLOW}🎯 What You've Accomplished:${NC}"
    echo ""
    echo -e "${GREEN}Level 1 - Getting Started (5 minutes each):${NC}"
    echo "   ✅ Validated your Langfuse + GenOps setup and connectivity"
    echo "   ✅ Learned basic LLM operations with governance enhancement"
    echo "   ✅ Enabled zero-code governance for existing Langfuse applications"
    echo ""
    echo -e "${YELLOW}Level 2 - Advanced Features (30 minutes each):${NC}"
    echo "   ✅ Implemented LLM evaluation workflows with cost intelligence"
    echo "   ✅ Built advanced prompt management with optimization insights"
    echo ""
    echo -e "${RED}Level 3 - Enterprise Grade (2 hours each):${NC}"
    echo "   ✅ Deployed advanced observability patterns with hierarchical tracing"
    echo "   ✅ Configured production-ready deployment with enterprise governance"
    echo ""
    echo -e "${PURPLE}🏆 Enterprise Capabilities Mastered:${NC}"
    echo "   🔍 Enhanced LLM observability with comprehensive governance"
    echo "   💰 Advanced cost intelligence and team attribution"
    echo "   🛡️  Enterprise governance with compliance automation"
    echo "   📊 Production-grade monitoring and alerting"
    echo "   🚀 High-availability deployment patterns"
    echo "   🏭 Scalable observability for enterprise workloads"
    echo ""
    echo -e "${CYAN}🚀 Next Steps:${NC}"
    echo "   📚 Review comprehensive guide: docs/integrations/langfuse.md"
    echo "   🏗️  Implement patterns from examples in your applications"
    echo "   🔧 Configure production deployment using production_patterns.py insights"
    echo "   📊 Set up monitoring dashboards for your observability platform"
    echo "   🏛️  Customize governance policies for your organization"
    echo ""
    echo -e "${GREEN}Ready to deploy Langfuse + GenOps in production! 🎉${NC}"
    echo ""
}

print_interrupted_summary() {
    local end_time=$(date +%s)
    local total_duration=$((end_time - START_TIME))
    local minutes=$((total_duration / 60))
    local seconds=$((total_duration % 60))
    
    echo ""
    echo -e "${YELLOW}"
    echo "================================================================================================"
    echo " ⏸️  Langfuse + GenOps Example Suite - Interrupted"
    echo "================================================================================================"
    echo -e "${NC}"
    echo -e "${YELLOW}Examples completed: $CURRENT_EXAMPLE/$TOTAL_EXAMPLES${NC}"
    echo -e "${CYAN}Time elapsed: ${minutes}m ${seconds}s${NC}"
    echo ""
    echo -e "${BLUE}💡 You can resume anytime by running individual examples:${NC}"
    for example_info in "${EXAMPLES[@]}"; do
        local filename=$(echo "$example_info" | cut -d'|' -f1)
        local name=$(echo "$example_info" | cut -d'|' -f2)
        echo "   python3 $filename  # $name"
    done
    echo ""
    echo "Or run this script again to start from the beginning."
    echo ""
}

# Trap Ctrl+C to show partial summary
trap print_interrupted_summary INT

# Main execution
print_header

# Interactive confirmation
echo -e "${YELLOW}🚀 Ready to run all $TOTAL_EXAMPLES Langfuse + GenOps examples?${NC}"
echo ""
echo "This comprehensive suite will demonstrate:"
echo "   • Enhanced LLM observability with governance intelligence"
echo "   • Cost optimization and team attribution"
echo "   • Advanced evaluation and prompt management"
echo "   • Enterprise-grade production deployment patterns"
echo ""
read -p "Continue? (Y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Nn]$ ]]; then
    echo -e "${YELLOW}🛑 Example suite cancelled by user${NC}"
    exit 0
fi

echo ""
check_prerequisites

echo -e "${BLUE}🚀 Starting Langfuse + GenOps Complete Example Suite...${NC}"
echo ""

# Run all examples in order
for example_info in "${EXAMPLES[@]}"; do
    run_example "$example_info"
done

# Print final summary
print_summary