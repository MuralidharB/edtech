# app/schemas/notification.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class NotificationType(str, Enum):
    email = "email"
    sms = "sms"
    push = "push"

class NotificationStatus(str, Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"

class NotificationBase(BaseModel):
    recipient_id: str
    recipient_role: str
    message: str
    type: NotificationType = NotificationType.push

class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    id: int
    status: NotificationStatus
    created_at: datetime
    sent_at: Optional[datetime]

    class Config:
        orm_mode = True

