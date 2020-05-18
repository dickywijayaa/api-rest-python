"""Create table Todos

Revision ID: a3fd2853a3f4
Revises: aaaf8878d19e
Create Date: 2020-05-18 10:41:53.729190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3fd2853a3f4'
down_revision = 'aaaf8878d19e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('todo', sa.String(length=140), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todos_created_at'), 'todos', ['created_at'], unique=False)
    op.create_index(op.f('ix_todos_updated_at'), 'todos', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todos_updated_at'), table_name='todos')
    op.drop_index(op.f('ix_todos_created_at'), table_name='todos')
    op.drop_table('todos')
    # ### end Alembic commands ###
