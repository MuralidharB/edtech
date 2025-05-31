from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.school import School, SchoolCreate, SchoolUpdate
from app.crud import school as crud_school
from app.db.session import get_db
from typing import List
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=School)
def create_school(school_in: SchoolCreate, db: Session = Depends(get_db)):
    return crud_school.create_school(db, school_in)

@router.get("/", response_model=List[School])
def list_schools(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_school.get_schools(db, skip=skip, limit=limit)

@router.get("/{school_id}", response_model=School)
def get_school(school_id: UUID, db: Session = Depends(get_db)):
    school = crud_school.get_school(db, school_id)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return school

@router.put("/{school_id}", response_model=School)
def update_school(school_id: UUID, school_in: SchoolUpdate, db: Session = Depends(get_db)):
    return crud_school.update_school(db, school_id, school_in)

@router.delete("/{school_id}")
def delete_school(school_id: UUID, db: Session = Depends(get_db)):
    return crud_school.delete_school(db, school_id)

