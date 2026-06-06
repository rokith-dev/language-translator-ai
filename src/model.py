from deep_translator import GoogleTranslator

LANGUAGE_CODES = {
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de"
}

def translate_text(text, language):
    translated = GoogleTranslator(
        source="en",
        target=LANGUAGE_CODES[language]
    ).translate(text)

    return translated