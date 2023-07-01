from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from api import models, schemas, cruds

from api.cruds import text_set as cruds
from api.schemas import text_set as schemas

from api.db import get_db

router = APIRouter()


@router.get("/{text_set_id}", response_model=schemas.TextSet)
def read_text_set(text_set_id: int, db: Session = Depends(get_db)):
    db_text_set = cruds.get_text_set(db, text_set_id=text_set_id)
    if db_text_set is None:
        raise HTTPException(status_code=404, detail="Text set not found")
    return db_text_set

# Similar routes for the other operations...
