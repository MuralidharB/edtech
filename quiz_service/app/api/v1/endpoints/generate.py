# app/api/v1/endpoints/generate.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.generate import QuizGenerationRequest
from app.schemas.quiz import QuizOut
from app.services.gpt_generator import generate_quiz_questions
from app.crud.quiz import create_quiz
import requests

router = APIRouter()

@router.post("/quizzes/generate", response_model=QuizOut)
def generate_quiz(request: QuizGenerationRequest, db: Session = Depends(get_db)):
    # Mock LMS lesson content fetch
    lesson_snippet = f"Lesson content for ID {request.lesson_id} (placeholder)."
    response = requests.get(f"http://lms-service/api/v1/lessons/{request.lesson_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Lesson not found")
    lesson_snippet = response.json().get("content_snippet")


    try:
        questions = generate_quiz_questions(lesson_snippet, count=request.num_questions, difficulty=request.difficulty, qtype=request.question_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GPT generation failed: {str(e)}")

    # Build quiz payload
    quiz_data = {
        "title": f"Auto Quiz for Lesson {request.lesson_id}",
        "mode": "self_learning",
        "subject": "Science",
        "grade": 6,
        "lesson_id": request.lesson_id,
        "questions": questions
    }
    return create_quiz(db, quiz_data)
