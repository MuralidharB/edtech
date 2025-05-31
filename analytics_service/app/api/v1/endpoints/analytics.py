from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.analytics import AnalyticMetricCreate, AnalyticMetric
from app.crud.analytics import create_metric, get_metrics_by_student
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=AnalyticMetric)
def add_metric(metric: AnalyticMetricCreate, db: Session = Depends(get_db)):
    return create_metric(db, metric)

@router.get("/student/{student_id}", response_model=List[AnalyticMetric])
def get_student_metrics(student_id: str, db: Session = Depends(get_db)):
    return get_metrics_by_student(db, student_id)

