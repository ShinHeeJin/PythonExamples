import logging.config

import yaml

with open("config.yaml", encoding="cp949") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)


def log(logger: logging.Logger):
    logger.debug("Debug Message")
    logger.info("Info Message")
    logger.warning("Warning Message")
    logger.error("Error Message")
    logger.critical("Critical Message")


# my_logger
logger = logging.getLogger("my_logger")
log(logger)


# root logging
logger = logging.getLogger("root")
log(logger)
