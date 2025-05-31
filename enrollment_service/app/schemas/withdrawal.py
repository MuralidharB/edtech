from pydantic import BaseModel
from datetime import date

class WithdrawalRequest(BaseModel):
    exit_date: date
    reason_for_exit: str

