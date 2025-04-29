
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("Services package initialized.")

# Example: Shared state (can be used across services)
shared_state = {
    "lang_models_loaded": False
}
