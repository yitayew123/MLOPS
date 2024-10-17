import logging
import os
from datetime import datetime

# Create a log file with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where the log files will be saved
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

# Full path of the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

# Example log messages
logging.info("Logging setup complete.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")


