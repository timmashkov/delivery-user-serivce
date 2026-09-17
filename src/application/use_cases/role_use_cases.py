from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter

from infrastructure.database import RepositoryMixin, UnitOfWork, Role


class RoleUseCases(RepositoryMixin):
    def __init__(self, unit_of_work: UnitOfWork) -> None:
        self._unit_of_work = unit_of_work
        self._model = Role

    async def get_roles_list(self, filters: Filter) -> list:
        async with self.read_repository() as read_repository:
            roles_list = await read_repository.get_all_objects(filters)
        return [role for role in roles_list]

    async def read_single_role(self, role_uuid: UUID):
        async with self.read_repository() as read_repository:
            return await read_repository.get_object_by_uuid(role_uuid)

    async def create_new_role(self, **kwargs):
        async with self.write_repository() as write_repository:
            return await write_repository.create_object(**kwargs)

    async def update_role(self, **kwargs):
        uuid = kwargs.pop("role_uuid")
        async with self.write_repository() as write_repository:
            return await write_repository.update_object(**kwargs, uuid=uuid)

    async def delete_role(self, role_uuid: UUID):
        async with self.write_repository() as write_repository:
            return await write_repository.delete_object(role_uuid)
