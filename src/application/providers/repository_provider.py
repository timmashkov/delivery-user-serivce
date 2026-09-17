from dishka import Provider, Scope, provide

from infrastructure.database import DatabaseGateway, AssociationRepository


class RepositoryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_repository(self, database_gateway: DatabaseGateway) -> AssociationRepository:
        return AssociationRepository(database_gateway)
