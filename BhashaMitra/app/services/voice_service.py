import pyttsx3

def speak_text(text, lang):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    lang_code = {"Marathi": "mr", "Tamil": "ta", "Bengali": "bn"}.get(lang, "mr")
    for voice in voices:
        if lang_code in voice.id:
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()