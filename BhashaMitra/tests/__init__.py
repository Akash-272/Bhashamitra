
import logging

# Set up logging for the tests package
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("Tests package initialized.")

# Any test-specific setup can go here (e.g., database connections, mock services)
