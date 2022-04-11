"""add content column to posts table

Revision ID: 78fea403a04a
Revises: edca08d6012f
Create Date: 2022-04-10 21:41:00.649056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78fea403a04a'
down_revision = 'edca08d6012f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
