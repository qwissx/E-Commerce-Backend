import uuid as ui

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from e_commerce.connections import session_getter
from e_commerce.repositories.goodsRepository import GoodsRepository
from e_commerce.schemas import goodsSchemas as gS
from e_commerce.dependencies.goods import remove_image
from e_commerce.dependencies.logger import logger_add_info
from e_commerce.exceptions import SQLExc
from e_commerce.models.usersModel import Users
from e_commerce.dependencies import users as uD
from e_commerce.cache.cacheService import Cache

goods_router = APIRouter(prefix="/goods", tags=["Goods"])  

# на правах админа
@goods_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create_good(
    good_data: gS.SGoodCreate,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    try:
        good_id = await GoodsRepository.add(connection, **good_data.model_dump())
    except SQLAlchemyError as e:
        logger_add_info(create_good.__name__, **good_data.model_dump())
        raise SQLExc.CannotAddGood

    await connection.commit()
    return {"message": "good was added successfully", "good_id": str(good_id)}


@goods_router.get(path="/all/")
async def get_pagination_goods(
    offset: int | None = None,
    limit: int | None = None,
    user: Users = Depends(uD.get_current_user),
    connection: AsyncSession = Depends(session_getter),
) -> gS.SGoodPagination:
    goods = await Cache.get(
        "good", 
        "pagination", 
        GoodsRepository, 
        connection, 
        offset=offset, 
        limit=limit
    )

    if not goods:
        raise SQLExc.CannotFindAnyGood

    total_count = await GoodsRepository.count(connection)

    return {
        "goods": goods,
        "total_count": total_count,
        "current_count": min((limit or 0) + (offset or 0), total_count),
    }


@goods_router.get(path="/{good_id}/")
async def get_good(
    good_id: ui.UUID,
    connection: AsyncSession = Depends(session_getter),
) -> gS.SGoodDisplay:
    good = await GoodsRepository.get(connection, id=good_id)
    if not good:
        logger_add_info(get_good.__name__, good_id=good_id)
        raise SQLExc.CannotFindGood
    
    return good

# на правах админа
@goods_router.delete(path="/{good_id}/")
async def del_good(
    good_id: ui.UUID,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    if not await GoodsRepository.get(connection, id=good_id):
        logger_add_info(del_good.__name__, id=good_id)
        raise SQLExc.CannotDeleteGood

    await GoodsRepository.rem(connection, id=good_id)
    await connection.commit()

    remove_image(good_id)

    return {"message": "good was successfully deleted"}
