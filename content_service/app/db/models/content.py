# app/db/models/content.py
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.db.base import Base

class Content(Base):
    __tablename__ = "contents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text)
    type = Column(String, nullable=False)  # pdf, video, image, slide, etc.
    file_url = Column(String, nullable=False)  # S3 path
    uploaded_by = Column(UUID(as_uuid=True), nullable=False)
    tags = Column(String)  # Comma-separated or separate table if needed
    locale = Column(String, default='en')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
