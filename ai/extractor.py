import streamlit as st

from openai import OpenAI

from ai.prompts import PROMPT


def analyze_document(document_text):

    key = st.secrets["OPENAI_API_KEY"]

    if not key.startswith("sk-"):

        raise Exception(
            f"Clé API invalide : {key[:10]}"
        )

    client = OpenAI(
        api_key=key
    )

    response = client.chat.completions.create(

        model="gpt-4o",

        messages=[
            {
                "role": "system",
                "content": PROMPT
            },
            {
                "role": "user",
                "content": document_text[:5000]
            }
        ]

    )

    return response.choices[0].message.content
