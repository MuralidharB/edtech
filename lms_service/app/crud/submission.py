# app/crud/submission.py

from sqlalchemy.orm import Session
from app.db.models.submission import Submission
from app.schemas.submission import SubmissionCreate
from uuid import UUID
from app.db.models.quiz import Quiz
from datetime import datetime

def auto_grade(quiz: Quiz, answers: list[dict]) -> int:
    """Compute score by matching answers against quiz.questions"""
    answer_map = {a["question_id"]: a["answer"] for a in answers}
    score = 0

    for question in quiz.questions:
        qid = question.get("id")
        qtype = question.get("type")
        correct = False

        if qtype == "multiple_choice":
            correct = answer_map.get(qid) == question.get("correct")

        elif qtype == "short_answer":
            keywords = question.get("keywords", [])
            student_answer = answer_map.get(qid, "").lower()
            correct = all(k.lower() in student_answer for k in keywords)

        if correct:
            score += 1

    return score


def create_submission(db: Session, payload: SubmissionCreate) -> Submission:
    # Load the associated quiz with questions
    quiz = db.query(Quiz).filter(Quiz.id == payload.quiz_id).first()
    if not quiz:
        raise Exception("Quiz not found")

    score = auto_grade(quiz, payload.answers)

    submission = Submission(
        student_id=payload.student_id,
        quiz_id=payload.quiz_id,
        answers=payload.answers,
        grade=score,
        submitted_at=datetime.utcnow()
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)
    return submission


def list_submissions_by_quiz(db: Session, quiz_id: UUID) -> list[Submission]:
    return db.query(Submission).filter(Submission.quiz_id == quiz_id).all()

def list_submissions_by_student(db: Session, student_id: UUID) -> list[Submission]:
    return db.query(Submission).filter(Submission.student_id == student_id).all()

