from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class MessageCreate(BaseModel):
    sender_id: UUID
    receiver_id: UUID
    content: str

class MessageOut(MessageCreate):
    id: UUID
    timestamp: datetime

    class Config:
        orm_mode = True

