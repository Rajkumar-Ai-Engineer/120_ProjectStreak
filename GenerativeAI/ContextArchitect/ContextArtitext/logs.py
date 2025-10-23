import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - Line %(lineno)d - %(message)s")
file_handler.setFormatter(formatter)

for handler in logger.handlers[:]:
    logger.removeHandler(handler)

logger.addHandler(file_handler)

logger.propagate = False

__all__ = ["logger"]