import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_community.llms import HuggingFaceEndpoint

huggingface_api_key = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_key

# Mendefinisikan model AI
llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",
    huggingface_api_key= huggingface_api_key
)

def chatbot(user_input):
    # defining a template
    template = """Question: {question}
    please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return llm(formated_prompt)

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(share=True)
