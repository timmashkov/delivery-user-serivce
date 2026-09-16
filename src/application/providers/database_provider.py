from dishka import Provider, Scope, provide

from application.config import Settings
from infrastructure.database import DatabaseGateway


class DatabaseProvider(Provider):
    scope = Scope.APP

    @provide(scope=Scope.APP)
    def provide_database(self, settings: Settings) -> DatabaseGateway:
        return DatabaseGateway(
            host=settings.postgres_host,
            port=settings.postgres_port,
            dialect=settings.postgres_dialect,
            login=settings.postgres_login,
            password=settings.postgres_password,
            database=settings.postgres_database,
            echo=settings.postgres_echo,
        )
