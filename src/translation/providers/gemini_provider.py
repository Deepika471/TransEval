
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_ID = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

client = genai.Client(api_key=API_KEY) if API_KEY else None


def translate_text(text, source_language, target_language):

    if not API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured.")

    prompt = f"""
Translate from {source_language} to {target_language}.

Preserve meaning, tone, sentiment, and context.
Do not summarize or explain.
Return only the translation.

Text:
{text}
"""

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text.strip()
