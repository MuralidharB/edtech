# app/crud/content.py
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.models.content import Content
from app.schemas.content import ContentCreate

def create_content(db: Session, content: ContentCreate) -> Content:
    db_obj = Content(**content.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_content(db: Session, content_id: UUID) -> Content:
    return db.query(Content).filter(Content.id == content_id).first()

def list_contents(db: Session, skip=0, limit=100):
    return db.query(Content).offset(skip).limit(limit).all()

