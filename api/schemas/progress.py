from pydantic import BaseModel
from typing import Optional

class ProgressBase(BaseModel):
    game_session_id: int
    task_progress: float
    energy_level: float
    money_amount: float
    satisfaction_level: float
    game_over: Optional[bool] = False

class ProgressCreate(ProgressBase):
    pass

class Progress(ProgressBase):
    id: int

    class Config:
        orm_mode = True
