"""empty message

Revision ID: 3cdfe2d806f8
Revises: 3b3917ea1e0e
Create Date: 2021-05-09 12:07:02.231068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cdfe2d806f8'
down_revision = '3b3917ea1e0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('product_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'product_id')
    # ### end Alembic commands ###
