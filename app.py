import streamlit as st

from src.model import translate_text
from src.database import save_translation, get_history
from src.text_to_speech import text_to_speech
from src.file_handler import read_pdf, create_pdf

# =========================
# App Title
# =========================

st.title("🌍 Language Translator AI")

# =========================
# Language Selection
# =========================

language = st.selectbox(
    "Select Language",
    ["Tamil", "Hindi", "French", "German"]
)

# =========================
# PDF Translator
# =========================

st.header("📄 PDF Translator")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    extracted_text = read_pdf(uploaded_file)

    st.subheader("Extracted Text")

    st.text_area(
        "PDF Content",
        extracted_text,
        height=200
    )

    if st.button("Translate PDF"):

        translated_pdf_text = translate_text(
            extracted_text,
            language
        )

        st.subheader("Translated PDF Content")

        st.text_area(
            "Translation",
            translated_pdf_text,
            height=200
        )

        pdf_file = create_pdf(
            translated_pdf_text
        )

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📥 Download Translated PDF",
                data=file,
                file_name="translated_document.pdf",
                mime="application/pdf"
            )

# =========================
# Text Translator
# =========================

st.header("📝 Text Translator")

text = st.text_area(
    "Enter English Text",
    height=150
)

if st.button("Translate"):

    result = translate_text(
        text,
        language
    )

    save_translation(
        text,
        language,
        result
    )

    st.subheader(f"{language} Translation")

    st.write(result)

    language_codes = {
        "Tamil": "ta",
        "Hindi": "hi",
        "French": "fr",
        "German": "de"
    }

    audio_file = text_to_speech(
        result,
        language_codes[language]
    )

    with open(audio_file, "rb") as audio:

        audio_bytes = audio.read()

    st.audio(audio_bytes)

# =========================
# Translation History
# =========================

st.divider()

st.subheader("📚 Translation History")

history = get_history()

st.table(history)