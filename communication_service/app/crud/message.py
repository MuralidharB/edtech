from sqlalchemy.orm import Session
from ..models.message import Message
from ..schemas.message import MessageCreate

def create_message(db: Session, message: MessageCreate):
    db_msg = Message(**message.dict())
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg

