from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.grading import GradingEntryCreate, GradingEntryRead
from app.crud import grading as crud_grading
from app.db.session import get_db

router = APIRouter(prefix="/grading", tags=["grading"])

@router.post("/", response_model=GradingEntryRead)
def create_entry(entry: GradingEntryCreate, db: Session = Depends(get_db)):
    return crud_grading.create_grading_entry(db, entry)

@router.get("/{entry_id}", response_model=GradingEntryRead)
def get_entry(entry_id: UUID, db: Session = Depends(get_db)):
    db_entry = crud_grading.get_grading_entry(db, entry_id)
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

@router.get("/", response_model=list[GradingEntryRead])
def list_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_grading.list_grading_entries(db, skip=skip, limit=limit)

@router.delete("/{entry_id}")
def delete_entry(entry_id: UUID, db: Session = Depends(get_db)):
    deleted = crud_grading.delete_grading_entry(db, entry_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Entry not found")
    return {"detail": "Grading entry deleted"}

