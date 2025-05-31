from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...schemas.announcement import AnnouncementCreate, AnnouncementOut
from ...crud.announcement import create_announcement
from ...core.security import require_roles, TokenData

router = APIRouter()

@router.post("/", response_model=AnnouncementOut)
def create_announcement_view(
    announcement: AnnouncementCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(require_roles(["teacher"]))
):
    return create_announcement(db, announcement)

