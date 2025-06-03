from app.db.models.question import Question
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List


def get_questions_by_quiz(db: Session, quiz_id: UUID) -> List[Question]:
    return db.query(Question).filter(Question.quiz_id == quiz_id).all()
