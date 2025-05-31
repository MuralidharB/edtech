from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.parent_student_link import ParentStudentLink
from app.schemas.parent_student_link import ParentStudentLinkCreate

async def create_link(db: AsyncSession, link_in: ParentStudentLinkCreate) -> ParentStudentLink:
    link = ParentStudentLink(parent_id=link_in.parent_id, student_id=link_in.student_id)
    db.add(link)
    await db.commit()
    await db.refresh(link)
    return link

async def get_links_for_parent(db: AsyncSession, parent_id) -> list[ParentStudentLink]:
    result = await db.execute(
        select(ParentStudentLink).where(ParentStudentLink.parent_id == parent_id)
    )
    return result.scalars().all()

