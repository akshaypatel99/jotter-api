"""Add content column to posts table

Revision ID: f6c3f3572af4
Revises: 7bb1c8bcd562
Create Date: 2023-03-31 13:42:43.572415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6c3f3572af4'
down_revision = '7bb1c8bcd562'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
