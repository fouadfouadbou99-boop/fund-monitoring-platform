import os

from dotenv import load_dotenv
from openai import OpenAI

from ai.prompts import PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_document(document_text):

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
