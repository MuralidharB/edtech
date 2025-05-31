from pydantic import BaseModel, UUID4
from datetime import date

class EnrollmentCreate(BaseModel):
    student_id: UUID4
    term_id: UUID4
    grade_id: UUID4
    section_id: UUID4

class EnrollmentOut(EnrollmentCreate):
    id: UUID4
    status: str
    enrollment_date: date

class ReEnrollmentRequest(BaseModel):
    term_id: UUID4
    promoted_grade_id: UUID4
    section_id: UUID4
    enrollment_date: date

