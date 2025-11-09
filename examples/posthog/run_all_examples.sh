#!/bin/bash
# PostHog + GenOps Interactive Examples Runner
# 
# This script runs all PostHog examples in sequence with interactive progress tracking,
# colored output, and error handling. Perfect for demonstrations and testing.
#
# Usage:
#   chmod +x run_all_examples.sh
#   ./run_all_examples.sh
#
# Prerequisites:
#   - POSTHOG_API_KEY environment variable
#   - genops[posthog] installed

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Unicode symbols
CHECKMARK="✅"
CROSSMARK="❌"
WARNING="⚠️"
INFO="ℹ️"
ROCKET="🚀"
CLOCK="⏱️"
GEAR="⚙️"
CHART="📊"

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXAMPLES_DIR="$SCRIPT_DIR"
LOG_FILE="$EXAMPLES_DIR/run_all_examples.log"
INTERACTIVE=true
CONTINUE_ON_ERROR=false

# Example definitions
declare -a EXAMPLES=(
    "setup_validation.py|Setup Validation|Validate PostHog + GenOps configuration|2 min|Beginner"
    "basic_tracking.py|Basic Analytics Tracking|Basic event tracking with governance|5 min|Beginner"
    "auto_instrumentation.py|Auto-Instrumentation|Zero-code auto-instrumentation demo|3 min|Beginner"
    "advanced_features.py|Advanced Features|Advanced analytics and governance|15 min|Intermediate"
    "cost_optimization.py|Cost Optimization|Cost intelligence and optimization|10 min|Intermediate"
    "production_patterns.py|Production Patterns|Production deployment patterns|20 min|Advanced"
)

# Initialize log file
echo "PostHog + GenOps Examples Run - $(date)" > "$LOG_FILE"
echo "=========================================" >> "$LOG_FILE"

# Functions
show_banner() {
    clear
    echo -e "${PURPLE}================================================================${NC}"
    echo -e "${WHITE}   🎯 PostHog + GenOps Interactive Examples Runner${NC}"
    echo -e "${PURPLE}================================================================${NC}"
    echo ""
    echo -e "${CYAN}This script will run all PostHog examples in sequence with${NC}"
    echo -e "${CYAN}interactive progress tracking and error handling.${NC}"
    echo ""
    echo -e "${YELLOW}Prerequisites:${NC}"
    echo -e "  ${CHECKMARK} POSTHOG_API_KEY environment variable"
    echo -e "  ${CHECKMARK} genops[posthog] installed"
    echo -e "  ${CHECKMARK} Python 3.9+ available"
    echo ""
}

show_progress() {
    local current=$1
    local total=$2
    local width=50
    local percentage=$((current * 100 / total))
    local filled=$((width * current / total))
    local empty=$((width - filled))
    
    printf "\r${BLUE}Progress: [${GREEN}"
    printf "%*s" $filled | tr ' ' '█'
    printf "${WHITE}"
    printf "%*s" $empty | tr ' ' '░'
    printf "${BLUE}] ${WHITE}%d%%${NC}" $percentage
}

check_prerequisites() {
    echo -e "${INFO} ${CYAN}Checking prerequisites...${NC}"
    local all_good=true
    
    # Check Python
    if command -v python3 >/dev/null 2>&1; then
        echo -e "  ${CHECKMARK} Python 3 available: $(python3 --version)"
    elif command -v python >/dev/null 2>&1; then
        echo -e "  ${CHECKMARK} Python available: $(python --version)"
    else
        echo -e "  ${CROSSMARK} Python not found"
        all_good=false
    fi
    
    # Check environment variables
    if [[ -n "${POSTHOG_API_KEY:-}" ]]; then
        echo -e "  ${CHECKMARK} POSTHOG_API_KEY configured"
    else
        echo -e "  ${WARNING} POSTHOG_API_KEY not set (some examples may fail)"
    fi
    
    if [[ -n "${GENOPS_TEAM:-}" ]]; then
        echo -e "  ${CHECKMARK} GENOPS_TEAM configured: $GENOPS_TEAM"
    else
        echo -e "  ${INFO} GENOPS_TEAM not set (will use defaults)"
    fi
    
    # Check GenOps installation
    if python3 -c "import genops" 2>/dev/null; then
        echo -e "  ${CHECKMARK} GenOps package available"
    elif python -c "import genops" 2>/dev/null; then
        echo -e "  ${CHECKMARK} GenOps package available"
    else
        echo -e "  ${CROSSMARK} GenOps not installed (run: pip install genops[posthog])"
        all_good=false
    fi
    
    # Check PostHog SDK
    if python3 -c "import posthog" 2>/dev/null; then
        echo -e "  ${CHECKMARK} PostHog SDK available"
    elif python -c "import posthog" 2>/dev/null; then
        echo -e "  ${CHECKMARK} PostHog SDK available"
    else
        echo -e "  ${WARNING} PostHog SDK not installed (some features may be limited)"
    fi
    
    echo ""
    
    if [[ "$all_good" != true ]]; then
        echo -e "${CROSSMARK} ${RED}Prerequisites check failed${NC}"
        echo -e "${INFO} ${CYAN}Please fix the issues above before continuing${NC}"
        echo ""
        echo -e "${YELLOW}Quick fixes:${NC}"
        echo -e "  pip install genops[posthog]"
        echo -e "  export POSTHOG_API_KEY='phc_your_project_api_key'"
        echo -e "  export GENOPS_TEAM='your-team-name'"
        echo ""
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    else
        echo -e "${CHECKMARK} ${GREEN}Prerequisites check passed${NC}"
    fi
}

run_example() {
    local example_num=$1
    local example_name=$2
    local example_file=$3
    local description=$4
    local estimated_time=$5
    local difficulty=$6
    
    echo ""
    echo -e "${PURPLE}================================================================${NC}"
    echo -e "${WHITE}Example $example_num: $example_name${NC}"
    echo -e "${PURPLE}================================================================${NC}"
    echo -e "${CYAN}Description: $description${NC}"
    echo -e "${YELLOW}Difficulty: $difficulty | Estimated time: $estimated_time${NC}"
    echo -e "${BLUE}File: $example_file${NC}"
    echo ""
    
    # Log example start
    echo "Example $example_num: $example_name - Started $(date)" >> "$LOG_FILE"
    
    if [[ "$INTERACTIVE" == true ]]; then
        echo -e "${INFO} ${CYAN}Press ENTER to run this example, 's' to skip, or 'q' to quit${NC}"
        read -n 1 -r user_input
        echo
        
        case $user_input in
            s|S)
                echo -e "${WARNING} ${YELLOW}Skipping $example_name${NC}"
                echo "Example $example_num: $example_name - Skipped by user $(date)" >> "$LOG_FILE"
                return 0
                ;;
            q|Q)
                echo -e "${INFO} ${CYAN}Exiting examples runner${NC}"
                exit 0
                ;;
        esac
    fi
    
    echo -e "${ROCKET} ${GREEN}Running $example_name...${NC}"
    echo -e "${CLOCK} ${CYAN}Start time: $(date '+%H:%M:%S')${NC}"
    
    local start_time=$(date +%s)
    
    # Run the example
    if cd "$EXAMPLES_DIR" && python3 "$example_file" 2>&1 | tee -a "$LOG_FILE"; then
        local end_time=$(date +%s)
        local duration=$((end_time - start_time))
        local minutes=$((duration / 60))
        local seconds=$((duration % 60))
        
        echo ""
        echo -e "${CHECKMARK} ${GREEN}Example completed successfully${NC}"
        echo -e "${CLOCK} ${CYAN}Duration: ${minutes}m ${seconds}s${NC}"
        echo "Example $example_num: $example_name - Completed successfully in ${minutes}m ${seconds}s $(date)" >> "$LOG_FILE"
        
        return 0
    else
        local end_time=$(date +%s)
        local duration=$((end_time - start_time))
        local minutes=$((duration / 60))
        local seconds=$((duration % 60))
        
        echo ""
        echo -e "${CROSSMARK} ${RED}Example failed${NC}"
        echo -e "${CLOCK} ${CYAN}Duration: ${minutes}m ${seconds}s${NC}"
        echo "Example $example_num: $example_name - Failed after ${minutes}m ${seconds}s $(date)" >> "$LOG_FILE"
        
        if [[ "$CONTINUE_ON_ERROR" != true ]]; then
            echo ""
            echo -e "${WARNING} ${YELLOW}Example failed. What would you like to do?${NC}"
            echo -e "  c) Continue with next example"
            echo -e "  r) Retry this example"  
            echo -e "  q) Quit"
            echo -e "  a) Continue all (ignore future errors)"
            echo ""
            read -p "Choice (c/r/q/a): " -n 1 -r
            echo
            
            case $REPLY in
                r|R)
                    echo -e "${INFO} ${CYAN}Retrying $example_name${NC}"
                    run_example "$example_num" "$example_name" "$example_file" "$description" "$estimated_time" "$difficulty"
                    return $?
                    ;;
                q|Q)
                    echo -e "${INFO} ${CYAN}Exiting due to user request${NC}"
                    exit 1
                    ;;
                a|A)
                    echo -e "${INFO} ${CYAN}Continuing with all remaining examples${NC}"
                    CONTINUE_ON_ERROR=true
                    return 1
                    ;;
                *)
                    echo -e "${INFO} ${CYAN}Continuing with next example${NC}"
                    return 1
                    ;;
            esac
        else
            return 1
        fi
    fi
}

show_summary() {
    local total_examples=$1
    local successful_examples=$2
    local failed_examples=$3
    local skipped_examples=$4
    local total_duration=$5
    
    echo ""
    echo -e "${PURPLE}================================================================${NC}"
    echo -e "${WHITE}   📊 Examples Execution Summary${NC}"
    echo -e "${PURPLE}================================================================${NC}"
    echo ""
    echo -e "${CHART} ${CYAN}Execution Statistics:${NC}"
    echo -e "  Total examples: $total_examples"
    echo -e "  ${GREEN}Successful: $successful_examples${NC}"
    if [[ $failed_examples -gt 0 ]]; then
        echo -e "  ${RED}Failed: $failed_examples${NC}"
    fi
    if [[ $skipped_examples -gt 0 ]]; then
        echo -e "  ${YELLOW}Skipped: $skipped_examples${NC}"
    fi
    
    local minutes=$((total_duration / 60))
    local seconds=$((total_duration % 60))
    echo -e "  ${CLOCK} Total time: ${minutes}m ${seconds}s"
    
    local success_rate=$((successful_examples * 100 / total_examples))
    echo -e "  ${CHART} Success rate: ${success_rate}%"
    
    echo ""
    echo -e "${INFO} ${CYAN}Log file: $LOG_FILE${NC}"
    
    if [[ $successful_examples -eq $total_examples ]]; then
        echo ""
        echo -e "${CHECKMARK} ${GREEN}All examples completed successfully!${NC}"
        echo -e "${ROCKET} ${CYAN}You're ready to integrate PostHog + GenOps into your applications${NC}"
        echo ""
        echo -e "${YELLOW}Next steps:${NC}"
        echo -e "  1. Check the documentation: docs/integrations/posthog.md"
        echo -e "  2. Explore the cost intelligence guide"
        echo -e "  3. Set up production monitoring"
        echo -e "  4. Join our community: https://github.com/KoshiHQ/GenOps-AI/discussions"
    elif [[ $failed_examples -gt 0 ]]; then
        echo ""
        echo -e "${WARNING} ${YELLOW}Some examples failed. Common solutions:${NC}"
        echo -e "  1. Check your POSTHOG_API_KEY configuration"
        echo -e "  2. Ensure all dependencies are installed"
        echo -e "  3. Review the log file for detailed error information"
        echo -e "  4. Report issues: https://github.com/KoshiHQ/GenOps-AI/issues"
    fi
    
    echo ""
}

# Main execution
main() {
    show_banner
    
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --non-interactive|-n)
                INTERACTIVE=false
                shift
                ;;
            --continue-on-error|-c)
                CONTINUE_ON_ERROR=true
                shift
                ;;
            --help|-h)
                echo "Usage: $0 [options]"
                echo "Options:"
                echo "  --non-interactive, -n    Run all examples without user prompts"
                echo "  --continue-on-error, -c  Continue running examples even if some fail"
                echo "  --help, -h              Show this help message"
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                echo "Use --help for usage information"
                exit 1
                ;;
        esac
    done
    
    # Check prerequisites
    check_prerequisites
    
    echo ""
    echo -e "${ROCKET} ${GREEN}Starting PostHog + GenOps examples...${NC}"
    echo ""
    
    local total_examples=${#EXAMPLES[@]}
    local successful_examples=0
    local failed_examples=0
    local skipped_examples=0
    local start_time=$(date +%s)
    
    # Run each example
    for i in "${!EXAMPLES[@]}"; do
        local example_data="${EXAMPLES[$i]}"
        IFS='|' read -r example_file example_name description estimated_time difficulty <<< "$example_data"
        
        local example_num=$((i + 1))
        
        # Show overall progress
        show_progress $example_num $total_examples
        echo ""
        
        # Run the example
        if run_example "$example_num" "$example_name" "$example_file" "$description" "$estimated_time" "$difficulty"; then
            ((successful_examples++))
        else
            if [[ "$CONTINUE_ON_ERROR" == true ]] || [[ "${REPLY:-}" == "s" ]] || [[ "${REPLY:-}" == "S" ]]; then
                if [[ "${REPLY:-}" == "s" ]] || [[ "${REPLY:-}" == "S" ]]; then
                    ((skipped_examples++))
                else
                    ((failed_examples++))
                fi
            else
                ((failed_examples++))
            fi
        fi
        
        # Brief pause between examples (except for the last one)
        if [[ $example_num -lt $total_examples ]] && [[ "$INTERACTIVE" == true ]]; then
            echo ""
            echo -e "${INFO} ${CYAN}Preparing next example...${NC}"
            sleep 1
        fi
    done
    
    local end_time=$(date +%s)
    local total_duration=$((end_time - start_time))
    
    # Show final progress
    show_progress $total_examples $total_examples
    echo ""
    
    # Show summary
    show_summary "$total_examples" "$successful_examples" "$failed_examples" "$skipped_examples" "$total_duration"
    
    # Log summary
    echo "" >> "$LOG_FILE"
    echo "=========================================" >> "$LOG_FILE"
    echo "Examples run completed $(date)" >> "$LOG_FILE"
    echo "Total: $total_examples, Successful: $successful_examples, Failed: $failed_examples, Skipped: $skipped_examples" >> "$LOG_FILE"
    
    # Exit with appropriate code
    if [[ $failed_examples -eq 0 ]]; then
        exit 0
    else
        exit 1
    fi
}

# Handle script interruption
trap 'echo -e "\n${WARNING} ${YELLOW}Examples runner interrupted by user${NC}"; exit 130' INT

# Run main function with all arguments
main "$@"