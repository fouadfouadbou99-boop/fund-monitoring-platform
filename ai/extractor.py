import streamlit as st

from openai import OpenAI

from ai.prompts import PROMPT


def analyze_document(document_text):

    if "OPENAI_API_KEY" not in st.secrets:

        raise Exception(
            """
            La clé OPENAI_API_KEY n'est pas configurée.

            Ouvrez :
            Manage App
            → Settings
            → Secrets

            Puis ajoutez :

            OPENAI_API_KEY="votre_cle_openai"
            """
        )

    client = OpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": PROMPT
            },
            {
                "role": "user",
                "content": document_text
            }
        ]
    )

    return response.choices[0].message.content
