# Security Best Practices for GenOps AI

This document outlines comprehensive security best practices for deploying and operating GenOps AI governance systems in production environments.

## Overview

GenOps AI handles sensitive data including:
- **AI Provider API Keys** - Access credentials for OpenAI, Anthropic, Google, etc.
- **Customer Data** - Queries, responses, and usage patterns
- **Cost Information** - Detailed spending and budget data  
- **Compliance Data** - Audit trails and governance records
- **Telemetry Data** - Performance and operational metrics

Securing this data requires a multi-layered approach covering authentication, authorization, data protection, compliance, and operational security.

## 1. API Key Management

### Secure Storage

```python
# ❌ NEVER store API keys in code
OPENAI_API_KEY = "sk-proj-abc123..."  # NEVER DO THIS

# ✅ Use environment variables
import os
openai_key = os.getenv("OPENAI_API_KEY")

# ✅ Use secure secret management services
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_api_key_from_vault(secret_name: str) -> str:
    """Retrieve API key from Azure Key Vault."""
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url="https://genops-vault.vault.azure.net/", credential=credential)
    secret = client.get_secret(secret_name)
    return secret.value

# ✅ Use AWS Secrets Manager
import boto3

def get_api_key_from_aws_secrets(secret_name: str) -> str:
    """Retrieve API key from AWS Secrets Manager."""
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']
```

### Key Rotation

```python
# Implement automatic API key rotation
class APIKeyManager:
    def __init__(self, secret_manager):
        self.secret_manager = secret_manager
        self.key_cache = {}
        self.key_expiry = {}
    
    def get_api_key(self, provider: str) -> str:
        """Get API key with automatic rotation."""
        current_time = time.time()
        
        # Check if key needs rotation (every 30 days)
        if (provider not in self.key_expiry or 
            current_time > self.key_expiry[provider]):
            
            # Fetch fresh key from secret manager
            key = self.secret_manager.get_secret(f"{provider}_api_key")
            self.key_cache[provider] = key
            self.key_expiry[provider] = current_time + (30 * 24 * 3600)  # 30 days
        
        return self.key_cache[provider]
    
    def rotate_key(self, provider: str, new_key: str):
        """Rotate API key with zero-downtime."""
        # Update in secret manager
        self.secret_manager.update_secret(f"{provider}_api_key", new_key)
        
        # Clear cache to force refresh
        if provider in self.key_cache:
            del self.key_cache[provider]
        if provider in self.key_expiry:
            del self.key_expiry[provider]
```

### Kubernetes Secret Management

```yaml
# genops-secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: genops-ai-secrets
  namespace: ai-production
type: Opaque
data:
  openai-api-key: <base64-encoded-key>
  anthropic-api-key: <base64-encoded-key>
  google-api-key: <base64-encoded-key>

---
# Use External Secrets Operator for automated secret sync
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: azure-keyvault-store
  namespace: ai-production
spec:
  provider:
    azurekv:
      vaultUrl: "https://genops-vault.vault.azure.net/"
      authSecretRef:
        clientId:
          name: azure-secret-sp
          key: ClientID
        clientSecret:
          name: azure-secret-sp  
          key: ClientSecret
      tenantId: "tenant-id-here"

---
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: genops-external-secrets
  namespace: ai-production
spec:
  refreshInterval: 15m
  secretStoreRef:
    name: azure-keyvault-store
    kind: SecretStore
  target:
    name: genops-ai-secrets
  data:
  - secretKey: openai-api-key
    remoteRef:
      key: openai-api-key
  - secretKey: anthropic-api-key
    remoteRef:
      key: anthropic-api-key
```

## 2. Data Protection and Privacy

### PII Detection and Redaction

```python
import re
from typing import Dict, Any, Optional

class PIIDetector:
    """Detect and redact personally identifiable information."""
    
    def __init__(self):
        self.patterns = {
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'phone': re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'),
            'ssn': re.compile(r'\b\d{3}-?\d{2}-?\d{4}\b'),
            'credit_card': re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'),
            'ip_address': re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
        }
    
    def detect_pii(self, text: str) -> Dict[str, list]:
        """Detect PII in text and return findings."""
        findings = {}
        
        for pii_type, pattern in self.patterns.items():
            matches = pattern.findall(text)
            if matches:
                findings[pii_type] = matches
        
        return findings
    
    def redact_pii(self, text: str, replacement: str = "[REDACTED]") -> str:
        """Redact PII from text."""
        redacted_text = text
        
        for pattern in self.patterns.values():
            redacted_text = pattern.sub(replacement, redacted_text)
        
        return redacted_text

# Integration with GenOps
class SecureGenOpsAdapter:
    def __init__(self, enable_pii_detection: bool = True):
        self.pii_detector = PIIDetector() if enable_pii_detection else None
        self.adapter = instrument_llamaindex()
    
    def secure_track_query(self, query_engine, query: str, **kwargs):
        """Track query with PII detection and redaction."""
        
        # Detect PII in query
        if self.pii_detector:
            pii_findings = self.pii_detector.detect_pii(query)
            
            if pii_findings:
                logger.warning(f"PII detected in query: {list(pii_findings.keys())}")
                
                # Redact PII for logging/telemetry
                safe_query = self.pii_detector.redact_pii(query)
                kwargs['pii_detected'] = True
                kwargs['pii_types'] = list(pii_findings.keys())
            else:
                safe_query = query
                kwargs['pii_detected'] = False
        else:
            safe_query = query
        
        # Execute query with redacted version for telemetry
        response = self.adapter.track_query(
            query_engine, 
            query,  # Original query for processing
            telemetry_query=safe_query,  # Redacted for telemetry
            **kwargs
        )
        
        # Redact PII from response if needed
        if self.pii_detector and hasattr(response, 'response'):
            response.response = self.pii_detector.redact_pii(response.response)
        
        return response
```

### Data Encryption

```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

class DataEncryption:
    """Encrypt sensitive data at rest."""
    
    def __init__(self, password: Optional[str] = None):
        if password is None:
            password = os.getenv('GENOPS_ENCRYPTION_KEY')
            if not password:
                raise ValueError("Encryption password must be provided")
        
        # Derive key from password
        salt = os.getenv('GENOPS_ENCRYPTION_SALT', 'genops-default-salt').encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        self.fernet = Fernet(key)
    
    def encrypt(self, data: str) -> str:
        """Encrypt string data."""
        return self.fernet.encrypt(data.encode()).decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        """Decrypt string data."""
        return self.fernet.decrypt(encrypted_data.encode()).decode()
    
    def encrypt_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Encrypt dictionary values."""
        encrypted = {}
        for key, value in data.items():
            if isinstance(value, str) and self._should_encrypt(key):
                encrypted[key] = self.encrypt(value)
            else:
                encrypted[key] = value
        return encrypted
    
    def _should_encrypt(self, key: str) -> bool:
        """Determine if field should be encrypted."""
        sensitive_fields = {
            'query', 'response', 'api_key', 'customer_id', 
            'email', 'user_data', 'personal_info'
        }
        return any(field in key.lower() for field in sensitive_fields)

# Usage in cost aggregator
class SecureCostAggregator(LlamaIndexCostAggregator):
    def __init__(self, *args, enable_encryption: bool = True, **kwargs):
        super().__init__(*args, **kwargs)
        self.encryption = DataEncryption() if enable_encryption else None
    
    def add_llamaindex_operation(self, operation_data: Dict[str, Any]) -> str:
        """Add operation with encryption of sensitive data."""
        
        if self.encryption:
            # Encrypt sensitive fields
            operation_data = self.encryption.encrypt_dict(operation_data)
        
        return super().add_llamaindex_operation(operation_data)
```

## 3. Access Control and Authentication

### Role-Based Access Control (RBAC)

```python
from enum import Enum
from dataclasses import dataclass
from typing import Set, Optional, Dict, Any
import jwt
import time

class Role(Enum):
    ADMIN = "admin"
    DEVELOPER = "developer" 
    ANALYST = "analyst"
    VIEWER = "viewer"

class Permission(Enum):
    READ_COSTS = "read_costs"
    WRITE_COSTS = "write_costs"
    READ_QUERIES = "read_queries"
    WRITE_QUERIES = "write_queries"
    ADMIN_SETTINGS = "admin_settings"
    EXPORT_DATA = "export_data"

@dataclass
class User:
    user_id: str
    email: str
    roles: Set[Role]
    team: str
    permissions: Set[Permission]
    
    def has_permission(self, permission: Permission) -> bool:
        return permission in self.permissions
    
    def can_access_team_data(self, team: str) -> bool:
        return self.team == team or Role.ADMIN in self.roles

class RBACManager:
    """Role-Based Access Control for GenOps operations."""
    
    def __init__(self, jwt_secret: str):
        self.jwt_secret = jwt_secret
        self.role_permissions = {
            Role.ADMIN: {
                Permission.READ_COSTS, Permission.WRITE_COSTS,
                Permission.READ_QUERIES, Permission.WRITE_QUERIES,
                Permission.ADMIN_SETTINGS, Permission.EXPORT_DATA
            },
            Role.DEVELOPER: {
                Permission.READ_COSTS, Permission.WRITE_COSTS,
                Permission.READ_QUERIES, Permission.WRITE_QUERIES
            },
            Role.ANALYST: {
                Permission.READ_COSTS, Permission.READ_QUERIES,
                Permission.EXPORT_DATA
            },
            Role.VIEWER: {
                Permission.READ_COSTS, Permission.READ_QUERIES
            }
        }
    
    def authenticate_user(self, token: str) -> Optional[User]:
        """Authenticate user from JWT token."""
        try:
            payload = jwt.decode(token, self.jwt_secret, algorithms=['HS256'])
            
            # Check token expiration
            if payload.get('exp', 0) < time.time():
                return None
            
            # Extract user information
            roles = {Role(role) for role in payload.get('roles', [])}
            permissions = set()
            
            # Aggregate permissions from roles
            for role in roles:
                permissions.update(self.role_permissions.get(role, set()))
            
            return User(
                user_id=payload['user_id'],
                email=payload['email'],
                roles=roles,
                team=payload.get('team', 'default'),
                permissions=permissions
            )
            
        except jwt.InvalidTokenError:
            return None
    
    def authorize_operation(self, user: User, operation: str, resource: Dict[str, Any]) -> bool:
        """Authorize user for specific operation on resource."""
        
        # Check basic permissions
        required_permission = {
            'query': Permission.WRITE_QUERIES,
            'view_costs': Permission.READ_COSTS,
            'export_data': Permission.EXPORT_DATA,
            'admin': Permission.ADMIN_SETTINGS
        }.get(operation)
        
        if required_permission and not user.has_permission(required_permission):
            return False
        
        # Check team-based access
        resource_team = resource.get('team')
        if resource_team and not user.can_access_team_data(resource_team):
            return False
        
        return True

# Secure adapter with RBAC
class SecureGenOpsAdapter:
    def __init__(self, jwt_secret: str):
        self.rbac = RBACManager(jwt_secret)
        self.adapter = instrument_llamaindex()
    
    def secure_track_query(self, token: str, query_engine, query: str, **kwargs):
        """Track query with authentication and authorization."""
        
        # Authenticate user
        user = self.rbac.authenticate_user(token)
        if not user:
            raise PermissionError("Authentication failed")
        
        # Authorize operation
        if not self.rbac.authorize_operation(user, 'query', kwargs):
            raise PermissionError("Insufficient permissions")
        
        # Add user context to governance attributes
        kwargs.update({
            'user_id': user.user_id,
            'user_email': user.email,
            'user_team': user.team,
            'user_roles': [role.value for role in user.roles]
        })
        
        # Execute query with user context
        return self.adapter.track_query(query_engine, query, **kwargs)
```

### API Authentication

```python
from functools import wraps
from flask import Flask, request, jsonify
import hmac
import hashlib

class APIAuthenticator:
    """API request authentication and rate limiting."""
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.rate_limits = {}  # Simple in-memory rate limiting
    
    def generate_signature(self, payload: str, timestamp: str) -> str:
        """Generate HMAC signature for request validation."""
        message = f"{timestamp}.{payload}"
        return hmac.new(
            self.secret_key.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
    
    def validate_signature(self, payload: str, timestamp: str, signature: str) -> bool:
        """Validate request signature."""
        expected_signature = self.generate_signature(payload, timestamp)
        return hmac.compare_digest(signature, expected_signature)
    
    def check_rate_limit(self, client_id: str, limit: int = 100, window: int = 3600) -> bool:
        """Check if client is within rate limits."""
        current_time = time.time()
        window_start = current_time - window
        
        if client_id not in self.rate_limits:
            self.rate_limits[client_id] = []
        
        # Clean old requests
        self.rate_limits[client_id] = [
            req_time for req_time in self.rate_limits[client_id] 
            if req_time > window_start
        ]
        
        # Check current count
        if len(self.rate_limits[client_id]) >= limit:
            return False
        
        # Add current request
        self.rate_limits[client_id].append(current_time)
        return True

def require_auth(f):
    """Decorator for API endpoint authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get authentication headers
        signature = request.headers.get('X-GenOps-Signature')
        timestamp = request.headers.get('X-GenOps-Timestamp')
        client_id = request.headers.get('X-GenOps-Client-ID')
        
        if not all([signature, timestamp, client_id]):
            return jsonify({'error': 'Missing authentication headers'}), 401
        
        # Validate timestamp (prevent replay attacks)
        if abs(time.time() - float(timestamp)) > 300:  # 5 minutes
            return jsonify({'error': 'Request timestamp too old'}), 401
        
        # Validate signature
        payload = request.get_data(as_text=True)
        if not authenticator.validate_signature(payload, timestamp, signature):
            return jsonify({'error': 'Invalid signature'}), 401
        
        # Check rate limits
        if not authenticator.check_rate_limit(client_id):
            return jsonify({'error': 'Rate limit exceeded'}), 429
        
        return f(*args, **kwargs)
    return decorated_function

# Flask API with authentication
app = Flask(__name__)
authenticator = APIAuthenticator(os.getenv('GENOPS_API_SECRET'))

@app.route('/api/query', methods=['POST'])
@require_auth
def secure_query_endpoint():
    """Secure API endpoint for AI queries."""
    try:
        data = request.get_json()
        query = data.get('query')
        
        if not query:
            return jsonify({'error': 'Query is required'}), 400
        
        # Execute secure query
        adapter = SecureGenOpsAdapter(os.getenv('JWT_SECRET'))
        result = adapter.secure_track_query(
            token=request.headers.get('Authorization', '').replace('Bearer ', ''),
            query_engine=get_query_engine(),
            query=query,
            **data.get('governance_attrs', {})
        )
        
        return jsonify({
            'response': result.response,
            'cost': getattr(result, 'cost', None),
            'latency': getattr(result, 'latency', None)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

## 4. Compliance and Audit

### GDPR Compliance

```python
class GDPRCompliantCostAggregator(LlamaIndexCostAggregator):
    """GDPR-compliant cost aggregator with data subject rights."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_retention_days = kwargs.get('data_retention_days', 30)
        self.anonymization_enabled = kwargs.get('anonymization_enabled', True)
    
    def anonymize_user_data(self, operation_data: Dict[str, Any]) -> Dict[str, Any]:
        """Anonymize user data to comply with GDPR."""
        if not self.anonymization_enabled:
            return operation_data
        
        # Replace user identifiers with anonymous IDs
        if 'user_id' in operation_data:
            operation_data['user_id'] = hashlib.sha256(
                operation_data['user_id'].encode()
            ).hexdigest()[:16]
        
        if 'email' in operation_data:
            operation_data['email'] = f"user-{operation_data['user_id'][:8]}@anonymous.local"
        
        # Remove or hash other PII
        pii_fields = ['name', 'phone', 'address', 'ip_address']
        for field in pii_fields:
            if field in operation_data:
                del operation_data[field]
        
        operation_data['gdpr_anonymized'] = True
        return operation_data
    
    def exercise_right_to_be_forgotten(self, user_id: str) -> Dict[str, Any]:
        """Implement GDPR right to be forgotten."""
        deleted_operations = []
        
        # Find and remove all operations for user
        self.operations = [
            op for op in self.operations 
            if op.get('user_id') != user_id
        ]
        
        # Log deletion for audit
        deletion_record = {
            'timestamp': time.time(),
            'action': 'right_to_be_forgotten',
            'user_id': user_id,
            'operations_deleted': len(deleted_operations)
        }
        
        return deletion_record
    
    def export_user_data(self, user_id: str) -> Dict[str, Any]:
        """Export user data for GDPR data portability."""
        user_operations = [
            op for op in self.operations 
            if op.get('user_id') == user_id
        ]
        
        export_data = {
            'user_id': user_id,
            'export_timestamp': time.time(),
            'operations': user_operations,
            'total_operations': len(user_operations),
            'total_cost': sum(op.get('cost_usd', 0) for op in user_operations),
            'data_retention_days': self.data_retention_days
        }
        
        return export_data
    
    def auto_delete_expired_data(self):
        """Automatically delete data past retention period."""
        cutoff_time = time.time() - (self.data_retention_days * 24 * 3600)
        
        original_count = len(self.operations)
        self.operations = [
            op for op in self.operations 
            if op.get('start_time', time.time()) > cutoff_time
        ]
        
        deleted_count = original_count - len(self.operations)
        
        if deleted_count > 0:
            logger.info(f"Auto-deleted {deleted_count} operations past retention period")
        
        return deleted_count
```

### SOC 2 Compliance

```python
class SOC2AuditLogger:
    """SOC 2 compliant audit logging."""
    
    def __init__(self, audit_log_path: str = "/var/log/genops/audit.log"):
        self.audit_log_path = audit_log_path
        self.logger = logging.getLogger('genops.audit')
        
        # Configure audit logger
        handler = logging.FileHandler(audit_log_path)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    def log_access_attempt(self, user_id: str, resource: str, action: str, 
                          success: bool, ip_address: str = None):
        """Log user access attempts."""
        self.logger.info(json.dumps({
            'event_type': 'access_attempt',
            'user_id': user_id,
            'resource': resource,
            'action': action,
            'success': success,
            'ip_address': ip_address,
            'timestamp': time.time()
        }))
    
    def log_data_modification(self, user_id: str, resource_type: str, 
                            resource_id: str, action: str, changes: Dict[str, Any]):
        """Log data modifications for SOC 2 audit trails."""
        self.logger.info(json.dumps({
            'event_type': 'data_modification',
            'user_id': user_id,
            'resource_type': resource_type,
            'resource_id': resource_id,
            'action': action,
            'changes': changes,
            'timestamp': time.time()
        }))
    
    def log_system_event(self, event_type: str, description: str, 
                        severity: str = 'info', metadata: Dict[str, Any] = None):
        """Log system events for operational monitoring."""
        log_level = getattr(logging, severity.upper(), logging.INFO)
        self.logger.log(log_level, json.dumps({
            'event_type': 'system_event',
            'system_event_type': event_type,
            'description': description,
            'severity': severity,
            'metadata': metadata or {},
            'timestamp': time.time()
        }))

# Integration with GenOps adapter
class SOC2CompliantAdapter:
    def __init__(self):
        self.audit_logger = SOC2AuditLogger()
        self.adapter = instrument_llamaindex()
    
    def track_query_with_audit(self, user_id: str, query_engine, query: str, **kwargs):
        """Track query with SOC 2 audit logging."""
        
        # Log access attempt
        self.audit_logger.log_access_attempt(
            user_id=user_id,
            resource='ai_query_engine',
            action='query_execution',
            success=True,  # Will be updated if it fails
            ip_address=kwargs.get('client_ip')
        )
        
        try:
            result = self.adapter.track_query(query_engine, query, user_id=user_id, **kwargs)
            
            # Log successful query
            self.audit_logger.log_system_event(
                event_type='ai_query_executed',
                description=f'AI query executed successfully',
                metadata={
                    'user_id': user_id,
                    'query_length': len(query),
                    'cost': getattr(result, 'cost', None),
                    'latency': getattr(result, 'latency', None)
                }
            )
            
            return result
            
        except Exception as e:
            # Log failed access attempt
            self.audit_logger.log_access_attempt(
                user_id=user_id,
                resource='ai_query_engine',
                action='query_execution',
                success=False,
                ip_address=kwargs.get('client_ip')
            )
            
            self.audit_logger.log_system_event(
                event_type='ai_query_failed',
                description=f'AI query execution failed: {str(e)}',
                severity='error',
                metadata={'user_id': user_id, 'error': str(e)}
            )
            
            raise
```

## 5. Network Security

### TLS/SSL Configuration

```python
# SSL context for secure connections
import ssl

def create_secure_ssl_context():
    """Create secure SSL context for API connections."""
    context = ssl.create_default_context()
    
    # Require TLS 1.2 or higher
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    
    # Disable weak ciphers
    context.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:!aNULL:!MD5:!DSS')
    
    # Enable certificate verification
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED
    
    return context

# Secure HTTP client
import requests

class SecureHTTPClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.verify = True  # Always verify SSL certificates
        
        # Configure secure headers
        self.session.headers.update({
            'User-Agent': 'GenOps-AI/1.0',
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'X-XSS-Protection': '1; mode=block'
        })
    
    def secure_post(self, url: str, data: Dict[str, Any], api_key: str):
        """Make secure POST request with proper headers."""
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
            'X-Request-ID': str(uuid.uuid4())
        }
        
        response = self.session.post(
            url,
            json=data,
            headers=headers,
            timeout=30  # Prevent hanging connections
        )
        
        response.raise_for_status()
        return response.json()
```

### Kubernetes Network Policies

```yaml
# network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: genops-ai-network-policy
  namespace: ai-production
spec:
  podSelector:
    matchLabels:
      app: genops-ai
  policyTypes:
  - Ingress
  - Egress
  
  # Ingress rules - only allow traffic from specific sources
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: api-gateway
    - namespaceSelector:
        matchLabels:
          name: monitoring
    ports:
    - protocol: TCP
      port: 8080
  
  # Egress rules - only allow necessary outbound traffic
  egress:
  - to: []  # Allow DNS resolution
    ports:
    - protocol: UDP
      port: 53
  - to: []  # Allow HTTPS to AI providers
    ports:
    - protocol: TCP
      port: 443
  - to:  # Allow telemetry to monitoring
    - namespaceSelector:
        matchLabels:
          name: monitoring
    ports:
    - protocol: TCP
      port: 4317  # OTLP gRPC
    - protocol: TCP
      port: 4318  # OTLP HTTP

---
# Pod Security Policy
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: genops-ai-psp
spec:
  privileged: false
  allowPrivilegeEscalation: false
  requiredDropCapabilities:
    - ALL
  volumes:
    - 'configMap'
    - 'emptyDir'
    - 'projected'
    - 'secret'
    - 'downwardAPI'
    - 'persistentVolumeClaim'
  runAsUser:
    rule: 'MustRunAsNonRoot'
  seLinux:
    rule: 'RunAsAny'
  fsGroup:
    rule: 'RunAsAny'
```

## 6. Security Monitoring and Incident Response

### Security Event Monitoring

```python
class SecurityEventMonitor:
    """Monitor and respond to security events."""
    
    def __init__(self, alert_webhook: str = None):
        self.alert_webhook = alert_webhook
        self.threat_patterns = {
            'sql_injection': re.compile(r'(union|select|insert|delete|drop|alter)\s+', re.IGNORECASE),
            'xss_attempt': re.compile(r'<script|javascript:|onerror=', re.IGNORECASE),
            'path_traversal': re.compile(r'\.\.\/|\.\.\\'),
            'command_injection': re.compile(r'[;&|`]')
        }
        
        self.anomaly_thresholds = {
            'high_cost_velocity': 10.0,  # $10/minute
            'unusual_query_volume': 100,   # 100 queries/minute from single user
            'failed_auth_rate': 5          # 5 failed auths/minute
        }
    
    def scan_query_for_threats(self, query: str, user_id: str) -> Dict[str, Any]:
        """Scan query for security threats."""
        threats_found = {}
        
        for threat_type, pattern in self.threat_patterns.items():
            if pattern.search(query):
                threats_found[threat_type] = True
                self.log_security_event(
                    event_type='threat_detected',
                    threat_type=threat_type,
                    user_id=user_id,
                    query_sample=query[:100]  # Log sample, not full query
                )
        
        return threats_found
    
    def monitor_cost_velocity(self, user_id: str, cost_per_minute: float):
        """Monitor for unusual cost velocity patterns."""
        if cost_per_minute > self.anomaly_thresholds['high_cost_velocity']:
            self.log_security_event(
                event_type='cost_anomaly',
                anomaly_type='high_velocity',
                user_id=user_id,
                cost_per_minute=cost_per_minute,
                severity='high'
            )
            
            # Automatic response: temporary rate limiting
            self.apply_temporary_rate_limit(user_id, duration=300)  # 5 minutes
    
    def log_security_event(self, event_type: str, **kwargs):
        """Log security event and trigger alerts if needed."""
        event = {
            'timestamp': time.time(),
            'event_type': event_type,
            'severity': kwargs.get('severity', 'medium'),
            **kwargs
        }
        
        logger.warning(f"Security event: {json.dumps(event)}")
        
        # Send alert for high-severity events
        if kwargs.get('severity') == 'high' and self.alert_webhook:
            self.send_security_alert(event)
    
    def send_security_alert(self, event: Dict[str, Any]):
        """Send security alert to monitoring system."""
        try:
            requests.post(
                self.alert_webhook,
                json={
                    'alert_type': 'security_event',
                    'event': event,
                    'timestamp': event['timestamp']
                },
                timeout=10
            )
        except Exception as e:
            logger.error(f"Failed to send security alert: {e}")

# Integrated secure adapter
class SecurityMonitoredAdapter:
    def __init__(self):
        self.security_monitor = SecurityEventMonitor()
        self.adapter = instrument_llamaindex()
        self.rate_limiter = {}
    
    def secure_track_query(self, user_id: str, query_engine, query: str, **kwargs):
        """Track query with comprehensive security monitoring."""
        
        # Security threat scanning
        threats = self.security_monitor.scan_query_for_threats(query, user_id)
        
        if threats:
            raise SecurityError(f"Security threats detected: {list(threats.keys())}")
        
        # Rate limiting check
        if self.is_rate_limited(user_id):
            raise RateLimitError(f"User {user_id} is temporarily rate limited")
        
        # Execute query
        start_time = time.time()
        result = self.adapter.track_query(query_engine, query, user_id=user_id, **kwargs)
        
        # Monitor cost velocity
        execution_time = time.time() - start_time
        if hasattr(result, 'cost') and execution_time > 0:
            cost_per_minute = (result.cost / execution_time) * 60
            self.security_monitor.monitor_cost_velocity(user_id, cost_per_minute)
        
        return result

class SecurityError(Exception):
    """Exception raised for security violations."""
    pass

class RateLimitError(Exception):
    """Exception raised for rate limit violations."""
    pass
```

## 7. Deployment Security Checklist

### Pre-Deployment Security Verification

```bash
#!/bin/bash
# security-check.sh - Pre-deployment security verification

echo "🔒 GenOps AI Security Verification"
echo "================================="

# 1. Check for hardcoded secrets
echo "🔍 Checking for hardcoded secrets..."
if grep -r "sk-proj-\|sk-[a-zA-Z0-9]\{32,\}\|anthropic_api_key.*=.*['\"][a-zA-Z0-9]" --include="*.py" --include="*.js" --include="*.yaml" .; then
    echo "❌ FAIL: Hardcoded API keys found"
    exit 1
else
    echo "✅ PASS: No hardcoded secrets detected"
fi

# 2. Verify TLS configuration
echo "🔍 Checking TLS configuration..."
python3 << 'EOF'
import ssl
import sys

try:
    context = ssl.create_default_context()
    if context.minimum_version < ssl.TLSVersion.TLSv1_2:
        print("❌ FAIL: TLS version too low")
        sys.exit(1)
    print("✅ PASS: TLS configuration secure")
except Exception as e:
    print(f"❌ FAIL: TLS configuration error: {e}")
    sys.exit(1)
EOF

# 3. Check file permissions
echo "🔍 Checking file permissions..."
if find . -name "*.py" -perm /o+w | grep -q .; then
    echo "❌ FAIL: World-writable Python files found"
    exit 1
else
    echo "✅ PASS: File permissions secure"
fi

# 4. Verify dependency security
echo "🔍 Checking dependency security..."
if command -v safety &> /dev/null; then
    if safety check; then
        echo "✅ PASS: No known security vulnerabilities"
    else
        echo "❌ FAIL: Security vulnerabilities in dependencies"
        exit 1
    fi
else
    echo "⚠️  WARNING: safety not installed, skipping dependency check"
fi

# 5. Check for debug mode
echo "🔍 Checking for debug mode..."
if grep -r "debug.*=.*True\|DEBUG.*=.*True" --include="*.py" --include="*.yaml" .; then
    echo "❌ FAIL: Debug mode enabled in production files"
    exit 1
else
    echo "✅ PASS: Debug mode not enabled"
fi

echo "🎉 Security verification completed successfully!"
```

This comprehensive security guide ensures that GenOps AI deployments maintain the highest security standards while providing robust AI governance capabilities. Regular security audits and updates to these practices are recommended as threats evolve.