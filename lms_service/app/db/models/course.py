class Course(Base):
    __tablename__ = "courses"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    subject = Column(String)
    grade_level = Column(Integer)
    curriculum = Column(String)
    created_by = Column(UUID)

