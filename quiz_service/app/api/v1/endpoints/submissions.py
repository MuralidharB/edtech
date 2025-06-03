from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.submission import SubmissionCreate, SubmissionOut
from app.crud import submission as submission_crud
from app.db.session import get_db

router = APIRouter()

@router.post("/submissions", response_model=SubmissionOut)
def submit_quiz(submission: SubmissionCreate, db: Session = Depends(get_db)):
    return submission_crud.create_submission(db, submission)
