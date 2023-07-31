import enum
import json
import logging
from datetime import datetime
from json import JSONEncoder
from typing import Any, Callable, Union

from app.settings import Settings

settings = Settings()

logging.basicConfig()

LOG_LEVEL = 20


class LogLevel(enum.Enum):
    INFO = 0
    WARNING = 1
    DEBUG = 2
    EXCEPTION = 3
    ERROR = 4


class Logger:
    def __init__(
        self,
        class_name: str,
    ):
        self.class_name = class_name
        logger = logging.getLogger(class_name)
        logger.setLevel(LOG_LEVEL)
        self.logger = logger

    def info(
        self,
        message: Union[str, dict],
    ):
        self._log(self.logger.info, LogLevel.INFO, message)

    def debug(
        self,
        message: Union[str, dict],
    ):
        self._log(self.logger.debug, LogLevel.DEBUG, message)

    def exception(
        self,
        message: Union[str, dict],
    ):
        self._log(self.logger.exception, LogLevel.EXCEPTION, message)

    def error(
        self,
        message: Union[str, dict],
    ):
        self._log(self.logger.error, LogLevel.ERROR, message)

    def warn(
        self,
        message: Union[str, dict],
    ):
        self._log(self.logger.warning, LogLevel.WARNING, message)

    def _log(
        self,
        log_level_function: Callable,
        log_level: LogLevel,
        message: str,
    ) -> None:
        log_data = {
            "message": message,
            "timestamp": datetime.utcnow().isoformat(),
            "level": log_level.name,
            "module": self.class_name,
            "service": "mashgin",
        }

        log_level_function(json.dumps(log_data, cls=JSONEncoder))
