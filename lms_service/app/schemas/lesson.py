# app/schemas/lesson.py

from pydantic import BaseModel, UUID4
from typing import Optional, Dict

class LessonCreate(BaseModel):
    course_id: UUID4
    title: str
    sequence_number: Optional[int] = None
    metadata: Optional[Dict[str, str]] = None

class LessonOut(LessonCreate):
    id: UUID4

