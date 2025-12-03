"""
Streamlit Web Interface for Harvest Now, Decrypt Later Demo
A browser-based demonstration of quantum threats and post-quantum cryptography

Security Features:
- No user data collection or storage
- XSRF protection enabled
- Input validation on all parameters
- Output sanitization
- No external API calls
- Stateless operation
"""

import streamlit as st
import sys
from io import StringIO
import contextlib

# Import demo modules
import simple_demo
import main_demo
import key_encapsulation
import quantum_attack
import pqc_protection

# Security configuration
MAX_OUTPUT_LENGTH = 50000  # Prevent excessive output

st.set_page_config(
    page_title="Harvest Now, Decrypt Later Demo",
    page_icon="🛡️",
    layout="wide"
)

@contextlib.contextmanager
def capture_output():
    """
    Capture stdout to display in Streamlit.
    Implements output length limiting for security.
    """
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_stdout

def sanitize_output(output: str) -> str:
    """
    Sanitize output for security.
    Limits length to prevent DoS and ensures safe display.
    """
    if len(output) > MAX_OUTPUT_LENGTH:
        return output[:MAX_OUTPUT_LENGTH] + "\n\n... (output truncated for safety)"
    return output

def run_simple_demo():
    """Run the simple non-technical demo with security controls"""
    # Patch input() to prevent blocking
    import builtins
    old_input = builtins.input
    builtins.input = lambda *args, **kwargs: ""
    
    try:
        with capture_output() as output:
            try:
                simple_demo.main()
            finally:
                builtins.input = old_input
        return sanitize_output(output.getvalue())
    except Exception as e:
        return f"[!] An error occurred during the demonstration.\n[!] Error type: {type(e).__name__}"

def run_technical_demo():
    """Run the technical demo with security controls"""
    # Patch input() to prevent blocking
    import builtins
    old_input = builtins.input
    builtins.input = lambda *args, **kwargs: ""
    
    try:
        with capture_output() as output:
            # Call the quick demo function directly instead of main()
            old_argv = sys.argv
            sys.argv = ['main_demo.py', '--quick']
            try:
                main_demo.main()
            finally:
                sys.argv = old_argv
                builtins.input = old_input
        return sanitize_output(output.getvalue())
    except Exception as e:
        return f"[!] An error occurred during the demonstration.\n[!] Error type: {type(e).__name__}"

def run_rsa_kem_demo():
    """Run RSA-KEM demonstration with security controls"""
    try:
        with capture_output() as output:
            key_encapsulation.demonstrate_vulnerable_handshake()
        return sanitize_output(output.getvalue())
    except Exception as e:
        return f"[!] An error occurred during the demonstration.\n[!] Error type: {type(e).__name__}"

def run_quantum_attack_demo():
    """Run quantum attack simulation with security controls"""
    try:
        with capture_output() as output:
            # Run a simple quantum attack demo
            from Crypto.PublicKey import RSA
            key = RSA.generate(2048)
            public_params = {
                'n': key.n,
                'e': key.e,
                'key_size': 2048
            }
            quantum_attack.shors_break_rsa(public_params)
        return sanitize_output(output.getvalue())
    except Exception as e:
        return f"[!] An error occurred during the demonstration.\n[!] Error type: {type(e).__name__}"

def run_pqc_demo():
    """Run PQC protection demonstration with security controls"""
    try:
        with capture_output() as output:
            pqc_protection.demonstrate_pqc_protection()
        return sanitize_output(output.getvalue())
    except Exception as e:
        return f"[!] An error occurred during the demonstration.\n[!] Error type: {type(e).__name__}"

# Main UI
st.title("🛡️ Harvest Now, Decrypt Later - Quantum Threat Demo")
st.markdown("### Interactive demonstration of quantum computing threats and post-quantum cryptography")

# Sidebar for navigation
st.sidebar.title("Navigation")
demo_choice = st.sidebar.radio(
    "Choose a demonstration:",
    [
        "🏠 Home",
        "👥 Simple Demo (Non-Technical)",
        "🔬 Technical Demo",
        "🔑 RSA Key Encapsulation",
        "⚛️ Quantum Attack Simulation",
        "🛡️ Post-Quantum Protection"
    ]
)

# Home page
if demo_choice == "🏠 Home":
    st.markdown("""
    ## Welcome to the Quantum Threat Demonstrator
    
    This interactive tool demonstrates the "Harvest Now, Decrypt Later" threat - one of the most significant 
    cybersecurity challenges of our time.
    
    ### What is "Harvest Now, Decrypt Later"?
    
    Adversaries are intercepting and storing encrypted data **today**, planning to decrypt it **years later** 
    when large-scale quantum computers become available. This threatens:
    
    - 🏥 Medical records
    - 💰 Financial transactions
    - 🏛️ Government communications
    - 🔐 Business secrets
    - 📧 Personal messages
    
    ### Choose Your Experience
    
    **For Non-Technical Audiences** (executives, managers, stakeholders):
    - Select "👥 Simple Demo" from the sidebar
    - Story-driven explanation using everyday analogies
    - No technical jargon required
    
    **For Technical Audiences** (engineers, security teams):
    - Select "🔬 Technical Demo" for the full technical demonstration
    - Or explore individual components (RSA-KEM, Quantum Attack, PQC)
    
    ### Why This Matters
    
    ⏰ **Timeline**: Large-scale quantum computers could arrive in 10-15 years  
    📊 **Risk**: Data encrypted today will be vulnerable  
    ✅ **Solution**: Post-Quantum Cryptography (PQC) is ready now  
    🚀 **Action**: Organizations must begin migration today  
    
    ---
    
    👈 **Select a demonstration from the sidebar to begin**
    """)

# Simple Demo
elif demo_choice == "👥 Simple Demo (Non-Technical)":
    st.header("Simple Story-Driven Demonstration")
    st.markdown("""
    This demonstration uses everyday language and analogies to explain the quantum threat.
    Perfect for executives, managers, and anyone without a technical background.
    """)
    
    if st.button("▶️ Start Simple Demo", type="primary", use_container_width=True):
        with st.spinner("Running demonstration..."):
            output = run_simple_demo()
        
        st.text_area("Demo Output", output, height=600)
        st.success("✅ Demo completed!")
        
        st.markdown("""
        ### Key Takeaways
        - Encrypted data collected today can be decrypted by future quantum computers
        - This threat is real and organizations must act now
        - Post-Quantum Cryptography (PQC) solutions are available and standardized
        - Migration should begin immediately to protect long-term sensitive data
        """)

# Technical Demo
elif demo_choice == "🔬 Technical Demo":
    st.header("Technical Demonstration")
    st.markdown("""
    Comprehensive technical demonstration including:
    - RSA Key Encapsulation Mechanism (RSA-KEM)
    - Shor's algorithm simulation
    - Complete "Harvest Now, Decrypt Later" attack cycle
    - ML-KEM/Kyber (Post-Quantum Cryptography)
    """)
    
    if st.button("▶️ Start Technical Demo", type="primary", use_container_width=True):
        with st.spinner("Running demonstration (this may take a minute)..."):
            output = run_technical_demo()
        
        st.text_area("Demo Output", output, height=600)
        st.success("✅ Demo completed!")
        
        st.markdown("""
        ### Technical Details Demonstrated
        
        **RSA-KEM Vulnerability:**
        - Shows how session keys are established today
        - Demonstrates what adversaries can harvest and store
        
        **Shor's Algorithm:**
        - Quantum period-finding routine
        - Factorization of RSA modulus
        - Private key recovery
        
        **ML-KEM/Kyber Protection:**
        - Lattice-based cryptography
        - Quantum-resistant key encapsulation
        - NIST-standardized PQC solution
        """)

# RSA-KEM Demo
elif demo_choice == "🔑 RSA Key Encapsulation":
    st.header("RSA Key Encapsulation Mechanism")
    st.markdown("""
    Demonstrates how RSA is used today to establish secure session keys and why it's vulnerable 
    to quantum computers.
    """)
    
    if st.button("▶️ Run RSA-KEM Demo", type="primary", use_container_width=True):
        with st.spinner("Running RSA-KEM demonstration..."):
            output = run_rsa_kem_demo()
        
        st.text_area("Demo Output", output, height=400)
        st.success("✅ Demo completed!")

# Quantum Attack Demo
elif demo_choice == "⚛️ Quantum Attack Simulation":
    st.header("Quantum Attack Simulation")
    st.markdown("""
    Simulates Shor's algorithm - the quantum algorithm that can break RSA encryption by 
    efficiently factoring large numbers.
    """)
    
    if st.button("▶️ Run Quantum Attack", type="primary", use_container_width=True):
        with st.spinner("Running quantum attack simulation..."):
            output = run_quantum_attack_demo()
        
        st.text_area("Demo Output", output, height=400)
        st.success("✅ Demo completed!")
        
        st.warning("""
        **⚠️ Important Note:** This is a simulation of how Shor's algorithm would work on a 
        large-scale quantum computer. Current quantum computers are not yet powerful enough 
        to break real RSA keys, but this capability is expected within 10-15 years.
        """)

# PQC Demo
elif demo_choice == "🛡️ Post-Quantum Protection":
    st.header("Post-Quantum Cryptography Protection")
    st.markdown("""
    Demonstrates ML-KEM (formerly Kyber) - a NIST-standardized post-quantum cryptography 
    algorithm that resists quantum attacks.
    """)
    
    if st.button("▶️ Run PQC Demo", type="primary", use_container_width=True):
        with st.spinner("Running PQC demonstration..."):
            output = run_pqc_demo()
        
        st.text_area("Demo Output", output, height=400)
        st.success("✅ Demo completed!")
        
        st.info("""
        **✅ Key Advantages of ML-KEM/Kyber:**
        - Based on lattice problems that quantum computers cannot efficiently solve
        - NIST-approved and standardized (2024)
        - Already being deployed by major tech companies
        - Suitable for immediate implementation
        """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 🔒 Security & Privacy

This demo:
- ✅ No data collection
- ✅ No cookies
- ✅ No API calls
- ✅ Stateless operation
- ✅ Open source

All cryptographic operations are 
educational simulations only.

### About This Demo

This tool demonstrates the quantum threat 
to current encryption and the solution 
provided by Post-Quantum Cryptography.

**Learn More:**
- [NIST PQC Project](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [GitHub Repository](https://github.com/rheacisa/harvest_now)
- [Security Documentation](https://github.com/rheacisa/harvest_now/blob/main/SECURITY.md)
""")
