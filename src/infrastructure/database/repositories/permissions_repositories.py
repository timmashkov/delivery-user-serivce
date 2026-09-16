from typing import Iterable

from fastapi_filter.contrib.sqlalchemy import Filter

from infrastructure.database.database_gateway import DatabaseGateway
from infrastructure.database.models import Permission
from infrastructure.database.repositories._base._base_read_repository import \
    _BaseReadRepository
from infrastructure.database.repositories._base._base_write_repository import \
    _BaseWriteRepository


class PermissionReadRepository(_BaseReadRepository):
    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self._session = database_gateway.autocommit_session
        self._model: type[Permission] = Permission

    async def get_permission(self, permission_uuid) -> Permission | None:
        return await self._get_object_by_uuid(permission_uuid)

    async def get_permissions(
        self, filters: Filter | None = None
    ) -> Iterable[Permission]:
        return await self._get_all_objects(filters)


class PermissionWriteRepository(_BaseWriteRepository):
    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self._session = database_gateway.transactional_session
        self._model: type[Permission] = Permission

    async def create_permission(self, **kwargs) -> Permission | None:
        return await self._create_object(**kwargs)

    async def update_permission(self, **kwargs) -> Permission | None:
        return await self._update_object(**kwargs)

    async def delete_permission(self, permission_uuid) -> Permission | None:
        return await self._delete_object(permission_uuid)
