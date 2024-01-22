from ilama_cpp import Llama

import streamlit as st

@st.cache_data
def load_llm():
    model_path = 