from sqlalchemy import Column, Integer, String, JSON
from app.db.base import Base

class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    rule_id = Column(String, unique=True, nullable=False)
    scope = Column(String, index=True)
    conditions = Column(JSON, nullable=False)
    action = Column(JSON, nullable=False)

