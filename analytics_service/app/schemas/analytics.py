from pydantic import BaseModel
from datetime import date
from typing import List

class AnalyticMetricBase(BaseModel):
    student_id: str
    metric_name: str
    value: float
    date: date

class AnalyticMetricCreate(AnalyticMetricBase):
    pass

class AnalyticMetric(AnalyticMetricBase):
    id: int

    class Config:
        orm_mode = True

