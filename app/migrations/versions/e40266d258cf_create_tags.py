"""create tags

Revision ID: e40266d258cf
Revises: 491a840a6212
Create Date: 2023-05-19 18:12:47.960083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e40266d258cf'
down_revision = '491a840a6212'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    tag = op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article_tag_association',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )

    op.bulk_insert(tag, [
        {'name': "flask"},
        {'name': "django"},
        {'name': "python"},
        {'name': "sqlalchemy"},
        {'name': "news"},
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_tag_association')
    op.drop_table('tag')
    # ### end Alembic commands ###