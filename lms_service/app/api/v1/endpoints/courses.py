# app/api/v1/endpoints/courses.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.db.session import get_db
from app.schemas.course import CourseCreate, CourseOut
from app.crud import course as crud

router = APIRouter()

@router.post("/", response_model=CourseOut, status_code=201)
def create_course(payload: CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, payload)

@router.get("/", response_model=List[CourseOut])
def list_courses(db: Session = Depends(get_db)):
    return crud.list_courses(db)

@router.get("/{course_id}", response_model=CourseOut)
def get_course(course_id: UUID, db: Session = Depends(get_db)):
    course = crud.get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

