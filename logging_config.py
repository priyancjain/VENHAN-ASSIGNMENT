import logging

# Set up logging
def setup_logging():
    logging.basicConfig(
        filename='library.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Function to log informational messages
def log_info(message):
    logging.info(message)

# Function to log error messages
def log_error(message):
    logging.error(message)
