from sqlalchemy.orm import Session
from app.db.models.result import Result
from app.schemas.result import ResultCreate

def create_result(db: Session, result: ResultCreate) -> Result:
    db_result = Result(**result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_result(db: Session, result_id: str) -> Result:
    return db.query(Result).filter(Result.id == result_id).first()

def list_results(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Result).offset(skip).limit(limit).all()

def delete_result(db: Session, result_id: str):
    db_result = db.query(Result).filter(Result.id == result_id).first()
    if db_result:
        db.delete(db_result)
        db.commit()
    return db_result

