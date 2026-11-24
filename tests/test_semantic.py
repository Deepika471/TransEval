
from src.evaluation.semantic import calculate_semantic_similarity


original = "I like learning new things."

translated = "నాకు కొత్త విషయాలు నేర్చుకోవడం ఇష్టం."


result = calculate_semantic_similarity(
    original_text=original,
    translated_text=translated
)

print("\n===== SEMANTIC EVALUATION =====")

print("Original:", original)
print("Translation:", translated)

print("Similarity Score:", result["score"])
print("Metric:", result["metric"])
print("Evaluation Model:", result["model"])
print("Interpretation:", result["interpretation"])
