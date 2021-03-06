"""followers

Revision ID: 893b3d867903
Revises: 0d567e641a30
Create Date: 2018-09-13 10:10:12.727239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '893b3d867903'
down_revision = '0d567e641a30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
