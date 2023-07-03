from pydantic import BaseModel

class ChoiceBase(BaseModel):
    choice_text: str
    scene_id: int
    belong_text_set_id: int #追加

class ChoiceCreate(ChoiceBase):
    pass

class Choice(ChoiceBase):
    id: int

    class Config:
        orm_mode = True
