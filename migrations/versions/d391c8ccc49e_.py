"""empty message

Revision ID: d391c8ccc49e
Revises: 
Create Date: 2019-06-29 19:07:46.444710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd391c8ccc49e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stima',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=100), nullable=True),
    sa.Column('imageurl', sa.String(length=100), nullable=True),
    sa.Column('date', sa.String(length=100), nullable=True),
    sa.Column('cost', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('stima')
    # ### end Alembic commands ###