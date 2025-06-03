from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional

class QuestionOut(BaseModel):
    id: UUID
    quiz_id: UUID
    question_text: str
    type: str
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None
    explanation: Optional[str] = None

    class Config:
        orm_mode = True
