"""empty message

Revision ID: aecfaa52f69f
Revises: 
Create Date: 2019-06-25 23:21:07.852930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aecfaa52f69f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaign_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile', sa.String(), nullable=True),
    sa.Column('campaign_text', sa.String(), nullable=True),
    sa.Column('campaign_start', sa.DateTime(timezone=True), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=True),
    sa.Column('project_code', sa.String(), nullable=True),
    sa.Column('row', sa.Integer(), nullable=True),
    sa.Column('section', sa.String(), nullable=True),
    sa.Column('target_group', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('campaign_requests')
    # ### end Alembic commands ###
