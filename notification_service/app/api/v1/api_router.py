# app/api/v1/api_router.py

from fastapi import APIRouter
from app.api.v1.endpoints import notifications

router = APIRouter()

# Route grouping for notifications
router.include_router(
    notifications.router,
    prefix="/notifications",
    tags=["Notifications"]
)

