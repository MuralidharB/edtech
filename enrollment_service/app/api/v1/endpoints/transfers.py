from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.enrollment_logic import transfer_student
from app.schemas.transfer import TransferRequest
from app.schemas.enrollment import EnrollmentOut

router = APIRouter()

@router.post("/{enrollment_id}/transfer", response_model=EnrollmentOut)
def transfer(enrollment_id: str, transfer: TransferRequest, db: Session = Depends(get_db)):
    return transfer_student(db, enrollment_id, transfer)

