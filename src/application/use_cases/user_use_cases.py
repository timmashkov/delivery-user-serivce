from uuid import UUID

from fastapi_filter.contrib.sqlalchemy import Filter

from infrastructure.database import UserReadRepository, UserWriteRepository


class UserUseCases:
    def __init__(
        self, read_repository: UserReadRepository, write_repository: UserWriteRepository
    ) -> None:
        self.read_repository = read_repository
        self.write_repository = write_repository

    async def get_users_list(self, filters: Filter) -> list:
        users_list = await self.read_repository.get_users(filters)
        return [user for user in users_list]

    async def read_single_user(self, user_uuid: UUID):
        return await self.read_repository.get_user(user_uuid)

    async def create_new_user(self, **kwargs):
        return await self.write_repository.create_user(**kwargs)

    async def update_user(self, **kwargs):
        uuid = kwargs.pop("user_uuid")
        return await self.write_repository.update_user(**kwargs, uuid=uuid)

    async def delete_user(self, user_uuid: UUID):
        return await self.write_repository.delete_user(user_uuid)
