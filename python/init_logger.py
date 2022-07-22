import sys
from logging import INFO, WARNING, Formatter, StreamHandler, getLogger


def init_logger():
    """Initialize logger.

    Put this on the top __init__.py to apply to whole app.
    """
    formatter = Formatter(
        "time:%(asctime)s	thread:%(threadName)s	logger:%(name)s	level:%(levelname)s	message:%(message)s")
    out_handler = StreamHandler(sys.stdout)
    out_handler.setFormatter(formatter)
    out_handler.addFilter(lambda record: record.levelno < WARNING)

    err_handler = StreamHandler(sys.stderr)
    err_handler.setLevel(WARNING)
    err_handler.setFormatter(formatter)

    logger = getLogger(__name__)
    logger.addHandler(out_handler)
    logger.addHandler(err_handler)
    logger.setLevel(INFO)


init_logger()
