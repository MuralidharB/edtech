from pydantic import BaseModel
from uuid import UUID
from datetime import date

class ExamBase(BaseModel):
    name: str
    subject: str
    date: date
    section_id: UUID
    term_id: UUID

class ExamCreate(ExamBase):
    pass

class ExamRead(ExamBase):
    id: UUID

    class Config:
        orm_mode = True

