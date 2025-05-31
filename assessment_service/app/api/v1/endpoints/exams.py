from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.exam import ExamCreate, ExamRead
from app.crud import exam as crud_exam
from app.db.session import get_db

router = APIRouter(prefix="/exams", tags=["exams"])

@router.post("/", response_model=ExamRead)
def create_exam(exam: ExamCreate, db: Session = Depends(get_db)):
    return crud_exam.create_exam(db, exam)

@router.get("/{exam_id}", response_model=ExamRead)
def get_exam(exam_id: UUID, db: Session = Depends(get_db)):
    db_exam = crud_exam.get_exam(db, exam_id)
    if not db_exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return db_exam

@router.get("/", response_model=list[ExamRead])
def list_exams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_exam.list_exams(db, skip=skip, limit=limit)

@router.delete("/{exam_id}")
def delete_exam(exam_id: UUID, db: Session = Depends(get_db)):
    deleted = crud_exam.delete_exam(db, exam_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Exam not found")
    return {"detail": "Exam deleted"}

