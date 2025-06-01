# app/schemas/submission.py

from pydantic import BaseModel, UUID4
from typing import List, Dict, Optional
from datetime import datetime

class SubmissionCreate(BaseModel):
    student_id: UUID4
    quiz_id: UUID4
    answers: List[Dict]  # each: { "question_id": ..., "answer": ... }

class SubmissionOut(SubmissionCreate):
    id: UUID4
    submitted_at: datetime
    grade: Optional[int] = None

