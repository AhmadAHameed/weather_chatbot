import logging
import os
from datetime import datetime

logging_str = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"
log_folder = "logs/"
os.makedirs(log_folder, exist_ok=True)

log_file_name = f"{datetime.now().strftime('%m_%d_%Y__%H_%M_%S')}.log"
log_file_path = os.path.join(log_folder, log_file_name)

logging.basicConfig(
    format=logging_str,
    level=logging.INFO,
    handlers=[logging.FileHandler(log_file_path), logging.StreamHandler()],
)


# logging.Formatter(logging_str)

logger = logging.getLogger("Project_Logger")

if __name__ == "__main__":
    logger.info("Ahmad")
