#!/usr/bin/env python3
"""
HARVEST NOW, DECRYPT LATER - Complete Demonstration

This is the main demonstration script following the execution steps:
1. Simulate Classical Encryption (The Vulnerable Handshake) - RSA-KEM
2. Simulate Quantum Attack (The Threat) - shors_break_rsa()
3. Implement Quantum Resistance (The Solution) - ML-KEM/Kyber

Author: Harvest Now Demonstrator
Purpose: Show the quantum threat and PQC solution for key encapsulation
"""

import sys
import time
from key_encapsulation import RSA_KEM, demonstrate_vulnerable_handshake
from quantum_attack import shors_break_rsa, decrypt_harvested_data, demonstrate_quantum_attack
from pqc_kem import Kyber_KEM, shors_fail_on_kyber, demonstrate_pqc_security, compare_kem_systems


def print_banner():
    """Print the demonstration banner."""
    print("\n" + "="*80)
    print("🛡️  HARVEST NOW, DECRYPT LATER - QUANTUM THREAT DEMONSTRATOR 🛡️".center(80))
    print("="*80)
    print("\nDemonstrating:")
    print("  ✓ Classical RSA Key Encapsulation (Vulnerable)")
    print("  ✓ Quantum Attack with Shor's Algorithm (The Threat)")
    print("  ✓ Post-Quantum Cryptography ML-KEM/Kyber (The Solution)")
    print("\n" + "="*80)


def step1_vulnerable_handshake():
    """
    STEP 1: Simulate Classical Encryption (The Vulnerable Handshake)
    
    Uses RSA-KEM (Key Encapsulation Mechanism) to establish a session key.
    The adversary harvests the encapsulated key for future decryption.
    """
    print("\n\n")
    print("█"*80)
    print("█ STEP 1: THE VULNERABLE HANDSHAKE (RSA-KEM)".ljust(79) + "█")
    print("█"*80)
    
    print("\n[*] Today's standard: RSA-based Key Encapsulation")
    print("[*] This is what needs to be replaced due to quantum threat")
    
    input("\nPress Enter to demonstrate RSA-KEM handshake...")
    
    # Demonstrate RSA-KEM
    kem_system, encapsulated_key, session_key = demonstrate_vulnerable_handshake()
    
    print("\n" + "-"*80)
    print("KEY POINT:")
    print("  The adversary has HARVESTED:")
    print(f"    • RSA public key (for future factorization)")
    print(f"    • Encapsulated session key (encrypted data)")
    print("  This data will be stored until quantum computers are available.")
    print("-"*80)
    
    return kem_system, encapsulated_key, session_key


def step2_quantum_attack(kem_system, encapsulated_key, session_key):
    """
    STEP 2: Simulate Quantum Attack (The Threat)
    
    Uses shors_break_rsa() to break the RSA encryption and decrypt
    the harvested session key. This demonstrates the quantum threat.
    """
    print("\n\n")
    print("█"*80)
    print("█ STEP 2: THE QUANTUM THREAT (Shor's Algorithm)".ljust(79) + "█")
    print("█"*80)
    
    print("\n[*] Years have passed...")
    print("[*] Quantum computers with Shor's algorithm are now available")
    print("[*] The adversary retrieves the harvested data")
    
    input("\nPress Enter to simulate quantum attack with Shor's algorithm...")
    
    # Get public key parameters for attack
    public_key_params = kem_system.get_public_key_params()
    
    # STEP 2A: Break RSA with Shor's algorithm
    print("\n--- Phase 2A: Breaking RSA with Shor's Algorithm ---")
    broken_private_key = shors_break_rsa(public_key_params)
    
    if broken_private_key:
        # STEP 2B: Decrypt the harvested session key
        print("\n--- Phase 2B: Decrypting Harvested Data ---")
        recovered_session_key = decrypt_harvested_data(encapsulated_key, broken_private_key)
        
        if recovered_session_key and recovered_session_key == session_key:
            print("\n" + "="*80)
            print("⚠️  CRITICAL: QUANTUM ATTACK SUCCESSFUL! ⚠️".center(80))
            print("="*80)
            print("\n✓ The adversary recovered the session key!")
            print("✓ All communications encrypted with this key are now EXPOSED!")
            print("✓ This demonstrates the 'HARVEST NOW, DECRYPT LATER' threat!")
            
            success = True
        else:
            success = False
    else:
        print("\n" + "-"*80)
        print("NOTE: Key too large for classical factorization in this demo")
        print("But a REAL quantum computer with Shor's algorithm WOULD succeed!")
        print("-"*80)
        success = False
    
    print("\n" + "-"*80)
    print("KEY POINT:")
    print("  Shor's algorithm on a quantum computer can:")
    print("    • Factor RSA modulus in polynomial time")
    print("    • Derive the private key from the factors")
    print("    • Decrypt all harvested RSA-encrypted data")
    print("  Timeline: ~10-20 years until large-scale quantum computers")
    print("  Risk: Data encrypted TODAY is at risk TOMORROW")
    print("-"*80)
    
    return success


def step3_pqc_solution():
    """
    STEP 3: Implement Quantum Resistance (The Solution)
    
    Switches to ML-KEM (Kyber) for key encapsulation and shows that
    the adversary's shors_break_rsa() function fails to break PQC.
    """
    print("\n\n")
    print("█"*80)
    print("█ STEP 3: THE SOLUTION (Post-Quantum Cryptography)".ljust(79) + "█")
    print("█"*80)
    
    print("\n[*] The solution: Post-Quantum Cryptography (PQC)")
    print("[*] Using ML-KEM (Kyber) - NIST standardized algorithm")
    print("[*] Based on lattice problems, not integer factorization")
    
    input("\nPress Enter to demonstrate quantum-resistant key encapsulation...")
    
    # Demonstrate PQC-KEM
    print("\n--- Phase 3A: Quantum-Resistant Key Exchange ---")
    pqc_kem, pqc_ciphertext, pqc_shared_secret = demonstrate_pqc_security()
    
    print("\n" + "-"*80)
    print("KEY POINT:")
    print("  ML-KEM (Kyber) is quantum-resistant because:")
    print("    • Based on Learning With Errors (LWE) problem")
    print("    • Shor's algorithm does NOT apply to lattice problems")
    print("    • No known quantum algorithm can break it efficiently")
    print("    • NIST approved and standardized in 2024")
    print("-"*80)
    
    # Show comparison
    input("\nPress Enter to see detailed comparison...")
    compare_kem_systems()
    
    return True


def complete_demonstration():
    """
    Run the complete demonstration following all three steps.
    """
    print_banner()
    
    input("\nPress Enter to begin the demonstration...")
    
    # STEP 1: Vulnerable RSA-KEM Handshake
    kem_system, encapsulated_key, session_key = step1_vulnerable_handshake()
    
    # STEP 2: Quantum Attack with Shor's Algorithm
    quantum_attack_succeeded = step2_quantum_attack(kem_system, encapsulated_key, session_key)
    
    # STEP 3: PQC Solution
    pqc_demonstrated = step3_pqc_solution()
    
    # Final Summary
    print("\n\n")
    print("█"*80)
    print("█ SUMMARY: KEY TAKEAWAYS".ljust(79) + "█")
    print("█"*80)
    
    print("\n1️⃣  THE VULNERABLE HANDSHAKE:")
    print("   • Current systems use RSA for key encapsulation")
    print("   • RSA security relies on factorization being hard")
    print("   • Adversaries can harvest encrypted data today")
    
    print("\n2️⃣  THE QUANTUM THREAT:")
    print("   • Shor's algorithm breaks RSA in polynomial time")
    print("   • Large quantum computers expected in 10-20 years")
    print("   • All harvested RSA data will become vulnerable")
    print("   • This is 'HARVEST NOW, DECRYPT LATER'")
    
    print("\n3️⃣  THE PQC SOLUTION:")
    print("   • ML-KEM (Kyber) is quantum-resistant")
    print("   • Based on lattice problems, not factorization")
    print("   • NIST standardized in 2024")
    print("   • Protects against current AND future threats")
    
    print("\n⚡ CALL TO ACTION:")
    print("   • Migrate to PQC NOW to protect long-term secrets")
    print("   • Implement crypto-agility in your systems")
    print("   • Don't wait - start the transition today!")
    
    print("\n" + "="*80)
    print("Demonstration Complete".center(80))
    print("="*80)
    print("\n✨ Resume Value: This demonstration shows understanding of:")
    print("   ✓ Shor's Algorithm and quantum computing threat")
    print("   ✓ Key exchange vulnerability and attack surface")
    print("   ✓ 'Harvest Now, Decrypt Later' attack scenario")
    print("   ✓ Practical necessity of PQC algorithms (ML-KEM/Kyber)")
    print("   ✓ NIST PQC standards and implementation considerations")
    print("="*80 + "\n")


def quick_demonstration():
    """Run a quick non-interactive demonstration."""
    print_banner()
    
    print("\n[QUICK MODE - Running all steps automatically]\n")
    
    # Step 1
    print("\n" + "█"*80)
    print("█ STEP 1: VULNERABLE RSA-KEM HANDSHAKE".ljust(79) + "█")
    print("█"*80)
    kem_system, encapsulated_key, session_key = demonstrate_vulnerable_handshake()
    
    time.sleep(2)
    
    # Step 2
    print("\n" + "█"*80)
    print("█ STEP 2: QUANTUM ATTACK WITH SHOR'S ALGORITHM".ljust(79) + "█")
    print("█"*80)
    public_key_params = kem_system.get_public_key_params()
    broken_key = shors_break_rsa(public_key_params)
    if broken_key:
        decrypt_harvested_data(encapsulated_key, broken_key)
    
    time.sleep(2)
    
    # Step 3
    print("\n" + "█"*80)
    print("█ STEP 3: PQC SOLUTION WITH ML-KEM (KYBER)".ljust(79) + "█")
    print("█"*80)
    demonstrate_pqc_security()
    compare_kem_systems()
    
    print("\n" + "="*80)
    print("Quick Demonstration Complete!".center(80))
    print("="*80 + "\n")


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--quick":
            quick_demonstration()
        elif sys.argv[1] == "--help":
            print("\nUsage: python main_demo.py [OPTIONS]")
            print("\nOptions:")
            print("  --quick    Run quick non-interactive demonstration")
            print("  --help     Show this help message")
            print("\nDefault: Interactive demonstration with explanations\n")
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Use --help for usage information")
    else:
        complete_demonstration()


if __name__ == "__main__":
    main()
