# app/schemas/section.py
from pydantic import BaseModel, UUID4
from typing import Optional

class SectionCreate(BaseModel):
    name: str
    grade_id: UUID4
    max_capacity: Optional[int] = None
    assigned_teacher_id: Optional[UUID4] = None

class SectionOut(SectionCreate):
    id: UUID4

