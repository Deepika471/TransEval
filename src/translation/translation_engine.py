
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from src.translation.providers.openai_provider import translate_text as openai_translate
from src.translation.providers.gemini_provider import translate_text as gemini_translate
from src.translation.providers.claude_provider import translate_text as claude_translate
from src.translation.providers.google_translate_provider import translate_text as google_translate
from src.translation.providers.llama_provider import translate_text as llama_translate


def translate_with_model(
    model_name,
    text,
    source_language,
    target_language
):

    start_time = time.time()

    try:

        if model_name == "GPT-3.5":
            translation = openai_translate(
                text,
                source_language,
                target_language,
                model_id="gpt-3.5-turbo"
            )

        elif model_name == "GPT-4o":
            translation = openai_translate(
                text,
                source_language,
                target_language,
                model_id="gpt-4o"
            )

        elif model_name == "Gemini":
            translation = gemini_translate(
                text,
                source_language,
                target_language
            )

        elif model_name == "Claude":
            translation = claude_translate(
                text,
                source_language,
                target_language
            )

        elif model_name == "Google Translate":
            translation = google_translate(
                text,
                source_language,
                target_language
            )

        elif model_name == "Llama":
            translation = llama_translate(
                text,
                source_language,
                target_language
            )

        else:
            raise ValueError(
                f"Unsupported model: {model_name}"
            )

        return {
            "model": model_name,
            "translation": translation,
            "execution_time": round(
                time.time() - start_time, 2
            ),
            "status": "success",
            "error": None
        }

    except Exception as e:

        return {
            "model": model_name,
            "translation": None,
            "execution_time": round(
                time.time() - start_time, 2
            ),
            "status": "failed",
            "error": str(e)
        }


def translate_with_multiple_models(
    selected_models,
    text,
    source_language,
    target_language
):

    results = []

    if not selected_models:
        return results

    with ThreadPoolExecutor(
        max_workers=len(selected_models)
    ) as executor:

        futures = {
            executor.submit(
                translate_with_model,
                model,
                text,
                source_language,
                target_language
            ): model
            for model in selected_models
        }

        for future in as_completed(futures):

            model_name = futures[future]

            try:
                result = future.result()

            except Exception as e:

                result = {
                    "model": model_name,
                    "translation": None,
                    "execution_time": None,
                    "status": "failed",
                    "error": str(e)
                }

            results.append(result)

    return results
