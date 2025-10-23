import logging 

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename="logs.txt",mode="a")


stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

formatter = logging.Formatter(fmt="%(asctime)s - %(name)s  - %(levelname)s  - Line %(lineno)d - %(message)s")
file_handler.setFormatter(formatter)

for handler in logger.handlers[:]:
    logger.removeHandler(handler)
    
logger.addHandler(file_handler)

logger.propagate = False 

__all__ = ["logger"]

