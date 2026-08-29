import streamlit as st
import google.generativeai as genai

from ai.prompts import PROMPT


def analyze_document(document_text):

    try:

        genai.configure(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        model = genai.GenerativeModel(
            "models/gemini-2.5-flash"
        )

        prompt = f"""
{PROMPT}

DOCUMENT :

{document_text[:3000]}
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"ERREUR GEMINI : {str(e)}"
