from typing import Iterable, Type, TypeVar
from uuid import UUID

from sqlalchemy import delete, insert, update
from sqlalchemy.ext.asyncio import async_sessionmaker

from infrastructure.database.models import _Base


class _BaseWriteRepository:

    _session: async_sessionmaker
    _model: type[_Base]

    async def _create_object(self, **kwargs) -> _model | None:
        async with self._session() as session:
            query = insert(self._model).values(**kwargs).returning(self._model)
            query = await session.execute(query)
            await session.commit()
        return query.scalar_one_or_none()

    async def _update_object(self, **kwargs) -> _model | None:
        async with self._session() as session:
            query = (
                update(self._model)
                .where(self._model.uuid == kwargs.get("uuid"))
                .values(**kwargs)
                .returning(self._model)
            )
            query = await session.execute(query)
            await session.commit()
        return query.scalar_one_or_none()

    async def _delete_object(self, uuid: UUID) -> _model | None:
        async with self._session() as session:
            query = (
                delete(self._model)
                .where(self._model.uuid == uuid)
                .returning(self._model)
            )
            query = await session.execute(query)
            await session.commit()
        return query.scalar_one_or_none()
