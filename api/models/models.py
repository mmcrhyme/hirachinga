from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import DATETIME
from datetime import datetime

from api.db import Base  # Base should be a declarative base instance from sqlalchemy.ext.declarative

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

class DifficultyLevel(Base):
    __tablename__ = "difficulty_levels"

    id = Column(Integer, primary_key=True, index=True)
    level_name = Column(String(255), index=True)
    items = relationship("Item", backref="difficulty_level")
    scenes = relationship("Scene", backref="difficulty_level")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(255), index=True)
    difficulty_level_id = Column(Integer, ForeignKey("difficulty_levels.id"))

class Scene(Base):
    __tablename__ = "scenes"

    id = Column(Integer, primary_key=True, index=True)
    background_image = Column(String(255))
    text = Column(String(255))
    difficulty_level_id = Column(Integer, ForeignKey("difficulty_levels.id"))
    choices = relationship("Choice", backref="scene")

class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String(255))
    scene_id = Column(Integer, ForeignKey("scenes.id"))

class GameSession(Base):
    __tablename__ = "game_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    difficulty_level_id = Column(Integer, ForeignKey("difficulty_levels.id"))
    start_time = Column(DATETIME(fsp=6), default=datetime.utcnow)
    end_time = Column(DATETIME(fsp=6))
    progress = relationship("Progress", backref="game_session")

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    game_session_id = Column(Integer, ForeignKey("game_sessions.id"))
    task_progress = Column(Float)
    energy_level = Column(Float)
    money_amount = Column(Float)
    satisfaction_level = Column(Float)
    game_over = Column(Boolean, default=False)