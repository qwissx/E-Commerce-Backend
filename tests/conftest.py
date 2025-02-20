import pytest_asyncio

from e_commerce.connections import Base, engine


@pytest_asyncio.fixture
async def clean_repositories():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
