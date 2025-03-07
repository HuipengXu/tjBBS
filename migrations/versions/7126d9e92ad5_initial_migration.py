"""initial migration

Revision ID: 7126d9e92ad5
Revises: b93258746a1f
Create Date: 2018-05-30 12:00:32.380940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7126d9e92ad5'
down_revision = 'b93258746a1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'category_id')
    # ### end Alembic commands ###
