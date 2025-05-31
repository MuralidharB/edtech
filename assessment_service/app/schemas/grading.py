from pydantic import BaseModel
from uuid import UUID

class GradingEntryBase(BaseModel):
    student_id: UUID
    exam_id: UUID
    marks: float
    grade: str | None = None

class GradingEntryCreate(GradingEntryBase):
    pass

class GradingEntryRead(GradingEntryBase):
    id: UUID

    class Config:
        orm_mode = True

