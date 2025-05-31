from sqlalchemy.orm import Session
from app.db.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate, AttendanceUpdate

def create_attendance(db: Session, record: AttendanceCreate) -> Attendance:
    db_record = Attendance(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_attendance(db: Session, student_id, date):
    return db.query(Attendance).filter(Attendance.student_id == student_id, Attendance.date == date).first()

def update_attendance(db: Session, attendance_id, update_data: AttendanceUpdate):
    record = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(record, field, value)
    db.commit()
    db.refresh(record)
    return record
