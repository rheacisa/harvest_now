# 🛡️ Harvest Now, Decrypt Later - Quantum Threat Demonstrator

A comprehensive demonstration of the "Harvest Now, Decrypt Later" quantum threat and Post-Quantum Cryptography (PQC) protection.

## 🎯 Overview

This project demonstrates one of the most significant cybersecurity threats of our time: adversaries can intercept and store encrypted data today, then decrypt it years later when large-scale quantum computers become available.

### What This Demonstrates

1. **RSA Key Exchange Vulnerability**: Shows how current RSA encryption works and why it's vulnerable
2. **Shor's Algorithm Simulation**: Demonstrates how quantum computers can break RSA by factoring large numbers
3. **Harvest Now, Decrypt Later Attack**: Illustrates the complete attack scenario
4. **PQC Protection**: Shows how Post-Quantum Cryptography algorithms resist quantum attacks

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/rheacisa/harvest_now.git
cd harvest_now

# Install dependencies
pip install -r requirements.txt
```

### Running the Demo

**Interactive Mode** (recommended for first-time viewers):
```bash
python harvest_now_demo.py
# Choose option 1 for step-by-step demonstration
```

**Quick Mode** (continuous demonstration with realistic key sizes):
```bash
python harvest_now_demo.py --quick
```

**Small Key Demo** (shows complete attack with successful factorization):
```bash
python harvest_now_demo.py --small
# Or run directly:
python small_rsa_demo.py
```

### Individual Modules

You can also run individual components:

```bash
# RSA encryption simulation
python rsa_simulation.py

# Shor's algorithm demonstration
python shors_algorithm.py

# Post-Quantum Cryptography protection
python pqc_protection.py

# Small RSA complete attack demonstration
python small_rsa_demo.py
```

## 📚 The Threat Explained

### What is "Harvest Now, Decrypt Later"?

1. **TODAY**: Adversaries intercept and store encrypted communications
2. **TOMORROW**: When quantum computers are available, they decrypt the stored data
3. **CONSEQUENCE**: Secrets that are secure today become exposed in the future

### Timeline

- **Current**: RSA encryption is secure against classical computers
- **~2030-2035**: Large-scale quantum computers may become available
- **Risk Window**: Any data encrypted today with RSA could be vulnerable for decades

### Why RSA is Vulnerable

RSA security is based on the difficulty of factoring large numbers:
- Classical computers: Takes centuries to factor 2048-bit RSA keys
- Quantum computers + Shor's Algorithm: Can factor in polynomial time (hours/minutes)

## 🔐 Post-Quantum Cryptography (PQC)

PQC algorithms are designed to resist attacks from both classical and quantum computers:

- **Kyber**: Lattice-based key encapsulation (NIST standard)
- **Security Basis**: Learning With Errors (LWE) problem
- **Status**: NIST standardized in 2024
- **Advantages**:
  - Quantum-resistant
  - Smaller key sizes than RSA (in some cases)
  - Faster operations
  - No known quantum algorithm can break it

## 📖 Technical Details

### Project Structure

```
harvest_now/
├── harvest_now_demo.py       # Main demonstration script
├── small_rsa_demo.py          # Small key complete attack demo
├── rsa_simulation.py          # RSA key exchange and encryption
├── shors_algorithm.py         # Shor's algorithm simulation
├── pqc_protection.py          # PQC protection demonstration
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

### Key Components

#### 1. RSA Simulation (`rsa_simulation.py`)
- Generates RSA key pairs (1024-bit for demonstration)
- Encrypts messages with public key
- Demonstrates typical secure communication
- Shows what data an adversary can capture

#### 2. Shor's Algorithm (`shors_algorithm.py`)
- Simulates quantum factorization
- Factors the RSA modulus to derive private key
- Shows the quantum threat in action
- *Note: Uses classical factorization as simulation; explains quantum advantage*

#### 3. PQC Protection (`pqc_protection.py`)
- Demonstrates quantum-resistant encryption
- Compares PQC with RSA
- Explains why PQC is quantum-resistant
- Shows the path forward

#### 4. Small RSA Demo (`small_rsa_demo.py`)
- Uses very small primes (61, 53) for complete demonstration
- Actually factors the modulus to show complete attack
- Perfect for understanding the full attack cycle
- Educational visualization of the threat

## 🎓 Educational Use

This demonstrator is perfect for:

- **Security Training**: Teaching about quantum threats
- **Academic Research**: Understanding PQC concepts
- **Awareness Campaigns**: Demonstrating why migration to PQC is urgent
- **Technical Presentations**: Illustrating cryptographic vulnerabilities

## ⚠️ Important Notes

1. **Simulation**: This uses classical factorization to simulate Shor's algorithm for educational purposes
2. **Key Sizes**: Uses smaller RSA keys (1024-bit) for demonstration that can be factored more quickly
3. **Real Threat**: Real-world RSA uses 2048-4096 bit keys, which are currently secure but vulnerable to future quantum computers
4. **Not for Production**: This is an educational tool, not production cryptographic software

## 🔬 Technical Background

### Shor's Algorithm Complexity
- Classical factoring: O(exp(∛(ln N ln ln N)))
- Shor's algorithm: O((log N)³)
- This exponential to polynomial reduction is what makes quantum computers so threatening

### PQC Standards (NIST 2024)
- **Kyber**: Key encapsulation mechanism
- **Dilithium**: Digital signatures
- **Falcon**: Compact digital signatures
- **SPHINCS+**: Hash-based signatures

## 🛠️ Requirements

- Python 3.8+
- cryptography library
- pycryptodome
- (Optional) qiskit for quantum simulations

See `requirements.txt` for complete dependencies.

## 📜 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:
- Real quantum circuit implementations with Qiskit
- Additional PQC algorithm demonstrations
- Performance benchmarks
- Interactive visualizations

## 📚 Further Reading

- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [Shor's Algorithm Paper](https://arxiv.org/abs/quant-ph/9508027)
- [Quantum Threat Timeline](https://globalriskinstitute.org/publications/quantum-threat-timeline-report-2020/)

## 🎯 Call to Action

**The time to act is NOW:**
- Start planning migration to PQC
- Identify sensitive data that needs long-term protection
- Implement crypto-agility in your systems
- Don't wait until quantum computers are here—it will be too late!

---

**Remember**: Data encrypted today with RSA could be vulnerable tomorrow. Protect your future by adopting PQC today!
