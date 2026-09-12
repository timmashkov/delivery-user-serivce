from uuid import UUID


class UserUseCases:
    def __init__(self, read_repository, write_repository) -> None:
        self.read_repository = read_repository
        self.write_repository = write_repository

    async def get_users_list(self) -> list:
        return await self.read_repository.get_users()

    async def read_single_user(self, user_uuid: UUID):
        return await self.read_repository.get_user(user_uuid)

    async def create_new_user(self, **kwargs):
        result = await self.write_repository.create_user(**kwargs)
        return result

    async def update_user(self, **kwargs):
        uuid = kwargs.pop("user_uuid")
        return await self.write_repository.update_user(**kwargs, uuid=uuid)

    async def delete_user(self, user_uuid: UUID):
        return await self.write_repository.delete_user(user_uuid)
