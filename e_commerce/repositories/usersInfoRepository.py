from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, select

from e_commerce.models import usersInfoModel as uiM
from e_commerce.models import usersModel as uM
from e_commerce.repositories import mixinRepository as mR


class UserInfoRepository(mR.MixinRepository):
    model_name = uiM.UsersInfo

    @classmethod
    async def get(cls, connection, **filter_by):
        """
        SELECT users.id, users.username, users.password, ui.email, ui.phone_number
        FROM users_info ui
        JOIN users ON users.id = users_info.user_id
        WHERE users.username = :username;
        """
        query = (
            select(
                uM.Users.id,
                uM.Users.username,
                uM.Users.password,
                uiM.UsersInfo.email,
                uiM.UsersInfo.phone_number,
            )
            .join(cls.model_name, cls.model_name.user_id == uM.Users.id)
            .filter_by(**filter_by)
        )

        result = await connection.execute(query)
        rows = result.all()
        row = rows[0]

        result_dict = {
            "id": str(row.id),
            "username": row.username,
            "password": row.password,
            "email": row.email,
            "phone number": row.phone_number,
        }

        return result_dict

    @classmethod
    async def update(cls, connection, user_id, **new_data):
        query = (
            update(cls.model_name)
            .values(email=new_data["email"], phone_number=new_data["phone_number"])
            .where(cls.model_name.user_id == user_id)
        )

        await connection.execute(query)