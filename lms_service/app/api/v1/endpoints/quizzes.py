# app/api/v1/endpoints/quizzes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.db.session import get_db
from app.schemas.quiz import QuizCreate, QuizOut
from app.crud import quiz as crud

router = APIRouter()

@router.post("/", response_model=QuizOut, status_code=201)
def create_quiz(payload: QuizCreate, db: Session = Depends(get_db)):
    return crud.create_quiz(db, payload)

@router.get("/{quiz_id}", response_model=QuizOut)
def get_quiz(quiz_id: UUID, db: Session = Depends(get_db)):
    quiz = crud.get_quiz(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@router.get("/lesson/{lesson_id}", response_model=List[QuizOut])
def list_quizzes_by_lesson(lesson_id: UUID, db: Session = Depends(get_db)):
    return crud.list_quizzes_by_lesson(db, lesson_id)

