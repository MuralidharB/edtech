# app/crud/notification.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.notification import Notification
from app.schemas.notification import NotificationCreate

async def create_notification(db: AsyncSession, notification: NotificationCreate) -> Notification:
    db_notification = Notification(**notification.dict())
    db.add(db_notification)
    await db.commit()
    await db.refresh(db_notification)
    return db_notification

async def get_notifications_by_recipient(db: AsyncSession, recipient_id: str):
    result = await db.execute(select(Notification).where(Notification.recipient_id == recipient_id))
    return result.scalars().all()

