from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.models import usersModel as uM
from e_commerce.repositories import baseRepository as bR


class UsersRepository(bR.BaseRepository):
    @classmethod
    async def add(cls, connection: AsyncSession, **data) -> None:
        query = insert(uM.Users).values(**data)
        await connection.execute(query)

    @classmethod
    async def get(cls, connection: AsyncSession, **filter_by) -> uM.Users:
        query = select(uM.Users).filter_by(**filter_by)
        user = await connection.execute(query)
        return user.scalar_one_or_none()

    @classmethod
    async def rem(cls, connection: AsyncSession, **filter_by) -> None:
        query = delete(uM.Users).filter_by(**filter_by)
        await connection.execute(query)
