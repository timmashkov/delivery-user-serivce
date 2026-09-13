from dishka import Provider, Scope, provide

from application.use_cases import UserUseCases
from infrastructure.database import UserReadRepository, UserWriteRepository


class UseCaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_user_use_cases(
        self, read_repository: UserReadRepository, write_repository: UserWriteRepository
    ) -> UserUseCases:
        return UserUseCases(read_repository, write_repository)
