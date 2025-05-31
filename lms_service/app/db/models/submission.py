class Submission(Base):
    __tablename__ = "submissions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID, nullable=False)
    lesson_id = Column(UUID, nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    answers = Column(JSONB)
    grade = Column(Integer)
    is_reviewed = Column(Boolean, default=False)
    teacher_comments = Column(Text, nullable=True)
    graded_by = Column(UUID, nullable=True)  # Teacher ID

class SubmissionResponse(Base):
    __tablename__ = "submission_responses"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    submission_id = Column(UUID, ForeignKey("submissions.id"))
    question_id = Column(String)
    student_answer = Column(Text)
    teacher_comment = Column(Text)
    is_correct = Column(Boolean)
