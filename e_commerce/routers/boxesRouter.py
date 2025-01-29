import uuid as ui

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.database import session_getter
from e_commerce.repositories.boxesRepository import BoxesRepository
from e_commerce.schemas import boxesSchemas as bS

boxes_router = APIRouter(prefix="/boxes", tags=["Boxes"])


@boxes_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def add_to_box(
    box_data: bS.SBoxCreate,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    await BoxesRepository.add(connection, **box_data.model_dump())
    await connection.commit()
    return {"message": "box was added successfully"}


@boxes_router.get(path="/{user_id}")
async def get_box(
    user_id: ui.UUID,
    connection: AsyncSession = Depends(session_getter),
) -> list[bS.SBoxDisplay]:
    box = await BoxesRepository.get(connection, user_id)
    return box


@boxes_router.delete(path="/{box_id}")
async def del_box(
    box_id: ui.UUID,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    await BoxesRepository.rem(connection, id=box_id)
    await connection.commit()
    return {"message": "box was successfully deleted"}
