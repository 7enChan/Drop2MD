"""
Drop2MD
A simple, efficient file conversion tool
"""

import streamlit as st
import tempfile
import os
import time
import zipfile
import io
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
    
    /* Button styles */
    .stButton > button {
        width: 100%;
        height: 3rem;
        border-radius: 8px;
        border: none;
        font-size: 1.1rem;
        font-weight: 500;
        transition: all 0.3s ease;
        margin-top: 0.5rem; /* Slight space above the button for tighter alignment */
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
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
    
    /* Hide title anchor links */
    h1 a.anchor-link {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function"""
    st.markdown('<h1 class="main-title">📝 Drop2MD</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Convert almost all file formats to Markdown</p>', unsafe_allow_html=True)
    
    _, col2, _ = st.columns([0.5, 4, 0.5])
    
    with col2:
        uploaded_files = st.file_uploader(
            "Choose files",
            type=APP_CONFIG["supported_extensions"],
            label_visibility="collapsed",
            accept_multiple_files=True,
        )
        
        if not uploaded_files:
            st.markdown("**Supported formats:** PDF, EPubs, PPT, Word, Excel, JPG, PNG, CSV, JSON, etc.")
        
        if uploaded_files:
            # --- Action Buttons --- #
            st.markdown("<br>", unsafe_allow_html=True) # Add some space
            if st.button(f"🚀 Start Batch Conversion ({len(uploaded_files)} files)", type="primary"):
                batch_convert_files(uploaded_files)
            
    # Footer
    st.markdown("""
        <div class="footer">
            Powered by <a href="https://streamlit.io" target="_blank">Streamlit</a>
            & <a href="https://github.com/microsoft/markitdown" target="_blank">MarkItDown</a>
            &nbsp;|&nbsp;
            <a href="https://github.com/7enChan/Drop2MD" target="_blank">GitHub</a>
        </div>
    """, unsafe_allow_html=True)

def batch_convert_files(uploaded_files):
    """Convert a list of uploaded files and package them into a zip."""
    
    total_files = len(uploaded_files)
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    results = []
    start_time = time.time()

    try:
        for i, uploaded_file in enumerate(uploaded_files):
            progress = (i + 1) / total_files
            status_text.info(f"({i+1}/{total_files}) ⚡ Converting {uploaded_file.name}...")
            
            with tempfile.NamedTemporaryFile(
                delete=False, 
                suffix=Path(uploaded_file.name).suffix
            ) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_path = tmp_file.name
            
            md = MarkItDown()
            result = md.convert(tmp_path)
            
            results.append({
                "filename": f"{Path(uploaded_file.name).stem}.md",
                "content": result.text_content
            })
            
            os.unlink(tmp_path)
            progress_bar.progress(progress)

        total_time = time.time() - start_time
        status_text.success(f"✅ All {total_files} files converted in {total_time:.2f}s.")
        progress_bar.empty()
        
        create_zip_and_download(results)

    except Exception as e:
        progress_bar.empty()
        status_text.error(f"An error occurred during conversion: {str(e)}")

def create_zip_and_download(results):
    """Create a zip file in memory and provide a download button."""
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for result in results:
            zip_file.writestr(result["filename"], result["content"])
            
    zip_buffer.seek(0)
    
    st.download_button(
        label=f"📥 Download All as ZIP ({len(results)} files)",
        data=zip_buffer,
        file_name="Drop2MD_converted_files.zip",
        mime="application/zip",
        type="primary"
    )

if __name__ == "__main__":
    main()