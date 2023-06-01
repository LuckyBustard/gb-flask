"""seed admin user

Revision ID: db24fa130b1c
Revises: c35b1c241b17
Create Date: 2023-05-05 11:08:59.191513

"""
import sqlalchemy as sa
from models.user import User


# revision identifiers, used by Alembic.
revision = 'db24fa130b1c'
down_revision = 'c35b1c241b17'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
