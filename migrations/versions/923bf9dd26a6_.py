"""empty message

Revision ID: 923bf9dd26a6
Revises: 63abb0f81ad8
Create Date: 2016-06-03 13:31:49.077455

"""

# revision identifiers, used by Alembic.
revision = '923bf9dd26a6'
down_revision = '63abb0f81ad8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dialogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('dialogid', sa.String(length=120), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dialogid'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dialogs')
    ### end Alembic commands ###