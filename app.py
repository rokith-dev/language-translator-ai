import streamlit as st
from src.model import translate_text

st.title("🌍 Language Translator AI")

text = st.text_area("Enter English Text")

if st.button("Translate"):
    result = translate_text(text)

    st.subheader("Tamil Translation")
    st.write(result)