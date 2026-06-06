import streamlit as st
from src.model import translate_text
from src.database import save_translation
from src.database import save_translation, get_history

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

    st.divider()

st.subheader("Translation History")

history = get_history()

st.table(
    history
)