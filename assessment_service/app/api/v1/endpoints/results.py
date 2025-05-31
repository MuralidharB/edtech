from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.result import ResultCreate, ResultRead
from app.crud import result as crud_result
from app.db.session import get_db

router = APIRouter(prefix="/results", tags=["results"])

@router.post("/", response_model=ResultRead)
def create_result(result: ResultCreate, db: Session = Depends(get_db)):
    return crud_result.create_result(db, result)

@router.get("/{result_id}", response_model=ResultRead)
def get_result(result_id: UUID, db: Session = Depends(get_db)):
    db_result = crud_result.get_result(db, result_id)
    if not db_result:
        raise HTTPException(status_code=404, detail="Result not found")
    return db_result

@router.get("/", response_model=list[ResultRead])
def list_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_result.list_results(db, skip=skip, limit=limit)

@router.delete("/{result_id}")
def delete_result(result_id: UUID, db: Session = Depends(get_db)):
    deleted = crud_result.delete_result(db, result_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Result not found")
    return {"detail": "Result deleted"}

