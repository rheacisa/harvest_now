"""
Quantum Attack Simulation - Shor's Algorithm Breaking RSA-KEM

This module simulates how a quantum computer with Shor's algorithm
can break RSA encryption and decrypt the "harvested" session keys.
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time


def shors_break_rsa(public_key_params):
    """
    Simulate Shor's algorithm breaking RSA.
    
    This function represents the quantum threat: given an RSA public key,
    a quantum computer running Shor's algorithm can efficiently factor
    the modulus and derive the private key.
    
    NOTE: This is a simulation. We're demonstrating the EFFECT of the threat,
    not implementing the complex quantum algorithm itself.
    
    Args:
        public_key_params: Dictionary with 'n' (modulus), 'e' (public exponent)
        
    Returns:
        RSA private key object if successful, None otherwise
    """
    n = public_key_params['n']
    e = public_key_params['e']
    key_size = public_key_params.get('key_size', n.bit_length())
    
    print("\n" + "="*70)
    print("QUANTUM ATTACK: Shor's Algorithm Breaking RSA")
    print("="*70)
    
    print(f"\n[!] ATTACKER: Quantum computer is now available!")
    print(f"[*] Target: RSA-{key_size} public key")
    print(f"[*] Public key modulus (n): {n}")
    print(f"[*] Public exponent (e): {e}")
    
    print("\n[*] Initializing quantum computer...")
    time.sleep(0.5)
    
    print("[*] Loading Shor's quantum factoring algorithm...")
    time.sleep(0.5)
    
    print("[*] Creating quantum superposition of all possible factors...")
    time.sleep(0.5)
    
    print("[*] Applying quantum period-finding routine...")
    print("[*] Executing quantum Fourier transform (QFT)...")
    time.sleep(0.5)
    
    print("[*] Measuring quantum states...")
    print("[*] Extracting period from quantum measurement...")
    time.sleep(0.5)
    
    # For smaller keys, we can actually attempt to factor
    # For larger keys, we simulate the quantum attack
    if key_size <= 1024:
        print(f"\n[*] Attempting classical factorization for demonstration...")
        factors = _attempt_classical_factorization(n, timeout=5)
        
        if factors:
            p, q = factors
            print(f"\n[✓] FACTORIZATION SUCCESSFUL!")
            print(f"[*] Found prime factors:")
            print(f"    p = {p}")
            print(f"    q = {q}")
            print(f"[*] Verification: {p} × {q} = {n}")
            
            # Derive private key from factors
            private_key = _derive_private_key(n, e, p, q)
            return private_key
    
    # For larger keys (>1024 bits), simulate successful quantum attack
    print(f"\n[!] Key size ({key_size} bits) too large for classical factorization")
    print(f"[*] But Shor's algorithm on quantum computer would succeed!")
    print(f"[*] Estimated quantum factorization time: O((log N)³)")
    print(f"[*] Classical computer: ~BILLIONS OF YEARS to factor {key_size}-bit RSA")
    print(f"[*] Quantum computer: ~8-10 HOURS to factor {key_size}-bit RSA")
    print(f"[!] That's a reduction from impossible to trivial!")
    
    print("\n[!] ⚠️  SIMULATING SUCCESSFUL QUANTUM ATTACK ⚠️")
    print("[!] In reality, the quantum computer WOULD factor this key")
    print("[!] and derive the private key, allowing decryption of all")
    print("[!] harvested encrypted data!")
    
    # Return None for large keys since we can't actually factor them classically
    # But emphasize that quantum computers WOULD succeed
    return None


def _attempt_classical_factorization(n, timeout=5):
    """
    Attempt classical factorization (for small keys only).
    This is just for demonstration with small key sizes.
    """
    if n % 2 == 0:
        return (2, n // 2)
    
    import math
    start_time = time.time()
    limit = min(int(math.sqrt(n)) + 1, 10000000)
    
    for i in range(3, limit, 2):
        if time.time() - start_time > timeout:
            return None
        if n % i == 0:
            return (i, n // i)
    
    return None


def _derive_private_key(n, e, p, q):
    """
    Derive RSA private key from prime factors.
    
    Args:
        n: RSA modulus
        e: Public exponent
        p, q: Prime factors of n
        
    Returns:
        RSA private key object
    """
    print("\n[*] Deriving private key from factors...")
    
    # Calculate φ(n) = (p-1)(q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Calculate d = e^(-1) mod φ(n)
    d = pow(e, -1, phi_n)
    
    print(f"[*] Computed φ(n) = (p-1)(q-1) = {phi_n}")
    print(f"[*] Computed private exponent d = {d}")
    
    # Reconstruct private key
    # For proper RSA key reconstruction, we need p, q, and d
    from Crypto.PublicKey import RSA
    
    # RSA key components: (n, e, d, p, q)
    key = RSA.construct((n, e, d, p, q))
    
    print(f"[✓] Private key successfully reconstructed!")
    
    return key


def decrypt_harvested_data(encapsulated_key, broken_private_key):
    """
    Use the quantum-broken private key to decrypt harvested session keys.
    
    This is the "DECRYPT LATER" part of the attack.
    
    Args:
        encapsulated_key: The harvested encrypted session key
        broken_private_key: Private key derived from quantum attack
        
    Returns:
        Decrypted session key
    """
    print("\n" + "="*70)
    print("DECRYPT LATER: Using Quantum-Broken Private Key")
    print("="*70)
    
    print("\n[!] ATTACKER: Now decrypting previously harvested data...")
    print(f"[*] Encapsulated key size: {len(encapsulated_key)} bytes")
    
    try:
        # Decrypt the encapsulated session key using the broken private key
        cipher = PKCS1_OAEP.new(broken_private_key)
        decrypted_session_key = cipher.decrypt(encapsulated_key)
        
        print(f"\n[✓] ⚠️  DECRYPTION SUCCESSFUL! ⚠️")
        print(f"[*] Recovered session key: {decrypted_session_key.hex()}")
        print(f"\n[!] CRITICAL BREACH:")
        print(f"[!] - The attacker now has the session key")
        print(f"[!] - All data encrypted with this session key can be decrypted")
        print(f"[!] - Data that was 'secure' when harvested is now EXPOSED")
        print(f"[!] - This is the 'HARVEST NOW, DECRYPT LATER' attack!")
        
        return decrypted_session_key
        
    except Exception as e:
        print(f"[!] Decryption failed: {e}")
        return None


def demonstrate_quantum_attack(kem_system, encapsulated_key, original_session_key):
    """
    Complete demonstration of quantum attack on harvested RSA-KEM data.
    
    Args:
        kem_system: The RSA_KEM system used for the original handshake
        encapsulated_key: The harvested encapsulated session key
        original_session_key: The original session key (for verification)
    """
    print("\n" + "="*70)
    print("QUANTUM THREAT DEMONSTRATION")
    print("="*70)
    
    print("\n[SCENARIO] Years have passed...")
    print("[*] Quantum computers with Shor's algorithm are now available")
    print("[*] The attacker retrieves the harvested encrypted data")
    
    # Get public key parameters
    public_key_params = kem_system.get_public_key_params()
    
    # Step 1: Break RSA with Shor's algorithm
    broken_private_key = shors_break_rsa(public_key_params)
    
    if broken_private_key:
        # Step 2: Decrypt the harvested session key
        recovered_session_key = decrypt_harvested_data(encapsulated_key, broken_private_key)
        
        if recovered_session_key:
            # Verify the attack succeeded
            print("\n[*] Verification:")
            print(f"[*] Original session key:  {original_session_key.hex()}")
            print(f"[*] Recovered session key: {recovered_session_key.hex()}")
            print(f"[*] Keys match: {original_session_key == recovered_session_key}")
            
            if original_session_key == recovered_session_key:
                print("\n" + "="*70)
                print("⚠️  ATTACK COMPLETELY SUCCESSFUL! ⚠️".center(70))
                print("="*70)
                print("\n[!] The quantum threat is REAL and DEMONSTRATED!")
                print("[!] All RSA-encrypted data is vulnerable!")
                print("[!] Migration to Post-Quantum Cryptography is URGENT!")
                
                return True
    else:
        # For large keys, we couldn't actually factor but explain the threat
        print("\n" + "="*70)
        print("QUANTUM THREAT DEMONSTRATED (Conceptually)".center(70))
        print("="*70)
        print("\n[!] This demonstration shows the quantum threat:")
        print("[!] - RSA relies on factorization being hard")
        print("[!] - Shor's algorithm makes factorization easy for quantum computers")
        print("[!] - Any RSA-encrypted data can be broken in the quantum era")
        print("[!] - 'Harvest Now, Decrypt Later' is a real, inevitable threat")
        print("\n[!] Post-Quantum Cryptography is the ONLY solution!")
    
    return False


if __name__ == "__main__":
    print("This module contains quantum attack simulation functions.")
    print("Run the main demonstration with: python main_demo.py")
