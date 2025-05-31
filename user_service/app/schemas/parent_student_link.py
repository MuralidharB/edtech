from pydantic import BaseModel
from uuid import UUID

class ParentStudentLinkBase(BaseModel):
    parent_id: UUID
    student_id: UUID

class ParentStudentLinkCreate(ParentStudentLinkBase):
    pass

class ParentStudentLinkRead(ParentStudentLinkBase):
    class Config:
        orm_mode = True

