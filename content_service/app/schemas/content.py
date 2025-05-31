# app/schemas/content.py
from pydantic import BaseModel, HttpUrl
from typing import Optional
from uuid import UUID
from datetime import datetime

class ContentBase(BaseModel):
    title: str
    description: Optional[str]
    type: str
    file_url: HttpUrl
    tags: Optional[str] = None
    locale: Optional[str] = "en"

class ContentCreate(ContentBase):
    uploaded_by: UUID

class ContentOut(ContentBase):
    id: UUID
    uploaded_by: UUID
    created_at: datetime

    class Config:
        orm_mode = True

