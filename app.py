import streamlit as st
from src.model import translate_text
from src.database import save_translation

st.title("🌍 Language Translator AI")

language = st.selectbox(
    "Select Language",
    ["Tamil", "Hindi", "French", "German"]
)

text = st.text_area("Enter English Text")

if st.button("Translate"):

    result = translate_text(text, language)

    save_translation(
        text,
        language,
        result
    )

    st.subheader(f"{language} Translation")
    st.write(result)