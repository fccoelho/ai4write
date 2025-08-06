import gradio as gr
from huggingface_hub import InferenceClient
from aiwrite.gradgui import app

"""
 For more information on `huggingface_hub` Inference API support, please check the docs: https://huggingface.co/docs/huggingface_hub/v0.22.2/en/guides/inference
"""
client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")


if __name__ == "__main__":
    # demo.launch()
    app.main()