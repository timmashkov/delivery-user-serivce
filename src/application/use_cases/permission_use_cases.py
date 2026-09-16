from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter

from infrastructure.database import (PermissionReadRepository,
                                     PermissionWriteRepository)


class PermissionUseCases:
    def __init__(
        self,
        read_repository: PermissionReadRepository,
        write_repository: PermissionWriteRepository,
    ) -> None:
        self.read_repository = read_repository
        self.write_repository = write_repository

    async def get_permissions_list(self, filters: Filter) -> list:
        permissions_list = await self.read_repository.get_permissions(filters)
        return [permission for permission in permissions_list]

    async def read_single_permission(self, permission_uuid: UUID):
        return await self.read_repository.get_permission(permission_uuid)

    async def create_new_permission(self, **kwargs):
        return await self.write_repository.create_permission(**kwargs)

    async def update_permission(self, **kwargs):
        uuid = kwargs.pop("perm_uuid")
        return await self.write_repository.update_permission(**kwargs, uuid=uuid)

    async def delete_permission(self, permission_uuid: UUID):
        return await self.write_repository.delete_permission(permission_uuid)
