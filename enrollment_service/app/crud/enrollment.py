from sqlalchemy.orm import Session
from app.db.models.enrollment import Enrollment
from app.schemas.enrollment import EnrollmentCreate

def create_enrollment(db: Session, payload: EnrollmentCreate):
    db_obj = Enrollment(**payload.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_enrollments_by_student(db: Session, student_id):
    return db.query(Enrollment).filter(Enrollment.student_id == student_id).all()

