
from app.config.settings import LANGUAGE_CODES

def get_language_code(language_name):
    """Get the language code for a given language name."""
    return LANGUAGE_CODES.get(language_name, None)

def validate_language(language_name):
    """Validate if the language is supported."""
    if language_name not in LANGUAGE_CODES:
        raise ValueError(f"Unsupported language: {language_name}")
    return True
