from dishka import Provider, Scope, provide

from application.use_cases import PermissionUseCases, RoleUseCases, UserUseCases
from infrastructure.database import UnitOfWork


class UseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_user_use_cases(
            self,
            unit_of_work: UnitOfWork,
    ) -> UserUseCases:
        return UserUseCases(unit_of_work)

    @provide(scope=Scope.REQUEST)
    def provide_perm_use_cases(self, unit_of_work: UnitOfWork) -> PermissionUseCases:
        return PermissionUseCases(unit_of_work)

    @provide(scope=Scope.REQUEST)
    def provide_role_use_cases(self, unit_of_work: UnitOfWork) -> RoleUseCases:
        return RoleUseCases(unit_of_work)
