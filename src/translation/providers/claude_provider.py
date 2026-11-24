
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL_ID = os.getenv(
    "CLAUDE_MODEL",
    "claude-3-5-sonnet-20241022"
)

client = Anthropic(api_key=API_KEY) if API_KEY else None


def translate_text(text, source_language, target_language):

    if not API_KEY:
        raise ValueError("ANTHROPIC_API_KEY is not configured.")

    prompt = f"""
Translate from {source_language} to {target_language}.

Preserve meaning, tone, sentiment, and context.
Do not summarize, add information, or explain.
Return only the translated text.

Text:
{text}
"""

    response = client.messages.create(
        model=MODEL_ID,
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return "".join(
        block.text
        for block in response.content
        if block.type == "text"
    ).strip()
