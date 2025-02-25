from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, select

from e_commerce.models import usersInfoModel as uiM
from e_commerce.models import usersModel as uM
from e_commerce.repositories import mixinRepository as mR


class UserInfoRepository(mR.MixinRepository):
    model_name = uiM.UsersInfo

    @classmethod
    async def get(cls, connection: AsyncSession, **filter_by):
        """
        SELECT users.id, users.username, ui.email, ui.phone_number
        FROM users_info ui
        JOIN users ON users.id = users_info.user_id;
        """
        query = (
            select(
                uM.Users.id,
                uM.Users.username,
                uiM.UsersInfo.email,
                uiM.UsersInfo.phone_number,
            )
            .join(cls.model_name, cls.model_name.user_id == uM.Users.id)
            .filter_by(**filter_by)
        )

        result = await connection.execute(query)
        rows = result.all()
        try:
            row = rows[0]
        except IndexError:
            return None

        result_dict = {
            "id": str(row.id),
            "email": row.email,
            "phone_number": row.phone_number,
        }

        return uiM.UsersInfo(**result_dict)

    @classmethod
    async def update(cls, connection, user_id, **new_data):
        query = (
            update(cls.model_name)
            .values(email=new_data["email"], phone_number=new_data["phone_number"])
            .where(cls.model_name.user_id == user_id)
        )

        await connection.execute(query)