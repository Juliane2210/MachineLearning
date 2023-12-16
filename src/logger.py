import logging
import os
from datetime import datetime

# name of the log file will be the date w/ time of creation
# beginin with"log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# creating the logs directory in the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# creating the full path for the log file by joining the LOG_FILE and the path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logging module (setting up the basic configuration for the logging system)
logging.basicConfig(
    # file where the logs will be written
    filename=LOG_FILE_PATH,
    # format of the log messages
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # minimum log level set to INFO (messages with INFO level or higher will be logged)
    level=logging.INFO,

)

if __name__ == "__main__":
    logging.info("Logging has started")
