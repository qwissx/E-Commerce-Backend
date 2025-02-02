from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.models import boxesModel as bM
from e_commerce.repositories import mixinRepository as mR
from e_commerce.models import goodsModel as gM


class BoxesRepository(mR.MixinRepository):
    model_name = bM.Boxes

    @classmethod
    async def get(cls, connection: AsyncSession, user_id) -> list[gM.Goods]:
        """
        SELECT goods.id, goods.name, goods.price
        FROM goods
        JOIN boxes ON goods.id = boxes.good_id
        WHERE boxes.user_id = :user_id;
        """
        
        query = (
            select(gM.Goods.id, gM.Goods.name, gM.Goods.type)
            .join(cls.model_name, cls.model_name.good_id == gM.Goods.id)
            .where(cls.model_name.user_id == user_id)
        )

        result = await connection.execute(query)
        rows = result.all()

        result_dicts = [{'id': row.id, 'good_name': row.name, 'good_type': row.type} for row in rows]
        return result_dicts