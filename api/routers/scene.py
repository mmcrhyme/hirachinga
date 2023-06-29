from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from api import cruds, schemas
from api.cruds import scene as cruds
from api.schemas import scene as schemas
from api.db import get_db

router = APIRouter()

@router.get("/scenes/{scene_id}", response_model=schemas.Scene)
def read_scene(scene_id: int, db: Session = Depends(get_db)):
    db_scene = cruds.get_scene(db, scene_id=scene_id)
    if db_scene is None:
        raise HTTPException(status_code=404, detail="Scene not found")
    return db_scene

@router.post("/scenes/", response_model=schemas.Scene)
def create_scene(scene: schemas.SceneCreate, db: Session = Depends(get_db)):
    return cruds.create_scene(db=db, scene=scene)

# @router.put("/scenes/{scene_id}", response_model=schemas.Scene)
# def update_scene(scene_id: int, scene: schemas.SceneUpdate, db: Session = Depends(get_db)):
#     db_scene = cruds.get_scene(db, scene_id=scene_id)
#     if db_scene is None:
#         raise HTTPException(status_code=404, detail="Scene not found")
#     return cruds.update_scene(db=db, scene_id=scene_id, scene=scene)

# @router.delete("/scenes/{scene_id}", response_model=schemas.Scene)
# def delete_scene(scene_id: int, db: Session = Depends(get_db)):
#     db_scene = cruds.get_scene(db, scene_id=scene_id)
#     if db_scene is None:
#         raise HTTPException(status_code=404, detail="Scene not found")
#     cruds.delete_scene(db=db, scene_id=scene_id)
#     return {"message": "Scene deleted"}
