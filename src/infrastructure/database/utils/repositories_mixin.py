from contextlib import asynccontextmanager
from typing import AsyncGenerator, Any, Callable

from sqlalchemy import select

from infrastructure.database.unit_of_work import UnitOfWork
from infrastructure.database.repositories.read_repository import ReadRepository
from infrastructure.database.repositories.write_repository import WriteRepository
from infrastructure.database.models._base import _Base


class RepositoryMixin:
    _unit_of_work: UnitOfWork
    _model: type[_Base]
    _query_modifier: Callable[[select], select] | None = None

    @asynccontextmanager
    async def read_repository(self) -> AsyncGenerator[ReadRepository, Any]:
        async with self._unit_of_work as uow:
            users = uow.repositories.read_repository(model=self._model, query_modifier=self._query_modifier)
            yield users

    @asynccontextmanager
    async def write_repository(self) -> AsyncGenerator[WriteRepository, Any]:
        async with self._unit_of_work as uow:
            users = uow.repositories.write_repository(model=self._model)
            yield users
