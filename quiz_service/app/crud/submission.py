from app.db.models.submission import Submission
from app.schemas.submission import SubmissionCreate
from sqlalchemy.orm import Session

def create_submission(db: Session, submission: SubmissionCreate):
    db_submission = Submission(
        quiz_id=submission.quiz_id,
        student_id=submission.student_id,
        answers=submission.answers
    )
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission
