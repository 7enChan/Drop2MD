FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# 安装 uv
RUN pip install uv

# 复制项目文件
COPY pyproject.toml .
COPY src/ ./src/
COPY data/ ./data/

# 创建虚拟环境并安装依赖
RUN uv venv .venv
RUN uv pip install -e .

# 暴露端口
EXPOSE 8501

# 健康检查
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# 启动命令
ENTRYPOINT ["/app/.venv/bin/streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"] 