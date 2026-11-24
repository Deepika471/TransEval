
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL_ID = os.getenv(
    "LLAMA_MODEL",
    "llama-3.3-70b-versatile"
)

client = Groq(api_key=API_KEY) if API_KEY else None


def translate_text(text, source_language, target_language):

    if not API_KEY:
        raise ValueError("GROQ_API_KEY is not configured.")

    prompt = f"""
Translate from {source_language} to {target_language}.

Preserve meaning, tone, sentiment, and context.
Do not summarize or explain.
Return only the translation.

Text:
{text}
"""

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
