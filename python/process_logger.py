import time
from contextlib import contextmanager
from logging import getLogger


@contextmanager
def process_logger(process_name: str, logger_name: str = __name__):
    """A context manager that logs a process starting and ending with elapsed time."""
    logger = getLogger(logger_name)

    logger.info(f"START {process_name}")
    start_time = time.perf_counter_ns()
    try:
        yield
    finally:
        end_time = time.perf_counter_ns()
        logger.info(
            f"END   {process_name} - elapsed={(end_time - start_time) / 1e6:.1f} ms")
