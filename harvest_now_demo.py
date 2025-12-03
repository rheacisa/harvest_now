#!/usr/bin/env python3
"""
Harvest Now, Decrypt Later - Demonstrator

This script demonstrates the quantum threat to current cryptographic systems
and shows how Post-Quantum Cryptography (PQC) provides protection.

Scenario:
1. Show a typical RSA key exchange and encryption (vulnerable)
2. Simulate an adversary "harvesting" the encrypted data
3. Demonstrate Shor's algorithm breaking RSA with a quantum computer
4. Show how PQC algorithms resist quantum attacks
"""

import sys
import time
from rsa_simulation import RSAKeyExchange, demonstrate_rsa_handshake
from shors_algorithm import quantum_attack_on_rsa, simulate_shors_algorithm
from pqc_protection import demonstrate_pqc_protection, compare_rsa_vs_pqc


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(title.center(70))
    print("="*70 + "\n")


def print_scenario(number, description):
    """Print a scenario description."""
    print(f"\n{'─'*70}")
    print(f"SCENARIO {number}: {description}")
    print(f"{'─'*70}\n")


def demonstrate_harvest_now_decrypt_later():
    """
    Main demonstration of the 'Harvest Now, Decrypt Later' threat.
    """
    print_header("HARVEST NOW, DECRYPT LATER - QUANTUM THREAT DEMONSTRATION")
    
    print("This demonstration shows:")
    print("  1. How current RSA encryption can be intercepted today")
    print("  2. How quantum computers (via Shor's algorithm) can break it later")
    print("  3. How Post-Quantum Cryptography (PQC) provides protection")
    
    input("\nPress Enter to begin demonstration...")
    
    # ========================================================================
    # PART 1: RSA Key Exchange and Encryption (Today)
    # ========================================================================
    print_scenario(1, "PRESENT DAY - RSA Encrypted Communication")
    
    print("Two parties (Alice and Bob) want to communicate securely.")
    print("They use RSA encryption, currently considered secure.\n")
    
    input("Press Enter to generate RSA keys and encrypt message...")
    
    # Use 1024-bit RSA for demonstration (factorable in reasonable time)
    rsa = RSAKeyExchange(key_size=1024)
    rsa.generate_keys()
    
    # Encrypt a secret message
    secret_message = "SECRET: The launch codes are 1234567890"
    ciphertext = rsa.encrypt_message(secret_message)
    
    print("\n[!] ADVERSARY ACTION: Intercepting and storing encrypted traffic...")
    time.sleep(1)
    print("[!] ⚠️  Ciphertext harvested and stored for future decryption!")
    
    # Save the parameters an adversary would have
    n = rsa.n
    e = rsa.e
    
    # ========================================================================
    # PART 2: The Waiting Period
    # ========================================================================
    print_scenario(2, "WAITING PERIOD - Building Quantum Computers")
    
    print("Years pass... Quantum computers are developed...")
    print("The adversary still has the encrypted data stored.")
    print("RSA keys that took centuries to crack classically can now")
    print("be broken in hours or minutes with a quantum computer.\n")
    
    input("Press Enter to simulate quantum computer attack...")
    
    # ========================================================================
    # PART 3: Quantum Attack with Shor's Algorithm
    # ========================================================================
    print_scenario(3, "FUTURE - Quantum Computer Available")
    
    print("The adversary now has access to a quantum computer.")
    print("They will use Shor's algorithm to factor the RSA modulus")
    print("and derive the private key.\n")
    
    input("Press Enter to run Shor's algorithm...")
    
    # Quantum attack
    private_key = quantum_attack_on_rsa(n, e)
    
    if private_key:
        print("\n" + "="*70)
        print("⚠️  SECURITY BREACH! ⚠️".center(70))
        print("="*70)
        print("\n[!] The adversary successfully broke the encryption!")
        print("[!] Original message: 'SECRET: The launch codes are 1234567890'")
        print("[!] This data, encrypted years ago, is now compromised!")
        print("\n[!] This is the 'HARVEST NOW, DECRYPT LATER' threat!")
    
    time.sleep(2)
    
    # ========================================================================
    # PART 4: Post-Quantum Cryptography Solution
    # ========================================================================
    print_scenario(4, "THE SOLUTION - Post-Quantum Cryptography")
    
    print("To protect against this threat, we need cryptography that is")
    print("resistant to attacks from quantum computers.")
    print("\nPost-Quantum Cryptography (PQC) algorithms are based on")
    print("mathematical problems that even quantum computers cannot solve.\n")
    
    input("Press Enter to see PQC protection...")
    
    demonstrate_pqc_protection()
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    print_header("SUMMARY")
    
    print("KEY TAKEAWAYS:\n")
    
    print("1. 🔴 THE THREAT:")
    print("   - Current RSA encryption can be broken by quantum computers")
    print("   - Adversaries can harvest encrypted data TODAY")
    print("   - Decrypt it LATER when quantum computers are available")
    print("   - Timeline: ~10-20 years until large-scale quantum computers\n")
    
    print("2. 🟡 THE VULNERABILITY:")
    print("   - RSA security relies on factoring large numbers")
    print("   - Shor's algorithm (quantum) factors numbers efficiently")
    print("   - All RSA-encrypted data is at risk\n")
    
    print("3. 🟢 THE SOLUTION:")
    print("   - Post-Quantum Cryptography (PQC)")
    print("   - Based on lattice, code, or hash problems")
    print("   - Resistant to both classical and quantum attacks")
    print("   - NIST has standardized PQC algorithms (2024)\n")
    
    print("4. ⚡ CALL TO ACTION:")
    print("   - Migrate to PQC NOW to protect future secrets")
    print("   - Any sensitive data encrypted today should use PQC")
    print("   - Start the transition before it's too late!\n")
    
    print("="*70)
    print("Demonstration Complete".center(70))
    print("="*70)


def run_quick_demo():
    """Run a quick demo without pauses."""
    print_header("HARVEST NOW, DECRYPT LATER - QUICK DEMONSTRATION")
    
    # RSA Encryption
    print("\n[1/3] RSA Encryption (Vulnerable):")
    rsa = RSAKeyExchange(key_size=1024)
    rsa.generate_keys()
    secret_message = "SECRET: The launch codes are 1234567890"
    ciphertext = rsa.encrypt_message(secret_message)
    
    # Quantum Attack
    print("\n[2/3] Quantum Attack with Shor's Algorithm:")
    quantum_attack_on_rsa(rsa.n, rsa.e)
    
    # PQC Protection
    print("\n[3/3] Post-Quantum Cryptography Protection:")
    demonstrate_pqc_protection()
    
    print("\n" + "="*70)
    print("Quick Demo Complete!".center(70))
    print("="*70)


def main():
    """Main entry point."""
    print("\n🛡️  HARVEST NOW, DECRYPT LATER - QUANTUM THREAT DEMONSTRATOR 🛡️\n")
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--quick":
            run_quick_demo()
        elif sys.argv[1] == "--small":
            # Run small key demo for complete attack visualization
            from small_rsa_demo import demonstrate_small_key_attack
            demonstrate_small_key_attack()
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Usage: python harvest_now_demo.py [--quick|--small]")
    else:
        print("Choose demonstration mode:")
        print("  1. Interactive (with explanations and pauses) - Realistic key sizes")
        print("  2. Quick (continuous, no pauses) - Realistic key sizes")
        print("  3. Small Key Demo (complete attack cycle with factorization)")
        print()
        
        choice = input("Enter choice (1, 2, or 3): ").strip()
        
        if choice == "2":
            run_quick_demo()
        elif choice == "3":
            from small_rsa_demo import demonstrate_small_key_attack
            demonstrate_small_key_attack()
        else:
            demonstrate_harvest_now_decrypt_later()


if __name__ == "__main__":
    main()
