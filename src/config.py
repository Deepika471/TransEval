import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PROJECT_NAME = "Indian Language LLM Evaluation Framework"

LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Marathi": "mr"
}

INDIAN_LANGUAGES = [
    "Telugu",
    "Hindi",
    "Tamil",
    "Kannada",
    "Marathi"
]

TARGET_LANGUAGE = "English"

TRANSLATION_DIRECTIONS = [
    "te-en",
    "en-te",
    "hi-en",
    "en-hi",
    "ta-en",
    "en-ta",
    "kn-en",
    "en-kn",
    "mr-en",
    "en-mr"
]

TEXT_CATEGORIES = [
    "general",
    "literary"
]

EVALUATION_DIMENSIONS = [
    "semantic_similarity",
    "sentiment_preservation",
    "linguistic_quality",
    "contextual_consistency",
    "keyword_trigram_analysis"
]
