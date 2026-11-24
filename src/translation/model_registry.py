
MODEL_REGISTRY = {
    "GPT-3.5": {
        "provider": "OpenAI",
        "model_id": "gpt-3.5-turbo"
    },
    "GPT-4o": {
        "provider": "OpenAI",
        "model_id": "gpt-4o"
    },
    "Gemini": {
        "provider": "Google",
        "model_id": "gemini"
    },
    "Claude": {
        "provider": "Anthropic",
        "model_id": "claude"
    },
    "Google Translate": {
        "provider": "Google Cloud",
        "model_id": "translation-api"
    },
    "Llama": {
        "provider": "Groq",
        "model_id": "llama"
    }
}


def get_model_details(model_name):
    return MODEL_REGISTRY.get(model_name)


def get_available_models():
    return list(MODEL_REGISTRY.keys())


def get_configured_models():
    return list(MODEL_REGISTRY.keys())
