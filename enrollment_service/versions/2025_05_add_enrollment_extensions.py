from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = '2025_05_add_enrollment_extensions'
down_revision = 'prev_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('enrollments', sa.Column('exit_date', sa.Date(), nullable=True))
    op.add_column('enrollments', sa.Column('reason_for_exit', sa.Text(), nullable=True))
    op.add_column('enrollments', sa.Column('transferred_from_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(
        'fk_transferred_from',
        'enrollments',
        'enrollments',
        ['transferred_from_id'],
        ['id'],
        ondelete='SET NULL'
    )

def downgrade():
    op.drop_constraint('fk_transferred_from', 'enrollments', type_='foreignkey')
    op.drop_column('enrollments', 'transferred_from_id')
    op.drop_column('enrollments', 'reason_for_exit')
    op.drop_column('enrollments', 'exit_date')

