# Drop2MD Deployment Guide

## 🚀 Quick Deployment Options

### Option 1: Streamlit Cloud (Recommended - Free)

**Advantages:** Free, simple, auto-updates

1. **Prepare Code**
   ```bash
   # Create requirements.txt
   echo "streamlit>=1.32.0
   markitdown[all]>=0.1.2" > requirements.txt
   
   # Push to GitHub
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deployment Steps**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Login with GitHub account
   - Select repository and branch
   - Main file path: `src/app.py`
   - Auto-deployment complete

3. **Access Application**
   - Get a URL like `https://your-app.streamlit.app`

---

### Option 3: Docker Deployment

**Advantages:** Can be deployed to any Docker-compatible platform

1. **Local Build and Run**
   ```bash
   # Build image
   docker build -t drop2md .
   
   # Run container
   docker run -p 8501:8501 drop2md
   ```

2. **Use Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Deploy to Cloud Platforms**
   - **Google Cloud Run**
   - **AWS ECS**
   - **Azure Container Instances**

---

### Option 4: VPS Deployment

**Suitable for:** Users with cloud servers

1. **Server Setup**
   ```bash
   # Clone project
   git clone <your-repo>
   cd Drop2MD
   
   # Install uv
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source ~/.local/bin/env
   
   # Setup project
   uv venv .venv
   source .venv/bin/activate
   uv pip install -e .
   ```

2. **Use systemd Service**
   ```bash
   # Create service file
   sudo tee /etc/systemd/system/markitdown.service > /dev/null <<EOF
   [Unit]
   Description=Drop2MD
   After=network.target
   
   [Service]
   Type=simple
   User=your-username
   WorkingDirectory=/path/to/Drop2MD
   ExecStart=/path/to/Drop2MD/.venv/bin/streamlit run src/app.py --server.port 8501 --server.address 0.0.0.0
   Restart=always
   
   [Install]
   WantedBy=multi-user.target
   EOF
   
   # Start service
   sudo systemctl enable markitdown
   sudo systemctl start markitdown
   ```

3. **Configure Reverse Proxy** (Nginx)
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://localhost:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```

---

## 📋 Deployment Checklist

### Required Files
- ✅ `src/app.py` - Main application
- ✅ `src/config.py` - Configuration file
- ✅ `src/utils.py` - Utility functions
- ✅ `pyproject.toml` - Project configuration

### Deployment Configuration Files
- ✅ `requirements.txt` - For Streamlit Cloud
- ✅ `Dockerfile` - For Docker deployment
- ✅ `docker-compose.yml` - For Docker Compose deployment

### Environment Variables
```bash
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

---

## 🔧 Post-Deployment Configuration

### Performance Optimization
- Set appropriate file size limits
- Configure caching strategies
- Monitor memory usage

### Security Considerations
- Use HTTPS
- Set file type whitelist
- Configure rate limiting

### Monitoring and Maintenance
- Set up logging
- Configure health checks
- Regular dependency updates

---

## 💡 Recommended Solutions

**Beginners:** Streamlit Cloud (free, simple)
**Advanced Users:** Docker
**Enterprise:** VPS + Docker + Reverse Proxy

Choose the deployment solution that best fits your needs! 