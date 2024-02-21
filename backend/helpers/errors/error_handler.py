from logging import Logger, StreamHandler
from sys import stderr
from typing import Union

from fastapi import HTTPException
from helpers.errors.exceptions import ErrorHTTP


class ErrorHandler:
    # Logger
    error_logger = Logger("RequestError", level=10)
    error_handler = StreamHandler(stderr)
    error_logger.addHandler(error_handler)

    @classmethod
    def handle_error(
        cls,
        exception: Union[Exception, ErrorHTTP],
        traceback: str,
    ) -> None:
        cls.error_logger.warning(traceback)

        if isinstance(exception, ErrorHTTP):
            err_msg = exception.msg_to_user
            err_code = exception.code
        else:
            err_msg = repr(exception)
            err_code = 500
        raise HTTPException(status_code=err_code, detail=err_msg)
