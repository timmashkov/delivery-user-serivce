from dishka import Provider, Scope, provide

from infrastructure.database import (DatabaseGateway, UserReadRepository,
                                     UserWriteRepository)


class UserRepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_user_read_repository(
        self, database_adapter: DatabaseGateway
    ) -> UserReadRepository:
        return UserReadRepository(database_adapter)

    @provide(scope=Scope.REQUEST)
    def provide_user_write_repository(
        self, database_adapter: DatabaseGateway
    ) -> UserWriteRepository:
        return UserWriteRepository(database_adapter)
