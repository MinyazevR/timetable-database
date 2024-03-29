"""empty message

Revision ID: 3aa86c6ba8f5
Revises: 19a45a816af3
Create Date: 2023-09-15 20:10:31.836276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aa86c6ba8f5'
down_revision = '19a45a816af3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Classroom',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('oid', sa.String(length=40), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('seating_type', sa.Integer(), nullable=True),
    sa.Column('additional_info', sa.String(length=300), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['Address.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('oid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Classroom')
    # ### end Alembic commands ###
