from pydantic import BaseModel
from typing import List, Optional, Any

class Condition(BaseModel):
    field: str
    operator: str
    value: Any

class Action(BaseModel):
    type: str
    parameters: Optional[dict] = None

class RuleBase(BaseModel):
    rule_id: str
    scope: Optional[str]
    conditions: List[Condition]
    action: Action

class RuleCreate(RuleBase):
    pass

class Rule(RuleBase):
    id: int

    class Config:
        orm_mode = True

class RuleEvalRequest(BaseModel):
    rule_id: str
    input: dict

class RuleEvalResponse(BaseModel):
    result: bool
    action: Optional[Action]
    message: Optional[str]

