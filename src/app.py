"""
Drop2MD
A simple, efficient file conversion tool
"""

import streamlit as st
import tempfile
import os
import time
from pathlib import Path
from markitdown import MarkItDown
from utils import get_file_info, format_file_size
from config import APP_CONFIG

# Page configuration
st.set_page_config(
    page_title="Drop2MD",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Minimalist CSS styles
st.markdown("""
<style>
    /* Hide default menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Simplify main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
        max-width: 800px;
    }
    
    /* Custom footer style */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: #888;
        text-align: center;
        padding: 1rem;
        font-size: 0.9rem;
        border-top: 1px solid #eaeaea;
        z-index: 100;
    }
    
    .footer a {
        color: #555;
        text-decoration: none;
    }
    
    /* Title styles */
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
    
    
    
    /* File info card */
    .file-info {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Button styles */
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
    
    /* Result area */
    .result-container {
        margin-top: 2rem;
        padding: 2rem;
        background: white;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    /* Statistics */
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
    
    /* Hide some Streamlit default elements */
    .stDeployButton {display: none;}
    .stDecoration {display: none;}
    
    /* Hide format hints in file uploader */
    [data-testid="stFileUploader"] small {
        display: none !important;
    }
    
    /* Adjust file uploader width */
    .stFileUploader {
        width: 100% !important;
    }
    
    .stFileUploader > div {
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Simple title
    st.markdown('<h1 class="main-title">📝 Drop2MD</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Convert almost all file formats to Markdown</p>', unsafe_allow_html=True)
    
    # File upload area
    col1, col2, col3 = st.columns([0.5, 4, 0.5])
    
    with col2:
        uploaded_file = st.file_uploader(
            "Choose file",
            type=APP_CONFIG["supported_extensions"],
            label_visibility="collapsed"
        )
        
        if uploaded_file is None:
            st.markdown("**Supported formats:** PDF, EPubs, PPT, Word, Excel, JPG, PNG, CSV, JSON, etc.")
        
        # File info and conversion
        if uploaded_file is not None:
            show_file_conversion(uploaded_file)
            
    # Footer
    st.markdown(
        """
        <div class="footer">
            Powered by <a href="https://streamlit.io" target="_blank">Streamlit</a>
            & <a href="https://github.com/microsoft/markitdown" target="_blank">MarkItDown</a>
        </div>
        """,
        unsafe_allow_html=True
    )

def show_file_conversion(uploaded_file):
    """Display file information and conversion functionality"""
    
    # Get file information
    file_info = get_file_info(uploaded_file)
    
    # File info card
    st.markdown(
        f'''
        <div class="file-info">
            <h4>📄 {file_info["name"]}</h4>
            <p><strong>Size:</strong> {format_file_size(file_info["size"])}</p>
            <p><strong>Type:</strong> {file_info["type"]}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    # Convert button
    if st.button("🚀 Start Conversion", type="primary"):
        convert_file(uploaded_file)

def convert_file(uploaded_file):
    """Convert file"""
    
    # Progress indicator
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        start_time = time.time()
        
        # Step 1: Save temporary file
        status_text.info("💾 Processing file...")
        progress_bar.progress(25)
        
        with tempfile.NamedTemporaryFile(
            delete=False, 
            suffix=Path(uploaded_file.name).suffix
        ) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        # Step 2: Execute conversion
        status_text.info("⚡ Converting...")
        progress_bar.progress(75)
        
        md = MarkItDown()
        result = md.convert(tmp_path)
        
        # Step 3: Complete
        progress_bar.progress(100)
        conversion_time = time.time() - start_time
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        # Show results
        show_conversion_result(result, uploaded_file.name, conversion_time)
        
        # Clean up temporary file
        os.unlink(tmp_path)
        
    except Exception as e:
        progress_bar.empty()
        status_text.empty()
        st.error(f"Conversion failed: {str(e)}")

def show_conversion_result(result, filename, conversion_time):
    """Display conversion results"""
    
    # Simple statistics
    word_count = len(result.text_content.split())
    char_count = len(result.text_content)
    
    st.markdown(
        f'''
        <div class="stats">
            <div class="stat-item">
                <div class="stat-value">{char_count:,}</div>
                <div class="stat-label">Characters</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{word_count:,}</div>
                <div class="stat-label">Words</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">{conversion_time:.1f}s</div>
                <div class="stat-label">Conversion Time</div>
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    # Download button
    output_filename = f"{Path(filename).stem}.md"
    st.download_button(
        label="📥 Download Markdown File",
        data=result.text_content,
        file_name=output_filename,
        mime="text/markdown",
        type="primary"
    )

if __name__ == "__main__":
    main() 