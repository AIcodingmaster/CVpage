"""empty message

Revision ID: 6487bac3239c
Revises: 
Create Date: 2020-08-16 11:55:25.844649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6487bac3239c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('file_name', sa.String(length=200), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paper_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('paper_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['paper_id'], ['paper.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('paper_image')
    op.drop_table('paper')
    # ### end Alembic commands ###
