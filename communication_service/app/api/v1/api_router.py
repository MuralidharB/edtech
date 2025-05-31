from fastapi import APIRouter
from .endpoints import messages, announcements

api_router = APIRouter()
api_router.include_router(messages.router, prefix="/messages", tags=["Messages"])
api_router.include_router(announcements.router, prefix="/announcements", tags=["Announcements"])

