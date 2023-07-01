from sqlalchemy.orm import Session
from api.schemas import text as schemas
from api.models import models
# from api.schemas import 

def get_text(db: Session, text_id: int):
    return db.query(models.Text).filter(models.Text.id == text_id).first()

# def get_texts(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Text).offset(skip).limit(limit).all()


def create_text(db: Session, text: schemas.TextCreate):
    db_text = models.Text(**text.dict())
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    return db_text


# def update_text(db: Session, text: models.TextUpdate):
#     db_text = get_text(db, text.id)
#     if db_text is None:
#         return None
#     for var, value in vars(text).items():
#         setattr(db_text, var, value) if value else None
#     db.add(db_text)
#     db.commit()
#     db.refresh(db_text)
#     return db_text


# def delete_text(db: Session, text_id: int):
#     db_text = get_text(db, text_id)
#     if db_text is None:
#         return None
#     db.delete(db_text)
#     db.commit()
#     return db_text