from gtts import gTTS
import os

class TextToSpeech:
    def __init__(self, language='en'):
        self.language = language

    def speak(self, text):
        tts = gTTS(text=text, lang=self.language, slow=False)
        tts_file = "temp_audio.mp3"
        tts.save(tts_file)
        os.system(f"start {tts_file}")  # This will work on Windows to play the audio file. Adjust for other OS if needed.