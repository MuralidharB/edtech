from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class SectionBase(BaseModel):
    name: str
    grade_id: UUID
    teacher_id: Optional[UUID] = None  # Link to user-service (teacher)

class SectionCreate(SectionBase):
    pass

class SectionUpdate(SectionBase):
    pass

class Section(SectionBase):
    id: UUID

    class Config:
        orm_mode = True

