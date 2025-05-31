from sqlalchemy.orm import Session
from app.db.models.school import School
from app.schemas.school import SchoolCreate, SchoolUpdate
from uuid import UUID

def create_school(db: Session, school: SchoolCreate):
    db_school = School(**school.dict())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

def get_school(db: Session, school_id: UUID):
    return db.query(School).filter(School.id == school_id).first()

def get_schools(db: Session, skip: int = 0, limit: int = 100):
    return db.query(School).offset(skip).limit(limit).all()

def update_school(db: Session, school_id: UUID, updates: SchoolUpdate):
    db_school = db.query(School).filter(School.id == school_id).first()
    if db_school:
        for field, value in updates.dict(exclude_unset=True).items():
            setattr(db_school, field, value)
        db.commit()
        db.refresh(db_school)
    return db_school

def delete_school(db: Session, school_id: UUID):
    db_school = db.query(School).filter(School.id == school_id).first()
    if db_school:
        db.delete(db_school)
        db.commit()
    return db_school

