# 🚀 Deployment Guide

## Deploy to Streamlit Community Cloud (FREE)

### Prerequisites
- GitHub account (you already have this ✓)
- Public repository (rheacisa/harvest_now is public ✓)

### Deployment Steps

1. **Go to Streamlit Community Cloud**
   - Visit: https://share.streamlit.io
   - Click "Sign in with GitHub"
   - Authorize Streamlit to access your repos

2. **Create New App**
   - Click "New app" button
   - Select your repository: `rheacisa/harvest_now`
   - Branch: `main` (or your preferred branch)
   - Main file path: `web_demo.py`
   - Click "Deploy!"

3. **Wait for Deployment** (~2-5 minutes)
   - Streamlit will install dependencies from `requirements.txt`
   - You'll see the build logs in real-time
   - Once complete, you'll get your public URL

4. **Your Public URL**
   - Format: `https://[app-name]-[random-string].streamlit.app`
   - Or: `https://harvest-now.streamlit.app` (if available)
   - Share this URL anywhere!

### Post-Deployment

**Automatic Updates:**
- Every time you push to GitHub, the app auto-updates
- Changes deploy in ~1-2 minutes

**Custom URL (Optional):**
- In Streamlit settings, you can customize your app name
- Makes the URL prettier for your resume

**App Management:**
- View logs and analytics in Streamlit dashboard
- Restart app if needed
- Monitor resource usage

### Troubleshooting

**If deployment fails:**
1. Check the logs in Streamlit dashboard
2. Ensure all dependencies are in `requirements.txt`
3. Verify Python version compatibility (3.8-3.11)

**If app is slow:**
- Streamlit free tier has 1GB RAM limit
- Demo runs fine within limits
- Consider caching if needed

### Alternative: Deploy to Hugging Face Spaces

1. Go to https://huggingface.co/spaces
2. Create new Space
3. Select "Streamlit" as SDK
4. Upload or link your repo
5. Get URL: `https://huggingface.co/spaces/rheacisa/harvest-now`

## 📝 Add to Your Resume

Once deployed, use this format:

```
Quantum Threat Demonstrator
🔗 Live Demo: https://harvest-now.streamlit.app
💻 GitHub: github.com/rheacisa/harvest_now

Interactive web application demonstrating "Harvest Now, Decrypt Later" 
quantum computing threats and post-quantum cryptography solutions. 
Built with Python, Streamlit, and implements RSA-KEM, Shor's algorithm 
simulation, and NIST-standardized ML-KEM/Kyber.

Technologies: Python, Streamlit, Cryptography, Qiskit, Post-Quantum 
Cryptography, Web Development
```

## 🎉 You're Done!

Your demo will be publicly accessible and free forever on Streamlit Community Cloud.
