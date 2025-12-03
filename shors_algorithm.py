"""
Shor's Algorithm Simulation
Demonstrates how a quantum computer could factor RSA keys and break encryption.
"""

import math
import random
import time


def classical_factor_small(n, timeout=10):
    """
    Classical factorization for small numbers (trial division).
    Used as a simulation of Shor's algorithm for demonstration.
    
    Args:
        n: Number to factor
        timeout: Maximum time to spend factoring
        
    Returns:
        Tuple of (p, q) factors if found, None otherwise
    """
    if n % 2 == 0:
        return (2, n // 2)
    
    start_time = time.time()
    limit = int(math.sqrt(n)) + 1
    
    for i in range(3, min(limit, 10000000), 2):
        if time.time() - start_time > timeout:
            return None
        if n % i == 0:
            return (i, n // i)
    
    return None


def simulate_shors_algorithm(n, verbose=True, timeout=30):
    """
    Simulate Shor's algorithm to factor n.
    
    For demonstration purposes, this uses classical factorization
    but presents it as if it were using Shor's quantum algorithm.
    
    Args:
        n: The RSA modulus to factor
        verbose: Print progress information
        timeout: Maximum time to spend on factorization
        
    Returns:
        Tuple of (p, q) factors if successful, None otherwise
    """
    if verbose:
        print("\n" + "="*70)
        print("SHOR'S ALGORITHM SIMULATION (Quantum Attack)")
        print("="*70)
        print(f"[*] Target modulus n = {n}")
        print(f"[*] Modulus size: {n.bit_length()} bits")
    
    # Check if n is even
    if n % 2 == 0:
        if verbose:
            print("[✓] n is even, trivial factorization")
        return (2, n // 2)
    
    if verbose:
        print("[*] Initializing quantum computer simulation...")
        print("[*] Preparing quantum superposition...")
        print("[*] Running quantum period-finding subroutine...")
    
    # Simulate the time a quantum computer would take
    # (In reality, Shor's algorithm on a quantum computer would be polynomial time)
    start_time = time.time()
    
    # For demonstration, use classical factorization
    # In a real quantum computer, this would use quantum period finding
    if verbose:
        print("[*] Executing quantum Fourier transform...")
        print("[*] Measuring quantum states...")
    
    factors = classical_factor_small(n, timeout=timeout)
    
    elapsed = time.time() - start_time
    
    if factors:
        p, q = factors
        if verbose:
            print(f"[✓] Factorization successful in {elapsed:.4f} seconds!")
            print(f"[*] Found factors: p = {p}, q = {q}")
            print(f"[*] Verification: {p} × {q} = {p * q}")
            print(f"[✓] RSA modulus successfully factored!")
        return factors
    else:
        if verbose:
            print(f"[!] Classical factorization timed out after {elapsed:.4f} seconds")
            print(f"[!] This demonstrates the strength of RSA against classical attacks")
            print(f"[*] HOWEVER: A real quantum computer with Shor's algorithm")
            print(f"[*] would factor this {n.bit_length()}-bit number in polynomial time!")
            print(f"[*] Estimated quantum factorization time: minutes to hours")
            print(f"[!] The quantum threat is REAL and INEVITABLE!")
        return None


def derive_private_key_from_factors(n, e, p, q):
    """
    Derive the RSA private key from the factors.
    
    Args:
        n: RSA modulus
        e: Public exponent
        p, q: Prime factors of n
        
    Returns:
        Private exponent d
    """
    print("\n[*] Deriving private key from factors...")
    
    # Calculate φ(n) = (p-1)(q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Calculate d = e^(-1) mod φ(n)
    d = pow(e, -1, phi_n)
    
    print(f"[*] φ(n) = {phi_n}")
    print(f"[*] Private exponent d = {d}")
    print(f"[✓] Private key successfully derived!")
    
    return d


def quantum_attack_on_rsa(n, e, ciphertext=None, timeout=5):
    """
    Simulate a complete quantum attack on RSA.
    
    Args:
        n: RSA modulus
        e: Public exponent
        ciphertext: Optional ciphertext to decrypt
        timeout: Time to spend attempting factorization
        
    Returns:
        Private key d if successful, None otherwise
    """
    print("\n" + "="*70)
    print("QUANTUM ATTACK: Harvest Now, Decrypt Later")
    print("="*70)
    print("\n[!] SCENARIO: An adversary has captured encrypted communications")
    print("[!] and now has access to a quantum computer...")
    print(f"\n[*] Public key captured: (n={n}, e={e})")
    
    # Step 1: Factor n using Shor's algorithm
    factors = simulate_shors_algorithm(n, timeout=timeout)
    
    if not factors:
        print("\n[!] Classical factorization failed (as expected for large keys)")
        print("[!] BUT: A real quantum computer with Shor's algorithm WOULD succeed!")
        print("[!] The quantum threat is real - migration to PQC is URGENT!")
        return None
    
    p, q = factors
    
    # Step 2: Derive private key
    d = derive_private_key_from_factors(n, e, p, q)
    
    print("\n[!] CRITICAL: The adversary now has the private key!")
    print("[!] All captured encrypted data can now be decrypted!")
    
    return d


def decrypt_with_quantum_derived_key(n, d, ciphertext):
    """
    Decrypt a message using the private key derived from quantum attack.
    
    Args:
        n: RSA modulus
        d: Private exponent (derived from quantum attack)
        ciphertext: Encrypted message
        
    Returns:
        Decrypted message
    """
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    
    print("\n[*] Reconstructing private key from quantum-derived components...")
    
    # For proper decryption with PKCS1_OAEP, we need the full key
    # This is a simplified demonstration
    print("[*] Attempting decryption with quantum-derived private key...")
    print("[!] (In a full implementation, this would decrypt the captured message)")
    
    return None


if __name__ == "__main__":
    # Example: Factor a small number
    print("Testing Shor's Algorithm on small numbers:\n")
    
    test_numbers = [15, 21, 35, 77, 143]
    
    for num in test_numbers:
        print(f"Factoring {num}:")
        factors = simulate_shors_algorithm(num, verbose=False)
        if factors:
            print(f"  {num} = {factors[0]} × {factors[1]}")
        print()
