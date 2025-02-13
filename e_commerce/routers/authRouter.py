from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.schemas import usersSchemas as uS
from e_commerce.database import session_getter
from e_commerce.repositories.usersRepository import UsersRepository
from e_commerce.repositories.usersInfoRepository import UserInfoRepository
from e_commerce.dependencies import auth as aD
from e_commerce.exceptions import AuthExc


reg_router = APIRouter(prefix="/auth", tags=["Authorization"])


@reg_router.post(path="/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    response: Response,
    user_data: uS.SUserAuth,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    if await UsersRepository.get(connection, username=user_data.username):
        raise AuthExc.UserExist

    hashed_pass = aD.get_password_hash(user_data.password)
    user_id = await UsersRepository.add(
        connection=connection,
        username=user_data.username,
        password=hashed_pass,
    )

    await UserInfoRepository.add(connection, user_id=user_id)
    await connection.commit()

    access_token = aD.create_access_token({"sub": str(user_id), "username": user_data.username})
    response.set_cookie("access_token", access_token, httponly=True)
    
    return {"message": "user was added successfully"}


@reg_router.post("/login")
async def login_user(
    response: Response,
    user_data: uS.SUserAuth,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    user = await aD.authenticate_user(connection, user_data.username, user_data.password)

    access_token = aD.create_access_token({"sub": str(user.id), "username": user.username})
    response.set_cookie("access_token", access_token, httponly=True)
    return {"message": "access is open"}


@reg_router.post("/logout")
async def log_out_user(
    response: Response,
    connection: AsyncSession = Depends(session_getter),
) -> dict[str, str]:
    response.delete_cookie("access_token")

    return {"message": "access is denied"}
    