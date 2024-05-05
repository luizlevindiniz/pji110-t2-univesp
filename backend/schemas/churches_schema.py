from pydantic import BaseModel, Field


class Church(BaseModel):
    church: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    faith: str = Field(..., min_length=1)

    class Config:
        from_attributes = True
