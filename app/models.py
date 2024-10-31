from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func

Base = declarative_base()


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    gender = Column(String, nullable=False)
    avatar = Column(String)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
