"""create tasks, tags, association_table

Revision ID: 3f6add627794
Revises: 
Create Date: 2024-08-27 00:37:51.705633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f6add627794'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tags')),
    sa.UniqueConstraint('name', name=op.f('uq_tags_name'))
    )
    op.create_table('tasks',
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('published_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tasks'))
    )
    op.create_table('tasks_tags_association',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name=op.f('fk_tasks_tags_association_tag_id_tags')),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], name=op.f('fk_tasks_tags_association_task_id_tasks')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tasks_tags_association')),
    sa.UniqueConstraint('task_id', 'tag_id', name=op.f('uq_tasks_tags_association_task_id'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks_tags_association')
    op.drop_table('tasks')
    op.drop_table('tags')
    # ### end Alembic commands ###
