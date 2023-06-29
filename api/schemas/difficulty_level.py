from pydantic import BaseModel
from typing import List, Optional
from .item import Item
from .scene import Scene

class DifficultyLevelBase(BaseModel):
    level_name: str

class DifficultyLevelCreate(DifficultyLevelBase):
    pass

class DifficultyLevel(DifficultyLevelBase):
    id: int
    items: List[Optional[Item]] = []
    scenes: List[Optional[Scene]] = []

    class Config:
        orm_mode = True

