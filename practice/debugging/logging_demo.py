import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("training.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


logger.info("Starting training")
logger.info("Learning rate: 0.001")
logger.warning("Loss spike detected")
logger.error("Example error message")

print("Logging demo completed")
