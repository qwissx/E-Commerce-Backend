import abc

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository(abc.ABC):
    @classmethod
    @abc.abstractmethod
    async def add(connection: AsyncSession, **data) -> None:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    async def get(connection: AsyncSession, **filter_by):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    async def rem(connection: AsyncSession, **filter_by):
        raise NotImplementedError
