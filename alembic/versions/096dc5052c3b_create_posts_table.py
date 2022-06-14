"""create posts table

Revision ID: 096dc5052c3b
Revises: 
Create Date: 2022-06-14 21:36:12.724028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '096dc5052c3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', 
    sa.Column('id', sa.Integer(),nullable=False, primary_key=True),
    sa.Column('title', sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
