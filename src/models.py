from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.sql import func
from src.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    institution_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=func.now())

class Batch(Base):
    __tablename__ = "batches"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    institution_id = Column(Integer)

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    batch_id = Column(Integer)
    trainer_id = Column(Integer)
    title = Column(String)

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer)
    student_id = Column(Integer)
    status = Column(String)