from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter

from domain.user import UserDomainModel
from infrastructure.database import User, UnitOfWork, user_query_modifier, RepositoryMixin, AssociationRepository


class UserUseCases(RepositoryMixin):
    def __init__(self, unit_of_work: UnitOfWork) -> None:
        self._unit_of_work = unit_of_work
        self._model = User
        self._query_modifier = user_query_modifier
        self._custom_repository = AssociationRepository

    async def get_users_list(self, filters: Filter) -> list:
        async with self.read_repository() as read_repository:
            users_list = await read_repository.get_all_objects(filters)
        return [user for user in users_list]

    async def read_single_user(self, user_uuid: UUID):
        async with self.read_repository() as read_repository:
            return await read_repository.get_object_by_uuid(user_uuid)

    async def create_new_user(self, **kwargs):
        new_user = UserDomainModel(**kwargs)
        async with self.write_repository() as write_repository:
            return await write_repository.create_object(**new_user.to_dict())

    async def add_roles_to_user(self, **kwargs):
        user_uuid, role_uuids = kwargs.get("user_uuid"), kwargs.get("role_uuids")
        new_roles = [{"user_uuid": user_uuid, "role_uuid": role_uuid} for role_uuid in role_uuids]
        async with self.custom_repository() as custom_repository:
            return await custom_repository.assign_roles_to_user(user_uuid, new_roles)

    async def update_user(self, **kwargs):
        uuid = kwargs.pop("user_uuid")
        async with self.write_repository() as write_repository:
            return await write_repository.update_object(**kwargs, uuid=uuid)

    async def delete_user(self, user_uuid: UUID):
        async with self.write_repository() as write_repository:
            return await write_repository.delete_object(user_uuid)
