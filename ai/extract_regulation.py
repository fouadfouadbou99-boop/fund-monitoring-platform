from openai import OpenAI
import os

from ai.regulation_prompt import REGULATION_PROMPT

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def extract_regulation_rules(text):

    response = client.chat.completions.create(

        model="gpt-4o",

        temperature=0,

        messages=[

            {
                "role": "system",
                "content": REGULATION_PROMPT
            },

            {
                "role": "user",
                "content": text
            }

        ]

    )

    return response.choices[0].message.content
