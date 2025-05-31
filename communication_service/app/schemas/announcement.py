from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class AnnouncementCreate(BaseModel):
    title: str
    content: str
    created_by: UUID

class AnnouncementOut(AnnouncementCreate):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

