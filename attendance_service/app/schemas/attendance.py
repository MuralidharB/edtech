from pydantic import BaseModel
from datetime import date
from uuid import UUID
from enum import Enum
from typing import Optional

class AttendanceStatus(str, Enum):
    present = "present"
    absent = "absent"
    late = "late"
    excused = "excused"

class AttendanceBase(BaseModel):
    student_id: UUID
    section_id: UUID
    date: date
    status: AttendanceStatus
    reason: Optional[str] = None

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceUpdate(BaseModel):
    status: Optional[AttendanceStatus]
    reason: Optional[str]

class AttendanceOut(AttendanceBase):
    id: UUID

    class Config:
        orm_mode = True
