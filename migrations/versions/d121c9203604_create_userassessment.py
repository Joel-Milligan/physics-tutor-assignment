"""Create userassessment

Revision ID: d121c9203604
Revises: e5e340a30c4c
Create Date: 2021-05-14 20:37:47.818321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd121c9203604'
down_revision = 'e5e340a30c4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_assessment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('assessment_id', sa.Integer(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('correct', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['assessment_id'], ['assessment.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_assessment')
    # ### end Alembic commands ###