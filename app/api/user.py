from flask_combo_jsonapi import ResourceDetail, ResourceList
from schemas.user import UserSchema
from models.database import db
from models.user import User
from permissions.user import UserPermission


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_get": [UserPermission],
    }
