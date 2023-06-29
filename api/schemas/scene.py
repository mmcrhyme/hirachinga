from pydantic import BaseModel
from typing import List, Optional
from .choice import Choice

class SceneBase(BaseModel):
    background_image: str
    text: str
    difficulty_level_id: int

class SceneCreate(SceneBase):
    pass

class Scene(SceneBase):
    id: int
    # choices: List[Optional['Choice']] = []
    choices: List[Optional[Choice]] = []

    class Config:
        orm_mode = True

