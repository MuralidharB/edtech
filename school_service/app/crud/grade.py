from sqlalchemy.orm import Session
from app.db.models.grade import Grade
from app.schemas.grade import GradeCreate, GradeUpdate
from uuid import UUID

def create_grade(db: Session, grade: GradeCreate):
    db_grade = Grade(**grade.dict())
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade

def get_grade(db: Session, grade_id: UUID):
    return db.query(Grade).filter(Grade.id == grade_id).first()

def get_grades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Grade).offset(skip).limit(limit).all()

def update_grade(db: Session, grade_id: UUID, updates: GradeUpdate):
    db_grade = db.query(Grade).filter(Grade.id == grade_id).first()
    if db_grade:
        for field, value in updates.dict(exclude_unset=True).items():
            setattr(db_grade, field, value)
        db.commit()
        db.refresh(db_grade)
    return db_grade

def delete_grade(db: Session, grade_id: UUID):
    db_grade = db.query(Grade).filter(Grade.id == grade_id).first()
    if db_grade:
        db.delete(db_grade)
        db.commit()
    return db_grade

