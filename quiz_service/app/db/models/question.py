from sqlalchemy import Column, String, ForeignKey, Enum, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class Question(Base):
    __tablename__ = "questions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quiz_id = Column(UUID(as_uuid=True), ForeignKey("quizzes.id"), nullable=False)
    question_text = Column(String, nullable=False)
    type = Column(Enum("mcq", "short_answer", "fill_blank", name="questiontype"))
    options = Column(JSON, nullable=True)  # Only for MCQ
    correct_answer = Column(String, nullable=True)
    explanation = Column(String, nullable=True)
