from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class CreateUserModel(BaseModel):
    username: str
    age: int
    email: EmailStr
    phone_number: str
    data: dict | None


class ReadUserModel(CreateUserModel):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
