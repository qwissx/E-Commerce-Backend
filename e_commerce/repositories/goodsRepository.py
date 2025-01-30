from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from e_commerce.models import goodsModel as gM
from e_commerce.repositories import mixinRepository as mR


class GoodsRepository(mR.MixinRepository):
    model_name = gM.Goods

    @classmethod
    async def get_all(cls, connection: AsyncSession, limit = 10, **filter_by) -> list[gM.Goods]:
        query = select(cls.model_name).filter_by(**filter_by).limit(limit)
        goods = await connection.execute(query)
        return goods.scalars().all()
    