# app/db/models/grade.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from app.db.base import Base
import uuid


class Grade(Base):
    __tablename__ = "grades"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)  # e.g., "Grade 6"
    level = Column(Integer, nullable=False)  # e.g., 6
    curriculum = Column(String, nullable=True)  # e.g., "CBSE", "IB"
