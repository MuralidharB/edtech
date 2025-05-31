from sqlalchemy.orm import Session
from app.db.models.exam import Exam
from app.schemas.exam import ExamCreate

def create_exam(db: Session, exam: ExamCreate) -> Exam:
    db_exam = Exam(**exam.dict())
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

def get_exam(db: Session, exam_id: str) -> Exam:
    return db.query(Exam).filter(Exam.id == exam_id).first()

def list_exams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Exam).offset(skip).limit(limit).all()

def delete_exam(db: Session, exam_id: str):
    db_exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if db_exam:
        db.delete(db_exam)
        db.commit()
    return db_exam

