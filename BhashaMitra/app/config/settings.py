# BhashaMitra\app\config\settings.py

import os

# Supported regional languages and their codes
LANGUAGE_CODES = {
    "Marathi": "mr",
    "Tamil": "ta",
    "Bengali": "bn"
}

# Translation model
TRANSLATION_MODEL_NAME = "ai4bharat/indictrans2-en-indic"

# Simplification model
SIMPLIFICATION_MODEL_NAME = "google/flan-t5-small"

# Logging level
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Voice output toggle
ENABLE_VOICE_OUTPUT = True

# Max length for simplification outputs
SIMPLIFICATION_MAX_LENGTH = 512
