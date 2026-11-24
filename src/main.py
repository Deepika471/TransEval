
from data_loader import load_dataset, display_dataset_summary


def main():

    print("=" * 50)
    print(" INDIAN LANGUAGE LLM EVALUATION SYSTEM ")
    print("=" * 50)

    print("\nLoading dataset...")

    dataset = load_dataset()

    print("Dataset loaded successfully!")

    display_dataset_summary(dataset)

    print("First sample details:\n")

    sample = dataset.iloc[0]

    print("Sample ID:", sample["sample_id"])
    print("Source Language:", sample["source_language"])
    print("Target Language:", sample["target_language"])
    print("Translation Direction:", sample["translation_direction"])
    print("Text Category:", sample["text_type"])
    print("Original Text:", sample["source_text"])
    print("Reference Translation:", sample["reference_translation"])

    print("\nStep 2 dataset validation completed successfully!")


if __name__ == "__main__":
    main()
