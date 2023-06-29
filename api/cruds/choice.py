from sqlalchemy.orm import Session
from api import schemas
from api.models import models
# from api.schemas import 

def get_choice(db: Session, choice_id: int):
    return db.query(models.Choice).filter(models.Choice.id == choice_id).first()

def create_choice(db: Session, choice: schemas.ChoiceCreate):
    db_choice = models.Choice(**choice.dict())
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice
