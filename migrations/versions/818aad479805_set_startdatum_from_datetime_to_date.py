"""Set startDatum from DateTime to Date

Revision ID: 818aad479805
Revises: 7694fbc4965d
Create Date: 2024-03-19 14:04:44.651253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '818aad479805'
down_revision = '7694fbc4965d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lessen', schema=None) as batch_op:
        batch_op.alter_column('startDatum',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lessen', schema=None) as batch_op:
        batch_op.alter_column('startDatum',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
