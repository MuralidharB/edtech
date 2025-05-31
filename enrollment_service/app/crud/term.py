# app/crud/term.py
from sqlalchemy.orm import Session
from app.db.models.term import AcademicTerm
from app.schemas.term import TermCreate

def create_term(db: Session, payload: TermCreate):
    term = AcademicTerm(**payload.dict())
    db.add(term)
    db.commit()
    db.refresh(term)
    return term

def get_term(db: Session, term_id):
    return db.query(AcademicTerm).filter(AcademicTerm.id == term_id).first()

def list_terms(db: Session):
    return db.query(AcademicTerm).order_by(AcademicTerm.start_date).all()

