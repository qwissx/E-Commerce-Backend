import uuid as ui
import os

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.database import session_getter
from e_commerce.repositories.goodsRepository import GoodsRepository
from e_commerce.schemas import goodsSchemas as gS

goods_router = APIRouter(prefix="/goods", tags=["Goods"])  


def remove_image(good_id):
    file_name = str(good_id) + ".webp"
    image_path = os.path.join("e_commerce/static/images", file_name)
    if os.path.exists(image_path):
        os.remove(image_path) 


@goods_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create_good(
    good_data: gS.SGoodCreate,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    good_id = await GoodsRepository.add(connection, **good_data.model_dump())
    await connection.commit()
    return {"message": "good was added successfully", "good_id": str(good_id)}


@goods_router.get(path="/{good_id}")
async def get_good(
    good_id: ui.UUID,
    connection: AsyncSession = Depends(session_getter),
) -> gS.SGoodDisplay:
    good = await GoodsRepository.get(connection, id=good_id)
    return good


@goods_router.get(path="/all/{good_id}")
async def get_all_goods(
    good_id: ui.UUID,
    connection: AsyncSession = Depends(session_getter),
) -> list[gS.SGoodDisplay]:
    goods = await GoodsRepository.get_all(connection)
    return goods


@goods_router.delete(path="/{good_id}")
async def del_good(
    good_id: ui.UUID,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    await GoodsRepository.rem(connection, id=good_id)
    await connection.commit()

    remove_image(good_id)

    return {"message": "good was successfully deleted"}
