"""empty message

Revision ID: 73893a0f7358
Revises: 865c1efd354a
Create Date: 2017-02-23 03:49:21.184268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73893a0f7358'
down_revision = '865c1efd354a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
