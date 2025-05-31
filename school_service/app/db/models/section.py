from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base

class Section(Base):
    __tablename__ = "sections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    grade_id = Column(UUID(as_uuid=True), ForeignKey("grades.id"), nullable=False)
    teacher_id = Column(UUID(as_uuid=True), nullable=True)  # optional FK from user-service

