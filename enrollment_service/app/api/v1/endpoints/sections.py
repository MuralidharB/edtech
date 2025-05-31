# app/api/v1/endpoints/sections.py
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.section import SectionCreate, SectionOut
from app.crud import section as crud

router = APIRouter()

@router.post("/", response_model=SectionOut)
def create_section(payload: SectionCreate, db: Session = Depends(get_db)):
    return crud.create_section(db, payload)

@router.get("/{section_id}", response_model=SectionOut)
def get_section(section_id: str, db: Session = Depends(get_db)):
    section = crud.get_section(db, section_id)
    if not section:
        raise HTTPException(404, "Section not found")
    return section

@router.get("/", response_model=list[SectionOut])
def list_sections(grade_id: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.list_sections(db, grade_id)

