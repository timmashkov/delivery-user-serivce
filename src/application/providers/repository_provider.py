from dishka import Provider, Scope, provide

from infrastructure.database import (DatabaseGateway, PermissionReadRepository,
                                     PermissionWriteRepository,
                                     RoleReadRepository, RoleWriteRepository,
                                     UserReadRepository, UserWriteRepository)


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

    @provide(scope=Scope.REQUEST)
    def provide_role_read_repository(
        self, database_adapter: DatabaseGateway
    ) -> RoleReadRepository:
        return RoleReadRepository(database_adapter)

    @provide(scope=Scope.REQUEST)
    def provide_role_write_repository(
        self, database_adapter: DatabaseGateway
    ) -> RoleWriteRepository:
        return RoleWriteRepository(database_adapter)

    @provide(scope=Scope.REQUEST)
    def provide_permission_read_repository(
        self, database_adapter: DatabaseGateway
    ) -> PermissionReadRepository:
        return PermissionReadRepository(database_adapter)

    @provide(scope=Scope.REQUEST)
    def provide_permission_write_repository(
        self, database_adapter: DatabaseGateway
    ) -> PermissionWriteRepository:
        return PermissionWriteRepository(database_adapter)
