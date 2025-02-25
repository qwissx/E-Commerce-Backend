import os

from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.cache import cache as cD
from e_commerce.repositories.goodsRepository import GoodsRepository


def remove_image(good_id):
    file_name = str(good_id) + ".webp"
    image_path = os.path.join("e_commerce/static/images", file_name)
    if os.path.exists(image_path):
        os.remove(image_path) 


async def get_good_from_cache(good_id, connection: AsyncSession):
    good = await cD.check_cache("good", good_id)
    if not good:
        good = await GoodsRepository.get(connection, id=good_id)
        await cD.add_cache("good", good_id, **good.model_dump())
        
    return good
    

async def get_goods_from_cache(offset, limit):
    pass