#!/bin/bash
# MarkItDown WebUI 项目设置脚本 (使用 uv)

set -e  # 遇到错误立即退出

PROJECT_NAME="markitdown-webui"
PYTHON_VERSION="3.12"

echo "🚀 使用 uv 创建 MarkItDown WebUI 项目..."

# 检查是否安装了 uv
if ! command -v uv &> /dev/null; then
    echo "❌ 请先安装 uv:"
    echo "   brew install uv"
    echo "   或者: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# 1. 使用 uv 创建虚拟环境（自动管理 Python 版本）
echo "📦 创建虚拟环境..."
uv venv --python=$PYTHON_VERSION .venv

# 2. 创建项目结构
echo "📁 创建项目结构..."
mkdir -p {src,tests,docs,data/{input,output,temp}}

# 3. 创建 pyproject.toml（现代 Python 项目配置）
echo "⚙️ 创建项目配置..."
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

# 4. 创建 .gitignore
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

# 虚拟环境
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

# 项目特定
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

# 5. 创建保持目录的文件
touch data/input/.gitkeep
touch data/output/.gitkeep
touch data/temp/.gitkeep

# 6. 激活虚拟环境并安装依赖
echo "📦 安装依赖..."
source .venv/bin/activate

# 使用 uv pip 安装依赖
uv pip install -e .

# 7. 安装开发依赖
echo "🔧 安装开发依赖..."
uv pip install -e ".[dev]"

# 8. 创建启动脚本
cat > run.sh << 'EOF'
#!/bin/bash
# 快速启动脚本
echo "🚀 启动 MarkItDown WebUI..."
source .venv/bin/activate
streamlit run src/app.py --server.port 8501 --server.address localhost
EOF

chmod +x run.sh

# 9. 创建 README
cat > README.md << 'EOF'
# MarkItDown WebUI

现代化的文件转换 WebUI，基于 MarkItDown 构建。

## 功能特点

- 🚀 支持多种文件格式转换为 Markdown
- 🎨 现代化的 Web 界面
- ⚡ 基于 uv 的快速包管理
- 🔒 隔离的虚拟环境，不污染系统

## 支持格式

- 📄 PDF、Word、PowerPoint、Excel
- 🖼️ 图像文件（JPG、PNG 等）
- 🎵 音频文件（MP3、WAV 等）
- 🌐 HTML、XML、JSON、CSV
- 📚 ZIP、EPUB 等

## 快速开始

```bash
# 一键启动
./run.sh

# 或者手动启动
source .venv/bin/activate
streamlit run src/app.py
```

## 开发

```bash
# 激活环境
source .venv/bin/activate

# 安装新依赖
uv pip install package-name

# 运行测试
pytest tests/

# 代码格式化
black src/
ruff check src/
```

## 项目结构

```
markitdown-webui/
├── .venv/              # 虚拟环境
├── src/               # 源代码
│   ├── app.py        # 主应用
│   ├── config.py     # 配置
│   └── utils.py      # 工具函数
├── data/             # 数据目录
├── tests/            # 测试
└── docs/             # 文档
```
EOF

echo "🎉 项目设置完成！"
echo ""
echo "接下来的步骤："
echo "1. ./run.sh  # 一键启动应用"
echo "2. 打开浏览器访问: http://localhost:8501"
echo ""
echo "开发模式："
echo "1. source .venv/bin/activate  # 激活环境"
echo "2. streamlit run src/app.py   # 启动应用"
echo "3. deactivate                 # 完成后退出环境" 