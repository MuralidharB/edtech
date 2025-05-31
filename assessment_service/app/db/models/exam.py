from sqlalchemy import Column, String, Date, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.db.base import Base

class Exam(Base):
    __tablename__ = "exams"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    section_id = Column(UUID(as_uuid=True), nullable=False)
    term_id = Column(UUID(as_uuid=True), nullable=False)  # no ForeignKey
