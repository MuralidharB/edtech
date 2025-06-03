from pydantic import BaseModel
from uuid import UUID

class QuizGenerationRequest(BaseModel):
    lesson_id: UUID
    num_questions: int = 5
    difficulty: str = "medium"
    question_type: str = "mcq"

