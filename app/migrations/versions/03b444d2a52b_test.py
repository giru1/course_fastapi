"""test

Revision ID: 03b444d2a52b
Revises: 517a1c120da9
Create Date: 2023-07-10 15:53:15.576011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03b444d2a52b'
down_revision = '517a1c120da9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contractors', 'hide')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contractors', sa.Column('hide', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
