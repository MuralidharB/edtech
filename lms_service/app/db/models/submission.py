# app/db/models/submission.py

from sqlalchemy import Column, ForeignKey, DateTime, JSON, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid
from datetime import datetime

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    quiz_id = Column(UUID(as_uuid=True), ForeignKey("quizzes.id", ondelete="CASCADE"), nullable=False)
    answers = Column(JSON, nullable=False)  # raw answers per question
    grade = Column(Integer, nullable=True)  # auto or manual scoring
    submitted_at = Column(DateTime, default=datetime.utcnow)

