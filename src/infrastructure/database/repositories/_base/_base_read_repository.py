from typing import Iterable, Type, TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from infrastructure.database.models import _Base


class _BaseReadRepository:

    _session: async_sessionmaker
    _model: type[_Base]

    def _get_query(self) -> Type[select]:
        query = select(self._model)
        return query

    async def _get_object_by_uuid(self, uuid: UUID) -> _model | None:
        async with self._session() as session:
            query = self._get_query().where(self._model.uuid == uuid)
            query = await session.execute(query)
        return query.unique().scalar_one_or_none()

    async def _get_all_objects(self) -> Iterable[_model] | Iterable:
        async with self._session() as session:
            query = self._get_query()
            query = await session.execute(query)
        return query.unique().scalars().all()
