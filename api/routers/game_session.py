from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import cruds, schemas
from api.cruds import game_session as cruds
from api.schemas import game_session as schemas
from api.db import get_db

router = APIRouter()

@router.get("/game_sessions/{game_session_id}", response_model=schemas.GameSession)
def read_game_session(game_session_id: int, db: Session = Depends(get_db)):
    db_game_session = cruds.get_game_session(db, game_session_id=game_session_id)
    if db_game_session is None:
        raise HTTPException(status_code=404, detail="GameSession not found")
    return db_game_session

@router.post("/game_sessions/", response_model=schemas.GameSession)
def create_game_session(game_session: schemas.GameSessionCreate, db: Session = Depends(get_db)):
    return cruds.create_game_session(db=db, game_session=game_session)

# @router.put("/game_sessions/{game_session_id}", response_model=schemas.GameSession)
# def update_game_session(game_session_id: int, game_session: schemas.GameSessionUpdate, db: Session = Depends(get_db)):
#     db_game_session = cruds.get_game_session(db, game_session_id=game_session_id)
#     if db_game_session is None:
#         raise HTTPException(status_code=404, detail="GameSession not found")
#     return cruds.update_game_session(db=db, game_session_id=game_session_id, game_session=game_session)

# @router.delete("/game_sessions/{game_session_id}", response_model=schemas.GameSession)
# def delete_game_session(game_session_id: int, db: Session = Depends(get_db)):
#     db_game_session = cruds.get_game_session(db, game_session_id=game_session_id)
#     if db_game_session is None:
#         raise HTTPException(status_code=404, detail="GameSession not found")
#     cruds.delete_game_session(db=db, game_session_id=game_session_id)
#     return {"message": "GameSession deleted"}
