# app/crud/quiz.py

from sqlalchemy.orm import Session
from app.db.models.quiz import Quiz
from app.schemas.quiz import QuizCreate
from uuid import UUID

def create_quiz(db: Session, payload: QuizCreate) -> Quiz:
    quiz = Quiz(**payload.dict())
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz

def get_quiz(db: Session, quiz_id: UUID) -> Quiz:
    return db.query(Quiz).filter(Quiz.id == quiz_id).first()

def list_quizzes_by_lesson(db: Session, lesson_id: UUID) -> list[Quiz]:
    return db.query(Quiz).filter(Quiz.lesson_id == lesson_id).all()

