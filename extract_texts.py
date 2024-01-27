import os
import streamlit as st

from extractor_obj import PDFextractor
from zipfile import ZipFile
from typing import Optional

def extract_text(
        pdf_directory: Optional[str] = None,
        pdf_filepaths: Optional[str] = None,
        extraction_dir: str = '',
        progress_text: str = 'Loading...',
        enable_downloads: bool = True,
        chunk_extraction: bool = False        
        ):
    
    # create the progress bar
    progress_bar = st.progress(0, text=progress_text)

    # specify the filepath
    if pdf_directory != None:
        fnames = os.listdir(pdf_directory)
        filepaths = [os.path.join(pdf_directory, name) for name in fnames]
    elif pdf_filepaths != None:
        filepaths = pdf_filepaths

    # extract the texts using the pdf extractor
    ex = PDFextractor(filepaths, chunk_extraction)

    # extract the PDF files 
    extracted_filepaths = []
    for i, fpath in ex.extract(extraction_dir, 1):
        extracted_filepaths.append(fpath)

        # update the extraction progess on the progress bar
        percentage = (i/len(filepaths)) * 100
        percentage = int(percentage)

        progress_bar.progress(
            percentage, 
            text = progress_text)
        # message returned after the process is completed
        st.success('Done')
        # reset the progress bar after the process is completed
        progress_bar.empty()


        # to zip and download the file 
        if enable_downloads:
            with ZipFile('files.zip', 'w') as zf:
                for fpath in extracted_filepaths:
                    zf.write(fpath, os.path.basename(fpath))

            with open('files.zip', 'rb') as f:
                st.download_button(
                    'Download Files', f, 
                    file_name='files.zip')
                


