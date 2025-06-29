#!/bin/bash
# MarkItDown WebUI project setup script (using uv)

set -e  # Exit immediately on error

PROJECT_NAME="markitdown-webui"
PYTHON_VERSION="3.12"

echo "🚀 Creating MarkItDown WebUI project with uv..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ Please install uv first:"
    echo "   brew install uv"
    echo "   or: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# 1. Create virtual environment with uv (auto-manages Python version)
echo "📦 Creating virtual environment..."
uv venv --python=$PYTHON_VERSION .venv

# 2. Create project structure
echo "📁 Creating project structure..."
mkdir -p {src,tests,docs,data/{input,output,temp}}

# 3. Create pyproject.toml (modern Python project configuration)
echo "⚙️ Creating project configuration..."
cat > pyproject.toml << 'EOF'
[project]
name = "markitdown-webui"
version = "1.0.0"
description = "A modern WebUI for MarkItDown file conversion"
authors = [
    {name = "Developer", email = "dev@example.com"}
]
dependencies = [
    "streamlit>=1.32.0",
    "markitdown[all]>=0.1.2",
]
requires-python = ">=3.10"

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "pre-commit>=3.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src"]

[tool.black]
line-length = 88
target-version = ['py310']

[tool.ruff]
line-length = 88
target-version = "py310"
EOF

# 4. Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environment
.venv/
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# macOS
.DS_Store

# Project specific
data/input/*
data/output/*
data/temp/*
!data/input/.gitkeep
!data/output/.gitkeep
!data/temp/.gitkeep

# Streamlit
.streamlit/
secrets.toml

# uv
.python-version
EOF

# 5. Create directory placeholder files
touch data/input/.gitkeep
touch data/output/.gitkeep
touch data/temp/.gitkeep

# 6. Activate virtual environment and install dependencies
echo "📦 Installing dependencies..."
source .venv/bin/activate

# Install dependencies using uv pip
uv pip install -e .

# 7. Install development dependencies
echo "🔧 Installing development dependencies..."
uv pip install -e ".[dev]"

# 8. Create startup script
cat > run.sh << 'EOF'
#!/bin/bash
# Quick start script
echo "🚀 Starting MarkItDown WebUI..."
source .venv/bin/activate
streamlit run src/app.py --server.port 8501 --server.address localhost
EOF

chmod +x run.sh

echo "🎉 Project setup complete!"
echo ""
echo "Next steps:"
echo "1. ./run.sh  # Start the application"
echo "2. Open browser at: http://localhost:8501"
echo ""
echo "Development mode:"
echo "1. source .venv/bin/activate  # Activate environment"
echo "2. streamlit run src/app.py   # Start application"
echo "3. deactivate                 # Exit environment when done" 