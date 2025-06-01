from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base
from datetime import datetime
import uuid

class Concept(Base):
    __tablename__ = "concepts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    course_id = Column(UUID, ForeignKey("courses.id"))

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

class ConceptGraphVersion(Base):
    __tablename__ = "concept_graph_versions"
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    saved_by = Column(UUID, nullable=False)
    version_number = Column(Integer)
    saved_at = Column(TIMESTAMP, default=datetime.utcnow)
    graph_json = Column(JSONB)

