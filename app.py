import gradio as gr
"""
Entry point for the application.

"""
import os
import logo_loader
from aiwrite.gradgui import app



if __name__ == "__main__":
    b64logo = logo_loader.get_logo_base64()
    app.main(db_path=os.getenv("DB_PATH", "/data"), logo=b64logo)