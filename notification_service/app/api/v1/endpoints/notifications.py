# app/api/v1/endpoints/notifications.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.notification import NotificationCreate, NotificationOut
from app.crud.notification import create_notification, get_notifications_by_recipient
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=NotificationOut, status_code=201)
async def send_notification(notification: NotificationCreate, db: AsyncSession = Depends(get_db)):
    return await create_notification(db, notification)

@router.get("/recipient/{recipient_id}", response_model=List[NotificationOut])
async def fetch_recipient_notifications(recipient_id: str, db: AsyncSession = Depends(get_db)):
    return await get_notifications_by_recipient(db, recipient_id)

