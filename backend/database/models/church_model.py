from database.db_connection import Base_DB_Model
from database.models.base_model import CreatedBase, DeletedBase, EditedBase
from sqlalchemy import Column, Integer, String


class ChurchModel(Base_DB_Model, CreatedBase, EditedBase, DeletedBase):
    __table_args__ = {"schema": "univesp"}
    __tablename__ = "churches"

    id = Column(Integer, primary_key=True)
    church = Column(String(255), name="church")
    location = Column(String(255), name="location")
    faith = Column(String(255), name="faith")

    def as_dict(self) -> dict:
        return dict(
            {c.church: str(getattr(self, c.church)) for c in self.__table__.columns}
        )

    def __repr__(self) -> str:
        return f"<Church {self.name} created at {self.created_at}>"
