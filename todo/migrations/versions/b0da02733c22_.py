"""empty message

Revision ID: b0da02733c22
Revises: c73e2db00b81
Create Date: 2022-07-27 03:43:45.560605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0da02733c22'
down_revision = 'c73e2db00b81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'tasklist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'tasklist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
