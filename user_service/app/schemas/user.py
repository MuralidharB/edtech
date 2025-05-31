from pydantic import BaseModel, EmailStr
from typing import Optional, List
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str]
    password: Optional[str]
    is_active: Optional[bool]

class UserRead(UserBase):
    id: UUID
    roles: List[str] = []

    class Config:
        orm_mode = True

