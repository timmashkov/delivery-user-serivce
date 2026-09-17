from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter

from infrastructure.database import RepositoryMixin, UnitOfWork, Permission


class PermissionUseCases(RepositoryMixin):
    def __init__(self, unit_of_work: UnitOfWork) -> None:
        self._unit_of_work = unit_of_work
        self._model = Permission

    async def get_permissions_list(self, filters: Filter) -> list:
        async with self.read_repository() as read_repository:
            permissions_list = await read_repository.get_all_objects(filters)
        return [permission for permission in permissions_list]

    async def read_single_permission(self, permission_uuid: UUID):
        async with self.read_repository() as read_repository:
            return await read_repository.get_object_by_uuid(permission_uuid)

    async def create_new_permission(self, **kwargs):
        async with self.write_repository() as write_repository:
            return await write_repository.create_object(**kwargs)

    async def update_permission(self, **kwargs):
        uuid = kwargs.pop("perm_uuid")
        async with self.write_repository() as write_repository:
            return await write_repository.update_object(**kwargs, uuid=uuid)

    async def delete_permission(self, permission_uuid: UUID):
        async with self.write_repository() as write_repository:
            return await write_repository.delete_object(permission_uuid)
