
import logging
import os
from .settings import LANGUAGE_CODES, TRANSLATION_MODEL_NAME, SIMPLIFICATION_MODEL_NAME, LOG_LEVEL, ENABLE_VOICE_OUTPUT, SIMPLIFICATION_MAX_LENGTH

# Set up logging
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("Config package initialized.")

# Environment variables (can be loaded using `dotenv` if needed)
os.environ["LANGUAGE_CODES"] = str(LANGUAGE_CODES)
os.environ["TRANSLATION_MODEL_NAME"] = TRANSLATION_MODEL_NAME
os.environ["SIMPLIFICATION_MODEL_NAME"] = SIMPLIFICATION_MODEL_NAME
os.environ["LOG_LEVEL"] = LOG_LEVEL
os.environ["ENABLE_VOICE_OUTPUT"] = str(ENABLE_VOICE_OUTPUT)
os.environ["SIMPLIFICATION_MAX_LENGTH"] = str(SIMPLIFICATION_MAX_LENGTH)
