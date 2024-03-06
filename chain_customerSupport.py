import gradio as gr
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
import os

# Mengatur LLM
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceEndpoint(repo_id="tiiuae/falcon-7b-instruct", temperature=0.9, max_new_tokens=600)

def handle_complaint(komplain: str) -> str:
    #Buat instance LLM dengan nilai temprature 0,9 (nilai lebih tinggi membuat keluaran lebih acak).
    

    # Merancang template untuk merespon komplain
    prompt = PromptTemplate(input_variables=["komplain"], template="Saya seorang perwakilan layanan pelanggan. Saya menerima keluhan berikut: {komplain}. Respon saya adalah:")

    # Membuat model bahasa berantai dengan template yang telah dirancang
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(komplain)

# Membuat antarmuka Gradio untuk fungsi handle_complaint
iface = gr.Interface(fn=handle_complaint, inputs="text", outputs="text")
iface.launch(share=True)
