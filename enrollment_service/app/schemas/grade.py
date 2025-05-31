# app/schemas/grade.py
from pydantic import BaseModel, UUID4
from typing import Optional

class GradeCreate(BaseModel):
    name: str
    level: int
    curriculum: Optional[str] = None

class GradeOut(GradeCreate):
    id: UUID4

