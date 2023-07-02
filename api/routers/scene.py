from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# from api import cruds, schemas
from api.cruds import scene as cruds
from api.schemas import scene as schemas
from api.db import get_db
from api.models import models

router = APIRouter()

# @router.get("/scenes/{scene_id}", response_model=schemas.Scene)
# def read_scene(scene_id: int, db: Session = Depends(get_db)):
#     db_scene = cruds.get_scene(db, scene_id=scene_id)
#     if db_scene is None:
#         raise HTTPException(status_code=404, detail="Scene not found")
#     return db_scene


@router.get("/scenes/{scene_id}")
def read_scene(scene_id: int, db: Session = Depends(get_db)):
    db_scene = cruds.get_scene(db, scene_id=scene_id)
    if db_scene is None:
        raise HTTPException(status_code=404, detail="Scene not found")

    # Build a new dict for the response
    response = {
        # "background_image": db_scene.background_image, 消した07020225
        "id": db_scene.id,
        "choices": [],
        "text_sets": [
            {
                "id": text_set.id,
                "scene_id": text_set.scene_id,
                "texts": [text.__dict__ for text in text_set.texts],
            }
            for text_set in db_scene.text_sets
        ],
    }

    # Replace "choices" with a version that includes "text_sets_id"
    for choice in db_scene.choices:
        new_choice = {
            "id": choice.id,
            "choice_text": choice.choice_text,
            "scene_id": choice.scene_id,
            "text_sets_id": [text_set.id for text_set in choice.choice_text_sets],
        }
        response["choices"].append(new_choice)

    return response



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
