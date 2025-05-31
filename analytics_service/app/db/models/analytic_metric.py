from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.db.base import Base

class AnalyticMetric(Base):
    __tablename__ = "analytic_metrics"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, index=True)
    metric_name = Column(String)
    value = Column(Float)
    date = Column(Date)

