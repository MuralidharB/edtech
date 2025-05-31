# app/crud/section.py
from sqlalchemy.orm import Session
from app.db.models.section import Section
from app.schemas.section import SectionCreate

def create_section(db: Session, payload: SectionCreate):
    section = Section(**payload.dict())
    db.add(section)
    db.commit()
    db.refresh(section)
    return section

def get_section(db: Session, section_id):
    return db.query(Section).filter(Section.id == section_id).first()

def list_sections(db: Session, grade_id=None):
    query = db.query(Section)
    if grade_id:
        query = query.filter(Section.grade_id == grade_id)
    return query.order_by(Section.name).all()

