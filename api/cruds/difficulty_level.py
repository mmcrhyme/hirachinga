from sqlalchemy.orm import Session
# from api import schemas
from api.models import models
from api.schemas import difficulty_level as schemas


def get_difficulty_level(db: Session, level_id: int):
    return db.query(models.DifficultyLevel).filter(models.DifficultyLevel.id == level_id).first()

def create_difficulty_level(db: Session, level: schemas.DifficultyLevelCreate):
    db_level = models.DifficultyLevel(**level.dict())
    db.add(db_level)
    db.commit()
    db.refresh(db_level)
    return db_level
