from sqlalchemy.orm import Session
from app.db.models.rule import Rule
from app.schemas.rule import RuleCreate

def create_rule(db: Session, rule: RuleCreate):
    db_rule = Rule(**rule.dict())
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule

def get_rule_by_id(db: Session, rule_id: str):
    return db.query(Rule).filter(Rule.rule_id == rule_id).first()

def list_rules(db: Session):
    return db.query(Rule).all()

