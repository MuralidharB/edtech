from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base
from datetime import datetime
import uuid

class ContentBlock(Base):
    __tablename__ = "content_blocks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lesson_id = Column(UUID, ForeignKey("lessons.id"), nullable=False)
    type = Column(String)  # text, video, quiz, file
    content = Column(JSONB)
