from sqlalchemy.orm import Session

from api.models import models
from api.schemas import text_set as schemas


def get_text_set(db: Session, text_set_id: int):
    return db.query(models.TextSet).filter(models.TextSet.id == text_set_id).first()


def get_text_sets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TextSet).offset(skip).limit(limit).all()


def create_text_set(db: Session, text_set: schemas.TextSetCreate):
    db_text_set = models.TextSet(**text_set.dict())
    db.add(db_text_set)
    db.commit()
    db.refresh(db_text_set)
    return db_text_set

# ↓変更前　↑変更後
# def create_text_set(db: Session, text_set: models.TextSetCreate):
#     db_text_set = models.TextSet(**text_set.dict())
#     db.add(db_text_set)
#     db.commit()
#     db.refresh(db_text_set)
#     return db_text_set


# def update_text_set(db: Session, text_set: models.TextSetUpdate):
#     db_text_set = get_text_set(db, text_set.id)
#     if db_text_set is None:
#         return None
#     for var, value in vars(text_set).items():
#         setattr(db_text_set, var, value) if value else None
#     db.add(db_text_set)
#     db.commit()
#     db.refresh(db_text_set)
#     return db_text_set


# def delete_text_set(db: Session, text_set_id: int):
#     db_text_set = get_text_set(db, text_set_id)
#     if db_text_set is None:
#         return None
#     db.delete(db_text_set)
#     db.commit()
#     return db_text_set
