"""set password for admin

Revision ID: c3f232e8931e
Revises: 8d01cc56fa2e
Create Date: 2023-05-07 17:58:26.212794

"""
import sqlalchemy as sa
from models.user import User
from models.database import db


# revision identifiers, used by Alembic.
revision = 'c3f232e8931e'
down_revision = '8d01cc56fa2e'
branch_labels = None
depends_on = None


def upgrade():
    user = User.query.filter_by(username='admin').one_or_none()
    if user is None:
        user = User(username="admin", is_staff=True)
    user.password = '1234'
    db.session.add(user)
    db.session.commit()


def downgrade():
    pass
