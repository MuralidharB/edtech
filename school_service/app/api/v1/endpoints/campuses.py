from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.campus import Campus, CampusCreate, CampusUpdate
from app.crud import campus as crud_campus
from app.db.session import get_db
from typing import List
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=Campus)
def create_campus(campus_in: CampusCreate, db: Session = Depends(get_db)):
    return crud_campus.create_campus(db, campus_in)

@router.get("/", response_model=List[Campus])
def list_campuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_campus.get_campuses(db, skip=skip, limit=limit)

@router.get("/{campus_id}", response_model=Campus)
def get_campus(campus_id: UUID, db: Session = Depends(get_db)):
    campus = crud_campus.get_campus(db, campus_id)
    if not campus:
        raise HTTPException(status_code=404, detail="Campus not found")
    return campus

@router.put("/{campus_id}", response_model=Campus)
def update_campus(campus_id: UUID, campus_in: CampusUpdate, db: Session = Depends(get_db)):
    return crud_campus.update_campus(db, campus_id, campus_in)

@router.delete("/{campus_id}")
def delete_campus(campus_id: UUID, db: Session = Depends(get_db)):
    return crud_campus.delete_campus(db, campus_id)

