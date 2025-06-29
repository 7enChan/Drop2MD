"""应用配置文件"""

import os
from pathlib import Path

# 获取项目根目录
PROJECT_ROOT = Path(__file__).parent.parent

# 应用配置
APP_CONFIG = {
    "title": "MarkItDown WebUI",
    "version": "1.0.0",
    "description": "现代化的文件转换 WebUI，基于 MarkItDown 构建",
    
    # 支持的文件扩展名
    "supported_extensions": [
        # 文档格式
        "pdf", "docx", "pptx", "xlsx", "xls",
        # 图像格式
        "jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp",
        # 音频格式
        "mp3", "wav", "m4a", "aac",
        # 网页和标记格式
        "html", "htm", "xml", "xhtml",
        # 数据格式
        "csv", "json", "yaml", "yml",
        # 压缩和电子书
        "zip", "epub",
        # 文本格式
        "txt", "rtf", "md"
    ],
    
    # 文件大小限制（MB）
    "max_file_size_mb": 50,
    
    # 目录配置
    "temp_dir": str(PROJECT_ROOT / "data" / "temp"),
    "input_dir": str(PROJECT_ROOT / "data" / "input"),
    "output_dir": str(PROJECT_ROOT / "data" / "output"),
    
    # 转换配置
    "conversion_options": {
        "enable_plugins": False,
        "enable_ocr": True,
        "timeout": 300,  # 转换超时时间（秒）
    },
    
    # UI 配置
    "ui_config": {
        "page_title": "MarkItDown WebUI",
        "page_icon": "📝",
        "layout": "wide",
        "initial_sidebar_state": "expanded"
    }
}

# Streamlit 主题配置
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

# 文件类型映射
FILE_TYPE_MAPPING = {
    # 文档类型
    "pdf": "📄 PDF 文档",
    "docx": "📝 Word 文档",
    "pptx": "📊 PowerPoint 演示文稿",
    "xlsx": "📈 Excel 电子表格",
    "xls": "📈 Excel 电子表格 (旧版)",
    
    # 图像类型
    "jpg": "🖼️ JPEG 图像",
    "jpeg": "🖼️ JPEG 图像",
    "png": "🖼️ PNG 图像",
    "gif": "🖼️ GIF 图像",
    "bmp": "🖼️ BMP 图像",
    "tiff": "🖼️ TIFF 图像",
    "webp": "🖼️ WebP 图像",
    
    # 音频类型
    "mp3": "🎵 MP3 音频",
    "wav": "🎵 WAV 音频",
    "m4a": "🎵 M4A 音频",
    "aac": "🎵 AAC 音频",
    
    # 网页类型
    "html": "🌐 HTML 网页",
    "htm": "🌐 HTML 网页",
    "xml": "🌐 XML 文档",
    "xhtml": "🌐 XHTML 网页",
    
    # 数据类型
    "csv": "📊 CSV 数据",
    "json": "📊 JSON 数据",
    "yaml": "📊 YAML 数据",
    "yml": "📊 YAML 数据",
    
    # 其他类型
    "zip": "🗜️ ZIP 压缩包",
    "epub": "📚 EPUB 电子书",
    "txt": "📄 文本文件",
    "rtf": "📄 RTF 文档",
    "md": "📝 Markdown 文档"
}

# 错误消息配置
ERROR_MESSAGES = {
    "file_too_large": "文件大小超过限制",
    "unsupported_format": "不支持的文件格式",
    "conversion_failed": "文件转换失败",
    "file_corrupted": "文件可能已损坏",
    "timeout": "转换超时",
    "unknown_error": "未知错误"
}

# 成功消息配置
SUCCESS_MESSAGES = {
    "conversion_complete": "文件转换完成",
    "file_uploaded": "文件上传成功",
    "download_ready": "文件准备下载"
}

def get_file_type_display(extension):
    """根据文件扩展名获取显示名称"""
    return FILE_TYPE_MAPPING.get(extension.lower(), f"📄 {extension.upper()} 文件")

def validate_file_size(file_size_bytes):
    """验证文件大小是否在允许范围内"""
    max_size_bytes = APP_CONFIG["max_file_size_mb"] * 1024 * 1024
    return file_size_bytes <= max_size_bytes

def get_temp_dir():
    """获取临时目录路径，如果不存在则创建"""
    temp_dir = Path(APP_CONFIG["temp_dir"])
    temp_dir.mkdir(parents=True, exist_ok=True)
    return str(temp_dir)

def get_output_dir():
    """获取输出目录路径，如果不存在则创建"""
    output_dir = Path(APP_CONFIG["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    return str(output_dir) 