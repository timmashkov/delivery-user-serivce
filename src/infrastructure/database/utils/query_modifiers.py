from sqlalchemy import select
from sqlalchemy.orm import joinedload

from infrastructure.database.models.user import User
from infrastructure.database.models.role import Role


def user_query_modifier(query: type[select]) -> type[select]:
    return query.options(joinedload(User.roles).joinedload(Role.permissions))
