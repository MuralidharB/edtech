from fastapi import APIRouter
from app.api.v1.endpoints import exams, grading, results

api_router = APIRouter()
api_router.include_router(exams.router)
api_router.include_router(grading.router)
api_router.include_router(results.router)

