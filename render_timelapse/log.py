import logging
import os
import tempfile
from typing import Optional

_logger: Optional[logging.Logger] = None


def get_log_path() -> str:
    # /tmp/render_timelapse.log on Linux
    log_path = os.path.join(tempfile.gettempdir(), "render_timelapse.log")
    return log_path


def get_logger() -> logging.Logger:
    global _logger
    if _logger is not None:
        return _logger

    _logger = logging.getLogger("render_timelapse")
    _logger.setLevel(logging.DEBUG)

    log_format = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )  # e.g. [2024-06-01 12:00:00] INFO     render_timelapse: This is a log message

    log_to_file = logging.FileHandler(get_log_path(), mode="a")
    log_to_file_level = logging.DEBUG  # TODO: Maybe set to INFO in production
    log_to_file.setLevel(log_to_file_level)
    log_to_file.setFormatter(log_format)
    _logger.addHandler(log_to_file)

    log_to_stderr = logging.StreamHandler()
    log_to_stderr_level = logging.INFO
    log_to_stderr.setLevel(log_to_stderr_level)
    log_to_stderr.setFormatter(log_format)
    _logger.addHandler(log_to_stderr)

    _logger.debug(
        f"Logging to {get_log_path()} with {log_to_file_level} level and {log_to_stderr_level} level for stderr"
    )

    return _logger
