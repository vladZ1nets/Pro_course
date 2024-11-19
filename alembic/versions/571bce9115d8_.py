"""empty message

Revision ID: 571bce9115d8
Revises: 
Create Date: 2024-11-18 23:21:44.649862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '571bce9115d8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leasers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('login', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('ipn', sa.Integer(), nullable=True),
    sa.Column('full_name', sa.String(length=150), nullable=True),
    sa.Column('contacts', sa.String(length=150), nullable=True),
    sa.Column('photo', sa.String(length=150), nullable=True),
    sa.Column('passport', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ipn'),
    sa.UniqueConstraint('login')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('photo', sa.String(length=150), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('price_hour', sa.REAL(), nullable=True),
    sa.Column('price_day', sa.REAL(), nullable=True),
    sa.Column('price_week', sa.REAL(), nullable=True),
    sa.Column('price_month', sa.REAL(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('search_history',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('search_text', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contracts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('start_date', sa.String(), nullable=True),
    sa.Column('end_date', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('leaser_id', sa.Integer(), nullable=True),
    sa.Column('taker_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['leaser_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['taker_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('contract_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    op.drop_table('favorites')
    op.drop_table('contracts')
    op.drop_table('search_history')
    op.drop_table('items')
    op.drop_table('users')
    op.drop_table('leasers')
    # ### end Alembic commands ###
