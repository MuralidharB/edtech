# app/api/v1/endpoints/contents.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.content import ContentCreate, ContentOut
from app.crud.content import create_content, get_content, list_contents
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=ContentOut, status_code=201)
def create(content: ContentCreate, db: Session = Depends(get_db)):
    return create_content(db, content)

@router.get("/{content_id}", response_model=ContentOut)
def fetch(content_id: UUID, db: Session = Depends(get_db)):
    db_obj = get_content(db, content_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_obj

@router.get("/", response_model=list[ContentOut])
def list_all(db: Session = Depends(get_db)):
    return list_contents(db)

