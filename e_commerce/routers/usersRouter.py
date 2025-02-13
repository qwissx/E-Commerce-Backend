import uuid as ui

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache
from sqlalchemy.exc import SQLAlchemyError

from e_commerce.database import session_getter
from e_commerce.repositories.usersRepository import UsersRepository
from e_commerce.schemas import usersSchemas as uS
from e_commerce.exceptions import SQLExc
from e_commerce.dependencies.logger import logger_add_info
from e_commerce.routers import userInfoRouter as uiR
from e_commerce.dependencies import users as uD
from e_commerce.models.usersModel import Users

users_router = APIRouter(prefix="/users", tags=["Users"])

# на правах админа
@users_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: uS.SUserCreate,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    user_data = update_data(**user_data.model_dump())

    try:
        await UsersRepository.add(connection, **user_data)
    except SQLAlchemyError as e:
        logger_add_info(create_user.__name__, **user_data.model_dump())
        raise SQLExc.CannotAddUser

    await connection.commit()
    return {"message": "user was added successfully"}


@users_router.get(path="/")
@cache(expire=60)
async def get_user(
    user: Users = Depends(uD.get_current_user), 
    connection: AsyncSession = Depends(session_getter),
) -> uS.SUserDisplay:
    user = await UsersRepository.get(connection, id=user.id)
    if not user:
        logger_add_info(get_user.__name__, user_id=user_id)
        raise SQLExc.CannotFindUser
        
    return user


@users_router.delete(path="/")
async def user_del_himself(
    user: Users = Depends(uD.get_current_user), 
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    if not await UsersRepository.get(connection, id=user.id):
        logger_add_info(user_del_himself.__name__, user_id=user.id)
        raise SQLExc.CannotDeleteUser

    await uiR.del_user_info(user.id, connection) # вернуться
    await UsersRepository.rem(connection, id=user.id)

    await connection.commit()
    return {"message": "user was successfully deleted"}

# на правах админа
@users_router.delete(path="/{user_id}")
async def user_del(
    user_id: ui.UUID, 
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    if not await UsersRepository.get(connection, id=user_id):
        logger_add_info(user_del.__name__, user_id=user_id)
        raise SQLExc.CannotDeleteUser

    await uiR.del_user_info(user_id, connection) # вернуться
    await UsersRepository.rem(connection, id=user_id)

    await connection.commit()
    return {"message": "user was successfully deleted"}