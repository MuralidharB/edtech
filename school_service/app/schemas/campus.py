from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class CampusBase(BaseModel):
    name: str
    school_id: UUID
    address: Optional[str] = None

class CampusCreate(CampusBase):
    pass

class CampusUpdate(CampusBase):
    pass

class Campus(CampusBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

