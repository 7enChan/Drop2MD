"""
MarkItDown WebUI - 极简版
简洁、高效的文件转换工具
"""

import streamlit as st
import tempfile
import os
import time
from pathlib import Path
from markitdown import MarkItDown
from utils import get_file_info, format_file_size
from config import APP_CONFIG

# 配置页面
st.set_page_config(
    page_title="MarkItDown 转换器",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 极简CSS样式
st.markdown("""
<style>
    /* 隐藏默认的菜单和页脚 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 简化主容器 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    
    /* 标题样式 */
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 300;
        margin-bottom: 0.5rem;
        color: #1f1f1f;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    
    
    /* 文件信息卡片 */
    .file-info {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* 按钮样式 */
    .stButton > button {
        width: 100%;
        height: 3rem;
        border-radius: 8px;
        border: none;
        font-size: 1.1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    /* 结果区域 */
    .result-container {
        margin-top: 2rem;
        padding: 2rem;
        background: white;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* 统计信息 */
    .stats {
        display: flex;
        justify-content: space-around;
        margin: 1rem 0;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-value {
        font-size: 1.5rem;
        font-weight: 600;
        color: #667eea;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        margin-top: 0.2rem;
    }
    
    /* 隐藏 Streamlit 的一些默认元素 */
    .stDeployButton {display: none;}
    .stDecoration {display: none;}
    
    /* 隐藏文件上传组件内的格式提示 */
    [data-testid="stFileUploader"] small {
        display: none !important;
    }
    
    /* 调整文件上传组件宽度 */
    .stFileUploader {
        width: 100% !important;
    }
    
    .stFileUploader > div {
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # 简洁的标题
    st.markdown('<h1 class="main-title">📝 MarkItDown</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">将任何文件转换为 Markdown 格式</p>', unsafe_allow_html=True)
    
    # 文件上传区域
    col1, col2, col3 = st.columns([0.5, 4, 0.5])
    
    with col2:
        uploaded_file = st.file_uploader(
            "选择文件",
            type=APP_CONFIG["supported_extensions"],
            label_visibility="collapsed"
        )
        
        if uploaded_file is None:
            st.markdown("**支持格式：** PDF、EPubs、PPT、Word、Excel、JPG、PNG、CSV、JSON 等")
        
        # 文件信息和转换
        if uploaded_file is not None:
            show_file_conversion(uploaded_file)

def show_file_conversion(uploaded_file):
    """显示文件信息和转换功能"""
    
    # 获取文件信息
    file_info = get_file_info(uploaded_file)
    
    # 文件信息卡片
    st.markdown(
        f'''
        <div class="file-info">
            <h4>📄 {file_info["name"]}</h4>
            <p><strong>大小：</strong> {format_file_size(file_info["size"])}</p>
            <p><strong>类型：</strong> {file_info["type"]}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    # 转换按钮
    if st.button("🚀 开始转换", type="primary"):
        convert_file(uploaded_file)

def convert_file(uploaded_file):
    """转换文件"""
    
    # 进度指示
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        start_time = time.time()
        
        # 步骤1: 保存临时文件
        status_text.info("💾 正在处理文件...")
        progress_bar.progress(25)
        
        with tempfile.NamedTemporaryFile(
            delete=False, 
            suffix=Path(uploaded_file.name).suffix
        ) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        # 步骤2: 执行转换
        status_text.info("⚡ 正在转换...")
        progress_bar.progress(75)
        
        md = MarkItDown()
        result = md.convert(tmp_path)
        
        # 步骤3: 完成
        progress_bar.progress(100)
        conversion_time = time.time() - start_time
        
        # 清理进度指示
        progress_bar.empty()
        status_text.empty()
        
        # 显示结果
        show_conversion_result(result, uploaded_file.name, conversion_time)
        
        # 清理临时文件
        os.unlink(tmp_path)
        
    except Exception as e:
        progress_bar.empty()
        status_text.empty()
        st.error(f"转换失败：{str(e)}")

def show_conversion_result(result, filename, conversion_time):
    """显示转换结果"""
    
    # 简单统计
    word_count = len(result.text_content.split())
    char_count = len(result.text_content)
    
    st.markdown(
        f'''
        <div class="stats">
            <div class="stat-item">
                <div class="stat-value">{char_count:,}</div>
                <div class="stat-label">字符数</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{word_count:,}</div>
                <div class="stat-label">单词数</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{conversion_time:.1f}s</div>
                <div class="stat-label">转换时间</div>
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    # 下载按钮
    output_filename = f"{Path(filename).stem}.md"
    st.download_button(
        label="📥 下载 Markdown 文件",
        data=result.text_content,
        file_name=output_filename,
        mime="text/markdown",
        type="primary"
    )

if __name__ == "__main__":
    main() 