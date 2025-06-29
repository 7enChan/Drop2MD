#!/bin/bash
# 快速启动脚本
echo "🚀 启动 MarkItDown WebUI..."
source .venv/bin/activate
streamlit run src/app.py --server.port 8501 --server.address localhost
