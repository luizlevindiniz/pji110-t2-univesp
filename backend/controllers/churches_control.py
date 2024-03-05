from typing import Union

from database.db_connection import get_session
from helpers.errors import ErrorHTTP
from repositories.churches_repository import ChurchRepository
from schemas.churches_schema import Church


class ChurchesControl:
    def __init__(self) -> None:
        self.session_maker = get_session
        self.repository = ChurchRepository()

    # Create
    def create_church(self, data: Church, current_user: str) -> Union[Church, None]:
        try:
            with self.session_maker() as session:
                create = data.model_dump()
                church = self.repository.create_church(
                    data=create, user=current_user, db=session
                )
                if church is None:
                    session.rollback()
                    raise ConnectionError(
                        "Error while connecting to churches repository!"
                    )
                session.expunge_all()
            return church

        except Exception as e:
            raise ErrorHTTP(
                msg=str(e), msg_to_user="Error while creating church!", code=400
            )

    # Read
    def get_all_churches(self) -> list:
        try:
            with self.session_maker() as session:
                churches = self.repository.get_all_churches(db=session)

                if churches is None:
                    session.rollback()
                    raise ConnectionError(
                        "Error while connecting to churches repository!"
                    )
                session.expunge_all()

                return churches
        except Exception as e:
            raise ErrorHTTP(
                msg=str(e), msg_to_user="Error while fetching churches!", code=400
            )
