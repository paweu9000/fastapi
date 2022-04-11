"""add foreign-key to post table

Revision ID: 25300d22fe2c
Revises: 38f4a1c25cce
Create Date: 2022-04-11 16:31:39.018343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25300d22fe2c'
down_revision = '38f4a1c25cce'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
