from pydantic import BaseModel, UUID4
from typing import List, Dict, Optional

class QuizCreate(BaseModel):
    lesson_id: UUID4
    title: str
    questions: List[Dict]  # flexible schema: multiple choice, short answer, etc.
    metadata: Optional[Dict[str, str]] = None

class QuizOut(QuizCreate):
    id: UUID4

class QuizAnswer(BaseModel):
    question_id: str
    answer: str

class QuizSubmission(BaseModel):
    student_id: UUID4
    lesson_id: UUID4
    answers: List[QuizAnswer]

class GradedResponse(BaseModel):
    question_id: str
    answer: str
    correct: bool
    feedback: Optional[str] = None

class SubmissionResult(BaseModel):
    score: int
    total: int
    responses: List[GradedResponse]

