from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.enrollment import EnrollmentCreate, EnrollmentOut
from app.crud import enrollment as crud
from app.db.session import get_db
from app.schemas.withdrawal import WithdrawalRequest
from app.services.enrollment_logic import withdraw_student

router = APIRouter()

@router.post("/", response_model=EnrollmentOut)
def create_enrollment(payload: EnrollmentCreate, db: Session = Depends(get_db)):
    return crud.create_enrollment(db, payload)

@router.get("/", response_model=list[EnrollmentOut])
def list_enrollments(student_id: str, db: Session = Depends(get_db)):
    return crud.get_enrollments_by_student(db, student_id)

@router.post("/{enrollment_id}/withdraw", response_model=EnrollmentOut)
def withdraw(enrollment_id: str, req: WithdrawalRequest, db: Session = Depends(get_db)):
    return withdraw_student(db, enrollment_id, req)

from app.schemas.enrollment import ReEnrollmentRequest
from app.services.enrollment_logic import re_enroll_student

@router.post("/re_enroll/{student_id}", response_model=EnrollmentOut)
def re_enroll(student_id: str, req: ReEnrollmentRequest, db: Session = Depends(get_db)):
    return re_enroll_student(db, student_id, req)

