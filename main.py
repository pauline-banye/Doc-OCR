import os
import shutil
import streamlit as st

from pdf2image import convert_from_bytes
from extract_texts import extract_text
# from qa import answer_question as ans
import qa

st.title('PDF Extractor and Explorer')

uploaded_files = st.file_uploader(
    'Upload a file',
    type = ['pdf'],
    accept_multiple_files = True,
    help = 'You can upload multiple PDF files.'
)
temp_dir = 'temp_uploads'
extraction_dir = 'temp_extract'
qa_extraction_dir = 'temp_qa_extract'

pdf_names = []

if uploaded_files:
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.mkdir(temp_dir)

    for uploaded_file in uploaded_files:
        pdf_names.append(uploaded_file.name)

        storage_path = os.path.join(
            temp_dir, 
            uploaded_file.name
        )
        with open(storage_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())

    st.success('Files uploaded successfully.')

pdf_choice_name = st.selectbox(
    'Select a PDF.',
    pdf_names,
    key = 'select_pdf'
)
display_pdfs = st.checkbox(
    'Display the selected PDF.', 
    value = False
)

if display_pdfs:
    if pdf_choice_name:
        st.write(f'Viewing PDF: {pdf_choice_name}')

        with st.spinner('Loading PDF ...'):
            pdf_choice_filepath = os.path.join(
                temp_dir, 
                pdf_choice_name
            )
            with open(
                pdf_choice_filepath, 
                mode = 'rb'
                ) as pdf_choice:
                images = convert_from_bytes(pdf_choice.read())

                for page_number, image in enumerate(images, 1):
                    st.image(image, caption = f'Page {page_number}')

st.markdown("""
            What would you like to do with all of these PDF files? )
- Extract texts: Extract and export the texts as a CSV file
- Ask questions: Ask questions to get answers from your documents.
            
Please make your selection below.
""")
radio_button = st.radio("Select an action:", ['Extract texts', 'Answer questions'], index = None)

if radio_button == 'Extract texts':
    if st.button('Extract'):
        extract_text(
            pdf_directory = temp_dir,
            pdf_filepath = None,
            extraction_dir = extraction_dir,
            progress_text = 'Extracting files...',
            enable_downloads = True,
            chunk_extraction = False
        )
elif radio_button == 'Ask questions':
    text = st.text_input('Enter a question:')
    if st.button('Ask'):
        qa.answer_question(
            question = text,
            pdf_directory = temp_dir,
            extraction_dir = qa_extraction_dir,
            extraction_progress_text = 'Preprocessing texts...'
        )

