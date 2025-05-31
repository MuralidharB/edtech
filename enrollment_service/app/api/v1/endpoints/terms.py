# app/api/v1/endpoints/terms.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.term import TermCreate, TermOut
from app.crud import term as crud

router = APIRouter()

@router.post("/", response_model=TermOut)
def create_term(payload: TermCreate, db: Session = Depends(get_db)):
    return crud.create_term(db, payload)

@router.get("/{term_id}", response_model=TermOut)
def get_term(term_id: str, db: Session = Depends(get_db)):
    term = crud.get_term(db, term_id)
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")
    return term

@router.get("/", response_model=list[TermOut])
def list_terms(db: Session = Depends(get_db)):
    return crud.list_terms(db)

