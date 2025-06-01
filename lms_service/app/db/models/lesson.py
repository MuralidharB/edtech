# app/db/models/lesson.py

from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    sequence_number = Column(Integer, nullable=True)  # e.g., Lesson 1, 2, 3
    lesson_metadata = Column(JSON, nullable=True)  # optional tags, duration, locale, etc.

