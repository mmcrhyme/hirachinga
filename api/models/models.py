from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import DATETIME
from datetime import datetime

from api.db import Base  

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

class Scene(Base):
    __tablename__ = "scenes"

    id = Column(Integer, primary_key=True, index=True)
    # background_image = Column(String(255)) 消した　07020226
    choices = relationship("Choice", backref="scene")
    text_sets = relationship("TextSet", backref="scene")

class TextSet(Base):
    __tablename__ = "text_sets"

    id = Column(Integer, primary_key=True, index=True)
    scene_id = Column(Integer, ForeignKey("scenes.id"))
    texts = relationship("Text", backref="text_set")

class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String(255))
    scene_id = Column(Integer, ForeignKey("scenes.id"))
    belong_text_set_id = Column(Integer) # 追加
    choice_text_sets = relationship("ChoiceTextSet", backref="choice")

class Text(Base):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(255))
    background_image = Column(String(255)) #追加
    gender = Column(String(255)) #追加
    progress = Column(Integer) #追加
    mental = Column(Integer) #Integerに変えた
    money = Column(Integer) #Integerに変えた
    satisfaction = Column(Integer) #Integerに変えた
    text_set_id = Column(Integer, ForeignKey("text_sets.id"))

class ChoiceTextSet(Base):
    __tablename__ = "choice_text_sets"

    id = Column(Integer, primary_key=True, index=True)
    choice_id = Column(Integer, ForeignKey("choices.id"))
    text_set_id = Column(Integer, ForeignKey("text_sets.id"))

class GameSession(Base):
    __tablename__ = "game_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
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
