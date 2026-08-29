import json


def clean_response(response_text):

    response_text = response_text.strip()

    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "")

    if response_text.endswith("```"):
        response_text = response_text.replace("```", "")

    return json.loads(response_text)
