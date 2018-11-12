"""empty message

Revision ID: e56c2ffb4c49
Revises: 5da77f3ada51
Create Date: 2018-11-12 08:18:00.714974

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e56c2ffb4c49'
down_revision = '5da77f3ada51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=128), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', mysql.VARCHAR(collation=u'utf8mb4_unicode_ci', length=128), nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
