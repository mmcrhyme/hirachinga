from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# from api import models, schemas, cruds

from api.cruds import choice_text_set as cruds
from api.schemas import text_set as schemas

from api.db import get_db

router = APIRouter()


@router.get("/choices/{choice_id}/textsets", response_model=List[schemas.TextSet])
def read_textsets(choice_id: int, db: Session = Depends(get_db)):
    textsets = cruds.get_textsets_by_choice_id(db, choice_id)
    if textsets is None:
        raise HTTPException(status_code=404, detail="Textsets not found")
    return textsets


# @router.get("/{choice_text_set_id}", response_model=schemas.ChoiceTextSet)
# def read_choice_text_set(choice_text_set_id: int, db: Session = Depends(get_db)):
#     db_choice_text_set = cruds.get_choice_text_set(db, choice_text_set_id=choice_text_set_id)
#     if db_choice_text_set is None:
#         raise HTTPException(status_code=404, detail="Choice text set not found")
#     return db_choice_text_set

# Similar routes for the other operations...
