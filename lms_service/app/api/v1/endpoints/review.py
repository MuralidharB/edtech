@router.post("/{submission_id}/review", status_code=200)
def review_submission(submission_id: str, review: ManualReviewRequest, db: Session = Depends(get_db)):
    submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    total_score = 0
    for r in review.responses:
        total_score += r.score
        db.add(SubmissionResponse(
            submission_id=submission_id,
            question_id=r.question_id,
            is_correct=r.score > 0,
            teacher_comment=r.teacher_comment,
            score=r.score
        ))

    submission.grade = total_score
    submission.is_reviewed = True
    submission.teacher_comments = review.comments
    submission.graded_by = review.teacher_id
    db.commit()

    return {"status": "reviewed", "score": total_score}

