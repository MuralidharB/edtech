from sqlalchemy.orm import Session
from ..models.announcement import Announcement
from ..schemas.announcement import AnnouncementCreate

def create_announcement(db: Session, announcement: AnnouncementCreate):
    db_announcement = Announcement(**announcement.dict())
    db.add(db_announcement)
    db.commit()
    db.refresh(db_announcement)
    return db_announcement

