from app.db.models.enrollment import Enrollment
from app.crud.enrollment import create_enrollment
from sqlalchemy.orm import Session
from app.schemas.transfer import TransferRequest
from app.schemas.withdrawal import WithdrawalRequest
from app.schemas.enrollment import ReEnrollmentRequest

def transfer_student(db: Session, enrollment_id: str, transfer: TransferRequest):
    # Mark current enrollment as transferred
    current = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if not current:
        raise Exception("Enrollment not found")

    current.status = "transferred"
    current.exit_date = transfer.transfer_date
    db.commit()

    # Create new enrollment
    new_enrollment = Enrollment(
        student_id=current.student_id,
        term_id=current.term_id,
        grade_id=transfer.new_grade_id,
        section_id=transfer.new_section_id,
        enrollment_date=transfer.transfer_date,
        status="active",
        transferred_from_id=current.id
    )
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment

def withdraw_student(db: Session, enrollment_id: str, req: WithdrawalRequest):
    enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if not enrollment:
        raise Exception("Enrollment not found")

    enrollment.status = "withdrawn"
    enrollment.exit_date = req.exit_date
    enrollment.reason_for_exit = req.reason_for_exit
    db.commit()
    db.refresh(enrollment)
    return enrollment

def re_enroll_student(db: Session, student_id: str, req: ReEnrollmentRequest):
    previous = db.query(Enrollment).filter(
        Enrollment.student_id == student_id,
        Enrollment.status == "active"
    ).order_by(Enrollment.enrollment_date.desc()).first()

    if not previous:
        raise Exception("No prior enrollment found")

    previous.status = "completed"
    db.commit()

    new_enrollment = Enrollment(
        student_id=student_id,
        term_id=req.term_id,
        grade_id=req.promoted_grade_id,
        section_id=req.section_id,
        enrollment_date=req.enrollment_date,
        status="active",
        transferred_from_id=previous.id
    )
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment

