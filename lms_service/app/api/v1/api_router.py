# app/api/v1/api_router.py

from fastapi import APIRouter
from .endpoints import courses, lessons, submissions, quizzes

router = APIRouter()

# Course management endpoints
router.include_router(courses.router, prefix="/courses", tags=["Courses"])

# Lesson content and sequencing
router.include_router(lessons.router, prefix="/lessons", tags=["Lessons"])

# Quiz and assessment submission
router.include_router(submissions.router, prefix="/submissions", tags=["Submissions"])

# (Optional) Quiz authoring, question bank, or grading logic
router.include_router(quizzes.router, prefix="/quizzes", tags=["Quizzes"])

