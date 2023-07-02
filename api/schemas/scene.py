from pydantic import BaseModel
from typing import List, Optional
from .choice import Choice
from .text_set import TextSet

class SceneBase(BaseModel):
    # background_image: str 消した07020237
    # text: str
    # difficulty_level_id: int
    pass

class SceneCreate(SceneBase):
    pass

class Scene(SceneBase):
    id: int
    # choices: List[Optional['Choice']] = []
    choices: List[Optional[Choice]] = []
    # texts: List[Optional[Text]] = []
    text_sets: List[Optional[TextSet]] = []

    class Config:
        orm_mode = True

