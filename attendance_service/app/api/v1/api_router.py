from fastapi import APIRouter
from app.api.v1.endpoints import attendance

api_router = APIRouter()
api_router.include_router(attendance.router, prefix="/api/v1/attendance", tags=["attendance"])
