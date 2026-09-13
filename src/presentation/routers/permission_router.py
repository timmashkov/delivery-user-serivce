from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from application.use_cases import PermissionUseCases
from presentation.models import CreatePermissionModel, ReadPermissionModel

perm_router = APIRouter(prefix="/permission", tags=["Permissions"])


@perm_router.get("/{perm_uuid}", response_model=ReadPermissionModel)
@inject
async def read_permission(
    perm_uuid: UUID, perm_provider: FromDishka[PermissionUseCases]
):
    return await perm_provider.read_single_permission(perm_uuid)


@perm_router.get("/", response_model=list[ReadPermissionModel])
@inject
async def read_permissions(perm_provider: FromDishka[PermissionUseCases]):
    return await perm_provider.get_permissions_list()


@perm_router.post("/", response_model=ReadPermissionModel)
@inject
async def create_permission(
    user_data: CreatePermissionModel, perm_provider: FromDishka[PermissionUseCases]
):
    return await perm_provider.create_new_permission(**user_data.model_dump())


@perm_router.patch("/{perm_uuid}", response_model=ReadPermissionModel)
@inject
async def update_permission(
    perm_uuid: UUID,
    user_data: CreatePermissionModel,
    perm_provider: FromDishka[PermissionUseCases],
):
    return await perm_provider.update_permission(
        **user_data.model_dump(), perm_uuid=perm_uuid
    )


@perm_router.delete("/{perm_uuid}", response_model=ReadPermissionModel)
@inject
async def delete_permission(
    perm_uuid: UUID, perm_provider: FromDishka[PermissionUseCases]
):
    return await perm_provider.delete_permission(perm_uuid)
