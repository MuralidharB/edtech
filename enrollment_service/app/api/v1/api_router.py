from fastapi import APIRouter
from .endpoints import enrollments

router = APIRouter()
router.include_router(enrollments.router, prefix="/enrollments", tags=["Enrollments"])

from .endpoints import grades

router.include_router(grades.router, prefix="/grades", tags=["Grades"])

from .endpoints import sections
router.include_router(sections.router, prefix="/sections", tags=["Sections"])

from .endpoints import terms
router.include_router(terms.router, prefix="/terms", tags=["Terms"])

