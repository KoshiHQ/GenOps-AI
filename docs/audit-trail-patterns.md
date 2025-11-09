# Audit Trail Architecture Patterns

This guide provides comprehensive patterns and best practices for implementing audit trails in GenOps provider integrations, focusing on immutability, integrity, and compliance requirements.

## 📋 Overview

Audit trails are critical for governance, compliance, and operational transparency. GenOps provides standardized patterns for implementing tamper-evident, immutable audit trails across all provider integrations.

## 🏗️ Architecture Patterns

### 1. Immutable Audit Log Pattern

**Core Requirements:**
- Cryptographically signed entries
- Tamper detection through hash chains
- Immutable storage with versioning
- Structured, searchable data format

```python
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from typing import Dict, Any, Optional

@dataclass
class AuditEntry:
    """Immutable audit entry with cryptographic integrity."""
    audit_id: str
    timestamp: str
    user_id: str
    action: str
    resource_type: str
    resource_id: str
    outcome: str  # success, failure, partial
    metadata: Dict[str, Any]
    parent_hash: Optional[str]  # Previous entry hash for chain integrity
    entry_hash: str  # This entry's hash
    signature: str  # Cryptographic signature
    
    def __post_init__(self):
        """Validate audit entry integrity."""
        expected_hash = self._calculate_hash()
        if self.entry_hash != expected_hash:
            raise AuditIntegrityError("Hash mismatch detected")
    
    def _calculate_hash(self) -> str:
        """Calculate SHA-256 hash of entry data."""
        data = {
            'audit_id': self.audit_id,
            'timestamp': self.timestamp,
            'user_id': self.user_id,
            'action': self.action,
            'resource_type': self.resource_type,
            'resource_id': self.resource_id,
            'outcome': self.outcome,
            'metadata': self.metadata,
            'parent_hash': self.parent_hash
        }
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
```

### 2. Chain of Custody Pattern

**Implementation:**
```python
class AuditChain:
    """Maintains chain of custody with hash linking."""
    
    def __init__(self):
        self.chain: List[AuditEntry] = []
        self.current_hash: Optional[str] = None
    
    def append_entry(self, entry_data: Dict[str, Any]) -> AuditEntry:
        """Add new entry to audit chain."""
        entry = AuditEntry(
            audit_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc).isoformat(),
            parent_hash=self.current_hash,
            entry_hash="",  # Will be calculated
            signature="",  # Will be signed
            **entry_data
        )
        
        # Calculate hash and signature
        entry.entry_hash = entry._calculate_hash()
        entry.signature = self._sign_entry(entry)
        
        # Validate chain integrity
        self._validate_chain_integrity(entry)
        
        self.chain.append(entry)
        self.current_hash = entry.entry_hash
        
        return entry
    
    def _validate_chain_integrity(self, new_entry: AuditEntry) -> bool:
        """Validate new entry maintains chain integrity."""
        if len(self.chain) == 0:
            return new_entry.parent_hash is None
        
        last_entry = self.chain[-1]
        return new_entry.parent_hash == last_entry.entry_hash
```

### 3. Distributed Audit Storage Pattern

**Multi-Location Storage:**
```python
class DistributedAuditStorage:
    """Store audit entries across multiple locations for redundancy."""
    
    def __init__(self, storage_backends: List[AuditStorageBackend]):
        self.backends = storage_backends
        self.quorum_size = len(storage_backends) // 2 + 1
    
    async def store_entry(self, entry: AuditEntry) -> bool:
        """Store entry across multiple backends with quorum consensus."""
        storage_tasks = [
            backend.store(entry) for backend in self.backends
        ]
        
        results = await asyncio.gather(*storage_tasks, return_exceptions=True)
        successful_stores = sum(1 for result in results if result is True)
        
        if successful_stores >= self.quorum_size:
            self._log_success(entry, successful_stores)
            return True
        else:
            self._handle_storage_failure(entry, results)
            return False
```

### 4. Event Sourcing Pattern

**Audit as Event Store:**
```python
class EventSourcedAudit:
    """Implement audit trail using event sourcing principles."""
    
    def __init__(self):
        self.events: List[AuditEvent] = []
        self.snapshots: Dict[str, Any] = {}
    
    def append_event(self, event_type: str, event_data: Dict[str, Any]):
        """Append new audit event to stream."""
        event = AuditEvent(
            event_id=str(uuid.uuid4()),
            event_type=event_type,
            event_data=event_data,
            timestamp=datetime.now(timezone.utc),
            sequence_number=len(self.events) + 1
        )
        
        self.events.append(event)
        self._update_projections(event)
    
    def reconstruct_state(self, resource_id: str) -> Dict[str, Any]:
        """Reconstruct current state from audit events."""
        relevant_events = [
            event for event in self.events 
            if event.event_data.get('resource_id') == resource_id
        ]
        
        state = {}
        for event in relevant_events:
            state = self._apply_event(state, event)
        
        return state
```

## 🔒 Security Patterns

### 1. Cryptographic Signing

**Digital Signatures:**
```python
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class AuditSigner:
    """Sign audit entries with private key for non-repudiation."""
    
    def __init__(self, private_key_path: str):
        with open(private_key_path, 'rb') as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(), password=None
            )
    
    def sign_entry(self, entry: AuditEntry) -> str:
        """Sign audit entry with private key."""
        message = f"{entry.audit_id}:{entry.timestamp}:{entry.entry_hash}".encode()
        
        signature = self.private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return base64.b64encode(signature).decode()
    
    def verify_signature(self, entry: AuditEntry, public_key) -> bool:
        """Verify audit entry signature."""
        message = f"{entry.audit_id}:{entry.timestamp}:{entry.entry_hash}".encode()
        signature = base64.b64decode(entry.signature.encode())
        
        try:
            public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
```

### 2. Encryption at Rest

**Encrypted Storage:**
```python
from cryptography.fernet import Fernet

class EncryptedAuditStorage:
    """Encrypt audit entries before storage."""
    
    def __init__(self, encryption_key: bytes):
        self.cipher_suite = Fernet(encryption_key)
    
    def store_encrypted(self, entry: AuditEntry) -> str:
        """Encrypt and store audit entry."""
        serialized_entry = json.dumps(asdict(entry))
        encrypted_data = self.cipher_suite.encrypt(serialized_entry.encode())
        
        # Store with metadata for retrieval
        storage_record = {
            'audit_id': entry.audit_id,
            'encrypted_data': base64.b64encode(encrypted_data).decode(),
            'encryption_algorithm': 'Fernet',
            'created_at': entry.timestamp
        }
        
        return self._store_to_backend(storage_record)
    
    def retrieve_decrypted(self, audit_id: str) -> AuditEntry:
        """Retrieve and decrypt audit entry."""
        storage_record = self._retrieve_from_backend(audit_id)
        encrypted_data = base64.b64decode(storage_record['encrypted_data'])
        
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        entry_dict = json.loads(decrypted_data.decode())
        
        return AuditEntry(**entry_dict)
```

## 📊 Query Patterns

### 1. Time-Range Queries

**Efficient Time-Based Retrieval:**
```python
class AuditQueryEngine:
    """Efficient querying of audit trails."""
    
    def __init__(self, storage: AuditStorage):
        self.storage = storage
        self._create_time_index()
    
    def query_time_range(
        self, 
        start_time: datetime, 
        end_time: datetime,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[AuditEntry]:
        """Query audit entries within time range."""
        
        # Use time index for efficient retrieval
        candidate_entries = self.storage.get_entries_by_time_range(
            start_time, end_time
        )
        
        # Apply additional filters
        if filters:
            candidate_entries = self._apply_filters(candidate_entries, filters)
        
        return candidate_entries
    
    def _apply_filters(self, entries: List[AuditEntry], filters: Dict[str, Any]) -> List[AuditEntry]:
        """Apply additional filters to entry list."""
        filtered_entries = entries
        
        for field, value in filters.items():
            if isinstance(value, list):
                filtered_entries = [
                    entry for entry in filtered_entries 
                    if getattr(entry, field, None) in value
                ]
            else:
                filtered_entries = [
                    entry for entry in filtered_entries 
                    if getattr(entry, field, None) == value
                ]
        
        return filtered_entries
```

### 2. Compliance Reporting Queries

**Regulatory Report Generation:**
```python
class ComplianceReportGenerator:
    """Generate compliance reports from audit trails."""
    
    def __init__(self, query_engine: AuditQueryEngine):
        self.query_engine = query_engine
    
    def generate_sox_report(self, fiscal_period: str) -> Dict[str, Any]:
        """Generate SOX compliance report."""
        start_date, end_date = self._parse_fiscal_period(fiscal_period)
        
        financial_entries = self.query_engine.query_time_range(
            start_date, end_date,
            filters={'resource_type': ['financial_transaction', 'revenue_entry']}
        )
        
        return {
            'reporting_period': fiscal_period,
            'total_transactions': len(financial_entries),
            'transaction_summary': self._summarize_transactions(financial_entries),
            'control_testing': self._perform_control_testing(financial_entries),
            'exceptions': self._identify_exceptions(financial_entries),
            'attestation': self._generate_management_attestation()
        }
    
    def generate_gdpr_report(self, data_subject_id: str) -> Dict[str, Any]:
        """Generate GDPR data subject report."""
        subject_entries = self.query_engine.query_time_range(
            datetime.now(timezone.utc) - timedelta(years=3),
            datetime.now(timezone.utc),
            filters={'metadata.data_subject_id': [data_subject_id]}
        )
        
        return {
            'data_subject_id': data_subject_id,
            'processing_activities': self._categorize_processing(subject_entries),
            'lawful_basis': self._analyze_lawful_basis(subject_entries),
            'data_categories': self._extract_data_categories(subject_entries),
            'retention_analysis': self._analyze_retention(subject_entries),
            'rights_exercised': self._track_rights_requests(subject_entries)
        }
```

## 🔧 Integration Patterns

### 1. Provider Integration

**GenOps Provider Audit Integration:**
```python
class AuditableProviderAdapter:
    """Base class for providers with audit trail integration."""
    
    def __init__(self, audit_chain: AuditChain, **kwargs):
        self.audit_chain = audit_chain
        self.provider_config = kwargs
    
    def _audit_operation(
        self, 
        operation: str, 
        resource_type: str, 
        resource_id: str,
        metadata: Dict[str, Any],
        outcome: str = "success"
    ):
        """Audit any provider operation."""
        self.audit_chain.append_entry({
            'user_id': self._get_current_user(),
            'action': operation,
            'resource_type': resource_type,
            'resource_id': resource_id,
            'outcome': outcome,
            'metadata': {
                **metadata,
                'provider': self.__class__.__name__,
                'provider_config': self.provider_config,
                'operation_context': self._get_operation_context()
            }
        })
    
    def _get_operation_context(self) -> Dict[str, Any]:
        """Get current operation context for audit."""
        return {
            'session_id': getattr(self, 'session_id', None),
            'request_id': getattr(self, 'request_id', None),
            'user_agent': getattr(self, 'user_agent', None),
            'ip_address': getattr(self, 'ip_address', None)
        }
```

### 2. Compliance Framework Integration

**Framework-Specific Audit Requirements:**
```python
class ComplianceAuditAdapter:
    """Adapt audit trails for specific compliance frameworks."""
    
    def __init__(self, framework: str, audit_chain: AuditChain):
        self.framework = framework
        self.audit_chain = audit_chain
        self.requirements = self._load_framework_requirements(framework)
    
    def audit_with_compliance(
        self, 
        operation_data: Dict[str, Any],
        compliance_metadata: Dict[str, Any]
    ):
        """Audit operation with framework-specific requirements."""
        
        # Enhance with compliance-specific data
        enhanced_metadata = {
            **operation_data.get('metadata', {}),
            **compliance_metadata,
            'compliance_framework': self.framework,
            'regulatory_scope': self.requirements.get('scope', []),
            'retention_period': self.requirements.get('retention_period'),
            'data_classification': self._classify_data(operation_data)
        }
        
        # Ensure required fields are present
        self._validate_required_fields(enhanced_metadata)
        
        # Create audit entry
        self.audit_chain.append_entry({
            **operation_data,
            'metadata': enhanced_metadata
        })
    
    def _classify_data(self, operation_data: Dict[str, Any]) -> str:
        """Classify data based on compliance framework."""
        data_types = operation_data.get('data_types', [])
        
        if self.framework == 'sox':
            if any(dt in ['financial', 'revenue', 'expense'] for dt in data_types):
                return 'financial_material'
            return 'financial_supporting'
        
        elif self.framework == 'gdpr':
            if any(dt in ['personal', 'sensitive'] for dt in data_types):
                return 'personal_data'
            return 'non_personal'
        
        return 'unclassified'
```

## 📈 Performance Patterns

### 1. Asynchronous Audit Writing

**Non-Blocking Audit Operations:**
```python
import asyncio
from asyncio import Queue

class AsyncAuditWriter:
    """Asynchronous audit trail writer for high-performance applications."""
    
    def __init__(self, storage: AuditStorage, batch_size: int = 100):
        self.storage = storage
        self.batch_size = batch_size
        self.entry_queue: Queue = Queue(maxsize=10000)
        self.running = False
    
    async def start(self):
        """Start async audit writing."""
        self.running = True
        asyncio.create_task(self._batch_writer())
    
    async def audit_async(self, entry_data: Dict[str, Any]):
        """Queue audit entry for async writing."""
        await self.entry_queue.put(entry_data)
    
    async def _batch_writer(self):
        """Batch writer coroutine."""
        batch = []
        
        while self.running or not self.entry_queue.empty():
            try:
                # Collect batch
                while len(batch) < self.batch_size:
                    entry_data = await asyncio.wait_for(
                        self.entry_queue.get(), timeout=1.0
                    )
                    batch.append(entry_data)
                
                # Write batch
                await self._write_batch(batch)
                batch.clear()
                
            except asyncio.TimeoutError:
                # Write partial batch on timeout
                if batch:
                    await self._write_batch(batch)
                    batch.clear()
            
            except Exception as e:
                logger.error(f"Batch writing error: {e}")
    
    async def _write_batch(self, entries: List[Dict[str, Any]]):
        """Write batch of entries to storage."""
        try:
            await self.storage.store_batch([
                self._create_entry(entry_data) 
                for entry_data in entries
            ])
        except Exception as e:
            # Handle batch write failure
            await self._handle_batch_failure(entries, e)
```

### 2. Audit Compression and Archival

**Long-Term Storage Optimization:**
```python
class AuditArchiver:
    """Compress and archive old audit entries."""
    
    def __init__(self, storage: AuditStorage, archive_storage: ArchiveStorage):
        self.storage = storage
        self.archive_storage = archive_storage
    
    async def archive_old_entries(self, older_than_days: int = 365):
        """Archive audit entries older than specified days."""
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=older_than_days)
        
        # Get entries to archive
        old_entries = await self.storage.get_entries_before(cutoff_date)
        
        # Compress entries
        compressed_data = self._compress_entries(old_entries)
        
        # Store in archive
        archive_id = await self.archive_storage.store_compressed(
            compressed_data,
            metadata={
                'entry_count': len(old_entries),
                'date_range': f"{old_entries[0].timestamp} to {old_entries[-1].timestamp}",
                'compression_ratio': len(compressed_data) / self._calculate_raw_size(old_entries)
            }
        )
        
        # Remove from active storage
        await self.storage.delete_entries([entry.audit_id for entry in old_entries])
        
        return archive_id
```

## 📚 Implementation Examples

### PostHog Integration Example

```python
from genops.providers.posthog import GenOpsPostHogAdapter

# PostHog adapter with audit trail
adapter = GenOpsPostHogAdapter(
    audit_trail_enabled=True,
    audit_framework="gdpr",
    immutable_logging=True
)

# Operations are automatically audited
with adapter.track_analytics_session("user_onboarding") as session:
    # This event capture is automatically audited
    result = adapter.capture_event_with_governance(
        event_name="signup_completed",
        properties={"plan": "premium"},
        distinct_id="user_123"
    )
    # Audit entry created automatically with:
    # - Event details and governance metadata
    # - Cost and attribution information  
    # - GDPR compliance data
    # - Immutable hash and signature
```

## 🎯 Best Practices

### 1. Audit Trail Design

**Essential Principles:**
- **Immutability**: Once written, entries cannot be modified
- **Integrity**: Cryptographic hashes and signatures prevent tampering
- **Completeness**: All relevant operations are audited
- **Availability**: Audit data is accessible when needed
- **Retention**: Appropriate retention policies for compliance

### 2. Performance Considerations

**Optimization Strategies:**
- Use asynchronous writing to avoid blocking operations
- Implement batch writing for high-volume scenarios
- Create appropriate indexes for common query patterns
- Archive old entries to maintain performance
- Use compression for long-term storage

### 3. Security Best Practices

**Security Measures:**
- Encrypt audit data at rest and in transit
- Use strong cryptographic signatures for integrity
- Implement proper access controls for audit data
- Separate audit storage from application storage
- Regular integrity verification and monitoring

## 🔍 Monitoring and Alerting

### Audit Trail Health

Monitor audit trail health with these metrics:

```python
audit_health_metrics = {
    "entries_per_second": monitor_write_rate(),
    "chain_integrity_status": verify_chain_integrity(),
    "storage_health": check_storage_backends(),
    "signature_verification_rate": verify_signatures(),
    "failed_writes": count_failed_writes(),
    "archive_storage_utilization": check_archive_usage()
}
```

### Compliance Monitoring

```python
compliance_metrics = {
    "retention_compliance": check_retention_policies(),
    "data_classification_coverage": verify_data_classification(),
    "access_control_violations": count_unauthorized_access(),
    "regulatory_reporting_status": check_report_generation()
}
```

---

This audit trail architecture provides the foundation for robust, compliant, and performant audit capabilities across all GenOps provider integrations.