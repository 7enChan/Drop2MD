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
