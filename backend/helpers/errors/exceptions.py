from typing import List, Optional, Union


class ErrorHTTP(Exception):
    def __init__(
        self,
        msg: Union[str, List[str]],
        code: int,
        msg_to_user: Optional[str] = None,
        notify: Optional[bool] = False,
    ) -> None:

        if isinstance(msg, str):
            super().__init__(msg)
        elif isinstance(msg, List):
            super().__init__(*msg)
        if msg_to_user is None:
            msg_to_user = str(msg)
        self.msg_to_user = msg_to_user
        self.code = code
        self.notify = notify
