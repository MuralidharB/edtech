# app/db/models/course.py

from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class Course(Base):
    __tablename__ = "courses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    subject = Column(String, nullable=True)  # e.g., "Mathematics"
    grade_level = Column(Integer, nullable=True)  # e.g., 8
    curriculum = Column(String, nullable=True)  # e.g., "CBSE", "IB"
    created_by = Column(UUID(as_uuid=True), nullable=True)  # teacher or admin


class CourseConceptView(Base):
    __tablename__ = "course_concept_views"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    concept_id = Column(UUID, ForeignKey("concepts.id"))
    course_id = Column(UUID, ForeignKey("courses.id"))
