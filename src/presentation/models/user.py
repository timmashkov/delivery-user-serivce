from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from infrastructure.database.models import User
from presentation.models.patched_filter import PatchedFilter


class CreateUserModel(BaseModel):
    username:  str = Field(description=User.username.comment)
    age: int = Field(description=User.age.comment)
    email: EmailStr = Field(description=User.email.comment)
    phone_number: str = Field(description=User.phone_number.comment)
    data: dict | None = Field(description=User.data.comment)


class ReadUserModel(CreateUserModel):
    uuid: UUID = Field(description=User.uuid.comment)
    created_at: datetime = Field(description=User.created_at.comment)
    updated_at: datetime = Field(description=User.updated_at.comment)


class UserFilter(PatchedFilter):
    uuid: UUID | None = None
    first_name: str | None = None
    last_name: str | None = None
    patronymic: str | None = None
    email: EmailStr | None = None

    class Constants(PatchedFilter.Constants):
        model = User
