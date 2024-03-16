"""Added Lessen and Talen

Revision ID: d9cdf3c68373
Revises: 273a9e170a5c
Create Date: 2024-03-16 18:50:37.298810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9cdf3c68373'
down_revision = '273a9e170a5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('talen',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('lessen',
    sa.Column('lesID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('docentID', sa.Integer(), nullable=True),
    sa.Column('talenID', sa.Integer(), nullable=True),
    sa.Column('startDatum', sa.DateTime(), nullable=True),
    sa.Column('locatie', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['docentID'], ['users.id'], ),
    sa.ForeignKeyConstraint(['talenID'], ['talen.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('lesID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lessen')
    op.drop_table('talen')
    # ### end Alembic commands ###
