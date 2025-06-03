from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class QuestionCreate(BaseModel):
    question_text: str
    type: str
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None
    explanation: Optional[str] = None

class QuizCreate(BaseModel):
    title: str
    mode: str
    subject: str
    grade: int
    lesson_id: Optional[UUID]
    questions: List[QuestionCreate]

class QuizOut(QuizCreate):
    id: UUID

