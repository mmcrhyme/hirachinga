from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .progress import Progress

class GameSessionBase(BaseModel):
    user_id: int
    # difficulty_level_id: int
    start_time: Optional[datetime] = None

class GameSessionCreate(GameSessionBase):
    pass

class GameSession(GameSessionBase):
    id: int
    end_time: Optional[datetime] = None
    progress: Optional[Progress] = None

    class Config:
        orm_mode = True

