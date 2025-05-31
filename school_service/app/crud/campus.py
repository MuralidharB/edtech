from sqlalchemy.orm import Session
from app.db.models.campus import Campus
from app.schemas.campus import CampusCreate, CampusUpdate
from uuid import UUID

def create_campus(db: Session, campus: CampusCreate):
    db_campus = Campus(**campus.dict())
    db.add(db_campus)
    db.commit()
    db.refresh(db_campus)
    return db_campus

def get_campus(db: Session, campus_id: UUID):
    return db.query(Campus).filter(Campus.id == campus_id).first()

def get_campuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Campus).offset(skip).limit(limit).all()

def update_campus(db: Session, campus_id: UUID, updates: CampusUpdate):
    db_campus = db.query(Campus).filter(Campus.id == campus_id).first()
    if db_campus:
        for field, value in updates.dict(exclude_unset=True).items():
            setattr(db_campus, field, value)
        db.commit()
        db.refresh(db_campus)
    return db_campus

def delete_campus(db: Session, campus_id: UUID):
    db_campus = db.query(Campus).filter(Campus.id == campus_id).first()
    if db_campus:
        db.delete(db_campus)
        db.commit()
    return db_campus

