from datetime import datetime
from uuid import UUID

from fastapi import Request, Depends
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.exceptions import AuthExc, SQLExc
from e_commerce import settings as st
from e_commerce.dependencies.auth import get_password_hash, check_access_token
from e_commerce.repositories.usersRepository import UsersRepository
from e_commerce.database import session_getter
from e_commerce.dependencies import cache as ca
from e_commerce.schemas import usersSchemas as uS


def update_data(**data):
    data["password"] = get_password_hash(data.get("password"))
    return data


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise AuthExc.UserNotAuthorized
    return token


async def get_current_user(
    connection: AsyncSession = Depends(session_getter), 
    token: str = Depends(get_token)
):
    try:
        payload = jwt.decode(
            token, st.secret, st.hash,
        )
    except JWTError as e:
        raise AuthExc.UserNotAuthorized

    check_access_token(payload)

    user = await ca.check_cache("user", payload.get("sub"))
    if user:
        return uS.SUserDisplay(
            id=UUID(user.get("id")),
            username=str(user.get("username")),
            password=str(user.get("password")),
        )

    user = await UsersRepository.get(connection, id=payload.get("sub"))

    try:
        await ca.add_cache(
            "user", 
            payload.get("sub"), 
            id=str(user.id), 
            username=user.username, 
            password=user.password
        )
    except AttributeError:
        raise SQLExc.CannotDeleteUser

    return user
    