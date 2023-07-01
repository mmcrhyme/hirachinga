from typing import List
from pydantic import BaseModel
from .text import Text

class TextSetBase(BaseModel):
    pass

class TextSetCreate(TextSetBase):
    pass

class TextSet(TextSetBase):
    id: int
    scene_id: int
    texts: List[Text] = []

    class Config:
        orm_mode = True
