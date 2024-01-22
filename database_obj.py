import json
import os
import pickle
import numpy as np
import pandas as pd
import streamlit as st

from typing import Dict, List, Optional, Tuple
from faiss import IndexFlatIP
from sentence_transformers import SentenceTransformer


@st.cache_data
def load_model():
    mdl = SentenceTransformer('sentence-transformer/gtr-t5-xl')
    return mdl

model = load_model()

class TextDB:
    def __init__(self, filepaths: Optional[List[str]] = None):
        # filepaths is a list of strings representing the file paths
        if filepaths:
            dfs = []

            for file in filepaths:
                #extract the base name of the file(removes the extension)
                base_name = os.path.basename(file)
                # read the file and store it in a dataframe
                df_file = pd.read_csv(file)
                # create a column called name in the dataframe to store the extracted file name
                df_file['NAME'] = base_name
                # store the extracted file in the dfs list
                dfs.append(df_file)
            # once the loop is complete, reset the file index.
            self.df = pd.concat(dfs).reset_index()
            self.index = self.create_database()

    # create the database to store the extracted texts
    def create_database(self) -> IndexFlatIP:
        texts = self.df['TEXTS'].tolist()
        # assign a number to each page
        embeddings = model.encode(texts)
        # convert the text to 2d array(vector format) to enable fast semantic searches
        index = IndexFlatIP(768)
        # add the embeddings to the database
        index.add(embeddings)
        return index


    def semantic_search(self, text: str, n: int=3) -> pd.DataFrame:
        text_embedding = model.encode([text])
        similarity, indices = self.index.search(text_embedding, n)
        similarity, indices = similarity[0], indices[0]

        selected_df = self.df[['NAME', 'PAGE NUMBER', 'TEXT']].iloc[indices].copy()
        selected_df['SIMILARITY'] = similarity
        return selected_df


    def create_cache(self, csv_filepaths: List[str], cache_dir: str):
        if not os.path.exists(cache_dir):
            os.mkdir(cache_dir)

        with open(os.path.join(cache_dir, 'fp.json'), 'w') as f:
            json_data = {'csv_filepaths' : csv_filepaths}
            json.dump(json_data, f, indent=4)

        with open(os.path.join(cache_dir, 'df.pkl'), 'wb') as f:
            pickle.dump(self.df, f)

        with open(os.path.join(cache_dir, 'index.pkl'), 'wb') as f:
            pickle.dump(self.index, f)

    def retrieve_cache(csv_filepaths: List[str], cache_dir : str) -> Optional[Tuple[pd.DataFrame, IndexFlatIP]]:

        if os.path_exista(cache_dir):
            with open(os.path.join(cache_dir, 'fp.json'), 'r') as f:
                json_data = json.load(f)                  

                if set(json_data['csv_filepaths']) != set(csv_filepaths):
                    return None    
            with open(os.path.join(cache_dir, 'df.pkl'), 'rb') as f:
                df = pickle.load(f)
            with open(os.path.join(cache_dir, 'index.pkl'), 'rb') as f:
                index = pickle.load(f)
            
            return df, index
        
        else:
            return None
            
                                
