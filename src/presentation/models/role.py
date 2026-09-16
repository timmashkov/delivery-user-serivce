from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from infrastructure.database.models import Role
from presentation.models.patched_filter import PatchedFilter
from presentation.models.permission import ReadPermissionModel


class CreateRoleModel(BaseModel):
    name: str = Field(description=Role.name.comment)
    data: Optional[dict] = Field(description=Role.data.comment)


class ReadRoleModel(CreateRoleModel):
    uuid: UUID = Field(description=Role.uuid.comment)
    created_at: datetime = Field(description=Role.created_at.comment)
    updated_at: datetime = Field(description=Role.updated_at.comment)
    permissions: list[ReadPermissionModel] = Field(default_factory=list)


class RoleFilter(PatchedFilter):
    uuid: Optional[UUID] = None
    name: Optional[str] = None

    class Constants(PatchedFilter.Constants):
        model = Role
