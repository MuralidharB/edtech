# app/db/models/term.py
from sqlalchemy import Column, String, Date, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid
import enum

class TermStatus(str, enum.Enum):
    planned = "planned"
    active = "active"
    completed = "completed"

class AcademicTerm(Base):
    __tablename__ = "academic_terms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)  # e.g., "2024–25 Term 1"
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(Enum(TermStatus), default=TermStatus.planned, nullable=False)

