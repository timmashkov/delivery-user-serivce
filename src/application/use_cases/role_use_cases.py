from uuid import UUID

from infrastructure.database import RoleReadRepository, RoleWriteRepository


class RoleUseCases:
    def __init__(
        self, read_repository: RoleReadRepository, write_repository: RoleWriteRepository
    ) -> None:
        self.read_repository = read_repository
        self.write_repository = write_repository

    async def get_roles_list(self) -> list:
        roles_list = await self.read_repository.get_roles()
        return [role for role in roles_list]

    async def read_single_role(self, role_uuid: UUID):
        return await self.read_repository.get_role(role_uuid)

    async def create_new_role(self, **kwargs):
        return await self.write_repository.create_role(**kwargs)

    async def update_role(self, **kwargs):
        uuid = kwargs.pop("role_uuid")
        return await self.write_repository.update_role(**kwargs, uuid=uuid)

    async def delete_role(self, role_uuid: UUID):
        return await self.write_repository.delete_role(role_uuid)
