from sqlalchemy import Column, String, Date, Enum, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.db.base import Base

class GradingEntry(Base):
    __tablename__ = "grading_entries"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    exam_id = Column(UUID(as_uuid=True), ForeignKey("exams.id"))
    marks = Column(Float, nullable=False)
    grade = Column(String)

