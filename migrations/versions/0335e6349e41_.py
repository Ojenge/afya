"""empty message

Revision ID: 0335e6349e41
Revises: e75d186ea631
Create Date: 2016-05-30 12:44:42.595178

"""

# revision identifiers, used by Alembic.
revision = '0335e6349e41'
down_revision = 'e75d186ea631'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('timestamp', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'timestamp')
    ### end Alembic commands ###
