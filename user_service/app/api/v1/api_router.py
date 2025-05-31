from fastapi import APIRouter
from app.api.v1.endpoints import auth
from app.api.v1.endpoints import users, roles, parent_student_links

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(roles.router, prefix="/roles", tags=["Roles"])
router.include_router(parent_student_links.router, prefix="/links", tags=["Parent-Student Links"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])

