from gtts import gTTS
from playsound import playsound
import os
import tempfile

def text_to_speech(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tmp_filename = tmp_file.name
        tts.save(tmp_filename)
        playsound(tmp_filename)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.exists(tmp_filename):
            os.remove(tmp_filename)

if __name__ == "__main__":
    text = input("Enter text to convert to speech: ")
    language = input("Enter language ('ko' for Korean, 'en' for English): ")
    text_to_speech(text, lang=language)