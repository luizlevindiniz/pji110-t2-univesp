from database.db_connection import Base_DB_Model
from database.models.base_model import CreatedBase, DeletedBase, EditedBase
from sqlalchemy import Column, Integer, String


class ChurchModel(Base_DB_Model, CreatedBase, EditedBase, DeletedBase):
    __table_args__ = {"schema": "schema"}
    __tablename__ = "churches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), name="church")

    def as_dict(self) -> dict:
        return dict(
            {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
        )

    def __repr__(self) -> str:
        return f"<Church {self.name} created at {self.created_at}>"
