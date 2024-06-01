import logging

# Create separate loggers for info and error
info_logger  = logging.getLogger("info_logger")
error_logger = logging.getLogger("error_logger")

# Set the logging levels
info_logger.setLevel(logging.INFO)
error_logger.setLevel(logging.ERROR)

# Create file handlers
info_handler = logging.FileHandler('./info.log')
error_handler = logging.FileHandler('./error.log')

# Set the logging levels for the handlers
info_handler.setLevel(logging.INFO)
error_handler.setLevel(logging.ERROR)

# Create formatters and add them to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# Add handlers to the loggers
info_logger.addHandler(info_handler)
error_logger.addHandler(error_handler)

# Example log messages
info_logger.info("This is an informational message.")
error_logger.error("This is an error message.")

x = 500
info_logger.info(f"The x value is {x}")

try:
    1 / 0
except ZeroDivisionError as e:
    error_logger.error("ZeroDivisionError occurred", exc_info=True)
    error_logger.exception("Exception details")

# Additional log messages to demonstrate logging levels
info_logger.debug("This debug message will not be logged because the level is set to INFO.")
error_logger.critical("This critical message will be logged to error.log.")

# Note: This part demonstrates how to configure the root logger if needed
logging.basicConfig(level=logging.DEBUG, filemode='w', filename='./Basic.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("This is information log to Basic.log")
logging.debug("This is debug information to Basic.log")
logging.error("This is error information to Basic.log")
logging.critical("This is critical information to Basic.log")
logging.warning("This is warning information to Basic.log")
