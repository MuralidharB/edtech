# app/api/v1/endpoints/submissions.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.db.session import get_db
from app.schemas.submission import SubmissionCreate, SubmissionOut
from app.crud import submission as crud

router = APIRouter()

@router.post("/", response_model=SubmissionOut, status_code=201)
def submit_quiz(payload: SubmissionCreate, db: Session = Depends(get_db)):
    return crud.create_submission(db, payload)

@router.get("/quiz/{quiz_id}", response_model=List[SubmissionOut])
def get_submissions_by_quiz(quiz_id: UUID, db: Session = Depends(get_db)):
    return crud.list_submissions_by_quiz(db, quiz_id)

@router.get("/student/{student_id}", response_model=List[SubmissionOut])
def get_submissions_by_student(student_id: UUID, db: Session = Depends(get_db)):
    return crud.list_submissions_by_student(db, student_id)

