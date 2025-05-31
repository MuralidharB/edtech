class Concept(Base):
    __tablename__ = "concepts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)

class ConceptEdge(Base):
    __tablename__ = "concept_prerequisites"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_id = Column(UUID, ForeignKey("concepts.id"))
    target_id = Column(UUID, ForeignKey("concepts.id"))
    relationship = Column(String)  # e.g., "requires", "related_to"

class LessonConcept(Base):
    __tablename__ = "lesson_concepts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lesson_id = Column(UUID, ForeignKey("lessons.id"))
    concept_id = Column(UUID, ForeignKey("concepts.id"))

class StudentConceptMastery(Base):
    student_id = Column(UUID)
    concept_id = Column(UUID)
    mastery_level = Column(Integer)  # e.g., 0–100
    last_updated = Column(TIMESTAMP)

