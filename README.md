# 🛡️ Harvest Now, Decrypt Later - Quantum Threat Demonstrator

A comprehensive demonstration of the "Harvest Now, Decrypt Later" quantum threat and Post-Quantum Cryptography (PQC) protection.

**Now with a simple, non-technical explanation mode perfect for executives and stakeholders!**

## 🎯 Overview

This project demonstrates one of the most significant cybersecurity threats of our time: adversaries can intercept and store encrypted data today, then decrypt it years later when large-scale quantum computers become available.

### What This Demonstrates

1. **RSA Key Encapsulation (RSA-KEM)**: Shows how session keys are established today and why they're vulnerable
2. **Shor's Algorithm Simulation**: Demonstrates how quantum computers can break RSA by factoring large numbers
3. **Harvest Now, Decrypt Later Attack**: Complete attack scenario showing the threat
4. **ML-KEM/Kyber (PQC)**: Shows how Post-Quantum Cryptography algorithms resist quantum attacks

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/rheacisa/harvest_now.git
cd harvest_now

# Install dependencies
pip install -r requirements.txt
```

### For Non-Technical Audiences 👥

**Simple Story-Driven Demo** (recommended for executives, managers, non-technical stakeholders):
```bash
python simple_demo.py
```

This provides a narrative explanation using everyday language and analogies - no technical knowledge required!

### For Technical Audiences 🔬

**Main Technical Demo** (shows actual RSA-KEM, Shor's algorithm, and ML-KEM):
```bash
python main_demo.py
```

**Quick Technical Demo** (non-interactive):
```bash
python main_demo.py --quick
```

**Small Key Demo** (shows complete attack with successful factorization):
```bash
python small_rsa_demo.py
```

### Individual Modules

You can also run individual technical components:

```bash
# Simple non-technical explanation
python simple_demo.py

# RSA-KEM (Key Encapsulation Mechanism)
python key_encapsulation.py

# Quantum attack simulation
python quantum_attack.py

# ML-KEM/Kyber PQC demonstration
python pqc_kem.py

# Small RSA complete attack demonstration
python small_rsa_demo.py

# Legacy modules (still functional)
python rsa_simulation.py
python shors_algorithm.py
python pqc_protection.py
```

## 📚 The Threat Explained (Simple Version)

### What is "Harvest Now, Decrypt Later"?

Think of it like this:

1. **TODAY**: 
   - You send an encrypted email to your bank
   - A spy intercepts it but can't read it (it's encrypted)
   - The spy saves it on a hard drive for later

2. **10-20 YEARS FROM NOW**: 
   - Quantum computers become powerful enough
   - The spy uses the quantum computer to break the encryption
   - The spy can now read your email from years ago

3. **THE PROBLEM**: 
   - Anything encrypted today could be exposed tomorrow
   - Medical records, trade secrets, government data - all at risk
   - The clock is ticking!

### Who Should Care?

- **🏥 Healthcare**: Patient records need protection for decades
- **🏛️ Government**: Classified information must stay secret long-term  
- **🏢 Businesses**: Trade secrets and intellectual property
- **🏦 Finance**: Transaction history and customer data
- **👤 Everyone**: Your private communications and personal data

### The Solution: Post-Quantum Cryptography (PQC)

PQC uses different types of "locks" that even quantum computers can't break:
- **ML-KEM (Kyber)**: Safe against quantum computers
- **NIST Approved**: Standardized in 2024
- **Available Now**: Can be deployed today

## 📚 The Threat Explained (Technical Version)

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
├── simple_demo.py             # 👥 Simple explanation for non-technical audiences
├── main_demo.py               # 🔬 Main technical demonstration (3 steps)
├── key_encapsulation.py       # RSA-KEM implementation
├── quantum_attack.py          # Shor's algorithm simulation (shors_break_rsa)
├── pqc_kem.py                 # ML-KEM/Kyber PQC implementation
├── small_rsa_demo.py          # Small key complete attack demo
├── harvest_now_demo.py        # Legacy demo (still functional)
├── rsa_simulation.py          # Legacy RSA module
├── shors_algorithm.py         # Legacy Shor's module
├── pqc_protection.py          # Legacy PQC module
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

### Key Components

#### 1. Simple Demo (`simple_demo.py`) 👥
- Story-driven explanation for non-technical audiences
- Uses everyday analogies (locked boxes, keys)
- No technical jargon or complex math
- Perfect for executive briefings and stakeholder presentations

#### 2. Main Technical Demo (`main_demo.py`) 🔬
- **Step 1**: RSA-KEM vulnerable handshake
- **Step 2**: Quantum attack with `shors_break_rsa()`
- **Step 3**: ML-KEM/Kyber PQC solution
- Follows execution steps with proper KEM demonstration

#### 3. Key Encapsulation (`key_encapsulation.py`)
- RSA-KEM (Key Encapsulation Mechanism) implementation
- Demonstrates how session keys are established
- Shows what adversaries can "harvest"
- Uses 2048-bit keys for realistic demonstration

#### 4. Quantum Attack (`quantum_attack.py`)
- `shors_break_rsa()` function - simulates quantum threat
- Factors RSA modulus and derives private key
- Decrypts harvested session keys
- Shows the "DECRYPT LATER" phase

#### 5. PQC Solution (`pqc_kem.py`)
- ML-KEM (Kyber-768) implementation simulation
- Demonstrates quantum-resistant key encapsulation
- Shows `shors_fail_on_kyber()` - quantum attacks don't work!
- Compares RSA-KEM vs ML-KEM side-by-side

## 🎓 Educational Use

This demonstrator is perfect for:

- **Executive Briefings**: Use `simple_demo.py` to explain the threat to non-technical leadership
- **Security Training**: Show IT teams why migration to PQC is urgent
- **Academic Research**: Understand quantum threats and PQC concepts
- **Awareness Campaigns**: Demonstrate why migration can't wait
- **Technical Presentations**: Illustrate cryptographic vulnerabilities with `main_demo.py`
- **Policy Discussions**: Provide concrete examples for cybersecurity policy

### Audience-Specific Recommendations

| Audience | Recommended Demo | Duration |
|----------|-----------------|----------|
| Executives, Board Members | `simple_demo.py` | 10-15 min |
| IT Leadership | `main_demo.py` | 20-30 min |
| Security Engineers | `main_demo.py` + individual modules | 45-60 min |
| Developers | `main_demo.py` --quick | 15-20 min |
| General Staff | `simple_demo.py` | 10 min |

## ⚠️ Important Notes

1. **Educational Purpose**: This is a demonstration tool for understanding the quantum threat, not production cryptographic software
2. **Simulation**: Uses classical factorization to simulate Shor's algorithm for educational purposes
3. **Key Sizes**: Uses various key sizes (1024-2048 bit) for demonstration; real-world typically uses 2048-4096 bit keys
4. **Real Threat**: The threat demonstrated here is REAL - quantum computers will break RSA
5. **Timeline**: Large-scale quantum computers expected in 10-20 years
6. **Action Required**: Organizations should start PQC migration NOW

## 📊 Demo Comparison

| Demo | Audience | Technical Level | Duration | Key Features |
|------|----------|----------------|----------|--------------|
| `simple_demo.py` | Everyone | None | 10-15 min | Story-driven, no jargon |
| `main_demo.py` | Technical | Medium-High | 20-30 min | Full 3-step process, KEM |
| `small_rsa_demo.py` | Technical | Medium | 10 min | Complete attack, small keys |
| Legacy demos | Technical | Medium | 15-20 min | Original implementations |

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
- Additional language translations for simple demo
- Real quantum circuit implementations with Qiskit
- Additional PQC algorithm demonstrations (Dilithium, Falcon, SPHINCS+)
- Performance benchmarks
- Interactive web-based visualizations
- PowerPoint/presentation templates

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

**For Questions or Presentations**: This repository includes both technical and non-technical demonstrations. Choose the right one for your audience!
