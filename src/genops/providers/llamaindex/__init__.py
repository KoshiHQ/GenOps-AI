"""LlamaIndex provider for GenOps AI governance."""

from .adapter import (
    GenOpsLlamaIndexAdapter,
    GenOpsLlamaIndexCallback,
    LlamaIndexOperation,
    RAGPipelineMetrics,
    instrument_llamaindex,
    auto_instrument,
)
from .cost_aggregator import (
    LlamaIndexCostAggregator,
    create_llamaindex_cost_context,
    create_chain_cost_context,  # CLAUDE.md standard alias
    multi_provider_cost_tracking,  # CLAUDE.md standard function
    RAGCostBreakdown,
    LlamaIndexCostSummary,
    BudgetAlert,
    get_cost_aggregator,
    set_cost_aggregator,
)
from .rag_monitor import (
    LlamaIndexRAGInstrumentor,
    RAGOperationMonitor,
    RAGOperationSummary,
    RAGPipelineAnalytics,
    EmbeddingMetrics,
    RetrievalMetrics,
    SynthesisMetrics,
    get_rag_monitor,
    set_rag_monitor,
    create_rag_monitor,
)
from .registration import (
    register_llamaindex_provider,
    unregister_llamaindex_provider,
    get_registration_status,
    auto_register,
    patch_llamaindex,
    unpatch_llamaindex,
    get_adapter,
    get_cost_aggregator_instance,
    get_rag_monitor_instance,
    is_llamaindex_available,
    get_llamaindex_version,
    validate_llamaindex_setup,
)
from .validation import (
    validate_setup,
    print_validation_result,
    quick_validate,
    ValidationResult,
    ValidationIssue,
    LlamaIndexValidator,
)

# Auto-register with instrumentation system if available
auto_register()

__all__ = [
    # Main adapter classes
    "GenOpsLlamaIndexAdapter",
    "GenOpsLlamaIndexCallback",
    "LlamaIndexOperation", 
    "RAGPipelineMetrics",
    
    # Cost aggregation
    "LlamaIndexCostAggregator",
    "create_llamaindex_cost_context",
    "create_chain_cost_context",  # CLAUDE.md standard alias
    "multi_provider_cost_tracking",  # CLAUDE.md standard function
    "RAGCostBreakdown",
    "LlamaIndexCostSummary", 
    "BudgetAlert",
    "get_cost_aggregator",
    "set_cost_aggregator",
    
    # RAG monitoring
    "LlamaIndexRAGInstrumentor",
    "RAGOperationMonitor",
    "RAGOperationSummary",
    "RAGPipelineAnalytics",
    "EmbeddingMetrics",
    "RetrievalMetrics", 
    "SynthesisMetrics",
    "get_rag_monitor",
    "set_rag_monitor",
    "create_rag_monitor",
    
    # Registration and setup
    "register_llamaindex_provider",
    "unregister_llamaindex_provider",
    "get_registration_status",
    "auto_register",
    "patch_llamaindex",
    "unpatch_llamaindex", 
    "get_adapter",
    "get_cost_aggregator_instance",
    "get_rag_monitor_instance",
    "is_llamaindex_available",
    "get_llamaindex_version",
    "validate_llamaindex_setup",
    
    # Validation
    "validate_setup",
    "print_validation_result",
    "quick_validate",
    "ValidationResult",
    "ValidationIssue",
    "LlamaIndexValidator",
    
    # Main factory functions
    "instrument_llamaindex",
    "auto_instrument",
]