# MarkItDown WebUI 部署指南

## 🚀 快速部署选项

### 方案一：Streamlit Cloud（推荐 - 免费）

**优势：** 免费、简单、自动更新

1. **准备代码**
   ```bash
   # 创建 requirements.txt
   echo "streamlit>=1.32.0
   markitdown[all]>=0.1.2" > requirements.txt
   
   # 推送到 GitHub
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **部署步骤**
   - 访问 [share.streamlit.io](https://share.streamlit.io)
   - 使用 GitHub 账号登录
   - 选择仓库和分支
   - 主文件路径：`src/app.py`
   - 自动部署完成

3. **访问应用**
   - 获得类似 `https://your-app.streamlit.app` 的链接

---

### 方案二：Railway 部署

**优势：** 支持自定义域名、更多配置选项

1. **安装 Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **部署**
   ```bash
   railway login
   railway init
   railway up
   ```

3. **配置环境变量**（可选）
   - `PORT=8501`
   - `STREAMLIT_SERVER_HEADLESS=true`

---

### 方案三：Docker 部署

**优势：** 可部署到任何支持 Docker 的平台

1. **本地构建和运行**
   ```bash
   # 构建镜像
   docker build -t markitdown-webui .
   
   # 运行容器
   docker run -p 8501:8501 markitdown-webui
   ```

2. **使用 Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **部署到云平台**
   - **Google Cloud Run**
   - **AWS ECS**
   - **Azure Container Instances**

---

### 方案四：VPS 部署

**适用于：** 有云服务器的用户

1. **服务器配置**
   ```bash
   # 克隆项目
   git clone <your-repo>
   cd markitdown-webui
   
   # 安装 uv
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source ~/.local/bin/env
   
   # 设置项目
   uv venv .venv
   source .venv/bin/activate
   uv pip install -e .
   ```

2. **使用 systemd 服务**
   ```bash
   # 创建服务文件
   sudo tee /etc/systemd/system/markitdown.service > /dev/null <<EOF
   [Unit]
   Description=MarkItDown WebUI
   After=network.target
   
   [Service]
   Type=simple
   User=your-username
   WorkingDirectory=/path/to/markitdown-webui
   ExecStart=/path/to/markitdown-webui/.venv/bin/streamlit run src/app.py --server.port 8501 --server.address 0.0.0.0
   Restart=always
   
   [Install]
   WantedBy=multi-user.target
   EOF
   
   # 启动服务
   sudo systemctl enable markitdown
   sudo systemctl start markitdown
   ```

3. **配置反向代理**（Nginx）
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

## 📋 部署清单

### 必需文件
- ✅ `src/app.py` - 主应用
- ✅ `src/config.py` - 配置文件
- ✅ `src/utils.py` - 工具函数
- ✅ `pyproject.toml` - 项目配置

### 部署配置文件
- ✅ `requirements.txt` - Streamlit Cloud 需要
- ✅ `Dockerfile` - Docker 部署
- ✅ `docker-compose.yml` - Docker Compose 部署

### 环境变量
```bash
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

---

## 🔧 部署后配置

### 性能优化
- 设置合适的文件大小限制
- 配置缓存策略
- 监控内存使用情况

### 安全考虑
- 使用 HTTPS
- 设置文件类型白名单
- 配置速率限制

### 监控和维护
- 设置日志记录
- 配置健康检查
- 定期更新依赖

---

## 💡 推荐方案

**新手用户：** Streamlit Cloud（免费、简单）
**进阶用户：** Railway 或 Docker
**企业用户：** VPS + Docker + 反向代理

选择最适合您需求的部署方案！ 