# app/db/models/section.py
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class Section(Base):
    __tablename__ = "sections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)  # e.g., "5A"
    grade_id = Column(UUID(as_uuid=True), ForeignKey("grades.id", ondelete="RESTRICT"), nullable=False)
    max_capacity = Column(Integer, nullable=True)
    assigned_teacher_id = Column(UUID(as_uuid=True), nullable=True)

