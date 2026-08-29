import json
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

    prompt = f"""
{PROMPT}

DOCUMENT :

{document_text[:5000]}
"""

    response = model.generate_content(prompt)

    response_text = response.text

    response_text = (
        response_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(response_text)
