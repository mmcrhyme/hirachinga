from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class ItemBase(BaseModel):
    item_name: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    difficulty_level_id: int

    class Config:
        orm_mode = True

class ChoiceBase(BaseModel):
    choice_text: str

class ChoiceCreate(ChoiceBase):
    pass

class Choice(ChoiceBase):
    id: int
    scene_id: int

    class Config:
        orm_mode = True

class SceneBase(BaseModel):
    background_image: str
    text: str

class SceneCreate(SceneBase):
    pass

class Scene(SceneBase):
    id: int
    difficulty_level_id: int
    choices: List[Choice] = []

    class Config:
        orm_mode = True

class DifficultyLevelBase(BaseModel):
    level_name: str

class DifficultyLevelCreate(DifficultyLevelBase):
    pass

class DifficultyLevel(DifficultyLevelBase):
    id: int
    items: List[Item] = []
    scenes: List[Scene] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ProgressBase(BaseModel):
    task_progress: float
    energy_level: float
    money_amount: float
    satisfaction_level: float
    game_over: bool

class ProgressCreate(ProgressBase):
    pass

class Progress(ProgressBase):
    id: int
    game_session_id: int

    class Config:
        orm_mode = True

class GameSessionBase(BaseModel):
    start_time: datetime
    end_time: Optional[datetime] = None

class GameSessionCreate(GameSessionBase):
    user_id: int
    difficulty_level_id: int

class GameSession(GameSessionBase):
    id: int
    progress: List[Progress] = []

    class Config:
        orm_mode = True
