from datetime import datetime

from fastapi import Request, Depends
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from e_commerce.exceptions import AuthExc
from e_commerce import settings as st
from e_commerce.dependencies.auth import get_password_hash, check_access_token
from e_commerce.repositories.usersRepository import UsersRepository
from e_commerce.database import session_getter


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

    user = await UsersRepository.get(connection, id=payload.get("sub")) 
    
    return user
    