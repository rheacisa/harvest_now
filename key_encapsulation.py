"""
Key Encapsulation Mechanism (KEM) Simulation
Demonstrates RSA-KEM for session key establishment - the vulnerable handshake
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import time


class RSA_KEM:
    """
    RSA-based Key Encapsulation Mechanism.
    This is what's vulnerable to "Harvest Now, Decrypt Later" attacks.
    """
    
    def __init__(self, key_size=2048):
        """Initialize RSA-KEM with specified key size."""
        self.key_size = key_size
        self.private_key = None
        self.public_key = None
        
    def generate_keypair(self):
        """Generate RSA key pair for key encapsulation."""
        print(f"\n[*] Generating RSA-{self.key_size} key pair for KEM...")
        start_time = time.time()
        
        key = RSA.generate(self.key_size)
        self.private_key = key
        self.public_key = key.publickey()
        
        elapsed = time.time() - start_time
        print(f"[✓] RSA key pair generated in {elapsed:.4f} seconds")
        print(f"[*] Public key modulus (n): {self.public_key.n}")
        print(f"[*] Modulus size: {self.public_key.n.bit_length()} bits")
        
        return self.public_key
    
    def encapsulate(self, public_key=None):
        """
        Encapsulate a session key using RSA public key.
        
        This simulates the client generating a random session key
        and encrypting it with the server's public key.
        
        Returns:
            tuple: (session_key, encapsulated_key)
                - session_key: The random symmetric key (what both parties will use)
                - encapsulated_key: The encrypted session key (transmitted over network)
        """
        if public_key is None:
            public_key = self.public_key
            
        # Generate random session key (32 bytes = 256 bits)
        session_key = get_random_bytes(32)
        
        print("\n[*] ALICE: Generating random session key...")
        print(f"[*] Session key (hex): {session_key.hex()}")
        
        # Encapsulate (encrypt) the session key with RSA public key
        cipher = PKCS1_OAEP.new(public_key)
        encapsulated_key = cipher.encrypt(session_key)
        
        print(f"[*] ALICE: Encapsulating session key with Bob's RSA public key...")
        print(f"[✓] Session key encapsulated")
        print(f"[*] Encapsulated key size: {len(encapsulated_key)} bytes")
        print(f"[*] Encapsulated key (hex, first 32 bytes): {encapsulated_key[:32].hex()}...")
        
        print(f"\n[*] ALICE → BOB: Sending encapsulated key over network...")
        print(f"[!] ⚠️  ADVERSARY: Intercepting and harvesting encapsulated key!")
        
        return session_key, encapsulated_key
    
    def decapsulate(self, encapsulated_key):
        """
        Decapsulate (decrypt) the session key using RSA private key.
        
        Args:
            encapsulated_key: The encrypted session key
            
        Returns:
            bytes: The decrypted session key
        """
        print(f"\n[*] BOB: Decapsulating session key with private key...")
        
        cipher = PKCS1_OAEP.new(self.private_key)
        session_key = cipher.decrypt(encapsulated_key)
        
        print(f"[✓] Session key decapsulated successfully")
        print(f"[*] Session key (hex): {session_key.hex()}")
        
        return session_key
    
    def get_public_key_params(self):
        """Get public key parameters for attacker simulation."""
        return {
            'n': self.public_key.n,
            'e': self.public_key.e,
            'key_size': self.key_size
        }


def demonstrate_vulnerable_handshake():
    """
    Demonstrate the vulnerable RSA-KEM handshake.
    This is what adversaries can "harvest now" to "decrypt later".
    """
    print("="*70)
    print("VULNERABLE RSA KEY ENCAPSULATION (The Handshake)")
    print("="*70)
    
    # Alice and Bob establish secure communication using RSA-KEM
    print("\n[SCENARIO] Alice and Bob want to establish a secure connection")
    print("[*] They use RSA-based Key Encapsulation Mechanism (RSA-KEM)")
    
    # Bob generates RSA key pair and publishes public key
    print("\n--- Bob's Setup ---")
    bob_kem = RSA_KEM(key_size=2048)
    bob_public_key = bob_kem.generate_keypair()
    
    # Alice encapsulates a session key using Bob's public key
    print("\n--- Key Exchange ---")
    alice_session_key, encapsulated_key = bob_kem.encapsulate()
    
    # This encapsulated key is transmitted over the network
    # An adversary intercepts and stores it
    print("\n[!] ⚠️  HARVEST NOW: Adversary has captured:")
    print(f"[!]    - Bob's public key (n={bob_kem.public_key.n})")
    print(f"[!]    - Encapsulated session key: {len(encapsulated_key)} bytes")
    print(f"[!]    - This data is stored for future decryption!")
    
    # Bob decapsulates to get the session key
    bob_session_key = bob_kem.decapsulate(encapsulated_key)
    
    # Verify both have the same session key
    print("\n[*] Verification:")
    print(f"[*] Alice's session key: {alice_session_key.hex()}")
    print(f"[*] Bob's session key:   {bob_session_key.hex()}")
    print(f"[✓] Keys match: {alice_session_key == bob_session_key}")
    
    print("\n[✓] Secure channel established (for now...)")
    print("[!] But the encapsulated key can be decrypted later with quantum computers!")
    
    return bob_kem, encapsulated_key, alice_session_key


if __name__ == "__main__":
    demonstrate_vulnerable_handshake()
