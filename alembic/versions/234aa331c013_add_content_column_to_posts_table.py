"""add content column to posts table

Revision ID: 234aa331c013
Revises: 096dc5052c3b
Create Date: 2022-06-14 21:40:32.685446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '234aa331c013'
down_revision = '096dc5052c3b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
