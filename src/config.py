"""Application configuration file"""

import os
from pathlib import Path

# Get project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Application configuration
APP_CONFIG = {
    "title": "MarkItDown WebUI",
    "version": "1.0.0",
    "description": "A modern, minimalist web interface for file conversion built on MarkItDown",
    
    # Supported file extensions
    "supported_extensions": [
        # Document formats
        "pdf", "docx", "pptx", "xlsx", "xls",
        # Image formats
        "jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp",
        # Audio formats
        "mp3", "wav", "m4a", "aac",
        # Web and markup formats
        "html", "htm", "xml", "xhtml",
        # Data formats
        "csv", "json", "yaml", "yml",
        # Archives and ebooks
        "zip", "epub",
        # Text formats
        "txt", "rtf", "md"
    ],
    
    # File size limit (MB)
    "max_file_size_mb": 50,
    
    # Directory configuration
    "temp_dir": str(PROJECT_ROOT / "data" / "temp"),
    "input_dir": str(PROJECT_ROOT / "data" / "input"),
    "output_dir": str(PROJECT_ROOT / "data" / "output"),
    
    # Conversion configuration
    "conversion_options": {
        "enable_plugins": False,
        "enable_ocr": True,
        "timeout": 300,  # Conversion timeout (seconds)
    },
    
    # UI configuration
    "ui_config": {
        "page_title": "MarkItDown WebUI",
        "page_icon": "📝",
        "layout": "wide",
        "initial_sidebar_state": "expanded"
    }
}

# Streamlit theme configuration
STREAMLIT_CONFIG = {
    "theme": {
        "primaryColor": "#667eea",
        "backgroundColor": "#ffffff",
        "secondaryBackgroundColor": "#f0f2f6",
        "textColor": "#262730",
        "font": "sans serif"
    },
    "server": {
        "port": 8501,
        "address": "localhost",
        "headless": False,
        "runOnSave": True,
        "allowRunOnSave": True
    }
}

# File type mapping
FILE_TYPE_MAPPING = {
    # Document types
    "pdf": "📄 PDF Document",
    "docx": "📝 Word Document",
    "pptx": "📊 PowerPoint Presentation",
    "xlsx": "📈 Excel Spreadsheet",
    "xls": "📈 Excel Spreadsheet (Legacy)",
    
    # Image types
    "jpg": "🖼️ JPEG Image",
    "jpeg": "🖼️ JPEG Image",
    "png": "🖼️ PNG Image",
    "gif": "🖼️ GIF Image",
    "bmp": "🖼️ BMP Image",
    "tiff": "🖼️ TIFF Image",
    "webp": "🖼️ WebP Image",
    
    # Audio types
    "mp3": "🎵 MP3 Audio",
    "wav": "🎵 WAV Audio",
    "m4a": "🎵 M4A Audio",
    "aac": "🎵 AAC Audio",
    
    # Web types
    "html": "🌐 HTML Page",
    "htm": "🌐 HTML Page",
    "xml": "🌐 XML Document",
    "xhtml": "🌐 XHTML Page",
    
    # Data types
    "csv": "📊 CSV Data",
    "json": "📊 JSON Data",
    "yaml": "📊 YAML Data",
    "yml": "📊 YAML Data",
    
    # Other types
    "zip": "🗜️ ZIP Archive",
    "epub": "📚 EPUB eBook",
    "txt": "📄 Text File",
    "rtf": "📄 RTF Document",
    "md": "📝 Markdown Document"
}

# Error message configuration
ERROR_MESSAGES = {
    "file_too_large": "File size exceeds limit",
    "unsupported_format": "Unsupported file format",
    "conversion_failed": "File conversion failed",
    "file_corrupted": "File may be corrupted",
    "timeout": "Conversion timeout",
    "unknown_error": "Unknown error"
}

# Success message configuration
SUCCESS_MESSAGES = {
    "conversion_complete": "File conversion completed",
    "file_uploaded": "File uploaded successfully",
    "download_ready": "File ready for download"
}

def get_file_type_display(extension):
    """Get display name based on file extension"""
    return FILE_TYPE_MAPPING.get(extension.lower(), f"📄 {extension.upper()} File")

def validate_file_size(file_size_bytes):
    """Validate if file size is within allowed range"""
    max_size_bytes = APP_CONFIG["max_file_size_mb"] * 1024 * 1024
    return file_size_bytes <= max_size_bytes

def get_temp_dir():
    """Get temporary directory path, create if not exists"""
    temp_dir = Path(APP_CONFIG["temp_dir"])
    temp_dir.mkdir(parents=True, exist_ok=True)
    return str(temp_dir)

def get_output_dir():
    """Get output directory path, create if not exists"""
    output_dir = Path(APP_CONFIG["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    return str(output_dir) 