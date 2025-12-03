#!/usr/bin/env python3
"""
Small RSA Demonstration - Using Factorable Keys

This version uses very small RSA keys that can actually be factored
to demonstrate the complete attack cycle including successful factorization.
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time


def generate_small_rsa_manually():
    """
    Generate a small RSA key using known small primes.
    This creates a truly factorable key for demonstration.
    """
    print("[*] Generating small RSA key with known small primes...")
    
    # Use small primes for demonstration
    p = 61
    q = 53
    n = p * q  # 3233
    
    # Calculate φ(n)
    phi_n = (p - 1) * (q - 1)
    
    # Use standard public exponent
    e = 17  # Common small public exponent
    
    # Calculate private exponent
    d = pow(e, -1, phi_n)
    
    print(f"[✓] Small RSA key generated:")
    print(f"    p = {p}")
    print(f"    q = {q}")
    print(f"    n = {n}")
    print(f"    e = {e}")
    print(f"    d = {d}")
    
    return n, e, d, p, q


def encrypt_small(message, n, e):
    """Encrypt a small integer message with RSA."""
    # Convert message to integer
    if isinstance(message, str):
        # For very small n, we can only encrypt small values
        m = int.from_bytes(message.encode()[:2], 'big') % n
    else:
        m = message % n
    
    # RSA encryption: c = m^e mod n
    c = pow(m, e, n)
    
    return c, m


def decrypt_small(ciphertext, n, d):
    """Decrypt with RSA private key."""
    # RSA decryption: m = c^d mod n
    m = pow(ciphertext, d, n)
    return m


def demonstrate_small_key_attack():
    """
    Demonstrate complete attack cycle with small factorable key.
    """
    print("="*70)
    print("SMALL RSA DEMONSTRATION - Complete Attack Cycle")
    print("="*70)
    
    print("\n[PHASE 1] Key Generation and Encryption")
    print("-" * 70)
    
    # Generate small key
    n, e, d, p_original, q_original = generate_small_rsa_manually()
    
    # Encrypt a simple numeric message
    message = 123
    print(f"\n[*] Original message: {message}")
    
    ciphertext, m_actual = encrypt_small(message, n, e)
    print(f"[*] Encrypted message value: {m_actual}")
    print(f"[*] Ciphertext: {ciphertext}")
    
    # Verify decryption works
    decrypted = decrypt_small(ciphertext, n, d)
    print(f"[*] Decrypted (with private key): {decrypted}")
    print(f"[✓] Encryption/decryption verified!")
    
    print("\n[PHASE 2] Adversary Intercepts Public Key and Ciphertext")
    print("-" * 70)
    print(f"[!] Adversary captures: n={n}, e={e}")
    print(f"[!] Adversary captures ciphertext: {ciphertext}")
    print("[!] Waiting for quantum computer...")
    
    time.sleep(1)
    
    print("\n[PHASE 3] Quantum Attack - Factoring with Shor's Algorithm")
    print("-" * 70)
    print("[*] Quantum computer available!")
    print(f"[*] Attempting to factor n = {n}")
    
    # Simulate Shor's algorithm (using trial division for small n)
    print("[*] Running Shor's quantum algorithm...")
    start = time.time()
    
    # Trial division (simulating quantum speedup)
    p_found = None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p_found = i
            break
    
    elapsed = time.time() - start
    
    if p_found:
        q_found = n // p_found
        print(f"[✓] Factorization successful in {elapsed:.6f} seconds!")
        print(f"[*] Found factors: p = {p_found}, q = {q_found}")
        print(f"[*] Verification: {p_found} × {q_found} = {n}")
        
        # Derive private key
        phi_n = (p_found - 1) * (q_found - 1)
        d_derived = pow(e, -1, phi_n)
        
        print(f"\n[*] Deriving private key from factors...")
        print(f"[*] φ(n) = (p-1)(q-1) = {phi_n}")
        print(f"[*] d = e^(-1) mod φ(n) = {d_derived}")
        print(f"[✓] Private key successfully derived!")
        
        # Decrypt the intercepted ciphertext
        print("\n[PHASE 4] Decrypting Harvested Data")
        print("-" * 70)
        print("[*] Using quantum-derived private key to decrypt...")
        
        decrypted_by_attacker = decrypt_small(ciphertext, n, d_derived)
        print(f"[✓] Decrypted message: {decrypted_by_attacker}")
        
        print("\n" + "="*70)
        print("⚠️  ATTACK SUCCESSFUL! ⚠️".center(70))
        print("="*70)
        print("\n[!] The adversary successfully:")
        print("    1. Harvested encrypted communications")
        print("    2. Waited for quantum computer availability")
        print("    3. Factored RSA modulus with Shor's algorithm")
        print("    4. Derived the private key")
        print("    5. Decrypted all harvested data")
        print("\n[!] This is the 'HARVEST NOW, DECRYPT LATER' threat!")


if __name__ == "__main__":
    demonstrate_small_key_attack()
