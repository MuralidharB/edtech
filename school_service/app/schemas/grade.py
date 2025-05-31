from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class GradeBase(BaseModel):
    name: str
    level: int
    campus_id: UUID
    curriculum: Optional[str] = None

class GradeCreate(GradeBase):
    pass

class GradeUpdate(GradeBase):
    pass

class Grade(GradeBase):
    id: UUID

    class Config:
        orm_mode = True
