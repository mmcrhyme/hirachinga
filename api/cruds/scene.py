from sqlalchemy.orm import Session
from api import schemas
from api.models import models
# from api.schemas import 

def get_scene(db: Session, scene_id: int):
    return db.query(models.Scene).filter(models.Scene.id == scene_id).first()

def create_scene(db: Session, scene: schemas.SceneCreate):
    db_scene = models.Scene(**scene.dict())
    db.add(db_scene)
    db.commit()
    db.refresh(db_scene)
    return db_scene
