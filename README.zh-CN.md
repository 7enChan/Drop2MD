<p align="right">
  简体中文 | <a href="README.md">English 🇺🇸</a>
</p>

# Drop2MD

[![在线演示](https://img.shields.io/badge/在线-演示-brightgreen?logo=streamlit)](https://drop2md.streamlit.app/)

一个基于 Microsoft MarkItDown 的现代化、极简文件转换 Web 界面。

## 🤖 关于本项目

**本项目最初由 AI 启动并完全生成。**

## ✨ 功能亮点

- 🚀 将多种常见文件格式转换为 Markdown
- 🎨 极简、响应式的拖拽式界面（基于 Streamlit）
- ⚡ 使用 `uv` 进行极速依赖管理
- 🔒 独立虚拟环境，不污染系统 Python

## 📄 支持的格式

- 📄 **文档**: PDF, Word, PowerPoint, Excel
- 🖼️ **图片**: JPG, PNG, GIF, BMP, TIFF, WebP
- 🎵 **音频**: MP3, WAV, M4A, AAC
- 🌐 **网页**: HTML, XML, XHTML
- 📊 **数据**: JSON, CSV, YAML
- 📚 **压缩/电子书**: ZIP, EPUB
- 📝 **文本**: TXT, RTF, Markdown

## ⚙️ 安装与环境准备

下列两种方式任选其一。

### 方案 A — 使用 uv（推荐）

```bash
# 1. 创建并激活虚拟环境
uv venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. 安装全部依赖（运行 + 开发）
uv pip install -e ".[dev]"
```

### 方案 B — 原生 Python & pip（通用）

```bash
# 1. 创建并激活虚拟环境
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. 安装依赖
pip install -e .                 # 仅运行依赖
pip install -e ".[dev]"          # 开发工具（可选）
```

环境就绪后，继续下一步。

## 🚀 快速开始

```bash
# 一键启动
./run.sh

# 或手动启动
source .venv/bin/activate
streamlit run src/app.py
```

## 🛠️ 开发指南

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

# 退出虚拟环境
deactivate
```

## 📁 项目结构

```
Drop2MD/
├── .venv/              # 虚拟环境
├── src/               # 源代码
│   ├── app.py        # 主应用入口
│   ├── config.py     # 配置
│   └── utils.py      # 工具函数
├── data/             # 数据目录
│   ├── input/        # 输入文件
│   ├── output/       # 输出文件
│   └── temp/         # 临时文件
├── tests/            # 测试
├── docs/             # 文档
├── Dockerfile        # Docker 配置
├── docker-compose.yml # Docker Compose
├── requirements.txt  # 云部署依赖
└── DEPLOY.md         # 部署指南
```

## 🎯 技术栈

- **后端**: Python 3.12+，FastAPI 风格
- **前端**: Streamlit 快速构建 UI
- **包管理**: uv 极速依赖安装
- **核心引擎**: Microsoft MarkItDown 文件转换
- **容器化**: Docker & Docker Compose

## 🌐 部署

详见 [DEPLOY.md](DEPLOY.md)，包含：

- 🆓 Streamlit Cloud（个人免费）
- 🚀 Railway（自定义域名）
- 🐳 Docker（几乎可部署至任何平台）
- 🖥️ VPS（企业级完全控制）

## 🤝 贡献

欢迎 PR！感谢任何形式的贡献。

## 📄 许可证

本项目使用 MIT License，详见 [LICENSE](LICENSE)。

## 🙏 鸣谢

- [Microsoft MarkItDown](https://github.com/microsoft/markitdown) — 核心转换引擎
- [Streamlit](https://streamlit.io/) — 卓越的 Web 框架
- [uv](https://github.com/astral-sh/uv) — 极速的 Python 包管理器 