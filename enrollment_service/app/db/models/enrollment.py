from sqlalchemy import Column, String, Date, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    term_id = Column(UUID(as_uuid=True), nullable=False)
    grade_id = Column(UUID(as_uuid=True), ForeignKey("grades.id", ondelete="RESTRICT"), nullable=False)
    section_id = Column(UUID(as_uuid=True), ForeignKey("sections.id", ondelete="RESTRICT"), nullable=False)

    status = Column(String, default="active")
    enrollment_date = Column(Date)
    exit_date = Column(Date, nullable=True)
    reason_for_exit = Column(String, nullable=True)
    transferred_from_id = Column(UUID(as_uuid=True), ForeignKey("enrollments.id"), nullable=True)
