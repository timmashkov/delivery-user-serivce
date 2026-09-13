from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CreatePermissionModel(BaseModel):
    name: str
    layer: str
    data: dict | None


class ReadPermissionModel(CreatePermissionModel):
    uuid: UUID
    created_at: datetime
    updated_at: datetime
