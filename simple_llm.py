import os
from langchain_community.llms import HuggingFaceEndpoint
import gradio as gr

# Mengatur environment variable "OPENAI_API_KEY" dengan OpenAI API key milikmu. ini diperlukan untuk proses autentikasi ke OpenAI API.
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Mendefinisikan jenis model 
# llm = HuggingFaceHub(repo_id="openai-community/gpt2-large",model_kwargs={"temperature": 0.1, "max_new_tokens": 250})
# llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")
llm = HuggingFaceEndpoint(repo_id="tiiuae/falcon-7b-instruct")

def chatbot(prompt):
    return llm(prompt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)
