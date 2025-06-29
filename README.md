# MarkItDown WebUI

A modern, minimalist web interface for file conversion built on Microsoft's MarkItDown.

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
markitdown-webui/
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
