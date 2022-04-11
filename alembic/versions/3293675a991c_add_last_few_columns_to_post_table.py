"""add last few columns to post table

Revision ID: 3293675a991c
Revises: 25300d22fe2c
Create Date: 2022-04-11 16:39:24.577102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3293675a991c'
down_revision = '25300d22fe2c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'
    ),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
    ('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
