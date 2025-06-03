from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.question import QuestionOut
from app.crud.question import get_questions_by_quiz
from app.db.session import get_db
from typing import List
from uuid import UUID

router = APIRouter()

@router.get("/quizzes/{quiz_id}/questions", response_model=List[QuestionOut])
def list_questions(quiz_id: UUID, db: Session = Depends(get_db)):
    return get_questions_by_quiz(db, quiz_id)
