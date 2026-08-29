import streamlit as st
import google.generativeai as genai

from ai.prompts import PROMPT


def analyze_document(document_text):

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-flash-latest"
    )

    prompt = f"""
{PROMPT}

DOCUMENT :

{document_text[:5000]}
"""

    response = model.generate_content(
        prompt
    )

    return response.text
