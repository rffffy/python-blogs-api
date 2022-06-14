"""add last few columns to posts table

Revision ID: 628e0dec75ee
Revises: 1599a9445429
Create Date: 2022-06-14 22:00:47.656811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '628e0dec75ee'
down_revision = '1599a9445429'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
