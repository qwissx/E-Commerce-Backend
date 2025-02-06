import uuid as ui

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache
from sqlalchemy.exc import SQLAlchemyError

from e_commerce.database import session_getter
from e_commerce.repositories.usersInfoRepository import UserInfoRepository
from e_commerce.schemas import usersInfoSchemas as uiS
from e_commerce.exceptions import SQLExc
from e_commerce.dependencies.logger import logger_add_info
from e_commerce.models.usersModel import Users
from e_commerce.dependencies import users as uD

users_info_router = APIRouter(prefix="/usersinfo", tags=["Users Info"])

# на правах админа
@users_info_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create_user_info(
    user_info: uiS.SUserInfoCreate,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    try:
        await UsersRepository.add(connection, **user_data.model_dump())
    except SQLAlchemyError as e:
        logger_add_info(create_user_info.__name__, **user_info.model_dump())
        raise SQLExc.CannotAddUserInfo

    await connection.commit()
    return {"message": "user info was added successfully"}


@users_info_router.get(path="/")
@cache(expire=60)
async def get_user_info(
    user: Users = Depends(uD.get_current_user), 
    connection: AsyncSession = Depends(session_getter),
) -> uiS.SUserInfoDisplay:
    user_info = await UserInfoRepository.get(connection, user_id=user.id)
    if not user_info:
        raise SQLExc.CannotFindUserInfo

    return user_info


@users_info_router.put(path="/")
async def update_user_info(
    new_data: uiS.SUserInfoUpdate,
    user: Users = Depends(uD.get_current_user), 
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    if not await UserInfoRepository.get(connection, user_id=user.id):
        logger_add_info(del_user_info.__name__, user_id=user_id)
        raise SQLExc.CannotDeleteUserInfo 

    await UserInfoRepository.update(connection, user.id, **new_data.model_dump())
    await connection.commit()

    return {"message": "success"}

# на правах админа
@users_info_router.delete(path="/{user_id}")
async def del_user_info(
    user_id: ui.UUID,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    if not await UserInfoRepository.get(connection, username): # добавит username при создании авторизации
        logger_add_info(del_user_info.__name__, user_id=user_id)
        raise SQLExc.CannotDeleteUserInfo

    await UserInfoRepository.rem(connection, user_id=user_id)
    await connection.commit()

    return {"message": "user was successfully deleted"}