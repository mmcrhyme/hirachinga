from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import cruds, schemas
from api.cruds import progress as cruds
from api.schemas import progress as schemas

from api.db import get_db

router = APIRouter()

@router.get("/progress/{progress_id}", response_model=schemas.Progress)
def read_progress(progress_id: int, db: Session = Depends(get_db)):
    db_progress = cruds.get_progress(db, progress_id=progress_id)
    if db_progress is None:
        raise HTTPException(status_code=404, detail="Progress not found")
    return db_progress

@router.post("/progress/", response_model=schemas.Progress)
def create_progress(progress: schemas.ProgressCreate, db: Session = Depends(get_db)):
    return cruds.create_progress(db=db, progress=progress)

# @router.put("/progress/{progress_id}", response_model=schemas.Progress)
# def update_progress(progress_id: int, progress: schemas.ProgressUpdate, db: Session = Depends(get_db)):
#     db_progress = cruds.get_progress(db, progress_id=progress_id)
#     if db_progress is None:
#         raise HTTPException(status_code=404, detail="Progress not found")
#     return cruds.update_progress(db=db, progress_id=progress_id, progress=progress)

# @router.delete("/progress/{progress_id}", response_model=schemas.Progress)
# def delete_progress(progress_id: int, db: Session = Depends(get_db)):
#     db_progress = cruds.get_progress(db, progress_id=progress_id)
#     if db_progress is None:
#         raise HTTPException(status_code=404, detail="Progress not found")
#     cruds.delete_progress(db=db, progress_id=progress_id)
#     return {"message": "Progress deleted"}
