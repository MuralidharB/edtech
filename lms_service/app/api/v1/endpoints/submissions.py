@router.post("/", response_model=SubmissionOut)
def submit_assignment(payload: SubmissionCreate, db: Session = Depends(get_db)):
    return submission_crud.create(db, payload)

from app.schemas.quiz import QuizSubmission, SubmissionResult
from app.services.quiz_grader import grade_quiz
from app.crud.lesson import get_quiz_block_by_lesson

@router.post("/quiz", response_model=SubmissionResult)
def submit_quiz(payload: QuizSubmission, db: Session = Depends(get_db)):
    quiz_block = get_quiz_block_by_lesson(db, payload.lesson_id)
    if not quiz_block:
        raise HTTPException(status_code=404, detail="Quiz not found")

    questions = quiz_block.content["questions"]
    grading = grade_quiz(questions, payload.answers)

    # Optionally persist result
    submission = Submission(
        student_id=payload.student_id,
        lesson_id=payload.lesson_id,
        answers=grading["responses"],
        grade=grading["score"]
    )
    db.add(submission)
    db.commit()

    return grading

