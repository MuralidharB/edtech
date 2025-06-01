# app/crud/course.py

from sqlalchemy.orm import Session
from app.db.models.course import Course
from app.schemas.course import CourseCreate
from uuid import UUID

def create_course(db: Session, payload: CourseCreate) -> Course:
    course = Course(**payload.dict())
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def get_course(db: Session, course_id: UUID) -> Course:
    return db.query(Course).filter(Course.id == course_id).first()

def list_courses(db: Session) -> list[Course]:
    return db.query(Course).order_by(Course.title).all()

