from llama_cpp import Llama

import streamlit as st


    # model_path="/Users/rlm/Desktop/Code/llama.cpp/models/llama-2-13b-chat.ggufv3.q4_0.bin",
  

@st.cache_data
def load_llm():
    # original (loaded but returns ValueError: Model path does not exist: ../llama/llama-2-13b-chat/ggml-model-q4_0.bin when you load a pdf file)
    # adjusted path. returned OSError: exception: access violation reading 0x0000000000010100
    model_path = '../llama/llama-2-13b-chat/ggml-model-q4_0.bin'

    model = Llama(
        model_path = model_path, 
        n_ctx = 2048,
        n_gpu_layers = 1,
        use_mlock = True,
        f16_kv=True,
        verbose=True
    )
    return model
# test 
model = load_llm()

def answer(
        question: str, 
        texts: str
    ):
    prompt = f"""
    [INST] <<SYS>>
    You are a question answering system. You have the context provided to you \ to answer the question the user has asked. If the answer in not present, \ simply say you don't know the answer. Let your answer be short and precise.

    CONTEXT:

    {texts}

    QUESTION: {question}

    [/INST]
    """
    response = model(
        prompt = prompt, 
        max_tokens = 512, 
        temperature = 0.2
    )
    answer = response['choices'][0]['text']
    return answer
