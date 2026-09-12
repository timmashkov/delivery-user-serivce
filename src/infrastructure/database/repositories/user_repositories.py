from typing import Iterable

from infrastructure.database.database_gateway import DatabaseGateway
from infrastructure.database.models import User
from infrastructure.database.repositories._base._base_read_repository import \
    _BaseReadRepository
from infrastructure.database.repositories._base._base_write_repository import \
    _BaseWriteRepository


class UserReadRepository(_BaseReadRepository):
    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self._session = database_gateway.autocommit_session
        self._model: type[User] = User

    async def get_user(self, user_uuid) -> User | None:
        return await self._get_object_by_uuid(user_uuid)

    async def get_users(self) -> Iterable[User]:
        return await self._get_all_objects()


class UserWriteRepository(_BaseWriteRepository):
    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self._session = database_gateway.transactional_session
        self._model: type[User] = User

    async def create_user(self, **kwargs) -> User | None:
        return await self._create_object(**kwargs)

    async def update_user(self, **kwargs) -> User | None:
        return await self._update_object(**kwargs)

    async def delete_user(self, user_uuid) -> User | None:
        return await self._delete_object(user_uuid)
