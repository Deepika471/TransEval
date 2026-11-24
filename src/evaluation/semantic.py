

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the multilingual semantic model
_model = None


def get_semantic_model():
    global _model

    if _model is None:
        _model = SentenceTransformer(
            "sentence-transformers/LaBSE"
        )

    return _model


def calculate_semantic_similarity(
    original_text,
    translated_text
):
    """
    Compare the semantic meaning of the original text
    and its translated text using multilingual embeddings.

    Returns a cosine similarity score.
    """

    if not original_text.strip():
        raise ValueError("Original text cannot be empty.")

    if not translated_text.strip():
        raise ValueError("Translated text cannot be empty.")

    model = get_semantic_model()

    embeddings = model.encode(
        [original_text, translated_text],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    similarity = float(similarity)

    return {
        "score": round(similarity, 4),
        "metric": "Cosine Similarity",
        "model": "LaBSE",
        "interpretation": interpret_similarity(similarity)
    }


def interpret_similarity(score):
    """
    Heuristic interpretation of the similarity score.
    These are not validated translation-quality thresholds.
    """

    if score >= 0.85:
        return "Very high semantic similarity"

    elif score >= 0.70:
        return "High semantic similarity"

    elif score >= 0.50:
        return "Moderate semantic similarity"

    else:
        return "Low semantic similarity"
