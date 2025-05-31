from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.role import RoleCreate, RoleRead
from app.crud import role as crud_role
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=RoleRead)
async def create_role(role_in: RoleCreate, db: AsyncSession = Depends(get_db)):
    return await crud_role.create_role(db, role_in)

@router.post("/assign/")
async def assign_role(user_id: UUID, role_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud_role.assign_role(db, user_id, role_id)
    return {"message": "Role assigned"}

@router.get("/", response_model=list[RoleRead])
async def list_roles(db: AsyncSession = Depends(get_db)):
    return await crud_role.get_roles(db)

