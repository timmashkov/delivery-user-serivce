from dishka import Provider, Scope, provide

from application.config import settings
from infrastructure.database import DatabaseGateway


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_database(self) -> DatabaseGateway:
        return DatabaseGateway(
            host=settings.POSTGRES.host,
            port=settings.POSTGRES.port,
            dialect=settings.POSTGRES.dialect,
            login=settings.POSTGRES.login,
            password=settings.POSTGRES.password,
            database=settings.POSTGRES.database,
            echo=settings.POSTGRES.echo,
        )
