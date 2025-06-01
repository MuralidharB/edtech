# app/schemas/course.py

from pydantic import BaseModel, UUID4
from typing import Optional

class CourseCreate(BaseModel):
    title: str
    subject: Optional[str]
    grade_level: Optional[int]
    curriculum: Optional[str]
    created_by: Optional[UUID4]

class CourseOut(CourseCreate):
    id: UUID4

