"""Utility functions module"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
from config import APP_CONFIG, get_file_type_display

# Conversion history file path
HISTORY_FILE = Path(APP_CONFIG["output_dir"]) / "conversion_history.json"

def get_file_info(uploaded_file) -> Dict[str, Any]:
    """
    Get detailed information about uploaded file
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        Dictionary containing file information
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
    Format file size for display
    
    Args:
        size_bytes: File size in bytes
        
    Returns:
        Formatted file size string
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
    Save conversion history record
    
    Args:
        filename: Original filename
        file_size: Original file size
        output_size: Output file size
        conversion_time: Conversion duration
    """
    try:
        # Ensure history file directory exists
        HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        # Load existing history records
        history = load_conversion_history()
        
        # Add new record
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
        
        # Keep only the latest 100 records
        if len(history) > 100:
            history = history[-100:]
        
        # Save to file
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        # Silent failure, don't affect main functionality
        print(f"Failed to save conversion history: {e}")

def load_conversion_history() -> list:
    """
    Load conversion history records
    
    Returns:
        List of history records
    """
    try:
        if HISTORY_FILE.exists():
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        print(f"Failed to load conversion history: {e}")
    
    return []

def get_conversion_stats() -> Dict[str, Any]:
    """
    Get conversion statistics
    
    Returns:
        Dictionary of statistics
    """
    history = load_conversion_history()
    
    if not history:
        return {
            "total_conversions": 0,
            "total_files_processed": 0,
            "average_conversion_time": 0,
            "most_common_format": "None",
            "total_input_size": 0,
            "total_output_size": 0
        }
    
    # Calculate statistics
    total_conversions = len(history)
    total_input_size = sum(record.get("input_size", 0) for record in history)
    total_output_size = sum(record.get("output_size", 0) for record in history)
    avg_conversion_time = sum(record.get("conversion_time", 0) for record in history) / total_conversions
    
    # Count most common file formats
    format_counts = {}
    for record in history:
        ext = record.get("file_extension", "unknown")
        format_counts[ext] = format_counts.get(ext, 0) + 1
    
    most_common_format = max(format_counts.items(), key=lambda x: x[1])[0] if format_counts else "None"
    
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
    Clean temporary files
    
    Args:
        temp_dir: Temporary directory path, defaults to configured directory
        
    Returns:
        Number of files cleaned
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
                # Delete temporary files older than 1 hour
                if current_time - file_path.stat().st_mtime > 3600:
                    file_path.unlink()
                    cleaned_count += 1
    except Exception as e:
        print(f"Error cleaning temporary files: {e}")
    
    return cleaned_count

def validate_file_type(filename: str) -> bool:
    """
    Validate if file type is supported
    
    Args:
        filename: Filename
        
    Returns:
        Whether the file type is supported
    """
    file_extension = Path(filename).suffix.lstrip('.').lower()
    return file_extension in APP_CONFIG["supported_extensions"]

def generate_output_filename(input_filename: str, add_timestamp: bool = False) -> str:
    """
    Generate output filename
    
    Args:
        input_filename: Input filename
        add_timestamp: Whether to add timestamp
        
    Returns:
        Output filename
    """
    base_name = Path(input_filename).stem
    
    if add_timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{base_name}_{timestamp}.md"
    else:
        return f"{base_name}.md"

def format_duration(seconds: float) -> str:
    """
    Format time duration
    
    Args:
        seconds: Number of seconds
        
    Returns:
        Formatted time string
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
    Sanitize filename by removing unsafe characters
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Remove or replace unsafe characters
    unsafe_chars = '<>:"/\\|?*'
    safe_filename = filename
    
    for char in unsafe_chars:
        safe_filename = safe_filename.replace(char, '_')
    
    # Remove extra spaces and dots
    safe_filename = safe_filename.strip(' .')
    
    # Ensure filename is not empty
    if not safe_filename:
        safe_filename = "untitled"
    
    return safe_filename

def create_markdown_preview(content: str, max_length: int = 1000) -> str:
    """
    Create preview of Markdown content
    
    Args:
        content: Markdown content
        max_length: Maximum preview length
        
    Returns:
        Preview content
    """
    if len(content) <= max_length:
        return content
    
    # Try to truncate at appropriate position (avoid breaking words)
    truncated = content[:max_length]
    last_space = truncated.rfind(' ')
    last_newline = truncated.rfind('\n')
    
    cut_point = max(last_space, last_newline)
    if cut_point > max_length * 0.8:  # If cut point is not too far
        truncated = content[:cut_point]
    
    return truncated + "\n\n... (Content too long, truncated)" 