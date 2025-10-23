import logging

logger = logging.getLogger("ProjectPilotLogger")
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler(filename="logs.txt", mode="a")


# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Line %(lineno)d - %(message)s")
file_handler.setFormatter(formatter)


for handler in logger.handlers[:]:
    logger.removeHandler(handler)

logger.addHandler(file_handler)


logger.propagate = False

# Export the logger
__all__ = ["logger"]