import pytest

from e_commerce.database import async_session_maker
from e_commerce.repositories.usersRepository import UsersRepository


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "data",
    [
        ({"id": "6e79d027-d2a6-4d9d-9755-934ab749a952", "username": "qwissx"}),
        ({"id": "6e79d027-d2a6-4d9d-9755-934ab749a952", "username": "bogdan"}),
    ],
)
async def test_users_repository_add_and_get(clean_repositories, data):
    async with async_session_maker() as connection:
        await UsersRepository.add(connection, **data)
        user = await UsersRepository.get(connection, **data)

        assert str(user.id) == data["id"]
        assert user.username == data["username"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "data",
    [
        ({"id": "6e79d027-d2a6-4d9d-9755-934ab749a952", "username": "qwissx"}),
        ({"id": "6e79d027-d2a6-4d9d-9755-934ab749a952", "username": "bogdan"}),
    ],
)
async def test_users_repository_add_rem_get(clean_repositories, data):
    async with async_session_maker() as connection:
        await UsersRepository.add(connection, **data)
        await UsersRepository.rem(connection, **data)
        user = await UsersRepository.get(connection, **data)

        assert user is None
