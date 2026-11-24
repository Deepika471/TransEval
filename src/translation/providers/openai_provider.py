
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY) if API_KEY else None

GPT35_MODEL = os.getenv("GPT35_MODEL", "gpt-3.5-turbo")
GPT4O_MODEL = os.getenv("GPT4O_MODEL", "gpt-4o")


def translate_text(text, source_language, target_language, model_id):
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY is not configured.")

    prompt = f"""
Translate the following text from {source_language}
to {target_language}.

Preserve meaning, tone, sentiment, and context.
Do not summarize, add information, or explain.
Return only the translated text.

Text:
{text}
"""

    response = client.responses.create(
        model=model_id,
        input=prompt
    )

    return response.output_text.strip()
