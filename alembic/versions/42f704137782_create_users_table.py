"""create users table

Revision ID: 42f704137782
Revises: 234aa331c013
Create Date: 2022-06-14 21:46:56.114789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42f704137782'
down_revision = '234aa331c013'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(),nullable=False),
                    sa.Column('email', sa.String(),nullable=False),
                    sa.Column('password', sa.String(),nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
