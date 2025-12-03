# Quick Reference Guide

## For Different Audiences

### Non-Technical Audiences (Executives, Managers, Board Members)
**Run:**
```bash
python simple_demo.py
```
**What it does:** Story-driven explanation using everyday analogies (locked boxes, keys). No technical jargon.
**Duration:** 10-15 minutes
**Best for:** Understanding the business impact and urgency

### Technical Audiences (Engineers, Security Teams)
**Run:**
```bash
python main_demo.py
```
**What it does:** Full technical demonstration of RSA-KEM, Shor's algorithm (shors_break_rsa), and ML-KEM/Kyber
**Duration:** 20-30 minutes
**Best for:** Understanding technical implementation and migration needs

### Quick Technical Overview
**Run:**
```bash
python main_demo.py --quick
```
**What it does:** Same as main demo but runs automatically without pauses
**Duration:** 10-15 minutes
**Best for:** Time-constrained technical presentations

### Educational - Complete Attack Cycle
**Run:**
```bash
python small_rsa_demo.py
```
**What it does:** Uses small RSA keys that can actually be factored to show the complete attack
**Duration:** 5-10 minutes
**Best for:** Understanding the step-by-step attack process

## Individual Component Testing

### Test RSA Key Encapsulation (Vulnerable)
```bash
python key_encapsulation.py
```
Shows how session keys are established with RSA-KEM and what adversaries can harvest.

### Test Quantum Attack Simulation
```bash
python quantum_attack.py
```
Note: This module contains functions used by other demos. Run main_demo.py for complete demonstration.

### Test PQC Solution
```bash
python pqc_kem.py
```
Shows ML-KEM (Kyber) quantum-resistant key encapsulation and why it resists attacks.

## Key Concepts Demonstrated

### 1. The Vulnerable Handshake (RSA-KEM)
- How RSA is used for key encapsulation today
- What data adversaries can harvest
- Why it's secure now but vulnerable later

### 2. The Quantum Threat (Shor's Algorithm)
- `shors_break_rsa(public_key_params)` - simulates quantum attack
- Factors RSA modulus to derive private key
- Decrypts harvested session keys
- Timeline: 10-20 years until large quantum computers

### 3. The PQC Solution (ML-KEM/Kyber)
- Quantum-resistant key encapsulation
- Based on lattice problems, not factorization
- `shors_fail_on_kyber()` - shows quantum attacks fail
- NIST standardized in 2024

## Presentation Tips

### For Executives (15-minute presentation)
1. Run `simple_demo.py` - follow the story
2. Key points to emphasize:
   - Adversaries are harvesting encrypted data RIGHT NOW
   - In 10-20 years they'll decrypt it with quantum computers
   - Need to act NOW to protect long-term secrets
3. Call to action: Start PQC migration planning

### For Technical Teams (30-minute presentation)
1. Run `main_demo.py` interactively
2. Key points to emphasize:
   - RSA-KEM is vulnerable to Shor's algorithm
   - `shors_break_rsa()` demonstrates the attack vector
   - ML-KEM/Kyber provides quantum resistance
3. Call to action: Begin crypto-agility implementation

### For Security Training (45-minute session)
1. Start with `simple_demo.py` for context (10 min)
2. Run `main_demo.py` for technical details (20 min)
3. Run `small_rsa_demo.py` to show complete attack (10 min)
4. Q&A and discussion (5 min)

## Troubleshooting

### Import Errors
```bash
pip install -r requirements.txt
```

### Demo Runs Too Fast
Use the interactive modes (don't use --quick flag) for pauses between steps.

### Want to Skip Pauses
Use `--quick` flag or redirect empty input:
```bash
echo "" | python main_demo.py
```

## Key Takeaways for All Audiences

1. **The Threat is Real**: Quantum computers WILL break RSA encryption
2. **Time is Running Out**: 10-20 years until large quantum computers
3. **Harvest Now, Decrypt Later**: Adversaries are collecting data TODAY
4. **Solution Exists**: Post-Quantum Cryptography (PQC) is ready
5. **Act Now**: Start migration before it's too late

## Resume/Interview Talking Points

This project demonstrates understanding of:
- ✅ Shor's Algorithm and its implications for RSA
- ✅ Key exchange vulnerabilities (RSA-KEM vs ML-KEM)
- ✅ "Harvest Now, Decrypt Later" attack scenario
- ✅ Practical necessity of PQC algorithms (ML-KEM/Kyber)
- ✅ NIST PQC standards and migration considerations
- ✅ Ability to explain complex technical concepts to non-technical audiences
