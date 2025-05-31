from sqlalchemy.orm import Session
from app.db.models.analytic_metric import AnalyticMetric
from app.schemas.analytics import AnalyticMetricCreate

def create_metric(db: Session, metric: AnalyticMetricCreate):
    db_metric = AnalyticMetric(**metric.dict())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

def get_metrics_by_student(db: Session, student_id: str):
    return db.query(AnalyticMetric).filter(AnalyticMetric.student_id == student_id).all()

