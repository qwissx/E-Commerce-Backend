from typing import AsyncGenerator
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from redis import asyncio as aioredis
from redis.asyncio import Redis
from celery import Celery

from e_commerce import settings as st

engine = create_async_engine(st.db_url, poolclass=NullPool)


async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def session_getter() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


redis = Redis(host=st.redis_host, port=st.redis_port, db=0)


broker = Celery(
    "tasks", 
    broker=st.rabbit_url,
    include=["e_commerce.tasks.tasks"],
)
