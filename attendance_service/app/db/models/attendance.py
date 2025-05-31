from sqlalchemy import Column, Date, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SAEnum  # import SQLAlchemy's Enum
import uuid
from enum import Enum  # make sure this is Python's enum
from app.db.base import Base


class AttendanceStatus(str, Enum):  # inherits from str and Enum
    present = "present"
    absent = "absent"
    late = "late"
    excused = "excused"


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    section_id = Column(UUID(as_uuid=True), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(SAEnum(AttendanceStatus, name="attendance_status", native_enum=False), nullable=False)
    reason = Column(String, nullable=True)


