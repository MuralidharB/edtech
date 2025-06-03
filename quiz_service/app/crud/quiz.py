from app.db.models.quiz import Quiz
from app.db.models.question import Question
from app.schemas.quiz import QuizCreate, QuestionCreate
from sqlalchemy.orm import Session

def create_quiz(db: Session, quiz: QuizCreate):
    db_quiz = Quiz(
        title=quiz.title,
        mode=quiz.mode,
        subject=quiz.subject,
        grade=quiz.grade,
        lesson_id=quiz.lesson_id
    )
    db.add(db_quiz)
    db.flush()  # Get ID before committing

    for q in quiz.questions:
        db_question = Question(
            quiz_id=db_quiz.id,
            question_text=q.question_text,
            type=q.type,
            options=q.options,
            correct_answer=q.correct_answer,
            explanation=q.explanation
        )
        db.add(db_question)

    db.commit()
    db.refresh(db_quiz)
    return db_quiz

