from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from models.database import db
from security import flask_bcrypt


class User(db.Model, UserMixin):
    class Meta:
        type_ = "user"
        self_view = "user_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "user_list"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    _password = Column(LargeBinary, nullable=True)
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")

    author = relationship("Author", uselist=False, back_populates="user")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, value):
        return flask_bcrypt.check_password_hash(self._password, value)
    email = Column(String(255), nullable=False, default="", server_default="")

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
