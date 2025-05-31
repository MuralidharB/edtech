from fastapi import APIRouter
from app.api.v1.endpoints import schools, campuses, grades, sections

router = APIRouter()
router.include_router(schools.router, prefix="/schools", tags=["schools"])
router.include_router(campuses.router, prefix="/campuses", tags=["campuses"])
router.include_router(grades.router, prefix="/grades", tags=["grades"])
router.include_router(sections.router, prefix="/sections", tags=["sections"])

