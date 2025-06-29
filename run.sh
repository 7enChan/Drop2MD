#!/bin/bash
# Quick start script
echo "🚀 Starting Drop2MD..."
source .venv/bin/activate
streamlit run src/app.py --server.port 8501 --server.address localhost
