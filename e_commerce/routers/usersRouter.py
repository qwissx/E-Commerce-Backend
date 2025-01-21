from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.database import session_getter
from e_commerce.repositories.usersRepository import UsersRepository
from e_commerce.schemas import usersSchemas as uS

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: uS.SUserCreate,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    await UsersRepository.add(connection, **user_data.model_dump())
    await connection.commit()
    return {"message": "user was added successfully"}


@users_router.get(path="/{user_id}")
async def get_user(
    user_id: int,
    connection: AsyncSession = Depends(session_getter),
) -> uS.SUserDisplay:
    user = await UsersRepository.get(connection, id=user_id)
    return user


@users_router.delete(path="/")
async def del_user(
    filter_by: uS.SUserDelete,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    await UsersRepository.rem(connection, **filter_by.model_dump())
    await connection.commit()
    return {"message": "user was successfully deleted"}
