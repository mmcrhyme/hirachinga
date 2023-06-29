from sqlalchemy.orm import Session
from api import schemas
from api.models import models
# from api.schemas import 

def get_game_session(db: Session, session_id: int):
    return db.query(models.GameSession).filter(models.GameSession.id == session_id).first()

def create_game_session(db: Session, session: schemas.GameSessionCreate):
    db_session = models.GameSession(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session
