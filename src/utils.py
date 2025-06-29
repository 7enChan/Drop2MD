"""工具函数模块"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
from config import APP_CONFIG, get_file_type_display

# 转换历史记录文件路径
HISTORY_FILE = Path(APP_CONFIG["output_dir"]) / "conversion_history.json"

def get_file_info(uploaded_file) -> Dict[str, Any]:
    """
    获取上传文件的详细信息
    
    Args:
        uploaded_file: Streamlit 上传的文件对象
        
    Returns:
        包含文件信息的字典
    """
    file_extension = Path(uploaded_file.name).suffix.lstrip('.').lower()
    
    return {
        "name": uploaded_file.name,
        "size": uploaded_file.size,
        "type": get_file_type_display(file_extension),
        "extension": file_extension,
        "upload_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def format_file_size(size_bytes: int) -> str:
    """
    格式化文件大小显示
    
    Args:
        size_bytes: 文件大小（字节）
        
    Returns:
        格式化的文件大小字符串
    """
    if size_bytes == 0:
        return "0 B"
    
    size_units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)
    unit_index = 0
    
    while size >= 1024.0 and unit_index < len(size_units) - 1:
        size /= 1024.0
        unit_index += 1
    
    if unit_index == 0:
        return f"{int(size)} {size_units[unit_index]}"
    else:
        return f"{size:.1f} {size_units[unit_index]}"

def save_conversion_history(
    filename: str, 
    file_size: int,
    output_size: int,
    conversion_time: float
) -> None:
    """
    保存转换历史记录
    
    Args:
        filename: 原文件名
        file_size: 原文件大小
        output_size: 输出文件大小
        conversion_time: 转换耗时
    """
    try:
        # 确保历史文件目录存在
        HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        # 读取现有历史记录
        history = load_conversion_history()
        
        # 添加新记录
        new_record = {
            "timestamp": datetime.now().isoformat(),
            "filename": filename,
            "file_extension": Path(filename).suffix.lstrip('.').lower(),
            "input_size": file_size,
            "output_size": output_size,
            "conversion_time": round(conversion_time, 2),
            "compression_ratio": round(output_size / file_size if file_size > 0 else 0, 2)
        }
        
        history.append(new_record)
        
        # 保留最近的 100 条记录
        if len(history) > 100:
            history = history[-100:]
        
        # 保存到文件
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        # 静默失败，不影响主要功能
        print(f"保存转换历史失败: {e}")

def load_conversion_history() -> list:
    """
    加载转换历史记录
    
    Returns:
        历史记录列表
    """
    try:
        if HISTORY_FILE.exists():
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"加载转换历史失败: {e}")
    
    return []

def get_conversion_stats() -> Dict[str, Any]:
    """
    获取转换统计信息
    
    Returns:
        统计信息字典
    """
    history = load_conversion_history()
    
    if not history:
        return {
            "total_conversions": 0,
            "total_files_processed": 0,
            "average_conversion_time": 0,
            "most_common_format": "无",
            "total_input_size": 0,
            "total_output_size": 0
        }
    
    # 计算统计信息
    total_conversions = len(history)
    total_input_size = sum(record.get("input_size", 0) for record in history)
    total_output_size = sum(record.get("output_size", 0) for record in history)
    avg_conversion_time = sum(record.get("conversion_time", 0) for record in history) / total_conversions
    
    # 统计最常见的文件格式
    format_counts = {}
    for record in history:
        ext = record.get("file_extension", "unknown")
        format_counts[ext] = format_counts.get(ext, 0) + 1
    
    most_common_format = max(format_counts.items(), key=lambda x: x[1])[0] if format_counts else "无"
    
    return {
        "total_conversions": total_conversions,
        "total_files_processed": total_conversions,
        "average_conversion_time": round(avg_conversion_time, 2),
        "most_common_format": most_common_format,
        "total_input_size": total_input_size,
        "total_output_size": total_output_size,
        "compression_ratio": round(total_output_size / total_input_size if total_input_size > 0 else 0, 2)
    }

def clean_temp_files(temp_dir: Optional[str] = None) -> int:
    """
    清理临时文件
    
    Args:
        temp_dir: 临时目录路径，默认使用配置中的目录
        
    Returns:
        清理的文件数量
    """
    if temp_dir is None:
        temp_dir = APP_CONFIG["temp_dir"]
    
    temp_path = Path(str(temp_dir))
    if not temp_path.exists():
        return 0
    
    cleaned_count = 0
    current_time = time.time()
    
    try:
        for file_path in temp_path.iterdir():
            if file_path.is_file():
                # 删除超过 1 小时的临时文件
                if current_time - file_path.stat().st_mtime > 3600:
                    file_path.unlink()
                    cleaned_count += 1
    except Exception as e:
        print(f"清理临时文件时出错: {e}")
    
    return cleaned_count

def validate_file_type(filename: str) -> bool:
    """
    验证文件类型是否支持
    
    Args:
        filename: 文件名
        
    Returns:
        是否支持该文件类型
    """
    file_extension = Path(filename).suffix.lstrip('.').lower()
    return file_extension in APP_CONFIG["supported_extensions"]

def generate_output_filename(input_filename: str, add_timestamp: bool = False) -> str:
    """
    生成输出文件名
    
    Args:
        input_filename: 输入文件名
        add_timestamp: 是否添加时间戳
        
    Returns:
        输出文件名
    """
    base_name = Path(input_filename).stem
    
    if add_timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{base_name}_{timestamp}.md"
    else:
        return f"{base_name}.md"

def format_duration(seconds: float) -> str:
    """
    格式化时间持续时间
    
    Args:
        seconds: 秒数
        
    Returns:
        格式化的时间字符串
    """
    if seconds < 1:
        return f"{seconds*1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        remaining_seconds = seconds % 60
        return f"{minutes}m {remaining_seconds:.0f}s"
    else:
        hours = int(seconds // 3600)
        remaining_minutes = int((seconds % 3600) // 60)
        return f"{hours}h {remaining_minutes}m"

def sanitize_filename(filename: str) -> str:
    """
    清理文件名，移除不安全字符
    
    Args:
        filename: 原始文件名
        
    Returns:
        清理后的文件名
    """
    # 移除或替换不安全字符
    unsafe_chars = '<>:"/\\|?*'
    safe_filename = filename
    
    for char in unsafe_chars:
        safe_filename = safe_filename.replace(char, '_')
    
    # 移除多余的空格和点
    safe_filename = safe_filename.strip(' .')
    
    # 确保文件名不为空
    if not safe_filename:
        safe_filename = "untitled"
    
    return safe_filename

def create_markdown_preview(content: str, max_length: int = 1000) -> str:
    """
    创建 Markdown 内容的预览
    
    Args:
        content: Markdown 内容
        max_length: 最大预览长度
        
    Returns:
        预览内容
    """
    if len(content) <= max_length:
        return content
    
    # 尝试在合适的位置截断（避免在单词中间截断）
    truncated = content[:max_length]
    last_space = truncated.rfind(' ')
    last_newline = truncated.rfind('\n')
    
    cut_point = max(last_space, last_newline)
    if cut_point > max_length * 0.8:  # 如果截断点不太远
        truncated = content[:cut_point]
    
    return truncated + "\n\n... (内容过长，已截断)" 