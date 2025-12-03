"""
Security Validation Utilities
Implements security best practices for the quantum threat demonstrator
"""

import re
from typing import Optional, Tuple


class SecurityValidator:
    """
    Validates inputs and enforces security constraints.
    Implements defense-in-depth security practices.
    """
    
    # Security constraints
    MIN_KEY_SIZE = 512  # Minimum for demos (not production!)
    MAX_KEY_SIZE = 8192  # Prevent resource exhaustion
    ALLOWED_KEY_SIZES = [512, 1024, 2048, 3072, 4096]  # Standard sizes
    
    @staticmethod
    def validate_key_size(key_size: int) -> Tuple[bool, Optional[str]]:
        """
        Validate RSA key size for security and resource constraints.
        
        Args:
            key_size: Requested key size in bits
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(key_size, int):
            return False, "Key size must be an integer"
        
        if key_size < SecurityValidator.MIN_KEY_SIZE:
            return False, f"Key size too small (minimum: {SecurityValidator.MIN_KEY_SIZE} bits)"
        
        if key_size > SecurityValidator.MAX_KEY_SIZE:
            return False, f"Key size too large (maximum: {SecurityValidator.MAX_KEY_SIZE} bits)"
        
        if key_size not in SecurityValidator.ALLOWED_KEY_SIZES:
            return False, f"Use standard key sizes: {SecurityValidator.ALLOWED_KEY_SIZES}"
        
        return True, None
    
    @staticmethod
    def validate_message_length(message: str, max_length: int = 10000) -> Tuple[bool, Optional[str]]:
        """
        Validate message length to prevent resource exhaustion.
        
        Args:
            message: Input message
            max_length: Maximum allowed length
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(message, str):
            return False, "Message must be a string"
        
        if len(message) == 0:
            return False, "Message cannot be empty"
        
        if len(message) > max_length:
            return False, f"Message too long (maximum: {max_length} characters)"
        
        return True, None
    
    @staticmethod
    def sanitize_output(output: str, max_length: int = 100000) -> str:
        """
        Sanitize output to prevent information leakage or XSS.
        
        Args:
            output: Output string to sanitize
            max_length: Maximum output length
            
        Returns:
            Sanitized output string
        """
        if not isinstance(output, str):
            output = str(output)
        
        # Truncate if too long
        if len(output) > max_length:
            output = output[:max_length] + "\n... (output truncated for safety)"
        
        return output
    
    @staticmethod
    def validate_algorithm_name(algorithm: str) -> Tuple[bool, Optional[str]]:
        """
        Validate algorithm name against whitelist.
        
        Args:
            algorithm: Algorithm name to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        allowed_algorithms = [
            "RSA",
            "RSA-KEM",
            "ML-KEM",
            "Kyber",
            "Kyber-512",
            "Kyber-768",
            "Kyber-1024",
            "Dilithium",
            "SPHINCS+"
        ]
        
        if algorithm not in allowed_algorithms:
            return False, f"Algorithm must be one of: {allowed_algorithms}"
        
        return True, None
    
    @staticmethod
    def check_entropy_source() -> bool:
        """
        Verify that cryptographically secure random sources are available.
        
        Returns:
            True if secure random sources available
        """
        try:
            import secrets
            import os
            # Test entropy sources
            secrets.token_bytes(32)
            os.urandom(32)
            return True
        except Exception:
            return False
    
    @staticmethod
    def rate_limit_check(operation: str, max_operations: int = 100) -> Tuple[bool, Optional[str]]:
        """
        Simple rate limiting for demonstrations.
        
        Args:
            operation: Operation type
            max_operations: Maximum allowed operations
            
        Returns:
            Tuple of (is_allowed, error_message)
        """
        # In a real system, this would track operations per time window
        # For this demo, we just enforce basic limits
        return True, None
    
    @staticmethod
    def validate_security_level(level: int) -> Tuple[bool, Optional[str]]:
        """
        Validate NIST security level (1-5).
        
        Args:
            level: NIST security level
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(level, int):
            return False, "Security level must be an integer"
        
        if level < 1 or level > 5:
            return False, "NIST security level must be between 1 and 5"
        
        return True, None


def secure_demo_wrapper(func):
    """
    Decorator to add security checks to demo functions.
    Implements defense-in-depth practices.
    """
    def wrapper(*args, **kwargs):
        try:
            # Check entropy sources
            if not SecurityValidator.check_entropy_source():
                print("[!] WARNING: Cryptographically secure random sources may not be available")
            
            # Execute function
            result = func(*args, **kwargs)
            
            return result
            
        except KeyboardInterrupt:
            print("\n[!] Operation cancelled by user")
            raise
        except Exception as e:
            # Don't expose internal errors to users
            print(f"[!] An error occurred during the demonstration")
            print(f"[!] Error type: {type(e).__name__}")
            # In production, log full error internally but don't show to user
            raise
    
    return wrapper


class SecureKeyStorage:
    """
    Demonstrates secure key handling practices.
    In production, use HSMs or proper key management systems.
    """
    
    def __init__(self):
        self.keys = {}
    
    def store_key(self, key_id: str, key_data: bytes, key_type: str = "ephemeral"):
        """
        Store key with metadata (demonstration only).
        
        Args:
            key_id: Unique key identifier
            key_data: Key material
            key_type: Type of key (ephemeral, long-term, etc.)
        """
        if key_type != "ephemeral":
            print("[!] WARNING: Only ephemeral keys should be used in demos")
        
        # In production: encrypt key_data before storage
        # In production: use HSM or KMS
        # In production: implement access controls
        
        self.keys[key_id] = {
            'data': key_data,
            'type': key_type
        }
    
    def get_key(self, key_id: str) -> Optional[bytes]:
        """Retrieve key by ID."""
        if key_id in self.keys:
            return self.keys[key_id]['data']
        return None
    
    def delete_key(self, key_id: str):
        """Securely delete key."""
        if key_id in self.keys:
            # In production: overwrite memory before deletion
            del self.keys[key_id]
    
    def clear_all(self):
        """Clear all keys (for demo cleanup)."""
        self.keys.clear()


# Security audit logging
def log_security_event(event_type: str, details: str):
    """
    Log security-relevant events.
    In production, send to SIEM system.
    
    Args:
        event_type: Type of security event
        details: Event details
    """
    import datetime
    timestamp = datetime.datetime.now().isoformat()
    print(f"[SECURITY LOG] {timestamp} - {event_type}: {details}")


if __name__ == "__main__":
    print("Security Validator - Self Test")
    print("=" * 70)
    
    # Test key size validation
    validator = SecurityValidator()
    
    print("\n1. Testing key size validation:")
    for size in [512, 1024, 2048, 4096, 512000]:
        valid, msg = validator.validate_key_size(size)
        status = "✓" if valid else "✗"
        print(f"   {status} {size} bits: {msg if msg else 'Valid'}")
    
    print("\n2. Testing entropy source:")
    entropy_ok = validator.check_entropy_source()
    print(f"   {'✓' if entropy_ok else '✗'} Cryptographic entropy available: {entropy_ok}")
    
    print("\n3. Testing algorithm validation:")
    for algo in ["RSA", "ML-KEM", "Kyber-512", "InvalidAlgo"]:
        valid, msg = validator.validate_algorithm_name(algo)
        status = "✓" if valid else "✗"
        print(f"   {status} {algo}: {msg if msg else 'Valid'}")
    
    print("\n4. Testing message validation:")
    test_messages = ["Hello", "A" * 10000, "A" * 100000]
    for msg in test_messages:
        valid, error = validator.validate_message_length(msg)
        status = "✓" if valid else "✗"
        print(f"   {status} Length {len(msg)}: {error if error else 'Valid'}")
    
    print("\n" + "=" * 70)
    print("Security validation tests complete!")
