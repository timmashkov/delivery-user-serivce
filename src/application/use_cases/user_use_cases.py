from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter

from domain.user import UserDomainModel
from infrastructure.database import (AssociationRepository, UserReadRepository,
                                     UserWriteRepository)


class UserUseCases:
    def __init__(
        self,
        read_repository: UserReadRepository,
        write_repository: UserWriteRepository,
        association_repository: AssociationRepository,
    ) -> None:
        self.read_repository = read_repository
        self.write_repository = write_repository
        self.association_repository = association_repository

    async def get_users_list(self, filters: Filter) -> list:
        users_list = await self.read_repository.get_users(filters)
        return [user for user in users_list]

    async def read_single_user(self, user_uuid: UUID):
        return await self.read_repository.get_user(user_uuid)

    async def create_new_user(self, **kwargs):
        new_user = UserDomainModel(**kwargs)
        new_user.verify_phone_number()
        new_user.verify_age()
        return await self.write_repository.create_user(**new_user.to_dict())

    async def add_roles_to_user(self, **kwargs):
        user_uuid, role_uuids = kwargs.get("user_uuid"), kwargs.get("role_uuids")
        new_roles = [
            {"user_uuid": user_uuid, "role_uuid": role_uuid} for role_uuid in role_uuids
        ]
        return await self.association_repository.assign_roles_to_user(
            user_uuid, new_roles
        )

    async def update_user(self, **kwargs):
        uuid = kwargs.pop("user_uuid")
        return await self.write_repository.update_user(**kwargs, uuid=uuid)

    async def delete_user(self, user_uuid: UUID):
        return await self.write_repository.delete_user(user_uuid)
