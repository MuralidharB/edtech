# app/crud/lesson.py

from sqlalchemy.orm import Session
from app.db.models.lesson import Lesson
from app.schemas.lesson import LessonCreate
from uuid import UUID

def create_lesson(db: Session, payload: LessonCreate) -> Lesson:
    lesson = Lesson(**payload.dict())
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson

def get_lesson(db: Session, lesson_id: UUID) -> Lesson:
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()

def list_lessons_by_course(db: Session, course_id: UUID) -> list[Lesson]:
    return db.query(Lesson).filter(Lesson.course_id == course_id).order_by(Lesson.sequence_number).all()

