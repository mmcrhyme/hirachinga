from sqlalchemy.orm import Session
from api import schemas

from api.models import models
# from api.schemas import 

def get_progress(db: Session, progress_id: int):
    return db.query(models.Progress).filter(models.Progress.id == progress_id).first()

def create_progress(db: Session, progress: schemas.ProgressCreate):
    db_progress = models.Progress(**progress.dict())
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)
    return db_progress
