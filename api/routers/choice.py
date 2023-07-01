from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from api import cruds, schemas
from api.cruds import choice as cruds
from api.schemas import choice as schemas
from api.db import get_db

router = APIRouter()

@router.get("/choices/{choice_id}", response_model=schemas.Choice)
def read_choice(choice_id: int, db: Session = Depends(get_db)):
    db_choice = cruds.get_choice(db, choice_id=choice_id)
    if db_choice is None:
        raise HTTPException(status_code=404, detail="Choice not found")
    return db_choice

@router.post("/choices/", response_model=schemas.Choice)
def create_choice(choice: schemas.ChoiceCreate, db: Session = Depends(get_db)):
    return cruds.create_choice(db=db, choice=choice)

# @router.put("/choices/{choice_id}", response_model=schemas.Choice)
# def update_choice(choice_id: int, choice: schemas.ChoiceUpdate, db: Session = Depends(get_db)):
#     db_choice = cruds.get_choice(db, choice_id=choice_id)
#     if db_choice is None:
#         raise HTTPException(status_code=404, detail="Choice not found")
#     return cruds.update_choice(db=db, choice_id=choice_id, choice=choice)

# @router.delete("/choices/{choice_id}", response_model=schemas.Choice)
# def delete_choice(choice_id: int, db: Session = Depends(get_db)):
#     db_choice = cruds.get_choice(db, choice_id=choice_id)
#     if db_choice is None:
#         raise HTTPException(status_code=404, detail="Choice not found")
#     cruds.delete_choice(db=db, choice_id=choice_id)
#     return {"message": "Choice deleted"}
