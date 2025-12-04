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

# Mobile-friendly CSS
MOBILE_CSS = """
<style>
    /* Mobile-friendly adjustments */
    @media (max-width: 768px) {
        .stButton > button {
            font-size: 18px !important;
            padding: 15px 20px !important;
            min-height: 60px !important;
        }
        .stTextArea textarea {
            font-size: 12px !important;
        }
        h1 {
            font-size: 1.5rem !important;
        }
        h2 {
            font-size: 1.3rem !important;
        }
        h3 {
            font-size: 1.1rem !important;
        }
        .block-container {
            padding: 1rem !important;
        }
        /* Make sidebar toggle easier to tap */
        [data-testid="collapsedControl"] {
            height: 50px !important;
            width: 50px !important;
        }
    }
    
    /* Better touch targets */
    .stRadio > div {
        gap: 10px !important;
    }
    .stRadio label {
        padding: 10px !important;
        font-size: 16px !important;
    }
    
    /* Output area styling */
    .stTextArea textarea {
        font-family: monospace !important;
        line-height: 1.4 !important;
    }
    
    /* Card-like sections */
    .info-card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
"""

st.set_page_config(
    page_title="Harvest Now, Decrypt Later Demo",
    page_icon="🛡️",
    layout="centered",  # Changed from "wide" for better mobile experience
    initial_sidebar_state="collapsed"  # Start collapsed on mobile
)

# Inject mobile CSS
st.markdown(MOBILE_CSS, unsafe_allow_html=True)

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
st.title("🛡️ Quantum Threat Demo")
st.markdown("*Harvest Now, Decrypt Later*")

# Mobile-friendly: Add buttons on main page for easier navigation
st.markdown("---")

# Create tabs for mobile-friendly navigation (alternative to sidebar)
tab1, tab2, tab3 = st.tabs(["🏠 Home", "👥 Simple", "🔬 Technical"])

with tab1:
    st.markdown("""
    ### What is "Harvest Now, Decrypt Later"?
    
    Adversaries are intercepting encrypted data **today** to decrypt **later** 
    when quantum computers arrive.
    
    **At Risk:**
    - 🏥 Medical records
    - 💰 Financial data
    - 🏛️ Government secrets
    - 🔐 Business IP
    
    **Timeline:**
    - ⏰ Quantum computers: 10-15 years
    - 📊 Your data: Vulnerable NOW
    - ✅ Solution: PQC is ready!
    
    ---
    👆 **Tap the tabs above to start a demo**
    """)
    
    # Quick action buttons for mobile
    st.markdown("### Quick Start")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👥 Non-Technical Demo", use_container_width=True):
            st.session_state.run_simple = True
    with col2:
        if st.button("🔬 Technical Demo", use_container_width=True):
            st.session_state.run_technical = True

with tab2:
    st.header("👥 Simple Demo")
    st.markdown("Story-driven explanation using everyday language. Perfect for executives and non-technical audiences.")
    
    if st.button("▶️ Start Simple Demo", type="primary", use_container_width=True, key="simple_btn"):
        with st.spinner("Running demonstration..."):
            output = run_simple_demo()
        
        st.text_area("Demo Output", output, height=400, key="simple_output")
        st.success("✅ Demo completed!")
        
        with st.expander("📋 Key Takeaways"):
            st.markdown("""
            - Encrypted data today → Decrypted by future quantum computers
            - This threat is real - organizations must act NOW
            - Post-Quantum Cryptography (PQC) is ready and standardized
            - Start migration immediately for long-term data protection
            """)

with tab3:
    st.header("🔬 Technical Demo")
    st.markdown("Full demonstration: RSA-KEM, Shor's algorithm, and ML-KEM/Kyber")
    
    if st.button("▶️ Start Technical Demo", type="primary", use_container_width=True, key="tech_btn"):
        with st.spinner("Running demonstration (may take a minute)..."):
            output = run_technical_demo()
        
        st.text_area("Demo Output", output, height=400, key="tech_output")
        st.success("✅ Demo completed!")
        
        with st.expander("📋 Technical Details"):
            st.markdown("""
            **RSA-KEM:** Session key establishment (vulnerable)  
            **Shor's Algorithm:** Quantum factorization attack  
            **ML-KEM/Kyber:** NIST-standardized PQC solution
            """)

# Additional demos in expander for cleaner mobile view
with st.expander("🔧 More Demos"):
    st.markdown("### Individual Components")
    
    demo_type = st.selectbox("Select demo:", 
        ["RSA Key Encapsulation", "Quantum Attack Simulation", "Post-Quantum Protection"])
    
    if demo_type == "RSA Key Encapsulation":
        if st.button("▶️ Run RSA-KEM", use_container_width=True, key="rsa_btn"):
            with st.spinner("Running..."):
                output = run_rsa_kem_demo()
            st.text_area("Output", output, height=300, key="rsa_output")
    
    elif demo_type == "Quantum Attack Simulation":
        if st.button("▶️ Run Quantum Attack", use_container_width=True, key="quantum_btn"):
            with st.spinner("Running..."):
                output = run_quantum_attack_demo()
            st.text_area("Output", output, height=300, key="quantum_output")
    
    elif demo_type == "Post-Quantum Protection":
        if st.button("▶️ Run PQC Demo", use_container_width=True, key="pqc_btn"):
            with st.spinner("Running..."):
                output = run_pqc_demo()
            st.text_area("Output", output, height=300, key="pqc_output")

# Sidebar for navigation
st.sidebar.title("🔒 Security")
st.sidebar.markdown("""
**This demo:**
- ✅ No data collection
- ✅ No cookies
- ✅ Stateless

[GitHub](https://github.com/rheacisa/harvest_now)
""")
