from typing import Iterable

from infrastructure.database.database_gateway import DatabaseGateway
from infrastructure.database.models import Role
from infrastructure.database.repositories._base._base_read_repository import \
    _BaseReadRepository
from infrastructure.database.repositories._base._base_write_repository import \
    _BaseWriteRepository


class RoleReadRepository(_BaseReadRepository):
    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self._session = database_gateway.autocommit_session
        self._model: type[Role] = Role

    async def get_role(self, role_uuid) -> Role | None:
        return await self._get_object_by_uuid(role_uuid)

    async def get_roles(self) -> Iterable[Role]:
        return await self._get_all_objects()


class RoleWriteRepository(_BaseWriteRepository):
    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self._session = database_gateway.transactional_session
        self._model: type[Role] = Role

    async def create_role(self, **kwargs) -> Role | None:
        return await self._create_object(**kwargs)

    async def update_role(self, **kwargs) -> Role | None:
        return await self._update_object(**kwargs)

    async def delete_role(self, role_uuid) -> Role | None:
        return await self._delete_object(role_uuid)
