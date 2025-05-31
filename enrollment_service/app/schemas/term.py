from pydantic import BaseModel
from enum import Enum
from datetime import date
from uuid import UUID


class TermStatus(str, Enum):
    planned = "planned"
    active = "active"
    completed = "completed"

class TermBase(BaseModel):
    name: str
    start_date: date
    end_date: date

class TermCreate(TermBase):
    status: TermStatus = TermStatus.planned  # optional with default

class TermUpdate(BaseModel):
    name: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    status: TermStatus | None = None

class TermOut(TermBase):
    id: UUID
    status: TermStatus

    class Config:
        orm_mode = True
        use_enum_values = True

