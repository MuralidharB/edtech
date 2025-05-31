from pydantic import BaseModel
from uuid import UUID

class ResultBase(BaseModel):
    student_id: UUID
    term_id: UUID
    gpa: float
    remarks: str | None = None

class ResultCreate(ResultBase):
    pass

class ResultRead(ResultBase):
    id: UUID

    class Config:
        orm_mode = True

