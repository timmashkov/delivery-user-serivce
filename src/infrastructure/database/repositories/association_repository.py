from typing import Iterable
from uuid import UUID

from sqlalchemy import delete, insert
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import DatabaseGateway
from infrastructure.database.models import UserRole


class AssociationRepository:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._user_role_model = UserRole

    async def assign_roles_to_user(self, user_uuid: UUID, roles: list[dict[str, UUID | None]]) -> Iterable[UserRole]:
        await self._session.execute(delete(UserRole).where(UserRole.user_uuid == user_uuid))
        query = insert(UserRole).values(roles).returning(UserRole)
        query = await self._session.execute(query)

        return query.unique().scalars().all()
