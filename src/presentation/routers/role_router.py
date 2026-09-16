from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi_filter import FilterDepends

from application.use_cases import RoleUseCases
from presentation.models import CreateRoleModel, ReadRoleModel, RoleFilter

role_router = APIRouter(prefix="/role", tags=["Roles"])


@role_router.get("/{role_uuid}", response_model=ReadRoleModel)
@inject
async def read_role(role_uuid: UUID, role_provider: FromDishka[RoleUseCases]):
    return await role_provider.read_single_role(role_uuid)


@role_router.get("/", response_model=list[ReadRoleModel])
@inject
async def read_roles(
    role_provider: FromDishka[RoleUseCases],
    role_filters: RoleFilter = FilterDepends(RoleFilter),
):
    return await role_provider.get_roles_list(role_filters)


@role_router.post("/", response_model=ReadRoleModel)
@inject
async def create_role(
    user_data: CreateRoleModel, role_provider: FromDishka[RoleUseCases]
):
    return await role_provider.create_new_role(**user_data.model_dump())


@role_router.patch("/{role_uuid}", response_model=ReadRoleModel)
@inject
async def update_role(
    role_uuid: UUID, user_data: CreateRoleModel, role_provider: FromDishka[RoleUseCases]
):
    return await role_provider.update_role(
        **user_data.model_dump(), role_uuid=role_uuid
    )


@role_router.delete("/{role_uuid}", response_model=ReadRoleModel)
@inject
async def delete_user(role_uuid: UUID, role_provider: FromDishka[RoleUseCases]):
    return await role_provider.delete_role(role_uuid)
