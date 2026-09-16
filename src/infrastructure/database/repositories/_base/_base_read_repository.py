from typing import Iterable, Type, Callable
from uuid import UUID
from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from infrastructure.database.models import _Base


class _BaseReadRepository:

    _session: async_sessionmaker
    _model: type[_Base]
    _query_modifier: Callable[[select], select] | None

    def _get_query(self) -> Type[select]:
        query = select(self._model)
        if self._query_modifier:
            print(self._query_modifier)
            query = self._query_modifier(query)
        return query

    @classmethod
    def __set_filter(cls, query: select, filters: Filter = None) -> select:
        if filters:
            query = filters.filter(query)
        return query

    async def _get_object_by_uuid(self, uuid: UUID) -> _model | None:
        async with self._session() as session:
            query = self._get_query().where(self._model.uuid == uuid)
            query = await session.execute(query)
        return query.unique().scalar_one_or_none()

    async def _get_all_objects(self, filters: Filter = None) -> Iterable[_model] | Iterable:
        async with self._session() as session:
            query = self._get_query()
            query = self.__set_filter(query, filters)
            query = await session.execute(query)
        return query.unique().scalars().all()
