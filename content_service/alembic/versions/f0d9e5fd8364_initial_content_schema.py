"""Initial content  schema

Revision ID: f0d9e5fd8364
Revises: 
Create Date: 2025-05-31 18:56:04.197356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0d9e5fd8364'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contents',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('file_url', sa.String(), nullable=False),
    sa.Column('uploaded_by', sa.UUID(), nullable=False),
    sa.Column('tags', sa.String(), nullable=True),
    sa.Column('locale', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contents')
    # ### end Alembic commands ###
