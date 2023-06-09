"""Add users table

Revision ID: 199c87ee6e44
Revises: f6c3f3572af4
Create Date: 2023-03-31 13:47:30.927350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '199c87ee6e44'
down_revision = 'f6c3f3572af4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
