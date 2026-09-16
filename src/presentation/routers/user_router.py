from uuid import UUID

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi_filter import FilterDepends

from application.use_cases import UserUseCases
from presentation.models import (CreateRolesToUser, CreateUserModel,
                                 ReadUserModel, UserFilter)

user_router = APIRouter(prefix="/user", tags=["Users"])


@user_router.get("/{user_uuid}", response_model=ReadUserModel)
@inject
async def read_user(user_uuid: UUID, user_provider: FromDishka[UserUseCases]):
    return await user_provider.read_single_user(user_uuid)


@user_router.get("/", response_model=list[ReadUserModel])
@inject
async def read_users(
    user_provider: FromDishka[UserUseCases],
    user_filters: UserFilter = FilterDepends(UserFilter),
):
    return await user_provider.get_users_list(user_filters)


@user_router.post("/", response_model=ReadUserModel)
@inject
async def create_user(
    user_data: CreateUserModel, user_provider: FromDishka[UserUseCases]
):
    return await user_provider.create_new_user(**user_data.model_dump())


@user_router.post("/{user_uuid}/roles", response_model=None)
@inject
async def assign_role_to_user(
    data: CreateRolesToUser, user_provider: FromDishka[UserUseCases]
):
    return await user_provider.add_roles_to_user(**data.model_dump())


@user_router.patch("/{user_uuid}", response_model=ReadUserModel)
@inject
async def update_user(
    user_uuid: UUID, user_data: CreateUserModel, user_provider: FromDishka[UserUseCases]
):
    return await user_provider.update_user(
        **user_data.model_dump(), user_uuid=user_uuid
    )


@user_router.delete("/{user_uuid}", response_model=ReadUserModel)
@inject
async def delete_user(user_uuid: UUID, user_provider: FromDishka[UserUseCases]):
    return await user_provider.delete_user(user_uuid)
