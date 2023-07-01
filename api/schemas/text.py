from pydantic import BaseModel

class TextBase(BaseModel):
    text: str
    gender: str
    emotion: str
    # scene_id: int
    text_set_id: int

class TextCreate(TextBase):
    # text: str
    # gender: str
    # emotion: str
    # scene_id: int
    pass

class Text(TextBase):
    id: int
    # text_set_id: int #もしくはここ

    class Config:
        orm_mode = True