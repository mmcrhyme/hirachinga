from pydantic import BaseModel

class ChoiceTextSetBase(BaseModel):
    choice_id: int
    text_set_id: int

class ChoiceTextSetCreate(ChoiceTextSetBase):
    pass

class ChoiceTextSet(ChoiceTextSetBase):
    id: int

    class Config:
        orm_mode = True
