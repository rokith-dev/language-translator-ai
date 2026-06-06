from gtts import gTTS

def text_to_speech(text, language_code):

    speech = gTTS(
        text=text,
        lang=language_code
    )

    speech.save("translation.mp3")

    return "translation.mp3"