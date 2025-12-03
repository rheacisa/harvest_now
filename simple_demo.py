#!/usr/bin/env python3
"""
HARVEST NOW, DECRYPT LATER - Simple Explanation Demo

A simple, non-technical demonstration of the quantum threat to encryption.
Perfect for executives, managers, and non-technical stakeholders.
"""

import time
import sys


def print_header(title):
    """Print a simple header."""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")


def pause(message="Press Enter to continue..."):
    """Pause for user input."""
    input(f"\n{message}")


def typing_effect(text, delay=0.03):
    """Print text with typing effect for emphasis."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def simple_demonstration():
    """
    A simple, story-driven demonstration for non-technical audiences.
    """
    print("\n" + "🛡️ "*23)
    print("       HARVEST NOW, DECRYPT LATER")
    print("     Understanding the Quantum Threat to Encryption")
    print("🛡️ "*23 + "\n")
    
    print("This demonstration explains a serious cybersecurity threat")
    print("in simple terms that anyone can understand.\n")
    
    pause("Press Enter to begin...")
    
    # ========================================================================
    # PART 1: How Encryption Works Today
    # ========================================================================
    print_header("PART 1: How We Protect Secrets Today")
    
    print("Imagine you want to send a secret message to your friend Bob.")
    print("You put the message in a locked box.\n")
    
    print("📦 The box has a special lock that needs a KEY to open.")
    print("🔑 Bob has the key to unlock the box and read your message.")
    print("✅ Anyone else who intercepts the box can't read it - they don't have the key!\n")
    
    print("This is how internet encryption works today:")
    print("  • Your bank uses this to protect your account details")
    print("  • Messaging apps use this to protect your conversations")
    print("  • Companies use this to protect trade secrets\n")
    
    print("💡 The 'lock' we use today is called RSA encryption")
    print("💡 It's considered very secure - would take normal computers")
    print("   thousands of years to break!\n")
    
    pause()
    
    # ========================================================================
    # PART 2: The Problem - Quantum Computers
    # ========================================================================
    print_header("PART 2: The Problem - Quantum Computers Are Coming")
    
    print("Here's the problem:\n")
    
    print("Scientists are building new types of computers called")
    typing_effect("'QUANTUM COMPUTERS' 🔬⚛️", delay=0.05)
    
    print("\nThese quantum computers are incredibly powerful.")
    print("They can solve certain problems MUCH faster than regular computers.\n")
    
    print("🔴 BAD NEWS: One thing quantum computers are good at is")
    print("   breaking RSA encryption (the 'locks' we use today)!\n")
    
    print("What takes a regular computer 1,000 years to break,")
    print("a quantum computer could break in just a few hours! ⏱️\n")
    
    print("📅 Timeline:")
    print("   • Today: Quantum computers are still small/experimental")
    print("   • 10-20 years: Large quantum computers expected")
    print("   • These computers WILL be able to break RSA encryption\n")
    
    pause()
    
    # ========================================================================
    # PART 3: The Harvest Now, Decrypt Later Attack
    # ========================================================================
    print_header("PART 3: The 'Harvest Now, Decrypt Later' Threat")
    
    print("Now here's the scary part...\n")
    
    print("Imagine a spy named Eve. She can't read your encrypted messages today,")
    print("but she's smart. Here's what she does:\n")
    
    print("STEP 1 (TODAY):")
    print("  🕵️  Eve intercepts and SAVES your encrypted messages")
    print("  📦 She can't read them now - they're still encrypted")
    print("  💾 But she stores them on a hard drive\n")
    
    time.sleep(1)
    
    print("STEP 2 (10-20 YEARS FROM NOW):")
    print("  ⏳ Eve waits until quantum computers are available")
    print("  🔬 She uses the quantum computer to break the encryption")
    print("  🔓 She can now read ALL the messages she saved years ago!\n")
    
    print("⚠️  This is called 'HARVEST NOW, DECRYPT LATER' ⚠️\n")
    
    print("Think about what this means:")
    print("  • Medical records encrypted today → exposed in 10 years")
    print("  • Trade secrets encrypted today → exposed in 10 years")
    print("  • Government communications today → exposed in 10 years")
    print("  • Your private messages today → exposed in 10 years\n")
    
    print("🔴 If the information is valuable in 10-20 years,")
    print("   it's NOT safe even though it's encrypted today!\n")
    
    pause()
    
    # ========================================================================
    # PART 4: Let's See It In Action
    # ========================================================================
    print_header("PART 4: Demonstration - Seeing The Attack")
    
    print("Let's demonstrate this with a simple example:\n")
    
    print("📧 Alice sends an encrypted message to Bob")
    print("   Message: 'The product launch is scheduled for June 15th'\n")
    
    time.sleep(1)
    
    print("🔒 Alice encrypts the message with RSA encryption")
    print("   Encrypted: [showing simulation...]")
    print("   Ciphertext: 7a8f2e9d4c1b6a3e5f7d9c2a8b4e6f1d...\n")
    
    time.sleep(1)
    
    print("🕵️  Eve intercepts the encrypted message (TODAY)")
    print("   Eve: 'I can't read this now, but I'll save it...'")
    print("   💾 Message stored for future decryption\n")
    
    time.sleep(1)
    
    print("📧 Bob receives and decrypts the message successfully")
    print("   Bob can read: 'The product launch is scheduled for June 15th'")
    print("   ✅ Communication successful!\n")
    
    pause("Press Enter to fast-forward to the future...")
    
    print("\n⏩ FAST FORWARD 15 YEARS... ⏩\n")
    time.sleep(1)
    
    print("🔬 Quantum computers are now available!")
    print("   Eve has access to a quantum computer\n")
    
    time.sleep(1)
    
    print("🕵️  Eve retrieves the old encrypted message from storage")
    print("   Eve: 'Time to see what this message said...'\n")
    
    time.sleep(1)
    
    print("💻 Eve uses quantum computer with 'Shor's Algorithm'")
    print("   [Quantum computer processing...]")
    print("   [Breaking RSA encryption...]")
    print("   [Factoring large numbers...]")
    
    time.sleep(2)
    
    print("\n✅ DECRYPTION SUCCESSFUL!")
    print("   Eve can now read: 'The product launch is scheduled for June 15th'\n")
    
    print("⚠️  The message from 15 years ago is now EXPOSED!")
    print("⚠️  This is the HARVEST NOW, DECRYPT LATER threat!\n")
    
    pause()
    
    # ========================================================================
    # PART 5: The Solution
    # ========================================================================
    print_header("PART 5: The Solution - Post-Quantum Cryptography")
    
    print("Good news! Scientists have a solution:\n")
    
    typing_effect("POST-QUANTUM CRYPTOGRAPHY (PQC) 🛡️", delay=0.05)
    
    print("\nWhat is PQC?")
    print("  • New types of encryption that quantum computers CAN'T break")
    print("  • Based on different math problems that even quantum computers")
    print("    can't solve efficiently")
    print("  • Approved and standardized by NIST (US government) in 2024\n")
    
    print("🔐 Example: ML-KEM (also called Kyber)")
    print("   • One of the new PQC encryption methods")
    print("   • Safe against both regular AND quantum computers")
    print("   • Ready to use TODAY\n")
    
    pause("Press Enter to see PQC in action...")
    
    print("\n📧 Alice sends a message using PQC (instead of RSA)")
    print("   Message: 'Next quarter target is $10M in revenue'\n")
    
    time.sleep(1)
    
    print("🔒 Alice encrypts with ML-KEM/Kyber (PQC)")
    print("   Encrypted: [using quantum-resistant encryption...]")
    print("   Ciphertext: 9c3f7e2a1d8b5f4e3c9a7d6b2f8e1a4c...\n")
    
    time.sleep(1)
    
    print("🕵️  Eve intercepts this encrypted message too")
    print("   Eve: 'I'll save this and decrypt it later...'\n")
    
    time.sleep(1)
    
    print("⏩ FAST FORWARD 15 YEARS... ⏩\n")
    time.sleep(1)
    
    print("🔬 Eve tries to use her quantum computer")
    print("   Eve: 'Time to decrypt this message...'\n")
    
    time.sleep(1)
    
    print("💻 Attempting to break PQC encryption...")
    print("   [Trying Shor's Algorithm...]")
    print("   ❌ ERROR: Shor's Algorithm doesn't work on PQC!")
    
    time.sleep(1)
    
    print("\n   [Trying other quantum algorithms...]")
    print("   ❌ ERROR: No quantum algorithm can break PQC efficiently!\n")
    
    time.sleep(1)
    
    print("🛡️  ATTACK FAILED!")
    print("   Eve CANNOT read the message - even with a quantum computer!")
    print("   ✅ The message remains secure!\n")
    
    print("🎉 This is why PQC protects against 'Harvest Now, Decrypt Later'!\n")
    
    pause()
    
    # ========================================================================
    # PART 6: Summary and What To Do
    # ========================================================================
    print_header("SUMMARY: What You Need to Know")
    
    print("🔴 THE THREAT:")
    print("   1. Today's encryption (RSA) will be broken by quantum computers")
    print("   2. Quantum computers expected in 10-20 years")
    print("   3. Adversaries can save encrypted data NOW and decrypt it LATER")
    print("   4. Any sensitive long-term data is at risk\n")
    
    print("🟡 WHO IS AT RISK?")
    print("   • Government agencies (classified information)")
    print("   • Healthcare (patient records)")
    print("   • Finance (transaction data)")
    print("   • Businesses (trade secrets, IP)")
    print("   • Anyone with secrets that matter for 10+ years\n")
    
    print("🟢 THE SOLUTION:")
    print("   1. Switch to Post-Quantum Cryptography (PQC) NOW")
    print("   2. PQC is ready and standardized (NIST 2024)")
    print("   3. Protects against current AND future threats")
    print("   4. Start migration today - don't wait!\n")
    
    print("⚡ ACTION ITEMS:")
    print("   ✓ Understand the threat is REAL and SOON")
    print("   ✓ Identify data that needs long-term protection")
    print("   ✓ Plan migration to PQC systems")
    print("   ✓ Start using PQC for sensitive communications NOW")
    print("   ✓ Don't wait until quantum computers arrive - it will be too late!\n")
    
    print("="*70)
    print("  Thank you for learning about this important security issue!")
    print("="*70 + "\n")


def main():
    """Main entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("\nSimple Demonstration of 'Harvest Now, Decrypt Later' Threat")
        print("\nUsage: python simple_demo.py")
        print("\nThis is a narrative-driven demo for non-technical audiences.\n")
    else:
        simple_demonstration()


if __name__ == "__main__":
    main()
