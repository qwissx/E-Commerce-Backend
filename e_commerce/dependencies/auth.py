from typing import Union
from datetime import datetime, timedelta

from passlib.context import CryptContext
from fastapi import HTTPException
from jose import jwt

from e_commerce.schemas.usersSchemas import SUserDisplay
from e_commerce.repositories import usersRepository as uR
from e_commerce import settings as st
from e_commerce.exceptions import AuthExc


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_pass, hashed_pass) -> bool:
    return pwd_context.verify(plain_pass, hashed_pass)



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, st.secret, st.hash,
    )

    return encoded_jwt


def check_access_token(payload: dict):
    expire = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise AuthExc.TokenTimeNotValid

    user_id = payload.get("sub")
    if not user_id:
        raise AuthExc.TokenIdNotValid
    
    username = payload.get("username")
    if not user_id:
        raise AuthExc.TokenUsernameNotValid


async def authenticate_user(connection, username, password):
    user = await uR.UsersRepository.get(connection, username=username)
    if not user:
        raise AuthExc.UserDoesNotExist

    password_is_valid = verify_password(password, user.password)
    if not password_is_valid:
        raise AuthExc.NotValidPass

    return user
