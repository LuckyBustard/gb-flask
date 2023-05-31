from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForPatch,
)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user
from models.article import Article


class ArticlePermission(PermissionMixin):
    PATCH_AVAILABLE_FIELDS = [
        "title",
        "body",
    ]

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(self, *args, data: dict = None, obj: Article = None, user_permission: PermissionUser = None, **kwargs) -> dict:
        if current_user.is_staff != True or current_user.id != obj.author.user.id:
            raise AccessDenied('You not author')

        permission_for_patch = user_permission.permission_for_patch_permission(model=Article)

        return {
            i_key: i_val
            for i_key, i_val in data.items()
            if i_key in permission_for_patch.columns
        }
