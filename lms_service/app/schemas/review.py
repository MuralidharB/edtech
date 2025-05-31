from pydantic import BaseModel, UUID4
from typing import List, Optional

class QuestionReview(BaseModel):
    question_id: str
    is_correct: bool
    teacher_comment: Optional[str] = None

class ManualReviewRequest(BaseModel):
    teacher_id: UUID4
    comments: Optional[str]
    responses: List[QuestionReview]

class QuestionReview(BaseModel):
    question_id: str
    score: int  # score awarded by teacher (0 to weight)
    max_score: Optional[int] = None
    teacher_comment: Optional[str] = None

class ManualReviewRequest(BaseModel):
    teacher_id: UUID4
    comments: Optional[str]
    responses: List[QuestionReview]

