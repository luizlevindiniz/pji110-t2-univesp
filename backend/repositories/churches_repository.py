from datetime import datetime
from typing import List, Union

from database.models.church_model import ChurchModel
from sqlalchemy.orm import Session


class ChurchRepository:
    @classmethod
    def create_church(cls, data: dict, db: Session) -> ChurchModel:
        try:
            create: dict = {
                "church": data.get("church"),
                "location": data.get("location"),
                "faith": data.get("faith"),
                "created_by": "admin",
                "created_at": datetime.now(),
            }
            new_church = ChurchModel(**create)
            db.add(new_church)
            db.flush()
            return new_church
        except Exception as e:
            db.rollback()
            raise ConnectionError(str(e))

    @classmethod
    def get_all_churches(cls, db: Session) -> Union[ChurchModel, List[ChurchModel]]:
        try:
            return db.query(ChurchModel).filter(ChurchModel.deleted_by == None).all()
        except Exception as e:
            db.rollback()
            raise ConnectionError(str(e))
