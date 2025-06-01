from fastapi import APIRouter
from app.api.v1.endpoints import rules

router = APIRouter()
router.include_router(rules.router, prefix="/rules", tags=["rules"])

