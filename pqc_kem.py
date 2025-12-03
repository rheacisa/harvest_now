"""
Post-Quantum Key Encapsulation - ML-KEM (Kyber)

This module demonstrates quantum-resistant key encapsulation using
lattice-based cryptography (ML-KEM/Kyber).
"""

import secrets
import time
import hashlib


class Kyber_KEM:
    """
    Simulated ML-KEM (Kyber) Key Encapsulation Mechanism.
    
    This simulates Kyber-768, a NIST-standardized PQC algorithm.
    In production, you would use a real PQC library like liboqs or pqcrypto.
    """
    
    # Kyber-768 parameters (NIST security level 3)
    PUBLIC_KEY_SIZE = 1184    # bytes
    SECRET_KEY_SIZE = 2400    # bytes
    CIPHERTEXT_SIZE = 1088    # bytes
    SHARED_SECRET_SIZE = 32   # bytes
    
    def __init__(self, security_level="Kyber-768"):
        """Initialize Kyber KEM."""
        self.security_level = security_level
        self.public_key = None
        self.secret_key = None
        
    def generate_keypair(self):
        """
        Generate Kyber key pair.
        
        Real implementation would use lattice-based key generation.
        This simulation creates random keys of appropriate sizes.
        """
        print(f"\n[*] Generating {self.security_level} key pair for PQC-KEM...")
        print(f"[*] Security basis: Learning With Errors (LWE) - lattice problem")
        
        start_time = time.time()
        
        # Simulate key generation
        # Real Kyber generates keys based on module lattice problems
        self.public_key = secrets.token_bytes(self.PUBLIC_KEY_SIZE)
        self.secret_key = secrets.token_bytes(self.SECRET_KEY_SIZE)
        
        elapsed = time.time() - start_time
        
        print(f"[✓] Kyber key pair generated in {elapsed:.6f} seconds")
        print(f"[*] Public key size: {len(self.public_key)} bytes")
        print(f"[*] Secret key size: {len(self.secret_key)} bytes")
        print(f"[*] Public key (first 32 bytes): {self.public_key[:32].hex()}...")
        
        return self.public_key
    
    def encapsulate(self, public_key=None):
        """
        Encapsulate a shared secret using Kyber.
        
        This uses lattice-based cryptography which is quantum-resistant.
        
        Returns:
            tuple: (shared_secret, ciphertext)
                - shared_secret: The session key to use
                - ciphertext: The encapsulated key to transmit
        """
        if public_key is None:
            public_key = self.public_key
        
        print("\n[*] ALICE: Encapsulating shared secret with Kyber...")
        
        start_time = time.time()
        
        # Generate shared secret
        # Real Kyber uses lattice-based encapsulation
        # The shared secret is derived from the ciphertext and random coins
        random_coins = secrets.token_bytes(32)
        
        # Simulate Kyber encapsulation
        # Real algorithm: ciphertext = Encrypt(public_key, random_coins)
        ciphertext = secrets.token_bytes(self.CIPHERTEXT_SIZE)
        
        # Derive shared secret from random coins
        # Real algorithm uses hash function on the encapsulation output
        shared_secret = hashlib.sha256(random_coins + public_key[:32]).digest()
        
        elapsed = time.time() - start_time
        
        print(f"[✓] Encapsulation complete in {elapsed:.6f} seconds")
        print(f"[*] Shared secret: {shared_secret.hex()}")
        print(f"[*] Ciphertext size: {len(ciphertext)} bytes")
        print(f"[*] Ciphertext (first 32 bytes): {ciphertext[:32].hex()}...")
        
        print(f"\n[*] ALICE → BOB: Sending Kyber ciphertext over network...")
        print(f"[!] ⚠️  ADVERSARY: Intercepting Kyber ciphertext...")
        print(f"[*] But this is QUANTUM-RESISTANT!")
        
        return shared_secret, ciphertext
    
    def decapsulate(self, ciphertext):
        """
        Decapsulate the shared secret using Kyber secret key.
        
        Args:
            ciphertext: The encapsulated shared secret
            
        Returns:
            bytes: The shared secret
        """
        print(f"\n[*] BOB: Decapsulating shared secret with Kyber secret key...")
        
        start_time = time.time()
        
        # Simulate Kyber decapsulation
        # Real algorithm: shared_secret = Decrypt(secret_key, ciphertext)
        # For simulation, we derive deterministically from ciphertext and secret key
        shared_secret = hashlib.sha256(ciphertext[:32] + self.secret_key[:32]).digest()
        
        # Note: In real Kyber, encapsulate and decapsulate would produce the same secret
        # For this simulation, we're showing the concept
        
        elapsed = time.time() - start_time
        
        print(f"[✓] Decapsulation complete in {elapsed:.6f} seconds")
        print(f"[*] Shared secret: {shared_secret.hex()}")
        
        return shared_secret
    
    def get_public_key(self):
        """Get the public key for transmission."""
        return self.public_key


def shors_fail_on_kyber(ciphertext, public_key):
    """
    Demonstrate that Shor's algorithm FAILS against Kyber/PQC.
    
    This function shows that quantum computers cannot break
    lattice-based cryptography like Kyber.
    
    Args:
        ciphertext: The Kyber ciphertext
        public_key: The Kyber public key
        
    Returns:
        None - Attack fails!
    """
    print("\n" + "="*70)
    print("QUANTUM ATTACK ATTEMPT: Shor's Algorithm vs Kyber")
    print("="*70)
    
    print("\n[!] ATTACKER: Attempting to break Kyber with quantum computer...")
    print(f"[*] Target: ML-KEM (Kyber-768) ciphertext")
    print(f"[*] Ciphertext size: {len(ciphertext)} bytes")
    
    time.sleep(0.5)
    
    print("\n[*] Loading Shor's algorithm...")
    time.sleep(0.5)
    
    print("[!] ERROR: Shor's algorithm requires integer factorization problem")
    print("[!] Kyber is based on Learning With Errors (LWE) - a lattice problem")
    print("[!] Shor's algorithm does NOT apply to lattice problems!")
    
    time.sleep(0.5)
    
    print("\n[*] Attempting Grover's algorithm (generic quantum attack)...")
    time.sleep(0.5)
    
    print("[!] Grover's algorithm provides only quadratic speedup")
    print("[!] Kyber-768 has 192-bit quantum security level")
    print("[!] Attack would require 2^192 quantum operations - INFEASIBLE!")
    
    time.sleep(0.5)
    
    print("\n[*] Attempting other known quantum algorithms...")
    print("[*] - BKZ lattice reduction: No quantum advantage")
    print("[*] - Lattice sieving: Only polynomial quantum speedup, still exponential")
    print("[*] - No known quantum algorithm breaks Kyber efficiently!")
    
    time.sleep(0.5)
    
    print("\n" + "="*70)
    print("❌ QUANTUM ATTACK FAILED! ❌".center(70))
    print("="*70)
    
    print("\n[✓] Kyber successfully resists quantum attacks!")
    print("[✓] The harvested ciphertext remains SECURE")
    print("[✓] No 'Decrypt Later' is possible with PQC!")
    print("\n[!] This is why Post-Quantum Cryptography is the solution!")
    
    return None


def demonstrate_pqc_security():
    """
    Demonstrate quantum-resistant key encapsulation with Kyber.
    """
    print("="*70)
    print("POST-QUANTUM KEY ENCAPSULATION (The Solution)")
    print("="*70)
    
    print("\n[SCENARIO] Alice and Bob use quantum-resistant cryptography")
    print("[*] They use ML-KEM (Kyber) - NIST PQC standard")
    
    # Bob generates Kyber key pair
    print("\n--- Bob's PQC Setup ---")
    bob_kem = Kyber_KEM()
    bob_public_key = bob_kem.generate_keypair()
    
    # Alice encapsulates a shared secret using Bob's Kyber public key
    print("\n--- Quantum-Resistant Key Exchange ---")
    alice_shared_secret, ciphertext = bob_kem.encapsulate()
    
    # Adversary intercepts but CANNOT break it
    print("\n[!] ⚠️  Adversary harvests:")
    print(f"[!]    - Bob's Kyber public key: {len(bob_public_key)} bytes")
    print(f"[!]    - Kyber ciphertext: {len(ciphertext)} bytes")
    print(f"[✓] But this data is QUANTUM-RESISTANT!")
    
    # Demonstrate that quantum attacks fail
    print("\n--- Quantum Attack Attempt ---")
    shors_fail_on_kyber(ciphertext, bob_public_key)
    
    print("\n[✓] Post-Quantum Cryptography protects against 'Harvest Now, Decrypt Later'!")
    
    return bob_kem, ciphertext, alice_shared_secret


def compare_kem_systems():
    """Compare RSA-KEM vs Kyber-KEM."""
    print("\n" + "="*70)
    print("COMPARISON: RSA-KEM vs ML-KEM (Kyber)")
    print("="*70)
    
    print("\n{:<30} {:<25} {:<25}".format("Property", "RSA-2048 KEM", "Kyber-768"))
    print("-" * 80)
    print("{:<30} {:<25} {:<25}".format("Public Key Size", "256 bytes", "1184 bytes"))
    print("{:<30} {:<25} {:<25}".format("Ciphertext Size", "256 bytes", "1088 bytes"))
    print("{:<30} {:<25} {:<25}".format("Security Basis", "Integer Factoring", "Lattice (LWE)"))
    print("{:<30} {:<25} {:<25}".format("Quantum-Resistant?", "❌ NO", "✅ YES"))
    print("{:<30} {:<25} {:<25}".format("Vulnerable to Shor's?", "✅ YES", "❌ NO"))
    print("{:<30} {:<25} {:<25}".format("Classical Security", "~112 bits", "~128 bits"))
    print("{:<30} {:<25} {:<25}".format("Quantum Security", "❌ 0 bits", "✅ ~192 bits"))
    print("{:<30} {:<25} {:<25}".format("Harvest Now Risk", "🔴 HIGH", "🟢 NONE"))
    print("{:<30} {:<25} {:<25}".format("NIST Approved", "Legacy", "✅ 2024"))
    
    print("\n" + "="*70)


if __name__ == "__main__":
    demonstrate_pqc_security()
    compare_kem_systems()
