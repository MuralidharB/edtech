from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.rule import RuleCreate, RuleEvalRequest, RuleEvalResponse
from app.crud import rule as crud_rule

router = APIRouter()

@router.post("/", response_model=dict)
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    return crud_rule.create_rule(db, rule)

@router.post("/evaluate", response_model=RuleEvalResponse)
def evaluate_rule(data: RuleEvalRequest, db: Session = Depends(get_db)):
    db_rule = crud_rule.get_rule_by_id(db, data.rule_id)
    if not db_rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    result = all(
        eval(f"{repr(data.input.get(c['field']))} {c['operator']} {repr(c['value'])}")
        for c in db_rule.conditions
    )

    return RuleEvalResponse(
        result=result,
        action=db_rule.action if result else None,
        message="Rule matched" if result else "Rule did not match"
    )

@router.get("/", response_model=list)
def list_rules(db: Session = Depends(get_db)):
    return crud_rule.list_rules(db)

