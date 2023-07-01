from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from api import cruds, schemas
from api.cruds import text as cruds
from api.schemas import text as schemas
from api.db import get_db

router = APIRouter()

@router.get("/texts/{text_id}", response_model=schemas.Text)
def read_text(text_id: int, db: Session = Depends(get_db)):
    db_text = cruds.get_text(db, text_id=text_id)
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")
    return db_text

@router.post("/texts/", response_model=schemas.Text)
def create_text(text: schemas.TextCreate, db: Session = Depends(get_db)):
    return cruds.create_text(db=db, text=text)