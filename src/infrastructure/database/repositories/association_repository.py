from uuid import UUID

from sqlalchemy import delete, insert

from infrastructure.database import DatabaseGateway
from infrastructure.database.models import UserRole


class AssociationRepository:

    def __init__(self, database_gateway: DatabaseGateway) -> None:
        self._session = database_gateway.transactional_session
        self._user_role_model = UserRole

    async def assign_roles_to_user(
        self, user_uuid: UUID, roles: list[dict[str, UUID | None]]
    ) -> UserRole:
        async with self._session() as session:
            await session.execute(
                delete(UserRole).where(UserRole.user_uuid == user_uuid)
            )
            query = insert(UserRole).values(roles).returning(UserRole)
            query = await session.execute(query)
            await session.commit()
        return query.scalar_one_or_none()
