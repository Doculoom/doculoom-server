import logging


formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger
