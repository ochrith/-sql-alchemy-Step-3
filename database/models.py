from enum import Enum
from database.db_connection import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum as SQLEnum


class Status(Enum):
    PENDING = "pending"
    DONE = "done"
    FAILED = "failed"
    PROCESSING = "processing"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)


class Upload(Base):
    __tablename__ = "uploads"

    uid = Column(Integer)
    upload_time = Column(String)
    status = Column(SQLEnum(Status))
    filename = Column(String)
    id = Column(Integer,primary_key=True)