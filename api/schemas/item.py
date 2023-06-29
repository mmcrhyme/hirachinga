from pydantic import BaseModel

class ItemBase(BaseModel):
    item_name: str
    difficulty_level_id: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
