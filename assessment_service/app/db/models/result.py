from sqlalchemy import Column, String, Date, Enum, ForeignKey, Float, Text
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.db.base import Base

class Result(Base):
    __tablename__ = "results"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    term_id = Column(UUID(as_uuid=True), nullable=False)
    gpa = Column(Float)
    remarks = Column(Text)

