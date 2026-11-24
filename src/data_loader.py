
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "processed" / "dataset.csv"

SUPPORTED_LANGUAGES = {
    "English",
    "Telugu",
    "Hindi",
    "Tamil",
    "Kannada",
    "Marathi"
}

SUPPORTED_DIRECTIONS = {
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
}

SUPPORTED_TEXT_TYPES = {
    "general",
    "literary"
}

REQUIRED_COLUMNS = [
    "sample_id",
    "source_language",
    "target_language",
    "translation_direction",
    "text_type",
    "source_text",
    "reference_translation",
    "reference_source",
    "split"
]


def load_dataset():

    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at: {DATASET_PATH}"
        )

    df = pd.read_csv(DATASET_PATH, encoding="utf-8")

    # Check required columns
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check missing values
    if df[REQUIRED_COLUMNS].isnull().any().any():
        raise ValueError(
            "Dataset contains missing values."
        )

    # Convert columns to strings and trim whitespace
    for column in REQUIRED_COLUMNS:
        df[column] = df[column].astype(str).str.strip()

    # Check duplicate IDs
    if df["sample_id"].duplicated().any():
        raise ValueError(
            "Duplicate sample_id values found."
        )

    # Check supported languages
    invalid_languages = (
        set(df["source_language"]) |
        set(df["target_language"])
    ) - SUPPORTED_LANGUAGES

    if invalid_languages:
        raise ValueError(
            f"Unsupported languages: {invalid_languages}"
        )

    # Check supported directions
    invalid_directions = (
        set(df["translation_direction"])
        - SUPPORTED_DIRECTIONS
    )

    if invalid_directions:
        raise ValueError(
            f"Unsupported directions: {invalid_directions}"
        )

    # Check text categories
    invalid_text_types = (
        set(df["text_type"])
        - SUPPORTED_TEXT_TYPES
    )

    if invalid_text_types:
        raise ValueError(
            f"Unsupported text types: {invalid_text_types}"
        )

    # Check empty strings
    text_columns = [
        "source_text",
        "reference_translation"
    ]

    for column in text_columns:
        if (df[column] == "").any():
            raise ValueError(
                f"Empty text found in column: {column}"
            )

    # Validate translation direction
    language_codes = {
        "Telugu": "te",
        "Hindi": "hi",
        "Tamil": "ta",
        "Kannada": "kn",
        "Marathi": "mr",
        "English": "en"
    }

    for _, row in df.iterrows():

        expected_direction = (
            f"{language_codes[row['source_language']]}-"
            f"{language_codes[row['target_language']]}"
        )

        if row["translation_direction"] != expected_direction:
            raise ValueError(
                f"Direction mismatch for sample "
                f"{row['sample_id']}"
            )

    return df


def display_dataset_summary(df):

    print("\n========== DATASET SUMMARY ==========\n")

    print(f"Total samples: {len(df)}")

    print("\nSamples per source language:")
    print(df["source_language"].value_counts())

    print("\nSamples per target language:")
    print(df["target_language"].value_counts())

    print("\nSamples per direction:")
    print(df["translation_direction"].value_counts())

    print("\nSamples per text type:")
    print(df["text_type"].value_counts())

    print("\nDataset preview:")

    print(
        df[
            [
                "sample_id",
                "source_language",
                "target_language",
                "translation_direction",
                "text_type"
            ]
        ].head()
    )

    print("\n==================================\n")
