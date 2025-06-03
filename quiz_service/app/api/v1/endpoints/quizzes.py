from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.quiz import QuizCreate, QuizOut
from app.crud import quiz as quiz_crud
from app.db.session import get_db

router = APIRouter()

@router.post("/quizzes", response_model=QuizOut)
def create_quiz(quiz: QuizCreate, db: Session = Depends(get_db)):
    return quiz_crud.create_quiz(db, quiz)
