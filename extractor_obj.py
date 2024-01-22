import os
import numpy as np
import pandas as pd

from typing import List, Literal, Optional
from pdf2image import convert_from_bytes
from pytesseract import image_to_string
from tqdm import tqdm

class PDFextractor:
    def __init__(
            self,
            filepaths : List[str],
            chunk : bool=False):
        
        self.filepath = filepaths
        self.chunk = chunk


    def extract_text(self, filepath : str) -> List[List]:
        with open(filepath, 'rb') as f:
            pdf_as_images = convert_from_bytes(f.read( ))
            pdf_as_arrays = [np.asarray(img) for img in pdf_as_images]

            extracted_pages = []

            for n, page in enumerate(pdf_as_arrays, 1):
                # convert the page to string
                pg_text = image_to_string(page)

                #if the page is to be split into smaller chunks
                # split it based on the paragraphs or sections
                if self.chunk:
                    pg_text = pg_text.split('\n\n')
                    pg_text_ = ['']

                    # check if the chunks are less than 1500
                    # if they are, then combine the smaller chunks together separated by 2 newlines
                    for pgt in pg_text:
                        if len(pg_text_[-1] + pgt) <= 1500:
                            pg_text_[-1] = pg_text_[-1] + '\n\n' + pgt
                        else:
                            pg_text_.append(pgt)
                    for pgt in pg_text_:
                        extracted_pages.append([n, pgt])
                else:
                    extracted_pages.append(n, pg_text)
        return extracted_pages
                             

    def extract(self, save_dir: str) -> str:
        for i in tqdm(range(len(self.filepaths))):
            filepath = self.filepaths[i]
            extracted_pages = self.extract_text(filepath)
            as_df = pd.DataFrame(extracted_pages, columns=['PAGE_NUMBER', 'TEXT'])

            fname = os.path.basename(filepath)
            save_path = os.path.join(save_dir, fname)
            save_path = save_path[:-3]+'csv'

            if not os.path.exists(save_dir):
                os.mkdir(save_dir)

            as_df.to_csv(save_path)

            yield save_path







