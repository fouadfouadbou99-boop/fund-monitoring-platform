import streamlit as st
import google.generativeai as genai

from ai.prompts import PROMPT


def analyze_document(document_text):

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "models/gemini-3.6-flash"
    )

    response = model.generate_content(
        "Réponds uniquement : OK"
    )

    return response.text
