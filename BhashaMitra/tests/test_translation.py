from app.services.translation_service import translate_text

def test_translation():
    text = "This is a test."
    translated = translate_text(text, "Marathi")
    assert isinstance(translated, str)
    assert len(translated) > 0