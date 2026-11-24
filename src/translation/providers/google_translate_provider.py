
import os
from dotenv import load_dotenv
from google.cloud import translate_v2 as translate

load_dotenv()

client = None


def get_client():
    global client

    if client is None:
        credentials_path = os.getenv(
            "GOOGLE_APPLICATION_CREDENTIALS"
        )

        if not credentials_path:
            raise ValueError(
                "Google Cloud credentials are not configured."
            )

        client = translate.Client()

    return client


LANGUAGE_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Marathi": "mr"
}


def translate_text(text, source_language, target_language):

    translator = get_client()

    source_code = LANGUAGE_CODES[source_language]
    target_code = LANGUAGE_CODES[target_language]

    result = translator.translate(
        text,
        source_language=source_code,
        target_language=target_code,
        format_="text"
    )

    return result["translatedText"]
