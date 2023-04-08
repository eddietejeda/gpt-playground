from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext, SimpleDirectoryReader
from langchain import OpenAI
import gradio as gr
import sys
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def create_index(path):
    # recursive=True, required_exts=["md", "rb"]
    # load documents
    documents = SimpleDirectoryReader(input_dir=path, recursive=False).load_data()

    # define LLM
    # text-ada-001
    # text-davinci-003
    # gpt-3.5-turbo
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="gpt-3.5-turbo"))

    # define prompt helper
    # set maximum input size
    max_input_size = 16384
    # set number of output tokens
    num_output = 1024
    # set maximum chunk overlap
    max_chunk_overlap = 80
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)
    index.save_to_disk('result/simple.json')
    return index

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('result/simple.json')
    response = index.query(input_text, response_mode="tree_summarize")
    return response.response


def run():
    index = create_index("data")
    iface = gr.Interface(fn=chatbot,
                            inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                            outputs="text",
                            title="Custom AI Chatbot",
                            server_name="0.0.0.0")
    iface.launch()