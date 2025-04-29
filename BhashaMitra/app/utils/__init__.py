# BhashaMitra\app\utils\__init__.py

import logging
from .language_utils import get_language_code, validate_language
from .file_util import save_uploaded_file, read_file, delete_file

# Set up logging for utils package
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("Utils package initialized.")

# Preload common utility functions
__all__ = ["get_language_code", "validate_language", "save_uploaded_file", "read_file", "delete_file"]
