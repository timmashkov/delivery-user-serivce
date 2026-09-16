from dishka import Provider, Scope, provide

from application.use_cases import (PermissionUseCases, RoleUseCases,
                                   UserUseCases)
from infrastructure.database import (PermissionReadRepository,
                                     PermissionWriteRepository,
                                     RoleReadRepository, RoleWriteRepository,
                                     UserReadRepository, UserWriteRepository)


class UseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_user_use_cases(
        self, read_repository: UserReadRepository, write_repository: UserWriteRepository
    ) -> UserUseCases:
        return UserUseCases(read_repository, write_repository)

    @provide(scope=Scope.REQUEST)
    def provide_perm_use_cases(
        self,
        read_repository: PermissionReadRepository,
        write_repository: PermissionWriteRepository,
    ) -> PermissionUseCases:
        return PermissionUseCases(read_repository, write_repository)

    @provide(scope=Scope.REQUEST)
    def provide_role_use_cases(
        self, read_repository: RoleReadRepository, write_repository: RoleWriteRepository
    ) -> RoleUseCases:
        return RoleUseCases(read_repository, write_repository)
