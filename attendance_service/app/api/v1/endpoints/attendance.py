from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.attendance import AttendanceCreate, AttendanceUpdate, AttendanceOut
from app.crud.attendance import create_attendance, get_attendance, update_attendance
from app.db.session import get_db
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=AttendanceOut)
def record_attendance(payload: AttendanceCreate, db: Session = Depends(get_db)):
    return create_attendance(db, payload)

@router.get("/{student_id}/{date}", response_model=AttendanceOut)
def fetch_attendance(student_id: UUID, date: str, db: Session = Depends(get_db)):
    record = get_attendance(db, student_id, date)
    if not record:
        raise HTTPException(status_code=404, detail="Attendance not found")
    return record

@router.put("/{attendance_id}", response_model=AttendanceOut)
def modify_attendance(attendance_id: UUID, payload: AttendanceUpdate, db: Session = Depends(get_db)):
    return update_attendance(db, attendance_id, payload)

