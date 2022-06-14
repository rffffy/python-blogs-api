"""add foreign key to posts table

Revision ID: 1599a9445429
Revises: 42f704137782
Create Date: 2022-06-14 21:55:59.294064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1599a9445429'
down_revision = '42f704137782'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk',source_table='posts', referent_table='users',
    local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')

    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
