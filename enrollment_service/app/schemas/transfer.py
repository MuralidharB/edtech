from pydantic import BaseModel, UUID4
from datetime import date

class TransferRequest(BaseModel):
    new_grade_id: UUID4
    new_section_id: UUID4
    transfer_date: date

