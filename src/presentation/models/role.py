from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CreateRoleModel(BaseModel):
    name: str
    data: dict | None


class ReadRoleModel(CreateRoleModel):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
