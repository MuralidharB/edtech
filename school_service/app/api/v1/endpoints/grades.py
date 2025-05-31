from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.grade import Grade, GradeCreate, GradeUpdate
from app.crud import grade as crud_grade
from app.db.session import get_db
from typing import List
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=Grade)
def create_grade(grade_in: GradeCreate, db: Session = Depends(get_db)):
    return crud_grade.create_grade(db, grade_in)

@router.get("/", response_model=List[Grade])
def list_grades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_grade.get_grades(db, skip=skip, limit=limit)

@router.get("/{grade_id}", response_model=Grade)
def get_grade(grade_id: UUID, db: Session = Depends(get_db)):
    grade = crud_grade.get_grade(db, grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    return grade

@router.put("/{grade_id}", response_model=Grade)
def update_grade(grade_id: UUID, grade_in: GradeUpdate, db: Session = Depends(get_db)):
    return crud_grade.update_grade(db, grade_id, grade_in)

@router.delete("/{grade_id}")
def delete_grade(grade_id: UUID, db: Session = Depends(get_db)):
    return crud_grade.delete_grade(db, grade_id)

