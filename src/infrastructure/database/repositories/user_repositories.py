from typing import Iterable
from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import delete, insert, select
from sqlalchemy.orm import joinedload

from infrastructure.database.database_gateway import DatabaseGateway
from infrastructure.database.models import User, UserRole, Role
from infrastructure.database.repositories._base._base_read_repository import \
    _BaseReadRepository
from infrastructure.database.repositories._base._base_write_repository import \
    _BaseWriteRepository


class UserReadRepository(_BaseReadRepository):
    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self._session = database_gateway.autocommit_session
        self._model: type[User] = User
        self._query_modifier = self.__apply_user_joins

    @staticmethod
    def __apply_user_joins(query: type[select]) -> type[select]:
        return query.options(joinedload(User.roles).joinedload(Role.permissions))

    async def get_user(self, user_uuid: UUID) -> User | None:
        return await self._get_object_by_uuid(user_uuid)

    async def get_users(self, filters: Filter | None = None) -> Iterable[User]:
        return await self._get_all_objects(filters)


class UserWriteRepository(_BaseWriteRepository):
    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self._session = database_gateway.transactional_session
        self._model: type[User] = User

    async def create_user(self, **kwargs) -> User | None:
        return await self._create_object(**kwargs)

    async def update_user(self, **kwargs) -> User | None:
        return await self._update_object(**kwargs)

    async def delete_user(self, user_uuid: UUID) -> User | None:
        return await self._delete_object(user_uuid)
