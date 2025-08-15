import gradio as gr
"""
Entry point for the application.

"""
import os
from aiwrite.gradgui import app



if __name__ == "__main__":
    app.main(db_path=os.getenv("DB_PATH", "/data"))