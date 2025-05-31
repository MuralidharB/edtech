class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(UUID, ForeignKey("courses.id"), nullable=False)
    title = Column(String)
    sequence_number = Column(Integer)
    metadata = Column(JSONB)  # e.g. tags, duration, etc.

