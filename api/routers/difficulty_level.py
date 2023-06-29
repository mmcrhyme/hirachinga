from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from api import cruds, schemas
from api.cruds import difficulty_level as cruds
from api.schemas import difficulty_level as schemas
from api.db import get_db

router = APIRouter()

@router.get("/difficulty_levels/{difficulty_level_id}", response_model=schemas.DifficultyLevel)
def read_difficulty_level(difficulty_level_id: int, db: Session = Depends(get_db)):
    db_difficulty_level = cruds.get_difficulty_level(db, difficulty_level_id=difficulty_level_id)
    if db_difficulty_level is None:
        raise HTTPException(status_code=404, detail="Difficulty Level not found")
    return db_difficulty_level

@router.post("/difficulty_levels/", response_model=schemas.DifficultyLevel)
def create_difficulty_level(difficulty_level: schemas.DifficultyLevelCreate, db: Session = Depends(get_db)):
    return cruds.create_difficulty_level(db=db, difficulty_level=difficulty_level)

# @router.put("/difficulty_levels/{difficulty_level_id}", response_model=schemas.DifficultyLevel)
# def update_difficulty_level(difficulty_level_id: int, difficulty_level: schemas.DifficultyLevelUpdate, db: Session = Depends(get_db)):
#     db_difficulty_level = cruds.get_difficulty_level(db, difficulty_level_id=difficulty_level_id)
#     if db_difficulty_level is None:
#         raise HTTPException(status_code=404, detail="Difficulty Level not found")
#     return cruds.update_difficulty_level(db=db, difficulty_level_id=difficulty_level_id, difficulty_level=difficulty_level)

# @router.delete("/difficulty_levels/{difficulty_level_id}", response_model=schemas.DifficultyLevel)
# def delete_difficulty_level(difficulty_level_id: int, db: Session = Depends(get_db)):
#     db_difficulty_level = cruds.get_difficulty_level(db, difficulty_level_id=difficulty_level_id)
#     if db_difficulty_level is None:
#         raise HTTPException(status_code=404, detail="Difficulty Level not found")
#     cruds.delete_difficulty_level(db=db, difficulty_level_id=difficulty_level_id)
#     return {"message": "Difficulty Level deleted"}
