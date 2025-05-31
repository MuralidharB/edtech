from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.section import Section, SectionCreate, SectionUpdate
from app.crud import section as crud_section
from app.db.session import get_db
from typing import List
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=Section)
def create_section(section_in: SectionCreate, db: Session = Depends(get_db)):
    return crud_section.create_section(db, section_in)

@router.get("/", response_model=List[Section])
def list_sections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_section.get_sections(db, skip=skip, limit=limit)

@router.get("/{section_id}", response_model=Section)
def get_section(section_id: UUID, db: Session = Depends(get_db)):
    section = crud_section.get_section(db, section_id)
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")
    return section

@router.put("/{section_id}", response_model=Section)
def update_section(section_id: UUID, section_in: SectionUpdate, db: Session = Depends(get_db)):
    return crud_section.update_section(db, section_id, section_in)

@router.delete("/{section_id}")
def delete_section(section_id: UUID, db: Session = Depends(get_db)):
    return crud_section.delete_section(db, section_id)

