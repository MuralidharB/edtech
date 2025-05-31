from sqlalchemy.orm import Session
from app.db.models.section import Section
from app.schemas.section import SectionCreate, SectionUpdate
from uuid import UUID

def create_section(db: Session, section: SectionCreate):
    db_section = Section(**section.dict())
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section

def get_section(db: Session, section_id: UUID):
    return db.query(Section).filter(Section.id == section_id).first()

def get_sections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Section).offset(skip).limit(limit).all()

def update_section(db: Session, section_id: UUID, updates: SectionUpdate):
    db_section = db.query(Section).filter(Section.id == section_id).first()
    if db_section:
        for field, value in updates.dict(exclude_unset=True).items():
            setattr(db_section, field, value)
        db.commit()
        db.refresh(db_section)
    return db_section

def delete_section(db: Session, section_id: UUID):
    db_section = db.query(Section).filter(Section.id == section_id).first()
    if db_section:
        db.delete(db_section)
        db.commit()
    return db_section

