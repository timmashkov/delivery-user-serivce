from typing import List, TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models import _Base

if TYPE_CHECKING:
    from infrastructure.database.models.role import Role


class User(_Base):

    username: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
        comment="Username пользователя",
    )
    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
        index=True,
        comment="Email пользователя",
    )
    age: Mapped[int] = mapped_column(
        Integer,
        unique=False,
        nullable=False,
        comment="Возраст пользователя",
    )
    phone_number: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
        comment="Телефонный номер пользователя",
    )

    roles: Mapped[List["Role"]] = relationship(
        secondary="user_roles",
        back_populates="users",
        lazy="noload",
    )
