"""empty message

Revision ID: 18a804ae6691
Revises: 827a6df1f8e2
Create Date: 2022-08-30 13:50:37.894318

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '18a804ae6691'
down_revision = '827a6df1f8e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'genres')
    op.alter_column('show', 'start_time_',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('show', 'start_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('start_time', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.alter_column('show', 'start_time_',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.add_column('artist', sa.Column('genres', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
