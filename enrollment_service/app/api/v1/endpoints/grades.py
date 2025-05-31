# app/api/v1/endpoints/grades.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.grade import GradeCreate, GradeOut
from app.crud import grade as crud

router = APIRouter()

@router.post("/", response_model=GradeOut)
def create_grade(payload: GradeCreate, db: Session = Depends(get_db)):
    return crud.create_grade(db, payload)

@router.get("/{grade_id}", response_model=GradeOut)
def get_grade(grade_id: str, db: Session = Depends(get_db)):
    grade = crud.get_grade(db, grade_id)
    if not grade:
        raise HTTPException(404, "Grade not found")
    return grade

@router.get("/", response_model=list[GradeOut])
def list_grades(db: Session = Depends(get_db)):
    return crud.list_grades(db)

