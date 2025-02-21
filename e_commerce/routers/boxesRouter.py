import uuid as ui

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from e_commerce.connections import session_getter
from e_commerce.repositories.boxesRepository import BoxesRepository
from e_commerce.schemas import boxesSchemas as bS
from e_commerce.dependencies.logger import logger_add_info
from e_commerce.exceptions import SQLExc
from e_commerce.models.usersModel import Users
from e_commerce.dependencies import users as uD

boxes_router = APIRouter(prefix="/boxes", tags=["Boxes"])


@boxes_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def add_to_box(
    good_id: ui.UUID,
    user: Users = Depends(uD.get_current_user),
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    try:
        await BoxesRepository.add(connection, user_id=user.id, good_id=good_id)
    except SQLAlchemyError as e:
        logger_add_info(add_to_box.__name__, user_id=user.id, good_id=good_id)
        raise SQLExc.CannotFindUserOrGood

    await connection.commit()
    return {"message": "good was added successfully"}


@boxes_router.get(path="/")
async def get_box(
    user: Users = Depends(uD.get_current_user),
    connection: AsyncSession = Depends(session_getter),
) -> list[bS.SBoxDisplay]:
    box = await BoxesRepository.get(connection, user_id=user.id)
    if not box:
        raise SQLExc.CannotFindGoods

    return box


@boxes_router.delete(path="/")
async def del_box(
    good_id: ui.UUID,
    user: Users = Depends(uD.get_current_user),
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    if not await BoxesRepository.get(connection, user_id=user.id):
        logger_add_info(del_box.__name__, good_id=good_id)
        raise SQLExc.CannotFindBox

    await BoxesRepository.rem(connection, user_id=user.id, good_id=good_id)
    await connection.commit()
    return {"message": "good from box was successfully deleted"}
