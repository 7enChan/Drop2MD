<p align="right">
  <a href="README.zh-CN.md">简体中文 🇨🇳</a> | English
</p>

# Drop2MD

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?logo=streamlit)](https://drop2md.streamlit.app/)

A modern, minimalist web interface for file conversion built on Microsoft's MarkItDown.

## 🤖 AI-Generated Project

**This project was bootstrapped and developed entirely by an AI**

## ✨ Features

- 🚀 Convert multiple file formats to Markdown
- 🎨 Clean, minimalist web interface
- ⚡ Fast package management with uv
- 🔒 Isolated virtual environment, no system pollution
- 📱 Responsive design with drag-and-drop support

## 📄 Supported Formats

- 📄 **Documents**: PDF, Word, PowerPoint, Excel
- 🖼️ **Images**: JPG, PNG, GIF, BMP, TIFF, WebP
- 🎵 **Audio**: MP3, WAV, M4A, AAC
- 🌐 **Web**: HTML, XML, XHTML
- 📊 **Data**: JSON, CSV, YAML
- 📚 **Archives**: ZIP, EPUB
- 📝 **Text**: TXT, RTF, Markdown

## ⚙️ Setup & Installation

Below are two common ways to prepare a local environment. Pick the one you prefer.

### Option A — Use uv (fast & recommended)

```bash
# 1. Create and activate a virtual environment
uv venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install all dependencies (runtime + dev tools)
uv pip install -e ".[dev]"
```

### Option B — Pure Python & pip (works everywhere)

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -e .                 # runtime only
pip install -e ".[dev]"          # dev tools (optional)
```

Once the environment is ready you can launch the app as described below.

## 🚀 Quick Start

```bash
# One-click start
./run.sh

# Or manual start
source .venv/bin/activate
streamlit run src/app.py
```

## 🛠️ Development

```bash
# Activate environment
source .venv/bin/activate

# Install new dependencies
uv pip install package-name

# Run tests
pytest tests/

# Code formatting
black src/
ruff check src/

# Deactivate when done
deactivate
```

## 📁 Project Structure

```
Drop2MD/
├── .venv/              # Virtual environment
├── src/               # Source code
│   ├── app.py        # Main application
│   ├── config.py     # Configuration
│   └── utils.py      # Utility functions
├── data/             # Data directory
│   ├── input/        # Input files
│   ├── output/       # Output files
│   └── temp/         # Temporary files
├── tests/            # Tests
├── docs/             # Documentation
├── Dockerfile        # Docker configuration
├── docker-compose.yml # Docker Compose setup
├── requirements.txt  # Dependencies for cloud deployment
└── DEPLOY.md         # Deployment guide
```

## 🎯 Technology Stack

- **Backend**: Python 3.12+ with FastAPI-like architecture
- **Frontend**: Streamlit for rapid UI development
- **Package Manager**: uv for lightning-fast dependency management
- **Core Engine**: Microsoft MarkItDown for file conversion
- **Containerization**: Docker & Docker Compose ready

## 🌐 Deployment

See [DEPLOY.md](DEPLOY.md) for detailed deployment instructions including:

- 🆓 **Streamlit Cloud** (Free, recommended for personal use)
- 🚀 **Railway** (Easy deployment with custom domains)
- 🐳 **Docker** (Flexible deployment anywhere)
- 🖥️ **VPS** (Full control for enterprise use)

## 📊 Usage Statistics

- ⚡ **Conversion Speed**: Typically under 2 seconds
- 📏 **File Size Limit**: Up to 200MB per file
- 🔧 **Dependencies**: Minimal, well-maintained packages
- 🎨 **UI/UX**: Minimalist design, zero configuration needed

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Microsoft MarkItDown](https://github.com/microsoft/markitdown) - The core conversion engine
- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [uv](https://github.com/astral-sh/uv) - For blazing fast Python package management
