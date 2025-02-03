import uuid as ui

from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.repositories import baseRepository as bR
from e_commerce import exceptions as exc
from e_commerce.decorators.repositoriesDecorator import SQLErrorHandrel


class MixinRepository(bR.BaseRepository):
    model_name = None
    exceptions = dict

    @classmethod
    @SQLErrorHandrel
    async def add(cls, connection: AsyncSession, **data) -> ui.UUID:
        new_id = ui.uuid4()
        query = insert(cls.model_name).values(id=new_id, **data)
        await connection.execute(query)
        return new_id

    @classmethod
    @SQLErrorHandrel
    async def get(cls, connection: AsyncSession, **filter_by):
        query = select(cls.model_name).filter_by(**filter_by)
        user = await connection.execute(query)
        return user.scalar_one_or_none()

    @classmethod
    @SQLErrorHandrel
    async def rem(cls, connection: AsyncSession, **filter_by) -> None:
        query = delete(cls.model_name).filter_by(**filter_by)
        await connection.execute(query)
        