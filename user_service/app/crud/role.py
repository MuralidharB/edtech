from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID
from app.db.models.role import Role
from app.db.models.user_role import UserRole
from app.db.models.user import User
from app.schemas.role import RoleCreate

async def create_role(db: AsyncSession, role_in: RoleCreate) -> Role:
    role = Role(name=role_in.name)
    db.add(role)
    await db.commit()
    await db.refresh(role)
    return role

async def assign_role(db: AsyncSession, user_id: UUID, role_id: UUID) -> None:
    user_role = UserRole(user_id=user_id, role_id=role_id)
    db.add(user_role)
    await db.commit()

async def get_roles(db: AsyncSession) -> list[Role]:
    result = await db.execute(select(Role))
    return result.scalars().all()

