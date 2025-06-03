from fastapi import APIRouter
from app.api.v1.endpoints import quizzes, submissions, questions, generate

router = APIRouter()
router.include_router(quizzes.router, prefix="/quizzes", tags=["quizzes"])
router.include_router(submissions.router, prefix="/submissions", tags=["submissions"])
router.include_router(questions.router, tags=["questions"])
router.include_router(generate.router, tags=["generate"])
