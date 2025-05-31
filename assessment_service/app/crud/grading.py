from sqlalchemy.orm import Session
from app.db.models.grading import GradingEntry
from app.schemas.grading import GradingEntryCreate

def create_grading_entry(db: Session, entry: GradingEntryCreate) -> GradingEntry:
    db_entry = GradingEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_grading_entry(db: Session, entry_id: str) -> GradingEntry:
    return db.query(GradingEntry).filter(GradingEntry.id == entry_id).first()

def list_grading_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GradingEntry).offset(skip).limit(limit).all()

def delete_grading_entry(db: Session, entry_id: str):
    db_entry = db.query(GradingEntry).filter(GradingEntry.id == entry_id).first()
    if db_entry:
        db.delete(db_entry)
        db.commit()
    return db_entry

