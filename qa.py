from typing import List, Tuple
from summarizer import Summarizer
from database_obj import TextDB
from llm import answer
from extract_texts import extract_text
import streamlit as st
import os


model = Summarizer()

# check if a pdf has already been extracted
def extraction_exists(
        pdf_directory: str,
        extraction_dir: str
                      ) -> Tuple[List[str], List[str]]:
    fnames = os.listdir(pdf_directory)
    pdf_filepaths = [os.path.join(pdf_directory, name) for name in fnames]
    all_csv_filepaths = [os.path.join(extraction_dir, name)[:-3] + ".csv" for name in fnames]
    unextracted_pdfs = [pdf_filepaths[i] for i in range(len(pdf_filepaths))
                        if not os.path.exists(all_csv_filepaths[i])]
    return unextracted_pdfs, all_csv_filepaths

def answer_question(question: str,
                    pdf_directory: str,
                    extraction_dir: str,
                    extraction_progress_text: str,
                    chunk_extraction: bool = True
                ):
    
    unextracted_pdf_filepaths, all_csv_filepaths = extraction_exists(pdf_directory,
                                                                     extraction_dir
                                                                     )

    extract_text(pdf_filepaths = unextracted_pdf_filepaths,
                 extraction_dir = extraction_dir,
                 progress_text = extraction_progress_text,
                 enable_downloads = False,
                 chunk_extraction = chunk_extraction
                )
    
    cache_dir = 'db'
    db = TextDB.retrieve_cache(all_csv_filepaths, 
                               cache_dir
                            )

    with st.spinner('Creating DB...'):
        if db == None:
            db = TextDB(all_csv_filepaths)
            db.create_cache(all_csv_filepaths,
                            cache_dir
                        )
        else:
            df, index = db
            db = TextDB()
            db.df = df
            db.index = index

    df = db.semantic_search(question, n = 3)
    texts = '\n'.join([model(t, ratio = 0.5) for t in df['TEXT']])

    with st.spinner('Thinking...'):
        response = answer(question, texts)
    st.info(response)
