from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from infrastructure.database.models import User
from presentation.models.patched_filter import PatchedFilter
from .role import ReadRoleModel


class CreateUserModel(BaseModel):
    username: str = Field(description=User.username.comment)
    age: int = Field(description=User.age.comment)
    email: EmailStr = Field(description=User.email.comment)
    phone_number: str = Field(description=User.phone_number.comment)
    data: dict | None = Field(description=User.data.comment)


class ReadUserModel(CreateUserModel):
    uuid: UUID = Field(description=User.uuid.comment)
    created_at: datetime = Field(description=User.created_at.comment)
    updated_at: datetime = Field(description=User.updated_at.comment)
    roles: list[ReadRoleModel] | None = Field(default_factory=list)


class CreateRolesToUser(BaseModel):
    user_uuid: UUID = Field(description=User.uuid.comment)
    role_uuids: list[UUID] = Field(default_factory=list, description=User.uuid.comment)


class UserFilter(PatchedFilter):
    uuid: UUID | None = None
    username: str | None = None
    age: int | None = None
    phone_number: str | None = None
    email: EmailStr | None = None

    class Constants(PatchedFilter.Constants):
        model = User
