from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class ParentStudentLink(Base):
    __tablename__ = "parent_student_links"

    parent_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)

    parent = relationship("User", foreign_keys=[parent_id], back_populates="students")
    student = relationship("User", foreign_keys=[student_id], back_populates="parents")

