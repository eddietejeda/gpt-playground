from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext, SimpleDirectoryReader
from langchain import OpenAI
import gradio as gr
import sys
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def create_index(path):
    return path


def run():
    print ("hello summerize")
    # index = create_index("data")
