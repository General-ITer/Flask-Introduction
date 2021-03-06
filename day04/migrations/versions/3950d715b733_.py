"""empty message

Revision ID: 3950d715b733
Revises: 
Create Date: 2018-11-15 09:46:16.019948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3950d715b733'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=30), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_news_title'), 'news', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_news_title'), table_name='news')
    op.drop_table('news')
    # ### end Alembic commands ###
