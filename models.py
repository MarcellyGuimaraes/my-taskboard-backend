# models.py
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from database import Base
from pydantic import BaseModel
from typing import Optional

class Task(Base):
    __tablename__ = 'task'

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    tsk_name = Column(String(255), nullable=False)
    tsk_description = Column(Text)
    status_id = Column(Integer)
    icone_id = Column(Integer)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class Status(Base):
    __tablename__ = 'status'

    status_id = Column(Integer, primary_key=True, autoincrement=True)
    sts_name = Column(String(255))
    sts_icon = Column(String(500))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class Icone(Base):
    __tablename__ = 'icone'

    icone_id = Column(Integer, primary_key=True, autoincrement=True)
    ico_name = Column(String(255))
    ico_url = Column(String(255))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class TaskCreate(BaseModel):
    tsk_name: str
    tsk_description: Optional[str] = None
    status_id: Optional[int] = None
    icone_id: Optional[int] = None
    
class TaskUpdate(BaseModel):
    tsk_name: str
    tsk_description: Optional[str] = None
    status_id: Optional[int] = None
    icone_id: Optional[int] = None