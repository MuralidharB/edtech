# app/crud/grade.py
from sqlalchemy.orm import Session
from app.db.models.grade import Grade
from app.schemas.grade import GradeCreate

def create_grade(db: Session, payload: GradeCreate):
    grade = Grade(**payload.dict())
    db.add(grade)
    db.commit()
    db.refresh(grade)
    return grade

def get_grade(db: Session, grade_id):
    return db.query(Grade).filter(Grade.id == grade_id).first()

def list_grades(db: Session):
    return db.query(Grade).order_by(Grade.level).all()

