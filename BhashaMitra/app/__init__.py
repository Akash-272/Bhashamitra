
# Initialize the app package.
# This can be used for app-wide logging or to initialize necessary components at the start.

import logging

# Set up logging for the entire app
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("App package initialized.")
