from pydantic import BaseModel, Field


class Church(BaseModel):
    name: str = Field(..., min_length=1)

    class Config:
        from_attributes = True
