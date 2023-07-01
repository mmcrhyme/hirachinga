from sqlalchemy.orm import Session

from api.schemas import choice_text_set as schemas
from api.models import models

# from api import models


# 特定のchoice_idに関連付けられたテキストセットのリストを取得する
def get_textsets_by_choice_id(db: Session, choice_id: int):
    return db.query(models.TextSet).join(models.ChoiceTextSet).filter(models.ChoiceTextSet.choice_id == choice_id).all()

# def get_choice_text_set(db: Session, choice_text_set_id: int):
#     return db.query(models.ChoiceTextSet).filter(models.ChoiceTextSet.id == choice_text_set_id).first()


# def get_choice_text_sets(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.ChoiceTextSet).offset(skip).limit(limit).all()


def create_choice_text_set(db: Session, choice_text_set: schemas.ChoiceTextSetCreate):
    db_choice_text_set = models.ChoiceTextSet(**choice_text_set.dict())
    db.add(db_choice_text_set)
    db.commit()
    db.refresh(db_choice_text_set)
    return db_choice_text_set


# def update_choice_text_set(db: Session, choice_text_set: models.ChoiceTextSetUpdate):
#     db_choice_text_set = get_choice_text_set(db, choice_text_set.id)
#     if db_choice_text_set is None:
#         return None
#     for var, value in vars(choice_text_set).items():
#         setattr(db_choice_text_set, var, value) if value else None
#     db.add(db_choice_text_set)
#     db.commit()
#     db.refresh(db_choice_text_set)
#     return db_choice_text_set


# def delete_choice_text_set(db: Session, choice_text_set_id: int):
#     db_choice_text_set = get_choice_text_set(db, choice_text_set_id)
#     if db_choice_text_set is None:
#         return None
#     db.delete(db_choice_text_set)
#     db.commit()
#     return db_choice_text_set
