# app/api/v1/api_router.py

from fastapi import APIRouter
from app.api.v1.endpoints import contents

api_router = APIRouter()

# Register the content endpoints
api_router.include_router(
    contents.router,
    prefix="/contents",
    tags=["Contents"]
)

