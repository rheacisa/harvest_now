"""
RSA Key Exchange and Encryption Simulation
Demonstrates the traditional RSA encryption that is vulnerable to quantum attacks.
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import time


class RSAKeyExchange:
    """Simulates RSA key exchange and encryption."""
    
    def __init__(self, key_size=2048):
        """
        Initialize RSA key pair.
        
        Args:
            key_size: Size of RSA key in bits (default: 2048)
        """
        self.key_size = key_size
        self.private_key = None
        self.public_key = None
        self.n = None
        self.e = None
        self.d = None
        
    def generate_keys(self):
        """Generate RSA key pair."""
        print(f"[*] Generating {self.key_size}-bit RSA key pair...")
        start_time = time.time()
        
        key = RSA.generate(self.key_size)
        self.private_key = key
        self.public_key = key.publickey()
        
        # Extract key components
        self.n = key.n  # Modulus
        self.e = key.e  # Public exponent
        self.d = key.d  # Private exponent
        
        elapsed = time.time() - start_time
        print(f"[✓] Keys generated in {elapsed:.4f} seconds")
        print(f"[*] Public key (n, e): (n={self.n}, e={self.e})")
        print(f"[*] Modulus size: {self.n.bit_length()} bits")
        
        return self.public_key
    
    def encrypt_message(self, message):
        """
        Encrypt a message using RSA public key.
        
        Args:
            message: String or bytes to encrypt
            
        Returns:
            Encrypted ciphertext (bytes)
        """
        if isinstance(message, str):
            message = message.encode('utf-8')
            
        print(f"\n[*] Encrypting message: '{message.decode('utf-8')}'")
        
        cipher = PKCS1_OAEP.new(self.public_key)
        ciphertext = cipher.encrypt(message)
        
        print(f"[✓] Message encrypted")
        print(f"[*] Ciphertext (hex): {ciphertext.hex()[:64]}...")
        
        return ciphertext
    
    def decrypt_message(self, ciphertext):
        """
        Decrypt a message using RSA private key.
        
        Args:
            ciphertext: Encrypted bytes
            
        Returns:
            Decrypted plaintext (bytes)
        """
        print(f"\n[*] Decrypting ciphertext with private key...")
        
        cipher = PKCS1_OAEP.new(self.private_key)
        plaintext = cipher.decrypt(ciphertext)
        
        print(f"[✓] Message decrypted: '{plaintext.decode('utf-8')}'")
        
        return plaintext
    
    def export_public_key(self):
        """Export public key in PEM format."""
        return self.public_key.export_key()
    
    def get_factorization_challenge(self):
        """
        Return the RSA modulus that needs to be factored.
        This is what an attacker would try to factor with Shor's algorithm.
        """
        return self.n


def demonstrate_rsa_handshake():
    """Demonstrate a typical RSA key exchange and encryption."""
    print("="*70)
    print("RSA KEY EXCHANGE SIMULATION")
    print("="*70)
    
    # Use smaller key size for demonstration (1024 bits is factorable)
    rsa = RSAKeyExchange(key_size=1024)
    rsa.generate_keys()
    
    # Simulate sending a secret message
    secret_message = "SECRET: The launch codes are 1234567890"
    ciphertext = rsa.encrypt_message(secret_message)
    
    # Legitimate receiver decrypts
    decrypted = rsa.decrypt_message(ciphertext)
    
    print(f"\n[✓] RSA handshake complete!")
    print(f"[!] WARNING: This encrypted data can be harvested by adversaries")
    print(f"[!] and decrypted later when quantum computers become available!")
    
    return rsa, ciphertext


if __name__ == "__main__":
    rsa, ciphertext = demonstrate_rsa_handshake()
