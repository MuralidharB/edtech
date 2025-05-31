from fastapi import APIRouter, Depends
from app.schemas.parent_student_link import ParentStudentLinkCreate, ParentStudentLinkRead
from app.crud import parent_student_link as crud_link
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=ParentStudentLinkRead)
async def link_parent_student(link_in: ParentStudentLinkCreate, db: AsyncSession = Depends(get_db)):
    return await crud_link.create_link(db, link_in)

@router.get("/parent/{parent_id}", response_model=list[ParentStudentLinkRead])
async def get_children(parent_id: UUID, db: AsyncSession = Depends(get_db)):
    return await crud_link.get_links_for_parent(db, parent_id)

