import streamlit as st
from openai import OpenAI

from ai.prompts import PROMPT


def analyze_document(document_text):

    try:

        client = OpenAI(
            api_key=st.secrets["OPENAI_API_KEY"]
        )

        response = client.chat.completions.create(

            model="gpt-4o-mini",

            temperature=0,

            messages=[
                {
                    "role": "system",
                    "content": PROMPT
                },
                {
                    "role": "user",
                    "content": document_text[:30000]
                }
            ]

        )

        return response.choices[0].message.content

    except Exception as e:

        raise Exception(
            f"Erreur OpenAI : {str(e)}"
        )
