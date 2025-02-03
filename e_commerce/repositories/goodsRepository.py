from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from e_commerce.models import goodsModel as gM
from e_commerce.repositories import mixinRepository as mR
from e_commerce.decorators.repositoriesDecorator import SQLErrorHandrel


class GoodsRepository(mR.MixinRepository):
    model_name = gM.Goods

    @classmethod
    @SQLErrorHandrel
    async def get_all(cls, connection: AsyncSession, limit=10) -> list[gM.Goods]:
        query = select(cls.model_name).limit(limit)
        goods = await connection.execute(query)
        return goods.scalars().all()
    