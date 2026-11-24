
import streamlit as st
import time

from src.translation.translation_engine import (
    translate_with_multiple_models
)

from src.evaluation.semantic import (
    calculate_semantic_similarity
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Multilingual AI Translation & Evaluation",
    page_icon="🌐",
    layout="wide"
)


# --------------------------------------------------
# APPLICATION TITLE
# --------------------------------------------------

st.title("🌐 Multilingual AI Translation & Evaluation System")

st.markdown(
    """
    Translate text between Indian languages and English using multiple AI models.
    Compare translations and evaluate their quality using our multidimensional framework.
    """
)

st.divider()


# --------------------------------------------------
# LANGUAGE CONFIGURATION
# --------------------------------------------------

languages = [
    "English",
    "Hindi",
    "Telugu",
    "Tamil",
    "Kannada",
    "Marathi"
]


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.subheader("📝 Translation Input")

col1, col2 = st.columns(2)

with col1:

    source_language = st.selectbox(
        "Source Language",
        languages,
        index=0
    )

with col2:

    target_language = st.selectbox(
        "Target Language",
        languages,
        index=2
    )


input_text = st.text_area(
    "Enter the text you want to translate",
    placeholder="Type or paste your text here...",
    height=200
)


# --------------------------------------------------
# MODEL SELECTION
# --------------------------------------------------

st.subheader("🤖 Select Translation Models")

models = {
    "GPT-3.5": "OpenAI",
    "GPT-4o": "OpenAI",
    "Gemini": "Google",
    "Claude": "Anthropic",
    "Google Translate": "Google",
    "Llama": "Meta"
}

selected_models = []

model_columns = st.columns(3)

for index, (model_name, provider) in enumerate(models.items()):

    with model_columns[index % 3]:

        selected = st.checkbox(
            model_name,
            key=f"model_{model_name}"
        )

        if selected:
            selected_models.append(model_name)


# --------------------------------------------------
# TRANSLATION EXECUTION
# --------------------------------------------------

st.divider()

if st.button("🚀 Translate", use_container_width=True):

    # Input validation

    if not input_text.strip():

        st.warning("Please enter some text to translate.")

    elif source_language == target_language:

        st.warning(
            "Source and target languages cannot be the same."
        )

    elif not selected_models:

        st.warning(
            "Please select at least one translation model."
        )

    else:

        # --------------------------------------------------
        # GENERATE TRANSLATIONS
        # --------------------------------------------------

        st.subheader("🌐 Translation Results")

        start_time = time.time()

        with st.spinner(
            "Generating translations from selected models..."
        ):

            results = translate_with_multiple_models(
                selected_models=selected_models,
                text=input_text,
                source_language=source_language,
                target_language=target_language
            )

        total_time = round(
            time.time() - start_time,
            2
        )

        st.success(
            f"Completed {len(results)} model requests "
            f"in {total_time} seconds."
        )


        # --------------------------------------------------
        # DISPLAY TRANSLATIONS AND SEMANTIC EVALUATION
        # --------------------------------------------------

        if results:

            result_columns = st.columns(
                min(len(results), 2)
            )

            for index, result in enumerate(results):

                with result_columns[index % len(result_columns)]:

                    with st.container(border=True):

                        st.markdown(
                            f"### 🤖 {result['model']}"
                        )

                        # ----------------------------------
                        # SUCCESSFUL TRANSLATION
                        # ----------------------------------

                        if result["status"] == "success":

                            st.markdown("**Translation**")

                            st.write(
                                result["translation"]
                            )

                            st.caption(
                                f"⏱ Execution time: "
                                f"{result['execution_time']} seconds"
                            )


                            # ----------------------------------
                            # SEMANTIC EVALUATION
                            # ----------------------------------

                            try:

                                semantic_result = (
                                    calculate_semantic_similarity(
                                        original_text=input_text,
                                        translated_text=result["translation"]
                                    )
                                )

                                st.divider()

                                st.markdown(
                                    "### 🧠 Semantic Evaluation"
                                )

                                st.metric(
                                    label="Semantic Similarity",
                                    value=semantic_result["score"]
                                )

                                score = semantic_result["score"]

                                st.progress(
                                    max(
                                        0.0,
                                        min(1.0, score)
                                    )
                                )

                                st.caption(
                                    f"Evaluation model: "
                                    f"{semantic_result['model']}"
                                )

                                st.info(
                                    semantic_result[
                                        "interpretation"
                                    ]
                                )

                            except Exception as e:

                                st.warning(
                                    "Semantic evaluation could not "
                                    f"be completed: {e}"
                                )


                        # ----------------------------------
                        # FAILED TRANSLATION
                        # ----------------------------------

                        else:

                            st.error(
                                f"Translation failed: "
                                f"{result['error']}"
                            )


        # --------------------------------------------------
        # REQUEST SUMMARY
        # --------------------------------------------------

        st.divider()

        st.subheader("📊 Request Summary")

        summary_col1, summary_col2, summary_col3 = st.columns(3)

        summary_col1.metric(
            "Source Language",
            source_language
        )

        summary_col2.metric(
            "Target Language",
            target_language
        )

        summary_col3.metric(
            "Models Selected",
            len(selected_models)
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Multilingual AI Translation & Evaluation System | "
    "Research Project"
)
