from pydantic import BaseModel
from uuid import UUID
from typing import Dict

class SubmissionCreate(BaseModel):
    quiz_id: UUID
    student_id: UUID
    answers: Dict[str, str]  # question_id -> answer

class SubmissionOut(SubmissionCreate):
    id: UUID

