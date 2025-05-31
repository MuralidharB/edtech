from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class SchoolBase(BaseModel):
    name: str
    address: Optional[str] = None

class SchoolCreate(SchoolBase):
    pass

class SchoolUpdate(SchoolBase):
    pass

class School(SchoolBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

