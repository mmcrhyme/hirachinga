from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from api import cruds, schemas
from api.cruds import item as cruds
from api.schemas import item as schemas
from api.db import get_db

router = APIRouter()

@router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = cruds.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return cruds.create_item(db=db, item=item)

# @router.put("/items/{item_id}", response_model=schemas.Item)
# def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
#     db_item = cruds.get_item(db, item_id=item_id)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return cruds.update_item(db=db, item_id=item_id, item=item)

# @router.delete("/items/{item_id}", response_model=schemas.Item)
# def delete_item(item_id: int, db: Session = Depends(get_db)):
#     db_item = cruds.get_item(db, item_id=item_id)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     cruds.delete_item(db=db, item_id=item_id)
#     return {"message": "Item deleted"}
